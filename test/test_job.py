import unittest
from src.job import Job


class TestJob(unittest.TestCase):
    def test_init(self):
        job = Job(id=1, workload=2)
        self.assertIsNotNone(job)

    def test_id(self):
        job = Job(id=1, workload=2)
        self.assertIsNotNone(job.get_id())

    def test_workload(self):
        job = Job(id=2, workload=1)
        self.assertIsNotNone(job.get_workload())
