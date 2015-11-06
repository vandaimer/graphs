from Graph import Graph

class DirectGraph( Graph ):

    def __init__( self ):
        super( DirectGraph,self ).__init__()
        self.reverseGraph = {}

    def addVertex( self,vertexName ):
        if super().addVertex( vertexName ) == False:
            return False
        self.reverseGraph[vertexName] = {}
        return True

    def getSuccessors( self,vertex ):
        if self._existVertex( {vertex} ) == None:
            return False
        return self.graph[vertex]

    def getPredecessors( self,vertex ):
        if self.reverseGraph.get( vertex,None ) == None:
            return False
        return self.reverseGraph[vertex]

    def connect( self,vertexA,vertexB ):
        if super().connect( vertexA,vertexB ) == False:
            return False
        self.reverseGraph[vertexB][vertexA] = {}
        return True

    def degreeOfEmission( self,vertex ):
        if self._existVertex( {vertex} ) == False:
            return False
        return self.degree( vertex )

    def degreeOfReception( self,vertex ):
        if self._existVertex( {vertex} ) == False:
            return False
        return len( self.reverseGraph[vertex] )

    def removeVertex( self,vertexChosen ):
        if super().removeVertex( vertexChosen ) == False:
            return False
        del self.reverseGraph[vertexChosen]
        for vertex in self.reverseGraph:
            for relatedVertex in self.reverseGraph[vertex]:
                if relatedVertex == vertexChosen:
                    del self.reverseGraph[vertex][vertexChosen]
                    break

