class Time:
    def __init__(self, hh, mm, ss):
        self.hour = hh
        self.minute = mm
        self.second = ss
        self.fix()

    def show(self):
        print(self.hour, ":", self.minute, ":", self.second)

    def fix(self):
        if self.second >= 60:
            self.second -= 60
            self.minute += 1
        if self.minute >= 60:
            self.minute -= 60
            self.hour += 1
        if self.second < 0:
            self.second += 60
            self.minute -= 1
        if self.minute < 0:
            self.minute += 60
            self.hour -= 1

    def sum(self, other):
        s_new = self.second+other.second
        m_new = self.minute+other.minute
        h_new = self.hour+other.hour
        result = Time(h_new, m_new, s_new)
        return (result)

    def minus(self, other):
        s_new = self.second-other.second
        m_new = self.minute-other.minute
        h_new = self.hour-other.hour
        result = Time(h_new, m_new, s_new)
        return (result)

    def time_to_second(self):
        h_sec = self.hour*3600
        m_sec = self.minute*60
        result = h_sec+m_sec+self.second
        return (result)

    def second_to_time(self, other):
        h_new = 0
        m_new = 0
        while other >= 3600:
            h_new += 1
            other -= 3600
        while other >= 60:
            m_new += 1
            other -= 60
        result = Time(h_new, m_new, other)
        return (result)

    def GMT_to_tehran(self, other):
        h_teh = other.hour+3
        m_teh = other.minute+30
        result = Time(h_teh, m_teh, other.second)
        return (result)


# Create two Time objects
time1 = Time(10, 45, 30)  # 10:45:30
time2 = Time(2, 15, 50)   # 02:15:50

# Test show() method
print("Time 1:")
time1.show()  # Expected output: 10 : 45 : 30
print("Time 2:")
time2.show()  # Expected output: 02 : 15 : 50

# Test sum() method
print("\nSum of Time 1 and Time 2:")
sum_time = time1.sum(time2)
sum_time.show()  # Expected output: 13 : 01 : 20

# Test minus() method
print("\nDifference between Time 1 and Time 2:")
diff_time = time1.minus(time2)
diff_time.show()  # Expected output: 08 : 29 : 40

# Test time_to_second() method
print("\nTime 1 in seconds:", time1.time_to_second())  # Expected output: 39330

# Test second_to_time() method
seconds = 4760
print("\nConvert", seconds, "seconds to Time format:")
time_from_seconds = time1.second_to_time(seconds)
time_from_seconds.show()  # Expected output: 01 : 19 : 20

# Test GMT_to_tehran() method
print("\nConvert Time 1 from GMT to Tehran time:")
tehran_time = time1.GMT_to_tehran(time1)
# Expected output depends on the initial time, adjusted for Tehran's timezone (GMT+3:30)
tehran_time.show()
