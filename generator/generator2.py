class Week:
    def __init__(self):
        self.days = {1: "Mon", 2: "Tue",
                     3: "Wen", 4: "Thu",
                     5: "Fri", 6: "Sat", 7: "San"}

    def week_gen(self):
        for x in self.days:
            yield self.days[x]


if __name__ == "__main__":
    wk = Week()
    iter1 = wk.week_gen()
    iter2 = iter(wk.week_gen())
    print("iter1", iter1.__next__())
    print("iter2", iter2.__next__())
    print("iter1", next(iter1))
    print("iter2", next(iter2))
    print("iter1", next(iter1))
    print("iter2", next(iter2))
    print("iter1", iter1.__next__())
    print("iter2", iter2.__next__())