import unittest
from should_dsl import should
from clube import Clube

from esporte import Esporte
from socio import Socio
from dependencias import Dependencias
from atleta import Atleta
from modalidade import Modalidade

class clubeSpec(unittest.TestCase):

    def it_creates_a_clube_object (self):
	    modalidade = Modalidade('001', 'natacao')
	    atleta = Atleta('001', 'Maria','002.222.011-9','Rua dos Andrades')
	    clube = Clube('001', '339.221.008/0001-12','Sport clube LDTA','Rua America Santos','(22) 2711-1234',[],[],[],atleta,modalidade)
	    clube.uidclube |should| equal_to('001')
	    clube.cnpj |should| equal_to('339.221.008/0001-12')
	    clube.nome |should| equal_to('Sport clube LDTA')
	    clube.endereco |should| equal_to('Rua America Santos')
	    clube.telefone |should| equal_to('(22) 2711-1234')
	    clube.uidesporte |should| equal_to([])
	    clube.uidsocio |should| equal_to([])
	    clube.uiddependencias |should| equal_to([])
	    clube.modalidade |should| equal_to(modalidade)
	    clube.atleta |should| equal_to(atleta)

#def: para FK esporte.

    def it_inserir_esporte(self):  

        clube = Clube('001', '339.221.008/0001-12', 'Sport clube LDTA', 'Rua America Santos','(22) 2711-1234')
        
        esporte = Esporte('001','volei',clube) 
        
        clube.inserirEsporte(esporte)
        (esporte in clube.uidesporte) |should| equal_to(True) 
    
    
    def it_verificar_esporte(self):

        clube = Clube('001', '339.221.008/0001-12', 'Sport clube LDTA', 'Rua America Santos','(22) 2711-1234')
        
        esporte = Esporte('001','volei',clube)
        
        clube.inserirEsporte(esporte)
        clube.verificaEsporte(esporte) |should| equal_to(True)

    def it_inserir_socio(self):  

		clube = Clube('001', '339.221.008/0001-12', 'Sport clube LDTA', 'Rua America Santos','(22) 2711-1234')
        
		socio = Socio('002', 'Pedro','123.546.789-1', 'Rua dos Passos',clube) 
        
		clube.inserirSocio(socio)
		(socio in clube.uidsocio) |should| equal_to(True) 
    
    
    def it_verificar_socio(self):

        clube = Clube('001', '339.221.008/0001-12', 'Sport clube LDTA', 'Rua America Santos','(22) 2711-1234')
        
        socio = Socio('002', 'Pedro','123.546.789-1', 'Rua dos Passos',clube)
        
        clube.inserirSocio(socio)
        clube.verificaSocio(socio) |should| equal_to(True)

    def it_verificar_dependencias(self):

        clube = Clube('001', '339.221.008/0001-12', 'Sport clube LDTA', 'Rua America Santos','(22) 2711-1234')
        
        dependencias = Dependencias('001', 'piscina','200m',clube)
        
        clube.inserirDependencias(dependencias)
        clube.verificaDependencias(dependencias) |should| equal_to(True)

    def it_inserir_dependencias(self):  

        clube = Clube('001', '339.221.008/0001-12', 'Sport Clube LDTA', 'Rua America Santos','(22) 2711-1234')
        
        dependencias = Dependencias('001', 'piscina','200m',clube) 
        
        clube.inserirDependencias(dependencias)
        (dependencias in clube.uiddependencias) |should| equal_to(True) 
    