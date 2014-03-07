import unittest
from should_dsl import should
from socio import Socio
from clube import Clube

class SocioSpec(unittest.TestCase):

	def it_creates_a_socio_object (self):
		clube = Clube('001', '339.221.008/0001-12', 'Sport Clube LDTA', 'Rua America Santos','(22) 2711-1234')
		socio = Socio('002', 'Pedro','123.546.789-1', 'Rua dos Passos',clube)
		socio.uidsocio |should| equal_to('002')
		socio.nome |should| equal_to('Pedro')
		socio.rg |should| equal_to('123.546.789-1')
		socio.endereco |should| equal_to('Rua dos Passos')
		socio.clube |should| equal_to(clube)
		socio.valor_salario |should| equal_to(724)

	def it_calcularMensalidade(self):
		clube = Clube('001', '339.221.008/0001-12', 'Sport Clube LDTA', 'Rua America Santos','(22) 2711-1234')
		socio = Socio('002', 'Pedro','123.546.789-1', 'Rua dos Passos',clube)
		socio.calcularMensalidade() |should| equal_to(72.4)

