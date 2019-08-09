import random
import string


class StringGen:

    def __init__(self, name, required, value, size):
        self.name = name
        self.required = required
        self.value = value
        self.size = size

    def get_required(self):
        return self.required

    def get_value(self):
        return self.value

    def set_value(self, value):
        self.value = value

    def get_name(self):
        return self.name

    def set_size(self, size):
        self.size = size

    def get_size(self):
        return self.size

    def mutate(self):
        size = self.get_size()
        chars = string.ascii_lowercase + size*" "
        self.set_value(''.join(random.choice(chars) for _ in range(size)))
        return self.get_value()