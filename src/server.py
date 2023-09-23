class Server:
    def __init__(self, capacity=5) -> None:
        self.__capacity = capacity
        self.__state = "inactive"

    def get_capacity(self) -> int:
        return self.__capacity

    def do_job(self, job_size: int) -> int:
        return job_size * 10

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
