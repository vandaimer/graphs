from DirectGraph import DirectGraph
from collections import OrderedDict
from pprint import pprint
from sys import exit


g = DirectGraph()
g.addVertex("Grafos", {'c':4})
g.addVertex("IA", {'c':4})
g.addVertex("SOI", {'c':4})
g.addVertex("SOII", {'c':4})
g.addVertex("Distribuida", {'c':4})
g.addVertex("Calc A", {'c':4})
g.addVertex("Calc B", {'c':4})
g.addVertex("Calc nº", {'c':4})
g.addVertex("Estatística", {'c':4})
g.addVertex("GA", {'c':4})
g.addVertex("AL", {'c':4})
g.addVertex("Segurança", {'c':4})
g.addVertex("Formais", {'c':4})
g.addVertex("Compiladores", {'c':4})

g.connect("GA", "AL")
g.connect("Calc A", "Calc B")
g.connect("Calc A", "Estatística")
g.connect("Calc B", "Calc nº")
g.connect("SOI", "SOII")
g.connect("SOI", "Distribuida")
g.connect("Grafos", "IA")
g.connect("Formais", "Compiladores")


potes = {}
pote = 0
creditos = 0
def proxSemestres(disciplinas):
    global creditos
    global pote
    global potes

    for b in disciplinas:
        credito = g.attrs[b]['c']
        if (creditos+credito) <= 28:
            if not potes.get(pote):
                potes[pote] = {'total_creditos': 0, 'disciplinas': []}
            potes[pote]['disciplinas'].append(b)
        else:
            potes[pote]['total_creditos'] = creditos
            pote += 1
            potes[pote] = {'total_creditos': 0, 'disciplinas': []}
            potes[pote]['disciplinas'].append(b)
            creditos = 0
        creditos += credito

    potes[pote]['total_creditos'] = creditos
    creditos = 0
    pote += 1


# Obtem a ordenação topológica
ordering = g.topologicalOrdering()
"""
    Pega a base e orderna a mesma.
    Se precisar de dois semestres para completar as disciplinas base,
    então as disciplinas com menos crédito serão cursadas inicialmente,
    para que não seja criado semestres desnecessários.

    Ordenar a base faz parte da resolução, é NECESSÁRIO ordernar
"""
base = sorted(g.getBase(), key=lambda b: g.attrs[b]['c'])
# Obtem as outras disciplinas que não fazem parter da base
others = [x for x in ordering if x not in base]
# Executa o algoritmo para a base, primeiramente
proxSemestres(base)
# Execute o algoritmo para as outras disciplinas
proxSemestres(others)
pprint(potes)
