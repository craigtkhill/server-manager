class Queue:
    def __init__(self):
        self._queue = []

    def enqueue(self, job):
        self._queue.append(job)

    def dequeue(self):
        if len(self._queue) == 0:
            return None

        return self._queue.pop(0)

    def __str__(self):
        return str(self._queue)
