import time
import queue

fila_processos = queue.Queue()

def simular_fila_impressao():
    for i in range(5, 0, -1):
        time.sleep(0.7)
        fila_processos.put(f"Processo {i}")
        while not fila_processos.empty():
            processo = fila_processos.get()
            mensagem = f"{processo} está usando a impressora..."
            mensagemAux = f"o processo {i - 1} está aguardando sua vez."
            if i != 1:
             print(mensagem + mensagemAux)
            else:
                print(mensagem)
    time.sleep(2)
    
simular_fila_impressao()