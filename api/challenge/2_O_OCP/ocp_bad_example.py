'''
OPEN CLOSED PRINCIPLE

Imagine que uma clínica veterinária tem seu sistema próprio para aprovação de exames. No primeiro momento, ela tem um método para
verificar exame de sangue. Em outro ela adiciona exame por raio-x. Notamos no código que, conforme a clínica adiciona exames,
deverão adicionar uma validação para o exame. O que aumentaria a complexidade do código e a manutenção do mesmo.

A solução deste caso pode ser feita com o princípio aberto-fechado (Open Closed Principle). 
Utilizando do conceito do OCP, crie uma interface e classes que implementam a mesma para que, caso a clínica necessite de um novo
tipo de exame, uma nova classe seja adicionada, implementando métodos de uma interface padrão para exames.

'''

from abc import ABC, abstractmethod

class AprovaExame:
    def aprovar_solicitacao_exame(self, exame):

        if exame_sangue.tipo == "sangue":
            if aprovador.verifica_condicoes_exame_sangue(exame_sangue):
                print("Exame sanguíneo aprovado!")

        elif exame_raio_x.tipo == "raio-x":
            if aprovador.verifica_condicoes_raio_x(exame_raio_x):
                print("Raio-X aprovado!")
                pass

    def verifica_condicoes_exame_sangue(self, exame):
        # implemente as condições específicas do exame de sangue
        pass

    def verifica_condicoes_raio_x(self, exame):
        # implemente as condições específicas do exame de raio-x
        pass


# Exemplo de uso:
class Exame:
    def __init__(self, tipo):
        self.tipo = tipo

exame_sangue = Exame("sangue")
exame_raio_x = Exame("raio-x")

aprovador = AprovaExame()



class Exam(ABC):
    def __init__(self, type: str):
      self.type = type
        
    @abstractmethod
    def verify(self): pass
        
    @abstractmethod
    def approve(self): pass
    


class BloodExam(Exam):
    def verify(self):
        return self.type == 'blood'
    
    def approve(self):
        if self.verify(): print('Blood exam approved!')

class XRayExam(Exam):
    def verify(self):
        return self.type == 'x-ray'
    
    def approve(self):
        if self.verify(): print('X-ray exam approved')




class ExamApprover:
    def approve(self, exam: Exam):
        exam.approve() 



bloodExam = BloodExam()
x_ray_exam = XRayExam()

approver = ExamApprover()
approver.approve(bloodExam)
approver.approve(x_ray_exam)