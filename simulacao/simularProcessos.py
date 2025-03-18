import time



def simular_processos():
    qtd = 0
    while True:
        if qtd == 0:
            continuar = str(input("Você gostaria de simular? [S/N]")).upper()
        else: 
            continuar = str(input('Você gostaria de repetir? [S/N]'))
        if continuar == "S":
            estado = "Pronto. O processo está na fila aguardando execução do processador."
            print(estado)
            time.sleep(0.5)
            estado = "Em execução. O processador começou a executar o processo."
            print(estado)
            time.sleep(2)
            estado = "Bloqueado."
            print(estado)
            qtd += 1
        elif continuar == "N":
            break

simular_processos()            