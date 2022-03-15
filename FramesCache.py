class FramesCache:
    """
    Simple implementation of circular queue.
    Which allows to store last n number of frames.
    And gives method to dump all frames in sequence so going from tail -> head direction
    With preserving original sequence of saving.
    This implementation is needed because videos which I will personally use are going to be 1 hour long
    So this array would grow into enormous sizes.

    flag circled is needed because on first `circle` tail doesn't need to updated.
    But after this it needs to increment same as head.
    """

    def __init__(self, size):
        self.size = int(size)
        self.queue = [None] * self.size
        self.head = 0
        self.tail = 1
        self.circled = False

    def append(self, frame):
        self.queue[self.head] = frame

        if self.circled:
            if self.tail is self.size - 1:
                self.tail = 0
            else:
                self.tail += 1

        if self.head is self.size - 1:
            self.head = 0
            self.circled = True
        else:
            self.head += 1

    def dump(self):
        return self.queue[self.tail - 1:self.size] + self.queue[0: self.head]
