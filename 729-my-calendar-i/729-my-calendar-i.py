class MyCalendar:
    def __init__(self):
        self.booked = []

    def book(self, start: int, end: int) -> bool:
        if self.booked ==[]:
            self.booked.append([start,end])
            return True
        else:
            self.booked = sorted(self.booked)
            for x in self.booked:
                if start >= x[0] and start < x[1]:
                    return False
                elif end > x[0] and end <= x[1]:
                    return False
                elif start <= x[0] and end >=x[1]:
                    return False
            self.booked.append([start,end])
            return True


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)