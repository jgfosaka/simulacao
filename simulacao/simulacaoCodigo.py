from PIL import Image  # Biblioteca Pillow para manipular imagens
import time
import threading
import queue
import os

modo = "usuario"
haEventos = False

fila_processos = queue.Queue()

def comando_kernel(tipo):
    if tipo == 1:
        print("Simulando gerenciamento de memória no modo Kernel...")
        print("Simulando acesso direto ao hardware no modo Kernel...")
        print("Simulando configuração de dispositivos no modo Kernel...")
    elif tipo == 2:
        print("Simulando gerenciamento de memória no modo Kernel...")
        time.sleep(0.75)
        print("Simulando acesso direto ao hardware no modo Kernel...")
        time.sleep(0.75)
        print("Simulando configuração de dispositivos no modo Kernel...")
        time.sleep(0.75)

def comando_usuario(comando):
    if comando == "abrir_arquivo":
        try:
            pastaAtual = os.path.dirname(__file__)
            caminhoImagem = os.path.join(pastaAtual, "naruto.jpg")
            
            imagem = Image.open(caminhoImagem)
            imagem.show()
            print("A imagem 'naruto.jpg' foi aberta com sucesso!")
        except FileNotFoundError:
            print("Erro: O arquivo 'naruto.jpg' não foi encontrado.")
        except Exception as e:
            print(f"Erro ao abrir o arquivo: {e}")
    elif comando == "executar_programa":
        print("Simulando execução de programa no modo Usuário...")
    elif comando == "editar_arquivo":
        try:
            nome_arquivo = "arquivo_simulado.txt"
            with open(nome_arquivo, "w") as arquivo:
                arquivo.write("Conteúdo editado no modo Usuário.\n")
                print(f"Arquivo '{nome_arquivo}' foi editado com sucesso!")
        except Exception as e:
            print(f"Erro ao editar o arquivo: {e}")
    else:
        print("Comando inválido para o modo Usuário.")

def trap():
    global modo
    time.sleep(1)
    if modo == "usuario":
        print("Alternando para o modo Kernel...")
        modo = "kernel"
    else:
        print("Alternando para o modo Usuário...")
        modo = "usuario"
    print(f"Modo atual: {modo}")

def polling():
    while True:
        time.sleep(4)
        if not haEventos:
            print("\nVerificando se há eventos...")
        else: break
            
       

def interrupcao(evento):
    print("Esperando evento de interrupção...")
    evento.wait()
    print("Evento detectado! Processando...")
    

def simular_processos():
    estado = "Bloqueado. Esperando ação do usuário"
    print(estado)
    input("Pressione qualquer tecla.")
    time.sleep(0.5)
    estado = "Pronto. Esperando tempo de CPU."
    print(estado)
    time.sleep(2)
    estado = "Em execução. O processo está sendo executado."
    print(estado)
    
    
    time.sleep(1)

def simular_fila_impressao():
    for i in range(5, 0, -1):
        time.sleep(0.7)
        fila_processos.put(f"Processo {i}")
        while not fila_processos.empty():
            processo = fila_processos.get()
            print(f"{processo} está usando a impressora...")
    time.sleep(2)

def main():
    global modo
    print("Bem-vindo à simulação de um sistema operacional!")
    print("Modo atual:", modo)
    
evento_interrupcao = threading.Event()
threading.Thread(target=polling, daemon=True).start()
threading.Thread(target=interrupcao, args=(evento_interrupcao,), daemon=False).start()

while True:
    time.sleep(1)
    print("\nEscolha uma opção:")
    print("1 - Executar comando")
    print("2 - Alternar modo (TRAP)")
    print("3 - Simular estados de processos")
    print("4 - Simular fila de impressão")
    print("5 - Acionar interrupção")
    print("6 - Sair")
    escolha = input("Digite o número da sua escolha: ")

    if escolha == "1":
        if modo == "usuario":
            comando = input(f"Digite um comando para o modo {modo}: ")
            comando_usuario(comando)
        elif modo == "kernel":
            tipoKernel = int(input("Digite o modo para simulação: \n [1] Kernel Monolítico \n [2] MicroKernel "))
            comando_kernel(tipoKernel)
    elif escolha == "2":
        trap()
    elif escolha == "3":
        simular_processos()
    elif escolha == "4":
        simular_fila_impressao()
    elif escolha == "5":
        evento_interrupcao.set()
        haEventos = True
    elif escolha == "6":
        print("Encerrando a simulação...")
        break
    else:
        print("Opção inválida. Tente novamente.")
        
if __name__ == "__main__":
    main()
