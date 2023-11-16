class DoubleElement:
    def __init__(self, *lst):
        self.lst = lst
        self.index = 0

    def __next__(self):
        if self.index < len(self.lst):
            if self.index + 1 < len(self.lst):
                pair = (self.lst[self.index], self.lst[self.index + 1])
            else:
                pair = (self.lst[self.index], None)
            self.index += 2
            return pair
        else:
            raise StopIteration

    def __iter__(self):
        return self

dL = DoubleElement(1, 2, 3, 4)
for pair in dL:
    print(pair)

print()

dL = DoubleElement(1, 2, 3, 4, 5)
for pair in dL:
    print(pair)
