import unittest
from src.server_manager import ServerManager
from src.server import Server


class TestServerManager(unittest.TestCase):
    def test_init(self):
        server_manager = ServerManager()
        self.assertIsNotNone(server_manager)

    def test_add_server(self):
        server_manager = ServerManager()
        server = Server()
        server_manager.add_server(server)
        self.assertEqual(server_manager.get_num_servers(), 1)

    def test_start_server(self):
        server_manager = ServerManager()
        server = Server()
        server_manager.add_server(server)
        server_manager.start_server(0)
        self.assertEqual(server_manager.get_server_state(0), "active")

    def test_stop_server(self):
        server_manager = ServerManager()
        server = Server()
        server_manager.add_server(server)
        server_manager.start_server(0)
        server_manager.stop_server(0)
        self.assertEqual(server_manager.get_server_state(0), "inactive")

    def test_check_capacity(self):
        server_manager = ServerManager()
        server = Server(10)
        server_manager.add_server(server)
        server_manager.start_server(0)
        self.assertEqual(server_manager.check_capacity(0), True)
