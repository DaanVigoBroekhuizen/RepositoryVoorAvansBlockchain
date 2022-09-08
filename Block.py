import time

class Block:
    def __init__(self, index, data, prevHash) -> None:
        self.index = index
        self.time = time.ctime()
        self.prevHash = prevHash
        self.data = data

        self.hash = hash((self.index, self.time, self.prevHash, self.data))