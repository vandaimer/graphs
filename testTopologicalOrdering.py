from DirectGraph import DirectGraph
from collections import OrderedDict
from pprint import pprint
from sys import exit


g = DirectGraph()
g.addVertex("Grafos", {'credito':4})
g.addVertex("IA", {'credito':4})
g.addVertex("SOI", {'credito':4})
g.addVertex("SOII", {'credito':4})
g.addVertex("Distribuida", {'credito':4})
g.addVertex("Calc A", {'credito':4})
g.addVertex("Calc B", {'credito':4})
g.addVertex("Calc nº", {'credito':4})
g.addVertex("Estatística", {'credito':4})
g.addVertex("GA", {'credito':4})
g.addVertex("AL", {'credito':4})
g.addVertex("Segurança", {'credito':4})
g.addVertex("Formais", {'credito':4})
g.addVertex("Compiladores", {'credito':4})

g.connect("GA", "AL")
g.connect("Calc A", "Calc B")
g.connect("Calc A", "Estatística")
g.connect("Calc B", "Calc nº")
g.connect("SOI", "SOII")
g.connect("SOI", "Distribuida")
g.connect("Grafos", "IA")
g.connect("Formais", "Compiladores")


semestres = {}
semestre = 0
creditos = 0
def proxSemestres(disciplinas):
    global creditos
    global semestre
    global semestres

    for disc in disciplinas:
        credito = g.attrs[disc]['credito']
        if (creditos+credito) <= 28:
            if not semestres.get(semestre):
                semestres[semestre] = {'total_creditos': 0, 'disciplinas': []}
            semestres[semestre]['disciplinas'].append(disc)
        else:
            semestres[semestre]['total_creditos'] = creditos
            semestre += 1
            semestres[semestre] = {'total_creditos': 0, 'disciplinas': []}
            semestres[semestre]['disciplinas'].append(disc)
            creditos = 0
        creditos += credito

    semestres[semestre]['total_creditos'] = creditos
    creditos = 0
    semestre += 1


# Obtem a ordenação topológica
ordering = g.topologicalOrdering()
"""
    Pega a base e orderna a mesma.
    Se precisar de dois semestres para completar as disciplinas base,
    então as disciplinas com menos crédito serão cursadas inicialmente,
    para que não seja criado semestres desnecessários.

    Ordenar a base faz parte da resolução, é NECESSÁRIO ordernar
"""
base = sorted(g.getBase(), key=lambda disc: g.attrs[disc]['credito'])
# Obtem as outras disciplinas que não fazem parter da base
disciplinas_nao_base = [x for x in ordering if x not in base]
# Executa o algoritmo para a base, primeiramente
proxSemestres(base)
# Execute o algoritmo para as outras disciplinas
proxSemestres(disciplinas_nao_base)
pprint(semestres)
