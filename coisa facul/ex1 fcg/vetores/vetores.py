import math

# classe base para os vetores contendo os métodos comuns
class vetor:

# aqui eu estou definindo a magnitude do vetor usando a lib math (é só matemática)
    def magnitude(self):
        return math.sqrt(sum(v*v for v in self.to_list()))

# aqui estou normalizando o vetor após calcular a magnitude, também deixando um backup caso a mag seja zero
    def normalizar(self):
        mag = self.magnitude()
        if mag == 0:
            return
        for attr in self.__slots__:
            setattr(self, attr, getattr(self, attr) / mag)

# aqui estão as operações básicas de soma, sub e escalares
    def soma(self, outro):
        valores = [a + b for a, b in zip(self.to_list(), outro.to_list())]
        return self.__class__(*valores)

    def sub(self, outro):
        valores = [a - b for a, b in zip(self.to_list(), outro.to_list())]
        return self.__class__(*valores)

    def escalar(self, k):
        valores = [v * k for v in self.to_list()]
        return self.__class__(*valores)

    def dividir(self, k):
        valores = [v / k for v in self.to_list()]
        return self.__class__(*valores)

# aqui estou calculando o produto escalar usando a função zip para iterar sobre os componentes dos vetores
    def dot(self, outro):
        return sum(a*b for a, b in zip(self.to_list(), outro.to_list()))

# este é o método de cópia que foi requisitado
    def copiar(self):
        return self.__class__(*self.to_list())

# este outro método facilita a conversão do vetor para uma lista, que deixa os cálculos mais simples e o print mais bonito
    def to_list(self):
        return [getattr(self, attr) for attr in self.__slots__]

# este método é só para facilitar a visualização do vetor quando der print, mostrando o nome da classe e os valores dos componentes de modo limpo
    def __str__(self):
        valores = ", ".join(map(str, self.to_list()))
        return f"{self.__class__.__name__}({valores})"

# classes herdadas dos vet2 3 e 4 com os componentes em float e usando slots (boa prática)
class vet2(vetor):

    __slots__ = ("x","y")

    def __init__(self, x=0.0, y=0.0):
        self.x = float(x)
        self.y = float(y)

class vet3(vetor):

    __slots__ = ("x","y","z")

    def __init__(self, x=0.0, y=0.0, z=0.0):
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)

class vet4(vetor):

    __slots__ = ("x","y","z","w")

    def __init__(self, x=0.0, y=0.0, z=0.0, w=0.0):
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)
        self.w = float(w)

# por fim este é o teste que montei para ver se não tem erros, caso queira testar também dê um "py vetores.py"
v1 = vet2(1,2)
v2 = vet2(3,4)

print(v1)
print(v2)

print(v1.soma(v2))
print(v1.sub(v2))

print(v1.dot(v2))

print(v1.magnitude())

v3 = v1.copiar()
print(v3)