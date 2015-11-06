from abc import ABCMeta

class Graph:
    __metaclass__ = ABCMeta

    def __init__( self ):
        self.graph = {}
        self.lastVertex = None

    def addVertex( self, vertexName ):
        if self.graph.get( vertexName ) != None:
            return False
        self.graph[vertexName]  = {}
        self.lastVertex         = vertexName
        return True

    def removeVertex( self, vertexName ):
        if self.graph.get( vertexName ) == None:
            return False
        del self.graph[vertexName]
        for vertex in self.graph:
            for relatedVertex in self.related( vertex ):
                if relatedVertex == vertexName:
                    del self.graph[vertex][vertexName]
                    break
        if self.lastVertex == vertexName:
            setOfVertex = tuple( self.graph )
            self.lastVertex = setOfVertex[len(setOfVertex)-1]

    def desconnect( self, vertexA, vertexB ):
        if self._existVertex( {vertexA,vertexB} ) == False:
            return False
        del self.graph[vertexA][vertexB]
        return True

    def connect( self, vertexA,vertexB ):
        if self._existVertex( {vertexA,vertexB} ) == False:
            return False
        self.graph[vertexA][vertexB] = {}

    def order( self ):
        return len( self.graph )

    def degree( self,vertex ):
        if self._existVertex( {vertex} ) == False:
            return False
        return len(self.graph[vertex])

    def getRelationVertex( self ):
        return self.graph

    def anyVertex( self ):
        return self.lastVertex

    def related( self,vertex ):
        if self._existVertex( { vertex } ) == False:
            return False
        return self.graph[vertex]

    def _existVertex( self, dictVertex = {} ):
        for v in dictVertex:
            if self.graph.get( v, None ) == None:
                return False
        return True
