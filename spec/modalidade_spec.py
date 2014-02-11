import unittest
from should_dsl import should
from modalidade import Modalidade

class ModalidadeSpec(unittest.TestCase):

	def it_creates_a_modalidade_object (self):
		modalidade = Modalidade('001', 'natacao','R$30.00')

		modalidade.uidmodalidade |should| equal_to('001')
		modalidade.nome |should| equal_to('natacao')
		modalidade.valor_hora |should| equal_to('R$30.00')
		
