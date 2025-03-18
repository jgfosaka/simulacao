# Execução de comandos em kernel ou usuário.
import time
import os
from PIL import Image

modo = "usuario"

def comando_kernel(tipo):
    if tipo == 1:
        print("Simulando gerenciamento de memória no modo Kernel...")
        print("Simulando acesso direto ao hardware no modo Kernel...")
        print("Simulando configuração de dispositivos no modo Kernel...")
        trap()
    elif tipo == 2:
        print("Simulando gerenciamento de memória no modo Kernel...")
        time.sleep(0.75)
        print("Simulando acesso direto ao hardware no modo Kernel...")
        time.sleep(0.75)
        print("Simulando configuração de dispositivos no modo Kernel...")
        time.sleep(0.75)
        trap()

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
        print("Comando inválido para o modo Usuário. Alterando para o modo kernel.")
        trap()
        
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
        
while True:     
    if modo == "usuario":
        comando = input(f"Digite um comando para o modo {modo}: ")
        comando_usuario(comando)
    elif modo == "kernel":
        tipoKernel = int(input("Digite o modo para simulação: \n [1] Kernel Monolítico \n [2] MicroKernel "))
        comando_kernel(tipoKernel)
