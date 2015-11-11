from Graph import Graph
class UndirectGraph( Graph ):

    def __init__( self ):
        super( UndirectGraph,self ).__init__()

    def connect( self, vertexA,vertexB,label = None ):
        if super().connect( vertexA,vertexB,label ) == False:
            return False
        self.graph[vertexB][vertexA] = label
        return True

    # verifica se o grafo é regular
    def isRegular( self ):
        lastValue = 0
        for v in self.graph:
            if lastValue == 0:
                lastValue = self.degree( v )
            elif lastValue != self.degree( v ):
                return False
        return True

    # verifica se o grafo é completo
    def isComplete( self ):
        totalVertex = len( self.graph )
        for v in self.graph:
            if self.degree( v ) != ( totalVertex -1 ):
                return False
        return True

    #verifica se o grafo é uma arvore
    def isTree( self ):
        anyVertex = self.anyVertex()
        return self.isConnected() and not( self._hasCycle( anyVertex,anyVertex,None,{} ) )

    #verifica se o grafo tem ciclos
    def _hasCycle( self,v,vCurrent,vPrevious,alreadyVisited ):

        if alreadyVisited.get( vCurrent,None ) != None:
            return vCurrent
        alreadyVisited[vCurrent] = {}
        for vertexRelated in self.related( v ):
            if vertexRelated != vPrevious:
                if self._hasCycle( v,vertexRelated,vCurrent,alreadyVisited ):
                    return True
        del alreadyVisited[vCurrent]
        return False

    #verifica se o grafo é conexo
    def isConnected( self ):
        return self.getRelationVertex() == self._findTransitiveClosure( self.anyVertex(),{} ).keys()

    #retorna fecho transitivo de um vertice
    def transitiveClosure( self,vertex ):
        return self.isConnected() and self._findTransitiveClosure( vertex,{} )

    def _findTransitiveClosure( self, vertex, alreadyVisited ):
        alreadyVisited[vertex] = {}
        ft = alreadyVisited.copy()
        for vertexRelated in self.related( vertex ):
            if alreadyVisited.get( vertexRelated,None ) == None:
                ft.update( self._findTransitiveClosure( vertexRelated,alreadyVisited ) )
        return ft
