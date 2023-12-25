class Week:
    def __init__(self):
        self.days = {1: "Mon", 2: "Tue",
                     3: "Wen", 4: "Thu",
                     5: "Fri", 6: "Sat", 7: "San"}

    def __iter__(self):
        return WeekIterator(self.days)


class WeekIterator:
    def __init__(self, days):
        self.days_ref = days
        self._index = 1

    def __next__(self):
        if self._index < 1 | self._index > 8:
            raise StopIteration
        else:
            ret_value = self.days_ref[self._index]
            self._index += 1
        return ret_value


if __name__ == "__main__":
    wk = Week()
    iter1 = iter(wk)
    iter2 = iter(wk)
    print("iter1", iter1.__next__())
    print("iter2", iter2.__next__())
    print("iter1", next(iter1))
    print("iter2", next(iter2))
    print("iter1", next(iter1))
    print("iter2", next(iter2))
    print("iter1", iter1.__next__())
    print("iter2", iter2.__next__())