from Controller import *
import os

while True:
    def clear():
        os.system("cls")

    def print_menu(opcoes):
        clear()
        print(f"{'-' * 50}\n"
            f"{' ' * 15}Software T0-DO{' ' * 15}\n"
            f"{'-' * 50}\n")
        for i, opcao in enumerate(opcoes):
            cor = "30" if i % 2 == 0 else "37"
            print(f"{i + 1}. {opcao: <25}{': ': <5}".format(cor=cor, descricao=opcao.split()[1]))


    opcoes = ["Adicionar Tarefa : ➕", "Listar Tarefas : 📋", "Alterar Tarefa : 📝", "Concluir Tarefa : ✅", "Listar Tarefas Concluidas : ☑️", "Excluir Tarefa : ➖", "Sair : ❌"]
    print_menu(opcoes)
    opção = input(">> ")
    match opção:
        case "1":
            print("Adiconar Tarefa")
            tarefa = input("Digite a nova tarefa: ")
            adicionartarefa = ControllerAdicionarTarefa(tarefa)
            os.system("pause")
            os.system("cls")        

        case "2":
            print("Lista de tarefas")
            listartarefa = ControllerListarTarefa("A")
            os.system("pause")
            os.system("cls")      

        case "3":
            print("Alterar tarefa")
            listartarefa = ControllerListarTarefa("A")
            indice = input("Digite o indice da tarefa para ser alterada: ")
            tarefa_nova = input("Digite a nova tarefa: ")
            mudartarefa = ControllerMudarTarefa(tarefa_nova, indice, "A")
            os.system("pause")
            os.system("cls")      

        case "4":
            print("Concluir tarefa")
            print("Tarefas existentes:")
            listartarefa = ControllerListarTarefa("A")
            indice = input("Digite o índice da tarefa para ser concluida: ")
            excluirtarefa = ControllerMudarTarefa("  ", indice, "C")
            os.system("pause")
            os.system("cls")

        case "5":
            print("Lista de tarefas concluidas")
            listartarefa = ControllerListarTarefa("C")
            os.system("pause")
            os.system("cls")   

        case "6":
            print("Exluir tarefa")
            print("Tarefas Existentes")
            listartarefa = ControllerListarTarefa("A")
            indice = input("Digite o índice da tarefa para ser excluida: ")
            excluirtarefa = ControllerMudarTarefa("  ", indice, "E")
            os.system("pause")
            os.system("cls")

        case "7":
            break
            
        case _:
            print("Inválido")