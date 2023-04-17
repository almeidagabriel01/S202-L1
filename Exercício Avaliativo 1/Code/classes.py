class Passageiro:
    def __init__(self, nome: str, documento: str):
        self.nome = nome
        self.documento = documento
            
class Corrida:
    def __init__(self, nota_corrida: int, distancia: float, valor: float, passageiro: Passageiro):
        self.nota_corrida = nota_corrida
        self.distancia = distancia
        self.valor = valor
        self.passageiro = passageiro
        
class Motorista:
    def __init__(self, nota_motorista: int, corridas: tuple):
        self.nota_motorista = nota_motorista
        self.corridas = corridas