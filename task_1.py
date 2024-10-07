import queue
import random as r
import time

q = queue.Queue()

def generate_request():
    ''' Генерация заявок '''
    id = r.randint(1, 100)
    print(f"Сгенерирована новая заявка {id}")
    q.put(id)

def process_request():
    if not q.empty():
        id = q.get()
        print(f"Заявка {id} обрабатывается")
        time.sleep(1)
        print(f"Заявка {id} обработана")
    else:
        print("Очередь пуста")

def main():
    while True:
        generate_request() 
        process_request()
        time.sleep(0.5) 

if __name__ == "__main__":
        main()  
