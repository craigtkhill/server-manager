from src.server_manager import ServerManager
from src.server import Server
from src.job_generator import JobGenerator
from src.clock import Clock
from src.queue import Queue

server_manager = ServerManager()

for i in range(10):
    server_manager.add_server(Server())
    server_manager.start_server(i)

clock = Clock()

job_generator = JobGenerator()

queue = Queue()

while True:
    # sleep every second. 
    # each object tracks its own time.
    # it can use the abstractions in the clock object
    # their states change based on time.
    clock.tick_random(2, 5)
    job = job_generator.generate()
    queue.enqueue(job)
    clock.tick_random(1, 3)
    job = queue.dequeue()
    server_manager.add_job(job)

    break
