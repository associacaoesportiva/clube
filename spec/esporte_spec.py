import unittest
from should_dsl import should
from esporte import Esporte
from modalidade import Modalidade
from atleta import Atleta


class EsporteSpec(unittest.TestCase):
    def it_creates_a_esporte_object (self):
        esporte = Esporte('001', 'volei', 'R$30.00', [],[])
        esporte.uidesporte |should| equal_to('001')
        esporte.nome |should| equal_to('volei')
        esporte.valor_hora |should| equal_to('R$30.00')
        esporte.uidmodalidade |should| equal_to([])
        esporte.uidatleta |should| equal_to([])


    def it_inserir_modalidade(self):  #classe:Modalidade / arquivo_spec:modalidade

        esporte = Esporte('001', 'volei', 'R$30.00') 
        
        modalidade = Modalidade('natacao', esporte) #chave-estrangeira-FK
        
        esporte.inserirModalidade(modalidade)
        (modalidade in esporte.uidmodalidade) |should| equal_to(True) 


    def it_inserir_atleta(self):  

        esporte = Esporte('001', 'volei', 'R$30.00') 
        
        atleta = Atleta('001', 'Maria', '002.222.011-9', 'Rua dos Andrades', esporte)
        
        esporte.inserirAtleta(atleta)
        (atleta in esporte.uidatleta) |should| equal_to(True) 
    
    
    def it_verificar_modalidade(self):

        esporte = Esporte('001', 'volei', 'R$30.00')
        
        modalidade = Modalidade('natacao', esporte)
        
        esporte.inserirModalidade(modalidade)
        esporte.verificaModalidade(modalidade) |should| equal_to(True)

    def it_verificar_atleta(self):

        esporte = Esporte('001', 'volei', 'R$30.00')
        
        atleta = Atleta('001', 'Maria','002.222.011-9','Rua dos Andrades', esporte)
        
        
        esporte.inserirAtleta(atleta)
        esporte.verificaAtleta(atleta) |should| equal_to(True)

    def it_consulta_atletas(self):

        esporte = Esporte('001', 'volei', 'R$30.00')
        
        atleta = Atleta('001', 'Maria','002.222.011-9','Rua dos Andrades', esporte)

        esporte.inserirAtleta(atleta)
        (atleta in esporte.uidatleta) |should| equal_to(True)


        









