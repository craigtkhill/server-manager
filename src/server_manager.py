from src.server import Server


class ServerManager:
    def __init__(self) -> None:
        self.servers = []

    def __str__(self) -> str:
        server_strs = [str(server) for server in self.servers]
        return f"ServerManager(num_servers={len(self.servers)},\
        servers={server_strs})"

    def __add_server(self, server) -> None:
        self.servers.append(server)

    def get_num_servers(self) -> int:
        return len(self.servers)

    def start_server(self, index: int) -> None:
        self.servers[index].set_state("active")

    def stop_server(self, index: int) -> None:
        self.servers[index].set_state("inactive")

    def get_server_state(self, index: int) -> str:
        return self.servers[index].get_state()

    def check_capacity(self, index: int) -> int:
        return self.servers[index].get_capacity() > 0

    def add_job(self, job) -> None:
        if len(self.servers) == 0:
            self.__add_server(Server())
            self.servers[-1].add_job(job)
            return
        for server in self.servers:
            if server.get_capacity() > 0 and server.get_state() == "active":
                server.add_job(job)
            elif server.get_state() == "idle":
                server.set_state("active")
                server.add_job(job)
        else:
            self.__add_server(Server())
            self.servers[-1].add_job(job)

    def idle_servers(self) -> None:
        for server in self.servers:
            if (
                server.get_capacity() == server.get_max_capacity()
                and server.get_state() == "active"
            ):
                server.set_state("idle")

    def draw_jobs(self) -> None:
        num_jobs = 0
        for server in self.servers:
            num_jobs += server.get_num_jobs()
        print("*" * num_jobs)
