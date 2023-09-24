import unittest
from src.server_manager import ServerManager
from src.server import Server
from src.job import Job
from src.clock import Clock


class TestServerManager(unittest.TestCase):
    def test_init(self):
        server_manager = ServerManager()
        self.assertIsNotNone(server_manager)

    def test_add_server(self):
        server_manager = ServerManager()
        job = Job(1, 2)
        server_manager.add_job(job)
        self.assertEqual(server_manager.get_num_servers(), 1)

    def test_start_server(self):
        server_manager = ServerManager()
        job = Job(1, 2)
        server_manager.add_job(job)
        server_manager.start_server(0)
        self.assertEqual(server_manager.get_server_state(0), "active")

    def test_stop_server(self):
        server_manager = ServerManager()
        job = Job(1, 2)
        server_manager.add_job(job)
        server_manager.start_server(0)
        server_manager.stop_server(0)
        self.assertEqual(server_manager.get_server_state(0), "inactive")

    def test_check_capacity(self):
        server_manager = ServerManager()
        job = Job(1, 2)
        server_manager.add_job(job)
        server_manager.start_server(0)
        self.assertEqual(server_manager.check_capacity(0), True)

    def test_add_job(self):
        server_manager = ServerManager()
        job = Job(1, 2)
        server_manager.add_job(job)
        self.assertEqual(len(server_manager.servers[0].get_jobs()), 0)

    def test_idle_servers(self):
        server_manager = ServerManager()
        job = Job(1, 2)
        server_manager.add_job(job)
        server_manager.idle_servers()
        self.assertEqual(server_manager.get_server_state(0), "idle")
