import threading
            

def interrupcao(evento):
    print("Esperando evento de interrupção...")
    evento.wait()
    print("Evento detectado! Processando...")
    
evento_interrupcao = threading.Event()
threading.Thread(target=interrupcao, args=(evento_interrupcao,), daemon=False).start()

print('Envie um sinal para o Sistema apertando qualquer tecla.')
input()
evento_interrupcao.set()


