from Graph import Graph

class DirectGraph( Graph ):

    def __init__( self ):
        super( DirectGraph, self ).__init__()
        self.reverseGraph = {}

    def topologicalOrdering( self ):
        anyVertex = self.anyVertex()
        hasCircuit = self._hasCircuit(anyVertex, anyVertex, None, set())
        if hasCircuit:
            raise Exception("The Graph has circuit. Not is possible get the Topolical Ordering.")

        listOfVertex = []
        setStampedVertex = set()

        base = self.getBase()

        for baseVertex in base:
            self._addTopolicalOrderingList( baseVertex, listOfVertex, setStampedVertex )

        listOfVertex.reverse()
        return listOfVertex

    def _addTopolicalOrderingList( self, vertex, listOfVertex, setVlistOfVertex ):
        for sucessor in self.getSuccessors(vertex):
            if not sucessor in setVlistOfVertex:
                setVlistOfVertex.add(sucessor)
                self._addTopolicalOrderingList( sucessor, listOfVertex, setVlistOfVertex )
        listOfVertex.append(vertex)

    def _hasCircuit(self,v,vCurrent,vPrevious,alreadyVisited):
        if vCurrent in alreadyVisited:
            return vCurrent
        alreadyVisited.add(vCurrent)
        for vertexRelated in self.getSuccessors(v):
            if vertexRelated != vPrevious:
                if self._hasCircuit( v,vertexRelated,vCurrent,alreadyVisited ):
                    return True
        alreadyVisited.discard(vCurrent)
        return False

    def addVertex( self,vertexName, attrs={} ):
        if super( DirectGraph, self ).addVertex( vertexName, attrs ) == False:
            return False
        self.reverseGraph[vertexName] = {}
        return True

    def getBase( self ):
        base = []
        for vertex in self.graph:
            if not self.getPredecessors( vertex ):
                base.append( vertex )
        return base

    #retorna os sucessores de um vertice
    def getSuccessors( self,vertex ):
        if self._existVertex( {vertex} ) == None:
            return False
        return self.graph[vertex]

    #retorna os antecessores de um vertice
    def getPredecessors( self,vertex ):
        if self.reverseGraph.get( vertex,None ) == None:
            return False
        return self.reverseGraph[vertex]

    def connect( self,vertexA,vertexB,label = None ):
        if super().connect( vertexA,vertexB,label ) == False:
            return False

        #Na linha abaixo não é necessário atribuir a label, pois o reseverGraph
        # é apenas para garantir O(1) em algumas operações
        self.reverseGraph[vertexB][vertexA] = None
        return True

    #retorna o grau de emissão de um vertice
    def degreeOfEmission( self,vertex ):
        if self._existVertex( {vertex} ) == False:
            return False
        return self.degree( vertex )

    #retorna o grau de recepção de um vertice
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
