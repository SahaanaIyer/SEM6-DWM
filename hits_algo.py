import networkx as nx 

def hits(G, max_iter=100, tol=1.0e-8, nstart=None, normalized=True):
  if (type(G) == nx.MultiGraph or type(G) == nx.MultiDiGraph):  
    raise Exception("hits() not defined for graphs with  multiedges") 
    if len(G) == 0: 
      return {}, {}
  if nstart is None: 
    h = dict.fromkeys(G, 1.0 / G.number_of_nodes())  
  else: 
    h = nstart 
    s = 1.0 / sum(h.values()) 
    for k in h: 
      h[k] *= s 
      for _ in range(max_iter): 
        hlast = h 
        h = dict.fromkeys(hlast.keys(), 0) 
        a = dict.fromkeys(hlast.keys(), 0) 
        for n in h: 
          for nbr in G[n]: 
            a[nbr] += hlast[n] * G[n][nbr].get("weight", 1)
        for n in h: 
          for nbr in G[n]: 
            h[n] += a[nbr] * G[n][nbr].get("weight", 1) 
            s = 1.0 / max(h.values()) 
            for n in h: 
              h[n] *= s 
              s = 1.0 / max(a.values()) 
        for n in a: 
          a[n] *= s 
          err = sum([abs(h[n] - hlast[n]) for n in h])  
          if err < tol: 
            break 
          else: 
            raise nx.PowerIterationFailedConvergence(max_iter)  
        if normalized: 
          s = 1.0 / sum(a.values()) 
        for n in a: 
          a[n] *= s 
          s = 1.0 / sum(h.values()) 
        for n in h: 
          h[n] *= s 
  return h, a 

G = nx.DiGraph() 
G.add_edges_from([(1, 2), (1, 3), (1, 4), (2, 3),  (2, 4), (3, 1), (4, 1), (4, 3)]) 
hubs, authorities = nx.hits(G, max_iter = 50, normalized = True)
print("Hub Scores: ", hubs) 
print("Authority Scores: ", authorities) 

# OUTPUT :
# Hub Scores:  {1: 0.39098432423031937, 2: 0.31612245554460533, 3: 0.0560803404601846, 4: 0.23681287976489077}
# Authority Scores:  {1: 0.1254412278344748, 2: 0.16745199206817146, 3: 0.4042648716820967, 4: 0.302841908415257}
