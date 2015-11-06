from DirectGraph import DirectGraph

g = DirectGraph()
g.addVertex(1)
g.addVertex(2)
g.addVertex(3)
g.addVertex(4)

g.connect(1,2)
g.connect(2,3)
g.connect(2,4)
