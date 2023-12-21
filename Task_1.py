from queue import Queue
import random
import uuid

queue = Queue()


def generate_request():

    request = {"id": str(uuid.uuid4()),
               "data": str(random.randint(1, 100000))}
    queue.put(request)


def process_request():
    if not queue.empty():
        request = queue.get()
        print(f"Обробка заявки id {request['id']} з даними: {request['data']}")

    else:
        print("Черга порожня")


try:

    while True:
        generate_request()
        process_request()


except KeyboardInterrupt:
    print("Програму завершено")

# Завершити Ctrl+C
