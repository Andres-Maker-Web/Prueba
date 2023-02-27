import networkx as nx
import matplotlib.pyplot as plt

class Vertice:
    def __init__(self, id):
        self.id = id
        self.vecinos =[]
        self.visitado = False
        self.padre = None
        self.distancia = float('inf')

    def agregar_vecino(self,v,p):
        if v not in self.vecinos:
            self.vecinos.append([v, p])
class Grafica:
    def __init__(self):
        self.G = nx.Graph()
        self.vertices={}

    def mostrar_grafica(self):
        pos = nx.layout.spring_layout(self.G)
        nx.draw_networkx(self.G, pos)
        labels =nx.get_edge_attributes(self.G, "weigth")
        nx.draw_networkx_edge_labels(self.G, pos, edge_labels=labels)
        plt.show()
    
    def agregar_vertice(self, id):
        if id not in self.vertices:
            self.vertices[id]= Vertice(id)
    
    def agregar_arista(self, vertice_a, vertice_b, peso):
        if vertice_a in self.vertices and vertice_b  in self.vertices:
            self.vertices[vertice_a].agregar_vecino(vertice_b,peso)
            self.vertices[vertice_b].agregar_vecino(vertice_a,peso)

            self.G.add_edge(vertice_a,vertice_b, weight= peso)
    
    def obtener_camino(self, vertice_b):
        camino =[]
        actual = vertice_b
        while(actual != None):
            camino.insert(0,actual)
            actual = self.vertices[actual].padre
        return [camino, self.vertices [vertice_b].distancia]
    
    def minimo (self, lista):
        if len(lista) > 0:
            m = self.vertices[lista[0]].distancia
            v= lista[0]
            for e in lista:
                if m > self.vertices[e].distancia:
                    m= self.vertices[e].distancia
                    v = e
            return v
        
    def dijkstra (self, vertice_a):
        if vertice_a in self.vertices:
            self.vertices[vertice_a].distancia = 0
            actual = vertice_a
            no_visitados= []

            for v in self.vertices:
                if v!= vertice_a:
                    self.vertices[v].distancia = float('inf')
                self.vertices[v].padre = None
                no_visitados.append(v)

            while(len(no_visitados) > 0):
                for vecino in self.vertices[actual].vecinos:
                    if self.vertices[vecino[0]].visitado == False:
                        if self.vertices[actual].distancia + vecino[1] < self.vertices[vecino[0]].distancia:
                            self.vertices[vecino[0]].distancia = self.vertices[actual].distancia + vecino[1]
                            self.vertices[vecino[0]].padre = actual
                
                self.vertices[actual].visitado = True
                no_visitados.remove(actual)

                actual= self.minimo(no_visitados)
        else:
            return False
        
if __name__ =='__main__':
    gr =Grafica()
    gr.agregar_vertice('n0')
    gr.agregar_vertice('n1')
    gr.agregar_vertice('n3')
    gr.agregar_vertice('n4')
    gr.agregar_vertice('n5')
    gr.agregar_vertice('n6')
    gr.agregar_vertice('n8')
    gr.agregar_vertice('n9')
    gr.agregar_vertice('n10')
    gr.agregar_vertice('n11')
    gr.agregar_vertice('n12')
    gr.agregar_vertice('n13')
    gr.agregar_vertice('n14')
    gr.agregar_vertice('n15')
    gr.agregar_vertice('n16')
    gr.agregar_vertice('n17')
    gr.agregar_vertice('n18')
    gr.agregar_vertice('n19')
    gr.agregar_vertice('n20')
    gr.agregar_vertice('n21')
    gr.agregar_vertice('n22')
    gr.agregar_vertice('n23')

    gr.agregar_arista('n0', 'n1', 900)
    gr.agregar_arista('n0', 'n4', 1000)
    gr.agregar_arista('n0', 'n7', 400)
    gr.agregar_arista('n0', 'n8', 140)
    gr.agregar_arista('n0', 'n9', 1000)
    gr.agregar_arista('n0', 'n13', 36)
    gr.agregar_arista('n0', 'n14', 120)
    gr.agregar_arista('n0', 'n15', 650)
    gr.agregar_arista('n0', 'n16', 500)
    gr.agregar_arista('n0', 'n18', 71)
    gr.agregar_arista('n0', 'n19', 230)
    gr.agregar_arista('n0', 'n22', 800)
    gr.agregar_arista('n0', 'n23', 300)
    gr.agregar_arista('n8', 'n5', 600)
    gr.agregar_arista('n8', 'n6', 230)
    gr.agregar_arista('n8', 'n11', 450)
    gr.agregar_arista('n8', 'n14', 120)
    gr.agregar_arista('n6', 'n3', 180)
    gr.agregar_arista('n6', 'n12', 270)
    gr.agregar_arista('n6', 'n17', 450)
    gr.agregar_arista('n6', 'n20', 300)
    gr.agregar_arista('n14','n20',350)
    gr.agregar_arista('n11','n23',300)
    gr.agregar_arista('n3', 'n12', 90)
    gr.agregar_arista('n17', 'n22', 46)
    gr.agregar_arista('n17', 'n14', 350)
    gr.agregar_arista('n22', 'n20', 53)
    gr.agregar_arista('n23', 'n10', 750)

    var = input("ingresa el nodo de inicio:")
    var2 = input("ingresa el nodo final:")
    print("la ruta mas rapida es:")
    gr.dijkstra(var)
    print(gr.obtener_camino(var2))

    gr.mostrar_grafica()




