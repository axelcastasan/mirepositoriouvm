import threading
import time

semaphore = threading.Semaphore(1)

def tarea (id):
    print (f"Cliente {id} esta intentando retira de su banco")
    with semaphore:
        print (f"Cliente {id} ha retirado su dinero")
        time.sleep(2)
        print (f"Cliente {id} ha salido del banco")

threads = []
for i in range (5):
    thread = threading.Thread(target=tarea, args=(i,))
    threads.append (thread)
    thread.start()

for thread in threads:
    thread.join()
