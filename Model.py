from Dao import *

class ToDo:
    def AdicionarTarefas(self, tarefa):
        dao = DaoAdicionar(tarefa)
        return dao.AdicionarTarefa()
    

    def MudarTarefa(self, tarefa_A, tarefa_N):
        dao = DaoMudar()
        return dao.mudarTarefa(tarefa_A, tarefa_N)
    
    
    def ListarTarefa(self):
        dao = DaoListar()
        return dao.listar()

todo = ToDo()