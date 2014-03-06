class Atleta:

	def __init__(self, uidatleta, nome, rg, endereco, uidesporte = []):
		self.uidatleta = uidatleta
		self.nome = nome
		self.rg = rg
		self.endereco = endereco
		self.uidesporte = uidesporte

	def inserirEsporte(self,uidesporte):
		self.uidesporte.append(uidesporte)

	def verificaEsporte(self,uidesporte):
		return uidesporte in self.uidesporte

	

