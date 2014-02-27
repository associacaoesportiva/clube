class Clube:

	def __init__(self, uidclube, cnpj, nome, endereco, telefone, uidesporte = [], uidsocio = [], uiddependencias = [],atleta=None, modalidade=None):
		self.uidclube = uidclube
		self.cnpj = cnpj
		self.nome = nome
		self.endereco = endereco
		self.telefone = telefone

		self.uidesporte = uidesporte
		self.uidsocio = uidsocio
		self.uiddependencias = uiddependencias
		self.atleta = atleta
		self.modalidade = modalidade


	def inserirEsporte(self,uidesporte):
		self.uidesporte.append(uidesporte)

	def verificaEsporte(self,uidesporte):
		return uidesporte in self.uidesporte



	def inserirSocio(self,uidsocio):
		self.uidsocio.append(uidsocio)

	def verificaSocio(self,uidsocio):
		return uidsocio in self.uidsocio



	def inserirDependencias(self,uiddependencias):
		self.uiddependencias.append(uiddependencias)

	def verificaDependencias(self,uiddependencias):
		return uiddependencias in self.uiddependencias




