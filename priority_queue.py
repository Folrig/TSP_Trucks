# James Spencer  ID: 000486930


class QueueItem:
    # A class where each item has a priority
    # where lower value is higher priority
    # i.e. #1 priority is 1
    def __init__(self, priority, item):
        self.priority = priority
        self.item = item


class PriorityQueue:
    # A class to store and manipulate QueueItems
    # based upon their priority value
    def __init__(self):
        self.queue = []

    def is_empty(self):
        return len(self.queue) == 0

    def push(self, priority, item):
        # Take the item and its assigned priority as a QueueItem
        # Worst case complexity time of O(n)
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
