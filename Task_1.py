from queue import Queue
import random


queue = Queue()


def generate_request():

    request = {"id": str(random.randint(1, 1000)),
               "data": str(random.randint(1, 100000))}
    queue.put(request)


def process_request():
    if not queue.empty():
        request = queue.get()
        print(f"Обробка заявки id {request['id']} даними: {request['data']}")

    else:
        print("Черга порожня")


while True:
    generate_request()
    process_request()

    user_input = input("Для виходу введіть 'exit': ")
    if user_input.lower() == 'exit':
        break
