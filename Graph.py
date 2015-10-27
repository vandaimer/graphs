from abc import ABCMeta

class Graph:
    __metaclass__ = ABCMeta

    def __init__( self ):
        self.graph = {}

    def addVertex( self, vertexName ):
        if self.graph.get( vertexName ) != None:
            return False
        self.graph[vertexName] = None
        return True

    def desconnect( self, vertexA, vertexB ):
        if self.__existVertex( {vertexA,vertexB} ) == False:
            return False
        del self.graph[vertexA][vertexB]
        return True

    def connect( self, vertexA,vertexB ):
        if self.__existVertex( {vertexA,vertexB} ) == False:
            return False
        self.graph[vertexA][vertexB] = {}

    def order( self ):
        return len( self.graph )

    def degree( self,vertex ):
        if self.__existVertex( {vertex} ) == False:
            return False
        return len(self.graph[vertex])

    def getListVertex( self ):
        pass

    def anyVertex( self ):
        pass

    def related( self ):
        pass

    def __existVertex( self, listVertex = {} ):
        for v in listVertex:
            if self.graph.get( v ) == None:
                return False
