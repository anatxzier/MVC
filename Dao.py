from random import *
Arquivo = "ToDo.txt"

class DaoAdicionar:
    def __init__(self,tarefa):
        self.tarefa = tarefa

    def AdicionarTarefa(self):
        with open(Arquivo, "a") as arquivo:
            arquivo.write(self.tarefa)
        return True

class DaoMudar:
    def mudarTarefa(self, tarefa_Antiga, tarefa_Nova):
        with open(Arquivo, "r") as arquivo:
            conteudo = arquivo.read()

        conteudo_Atualizado = conteudo.replace(tarefa_Antiga, tarefa_Nova)
        with open(Arquivo, "w") as arquivo2:
            arquivo2.write(conteudo_Atualizado)
        return True
    
        
class DaoListar:
    def listar(self):
        with open(Arquivo, "r") as arquivo:
            linhas = arquivo.readlines()
        return linhas