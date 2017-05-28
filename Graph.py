from abc import ABCMeta

class Graph:
    __metaclass__ = ABCMeta

    def __init__( self ):
        self.graph = {}
        self.attrs = {}
        self.lastVertex = None

    #adiciona um vértice, se o vertice já existe, retorna falso
    def addVertex( self, vertexName, attrs={}):
        if self._existVertex( {vertexName} ) != False:
            return False
        self.graph[vertexName]  = {}
        self.attrs[vertexName]  = attrs
        self.lastVertex         = vertexName
        return True

    #remove um vértice, se não existe retorna falso
    def removeVertex( self, vertexName ):
        if self._existVertex( { vertexName } ) == False:
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

    #desconecta dois vertices, caso um ou os dois não exista, ele retorna falso
    def desconnect( self, vertexA, vertexB ):
        if self._existVertex( {vertexA,vertexB} ) == False:
            return False
        del self.graph[vertexA][vertexB]
        return True

    #conecta dois vertices, caso um ou os dois não exista, ele retorna falso
    def connect( self, vertexA,vertexB,label = None ):
        if self._existVertex( {vertexA,vertexB} ) == False:
            return False
        self.graph[vertexA][vertexB] = label

    #Retorna o número de vértices do grafo
    def order( self ):
        return len( self.graph )

    #Retorna o número de vertices adjacentes de um vertice, se o vertice
    #passado não existir, retorna falso
    def degree( self,vertex ):
        if self._existVertex( {vertex} ) == False:
            return False
        return len(self.graph[vertex])

    #retorna todos os vertices do grafo
    def getRelationVertex( self ):
        return self.graph.keys()

    #retorna um vertice "qualquer", que nesse caso é sempre o último
    #adicionado
    def anyVertex( self ):
        return self.lastVertex

    #Retorna os adjacentes de um vertice, se o vertice passado não existir
    #retorn falso
    def related( self,vertex ):
        if self._existVertex( { vertex } ) == False:
            return False
        return self.graph[vertex]

    def _existVertex( self, dictVertex = {} ):
        for v in dictVertex:
            if self.graph.get( v, None ) == None:
                return False
        return True
