class QueueItem:
    def __init__(self, priority, item):
        self.priority = priority
        self.item = item


class PriorityQueue:
    def __init__(self):
        self.queue = []

    def is_empty(self):
        return len(self.queue) == 0

    def push(self, priority, item):
        # Worst case complexity time of O(n)
        # Take the item and its assigned priority as a QueueItem
        queue_item = QueueItem(priority, item)
        # Check the queue and insert it based on its priority
        for index in range(0, len(self.queue)):
            if self.queue[index].priority >= queue_item.priority:
                self.queue.insert(index, queue_item)
                break
        if queue_item not in self.queue:
            self.queue.append(queue_item)

    def pop(self):
        if self.is_empty():
            return 'Queue Empty'
        return self.queue.pop(0).item

    def peek(self):
        if self.is_empty():
            return 'Queue Empty'
        return self.queue[0].element

    def get_length(self):
        return len(self.queue)