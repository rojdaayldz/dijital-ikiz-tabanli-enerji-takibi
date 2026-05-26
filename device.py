
class Device:
    def __init__(self, name, power, room):
        self.name = name
        self.power = power
        self.room = room
        self.is_on = False
        self.usage_hours = 0

    def turn_on(self):
        self.is_on = True

    def turn_off(self):
        self.is_on = False

    def set_usage_hours(self, hours):
        self.usage_hours = hours

    def get_consumption(self):
        if self.is_on:
            return (self.power * self.usage_hours) / 1000
        return 0