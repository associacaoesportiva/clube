import unittest
from should_dsl import should
from dependencias import Dependencias

class DependenciasSpec(unittest.TestCase):

	def it_creates_a_dependencias_object (self):
		dependencias = Dependencias('001', 'piscina','200m')

		dependencias.uiddependencias |should| equal_to('001')
		dependencias.nome |should| equal_to('piscina')
		dependencias.capacidade |should| equal_to('200m')
		
