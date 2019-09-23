from secrets import SystemRandom
from string import ascii_uppercase as alphabet


class Robot(object):
    def __init__(self):
        self.name = ''
        self.reset()

    def reset(self):
        secure_random = SystemRandom()
        letters = secure_random.sample(alphabet, 2)
        numbers = secure_random.sample(range(10), 3)
        numbers = [str(number) for number in numbers]
        self.name = ''.join(letters + numbers)
