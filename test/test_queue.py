import unittest
from src.queue import Queue
from src.job import Job


class TestQueue(unittest.TestCase):
    def test_init(self):
        queue = Queue()
        self.assertIsNotNone(queue)

    def test_enqueue(self):
        queue = Queue()
        job = Job(id=1, workload=2)
        queue.enqueue(job)
        self.assertEqual(len(queue._queue), 1)

    def test_dequeue(self):
        queue = Queue()
        job = Job(id=1, workload=2)
        queue.enqueue(job)
        job = queue.dequeue()
        self.assertEqual(len(queue._queue), 0)
        self.assertIsNotNone(job)
        self.assertEqual(job.get_id(), 1)
        self.assertEqual(job.get_workload(), 2)

    def test_dequeue_empty(self):
        queue = Queue()
        job = queue.dequeue()
        self.assertEqual(len(queue._queue), 0)
        self.assertIsNone(job)
