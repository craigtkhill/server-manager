class Server:
    def __init__(self, capacity=5) -> None:
        self.__max_capacity = capacity
        self.__capacity = capacity
        self.__state = "active"
        self.__jobs = []

    def __str__(self) -> str:
        return f"Server(capacity={self.__capacity}, state={self.__state})"

    def get_capacity(self) -> int:
        return self.__capacity

    def add_job(self, job) -> None:
        self.__capacity -= 1
        self.__jobs.append(job)
        self.do_job()

    def get_jobs(self) -> list:
        return self.__jobs

    def do_job(self) -> None:
        job = self.__jobs.pop()
        wait_time = job.get_workload()
        self.finished_job()
        return wait_time

    def finished_job(self) -> None:
        self.__capacity += 1

    def get_state(self) -> str:
        return self.__state

    def set_state(self, state: str) -> None:
        if state == "active":
            self.__start()
        elif state == "inactive":
            self.__stop()
        elif state == "idle":
            self.__idle()

    def __start(self):
        self.__state = "active"

    def __stop(self):
        self.__state = "inactive"

    def __idle(self):
        self.__state = "idle"

    def get_max_capacity(self) -> int:
        return self.__max_capacity

    def get_num_jobs(self) -> int:
        return len(self.__jobs)
