class Job:
    def __init__(self, id, workload) -> None:
        self.__id = id
        self.__workload = workload

    def get_id(self) -> int:
        return self.__id

    def get_workload(self) -> int:
        return self.__workload
