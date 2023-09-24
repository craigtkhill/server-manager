from src.job import Job
import random


class JobGenerator:
    def __init__(self) -> None:
        self.__jobs = []

    def generate(self) -> Job:
        job = Job(id=random.randint(1, 10000), workload=random.randint(1, 100))
        self.__jobs.append(job)
        return job
