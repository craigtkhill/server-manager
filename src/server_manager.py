class ServerManager:
    def __init__(self) -> None:
        self.num_servers = 0
        self.servers = []

    def add_server(self, server) -> None:
        self.num_servers += 1
        self.servers.append(server)

    def get_num_servers(self) -> int:
        return self.num_servers

    def start_server(self, index: int) -> None:
        self.servers[index].set_state("active")

    def stop_server(self, index: int) -> None:
        self.servers[index].set_state("inactive")

    def get_server_state(self, index: int) -> str:
        return self.servers[index].get_state()

    def check_capacity(self, index: int) -> int:
        return self.servers[index].get_capacity() > 0
