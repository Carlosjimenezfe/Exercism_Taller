class PhoneNumber:
    def __init__(self, number):
        number = ''.join(s for s in number if s.isdigit())
        if len(number) < 10 or len(number) > 10 and int(number[:-10]) > 1 or int(number[-10]) < 2 or int(number[-7]) < 2:
            raise ValueError('Invalid number')
        self.number = number[-10:]
        self.area_code = self.number[:3]
    def pretty(self):
        return f"({self.area_code})-{self.number[3:6]}-{self.number[6:]}"
