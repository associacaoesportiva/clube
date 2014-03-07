class Socio:
	
	def __init__(self, uidsocio, nome, rg, endereco, clube, valor_salario = 724):
		self.uidsocio = uidsocio
		self.nome = nome
		self.rg = rg
		self.endereco = endereco
		self.clube = clube
		self.valor_salario = valor_salario

	def calcularMensalidade(self):
		return self.valor_salario *0.10


		
