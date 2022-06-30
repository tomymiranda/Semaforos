import threading
import time
import logging

logging.basicConfig(format='%(asctime)s.%(msecs)03d [%(threadName)s] - %(message)s', datefmt='%H:%M:%S', level=logging.INFO)

class Cocinero(threading.Thread):
    def __init__(self):
        super().__init__()
        self.name = 'Cocinero'

    def run(self):
        global platosDisponibles
        while True:
            semaCocinero.acquire()
            
      
            try:
                logging.info('Reponiendo los platos...')
                platosDisponibles = 3
            finally:    
                      
                semaPlatos.release()  

class Comensal(threading.Thread):
    def __init__(self, numero):
        super().__init__()
        self.name = f'Comensal {numero}'

    def run(self):
        global platosDisponibles
        
        semaPlatos.acquire()

        try :
            while platosDisponibles==0:
                semaCocinero.release()
                semaPlatos.acquire()
                

            platosDisponibles -= 1
            logging.info(f'¡Qué rico! Quedan {platosDisponibles} platos')
                    
        finally:
            
            semaPlatos.release()
           


platosDisponibles = 3
semaCocinero=threading.Semaphore(0)
semaPlatos=threading.Semaphore(1) 
Cocinero().start()

for i in range(5):
    Comensal(i).start()