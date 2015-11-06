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

    def __findTransitiveClosure( self, vertex, alreadyVisited ):
        ft = alreadyVisited.copy()
        print(len(ft))
        print(type(ft))
        alreadyVisited[vertex] = {}
        print( "{} paremotro -  qremos pegar o fecho desse cara".format(vertex) )
        for vertexRelated in self.related( vertex ):
            print("{} vertice relacionado com o parametro {}".format( vertexRelated,vertex ))
            if alreadyVisited.get( vertexRelated,None ) == None:
                print("entrou recursao com vertice {}".format(vertexRelated))
                test = self._findTransitiveClosure( vertexRelated,alreadyVisited )
                ft = ft.update( test )
                print("mostra tipo de test de novo depois da recusao: {}".format(type(ft)))
            print('---')
        print("retorno {}".format(ft))
        return ft
