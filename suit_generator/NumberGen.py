import random


class NumberGen:

    def __init__(self, name, value, minimum, maximum, dict_poss_val):
        self.name = name
        self.value = value
        self.minimum = minimum
        self.maximum = maximum + 1
        self.dict_poss_val = dict_poss_val

    def get_init_value(self):
        return self.init_value

    def get_minimum(self):
        return self.minimum

    def get_maximum(self):
        return self.maximum

    def get_name(self):
        return self.name

    def set_value(self, value):
        self.value = value

    def get_value(self):
        return self.value

    def set_minimum(self, minimum):
        self.minimum = minimum

    def set_maximum(self, maximum):
        self.maximum = maximum

    def mutate(self):
        self.set_value(random.choice(list(self.dict_poss_val.keys())))
        return self.get_value()
