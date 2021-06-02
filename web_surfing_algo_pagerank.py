import networkx as nx 

def pagerank(G, alpha=0.85, personalization=None, max_iter=100, tol=1.0e-6, nstart=None, weight='weight',  dangling=None): 
  if len(G) == 0: 
    return {} 
  if not G.is_directed(): 
    D = G.to_directed() 
  else: 
    D = G 
  W = nx.stochastic_graph(D, weight=weight) 
  N = W.number_of_nodes() 
  if nstart is None: 
    x = dict.fromkeys(W, 1.0 / N) 
  else: 
    s = float(sum(nstart.values())) 
    x = dict((k, v / s) for k, v in nstart.items())   
  if personalization is None: 
    p = dict.fromkeys(W, 1.0 / N) 
  else: 
    missing = set(G) - set(personalization) 
    if missing: 
      raise NetworkXError('Personalization dictionary '  'must have a value for every node. ' 'Missing nodes %s' % missing) 
      s = float(sum(personalization.values())) 
      p = dict((k, v / s) for k, v in personalization.items())   
  if dangling is None: 
    dangling_weights = p 
  else: 
    missing = set(G) - set(dangling) 
    if missing: 
      raise NetworkXError('Dangling node dictionary '  'must have a value for every node. '  'Missing nodes %s' % missing)  
      s = float(sum(dangling.values())) 
      dangling_weights = dict((k, v/s) for k, v in  dangling.items()) 
      dangling_nodes = [n for n in W if W.out_degree(n, weight=weight)  == 0.0] 
  for _ in range(max_iter): 
    xlast = x 
    x = dict.fromkeys(xlast.keys(), 0) 
    danglesum = alpha * sum(xlast[n] for n in dangling_nodes) 
    for n in x: 
      for nbr in W[n]: 
        x[nbr] += alpha * xlast[n] * W[n][nbr][weight]  
      x[n] += danglesum * dangling_weights[n] + (1.0 - alpha)  * p[n] 
      err = sum([abs(x[n] - xlast[n]) for n in x])  
      if err < N*tol: 
        return x 
        raise NetworkXError('pagerank: power iteration failed to converge ' 'in %d iterations.' % max_iter) 

G = nx.DiGraph() 
G.add_edges_from([(1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 1), (4, 1), (4, 3)]) 
pr = nx.pagerank(G,1) 
print(pr) 


# OUTPUT :
# {1: 0.38709615908859496, 2: 0.12903204605249047, 3: 0.29032302109901886, 4: 0.193548773759895}
