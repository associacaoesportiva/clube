import unittest
from should_dsl import should
from atleta import Atleta
from esporte import Esporte


class AtletaSpec(unittest.TestCase):
    def it_creates_a_atleta_object (self):
	atleta = Atleta('001', 'Maria','002.222.011-9','Rua dos Andrades',[])
	atleta.uidatleta |should| equal_to('001')
	atleta.nome |should| equal_to('Maria')
	atleta.rg |should| equal_to('002.222.011-9')
	atleta.endereco |should| equal_to('Rua dos Andrades')
	atleta.uidesporte |should| equal_to([])


    def it_inserir_esporte(self):  

        atleta = Atleta('001', 'Maria','002.222.011-9','Rua dos Andrades')
        
       	esporte = Esporte('001', 'volei',atleta) 

               
        
        atleta.inserirEsporte(esporte)
        (esporte in atleta.uidesporte) |should| equal_to(True) 
    
    
    def it_verificar_esporte(self):

        atleta = Atleta('001', 'Maria','002.222.011-9','Rua dos Andrades')
        
        esporte = Esporte('001', 'volei',atleta)

        
        
        atleta.inserirEsporte(esporte)
        atleta.verificaEsporte(esporte) |should| equal_to(True)
        









