from sortedcontainers import SortedDict

class MyCalendarThree:
    def __init__(self):
        self.bookings = SortedDict()
        
    def book(self, start: int, end: int) -> int:
        self.bookings[start] = self.bookings.get(start, 0) + 1
        self.bookings[end] = self.bookings.get(end, 0) - 1
        pointer, k = 0, 0
        for differential in self.bookings.values():
            pointer = pointer + differential
            k = max(k, pointer)
        return k

# Your MyCalendarThree object will be instantiated and called as such:
# obj = MyCalendarThree()
# param_1 = obj.book(start,end)