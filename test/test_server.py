import unittest
from src.server import Server


class TestServer(unittest.TestCase):
    def test_init(self):
        server = Server()
        self.assertIsNotNone(server)

    def test_capacity(self):
        server = Server(100)
        self.assertEqual(server.get_capacity(), 100)

    def test_do_job(self):
        server = Server(100)
        self.assertEqual(server.do_job(10), 100)

    def test_state(self):
        server = Server(100)
        self.assertEqual(server.get_state(), "inactive")

    def test_start(self):
        server = Server(100)
        server.set_state("active")
        self.assertEqual(server.get_state(), "active")

    def test_stop(self):
        server = Server(100)
        server.set_state("active")
        server.set_state("inactive")
        self.assertEqual(server.get_state(), "inactive")

    def test_idle(self):
        server = Server(100)
        server.set_state("idle")
        self.assertEqual(server.get_state(), "idle")
