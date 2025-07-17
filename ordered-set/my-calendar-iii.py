class MyCalendarThree:

    def __init__(self):
        self.events = []

    def book(self, startTime: int, endTime: int) -> int:
        self.events.append((startTime, 1))
        self.events.append((endTime, -1))

        self.events.sort()

        booking = 0
        res = 0
        for event in self.events:
            if event[1] == 1:
                booking += 1
                res = max(booking, res)
            else:
                booking -= 1

        return res


# Your MyCalendarThree object will be instantiated and called as such:
# obj = MyCalendarThree()
# param_1 = obj.book(startTime,endTime)