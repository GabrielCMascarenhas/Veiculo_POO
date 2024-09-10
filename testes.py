from moto import Moto
from veiculo import Veiculo
#Instanciando a classe Moto
falcon = Moto("Honda", "Falcon NX4", "abc", 2005, 400)
#Exibir uma informação na tela => 
#  Vai imprimir o RETORNO do método "__str__()"
print(falcon.__str__())

#Instanciando a classe Veiculo
cerato = Veiculo("Kia", "Cerato", "IRL", 2011)

print(cerato.__str__())



    
# Criando uma instância da Classe Veículo
uno = Veiculo("Fiat","Uno","ABC",2005)
print(uno)
print(uno.__str__())




# Abaixo estou instanciando um objeto
#   da Classe Veiculo
meuUno = Veiculo("Fiat", "Uno com Escada", "ABC-1234", 2000)
print(meuUno.get_marca())
print(meuUno.calcularTempoUso())
meuUno.__ano = 2010
print(meuUno.calcularTempoUso())


teuFusca = Veiculo("Volks", "Fusca do Itamar", "DEF-", 1995)

#print(meuUno.calcularTempoUso())
#print(teuFusca.calcularTempoUso())

#print("")