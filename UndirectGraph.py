from Graph import Graph

class UndirectGraph( Graph ):

    def __init__( self ):
        super( UndirectGraph,self ).__init__()

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
