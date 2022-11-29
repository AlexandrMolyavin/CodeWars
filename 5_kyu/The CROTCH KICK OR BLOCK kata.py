https://www.codewars.com/kata/528aa29bd8a0399fc5000cae
class dark_room:
    def __init__(self, kick_from):
        self.kick_from = kick_from
        self.position = 0
        self.block_count = 0
        self.blocked = False

    def __call__(self, block=False):
        self.position += 1

        if block:
            self.block_count += 1
            if self.kick_from == self.position:
                self.blocked = True

        return self

    def end(self):
        return "BLOCK" if self.block_count == 1 and self.blocked else "CROTCH KICK"
