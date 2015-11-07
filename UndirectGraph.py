from Graph import Graph

class UndirectGraph( Graph ):

    def __init__( self ):
        super( UndirectGraph,self ).__init__()

    def connect( self, vertexA,vertexB ):
        if super().connect( vertexA,vertexB ) == False:
            return False
        self.graph[vertexB][vertexA] = {}
        return True

    def isRegular( self ):
        lastValue = 0
        for v in self.graph:
            if lastValue == 0:
                lastValue = super().degree( v )
            elif lastValue != super().degree( v ):
                return False
        return True

    def isComplete( self ):
        totalVertex = len( self.graph )
        for v in self.graph:
            if super().degree( v ) != ( totalVertex -1 ):
                return False
        return True

    def isTree( self ):
        anyVertex = self.anyVertex()
        return self.isConnected() and not( self._hasCycle( anyVertex,anyVertex,None,{} ) )

    def _hasCycle( self,v,vCurrent,vPrevious,alreadyVisited ):

        if alreadyVisited.get( vCurrent,None ) != None:
            vCurrent = v
            return v
        alreadyVisited[vCurrent] = {}
        for vertexRelated in self.related( v ):
            if vertexRelated != vPrevious:
                if self._hasCycle( v,vertexRelated,vCurrent,alreadyVisited ):
                    print(v,vertexRelated,vCurrent,alreadyVisited)
                    return True
        del alreadyVisited[vCurrent]
        return False

    def isConnected( self ):
        for v in self.graph:
            if self.degree( v ) == 0:
                return False
        return True

    def transitiveClosure( self,vertex ):
        return self._findTransitiveClosure( vertex,{} )

    def _findTransitiveClosure( self, vertex, alreadyVisited ):
        ft = alreadyVisited.copy()
        alreadyVisited[vertex] = {}
        for vertexRelated in self.related( vertex ):
            if alreadyVisited.get( vertexRelated,None ) == None:
                ft.update( self._findTransitiveClosure( vertexRelated,alreadyVisited ) )
        return ft
