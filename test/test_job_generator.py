import unittest
from src.job_generator import JobGenerator


class TestJobGenerator(unittest.TestCase):
    def test_init(self):
        job_generator = JobGenerator()
        self.assertIsNotNone(job_generator)

    def test_generate(self):
        job_generater = JobGenerator()
        job = job_generater.generate()
        self.assertIsNotNone(job)
        self.assertIsNotNone(job.get_id())
        self.assertIsNotNone(job.get_workload())
