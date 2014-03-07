class Esporte:

	def __init__(self, uidesporte, nome, valor_hora, uidmodalidade = [], uidatleta = [] ):
		self.uidesporte = uidesporte
		self.nome = nome
		self.valor_hora = valor_hora
		self.uidmodalidade = uidmodalidade
		self.uidatleta = uidatleta

	def inserirModalidade(self,uidmodalidade):
		self.uidmodalidade.append(uidmodalidade)

	def inserirAtleta(self,uidatleta):
		self.uidatleta.append(uidatleta)

	def verificaModalidade(self,uidmodalidade):
		return uidmodalidade in self.uidmodalidade

	def verificaAtleta(self,uidatleta):
		return uidatleta in self.uidatleta


	'''def consulta_atletas(self):
		relatorio = ''
		for objeto in self.uidatleta:
			relatorio += ('%s faz esporte:\n %s'%(objeto.nome,self.nome)) 
		return relatorio '''
