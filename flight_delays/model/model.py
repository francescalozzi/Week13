import networkx as nx
from flight_delays.database.DAO import DAO


class Model:
    def __init__(self):
        self._grafo = nx.Graph()
        self._nodi = []
        self._archi = []
        self._dizionarioAeroporti = {}
        self._lista_aereoporti = DAO.getAllAirports()
        for a in self._lista_aereoporti:
            self._dizionarioAeroporti[a.ID] = a


    def buildGraph(self, min):
        # NODI
        self._nodi = DAO.getNodes(min, self._dizionarioAeroporti)
        self._grafo.add_nodes_from(self._nodi)

        # ARCHI
        connessioni = DAO.getEdges(self._dizionarioAeroporti)
        for c in connessioni:
            if c.aPartenza in self._grafo and c.aArrivo in self._grafo:
                if self._grafo.has_edge(c.aPartenza, c.aArrivo):
                    self._grafo[c.aPartenza][c.aArrivo]["weight"] += c.voli
                else:
                    self._grafo.add_edge(c.aPartenza, c.aArrivo, weight=c.voli)