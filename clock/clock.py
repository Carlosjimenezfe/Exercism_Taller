class Clock:
    def __init__(self, hour, minute):
        additional_hours, self.minute = divmod(minute, 60)
        self.hour = (hour + additional_hours)%24
    def __repr__(self):
        return f"{self.hour:0>2d}:{self.minute:0>2d}"
    def __eq__(self, other):
        return (self.hour, self.minute) == (other.hour, other.minute)
    def __add__(self, minutes):
        return Clock(self.hour, self.minute + minutes)
    def __sub__(self, minutes):
        return Clock(self.hour, self.minute - minutes)
