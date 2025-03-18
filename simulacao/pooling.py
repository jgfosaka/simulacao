import time
import threading

haEventos = False


def pooling():
    while not haEventos:
        time.sleep(0.5) 
        print("\nVerificando se há eventos...")

evento_interrupcao = threading.Event()
threading.Thread(target=pooling, daemon=True).start()

evento_interrupcao.set()
input()
haEventos = True
print('Sinal recebido.')

