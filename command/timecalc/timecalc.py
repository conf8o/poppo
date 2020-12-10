from .. import Command


class Timecalc(Command):
    def __init__(self, options, argv):
        self.options = options
        self.argv = argv
        self.FORMAT_ERROR = "incorrect time format.(expected: HH:mm)"
        self.INPUT_ERROR = "incorrect input"
        return
    
    def exec(self):
        print("Calculates the time difference.")
        (h1, m1) = self.input_time(1)
        (h2, m2) = self.input_time(2)

        print("diff")
        print(f"    hour: {abs(h1 - h2)}")
        print(f"    minute: {abs((h1*60 + m1) - (h2*60 + m2))}")

        return

    def input_time(self, n):
        while True:
            t = input(f"time{n} >>").split(":")
            if len(t) != 2:
                print(self.FORMAT_ERROR)
            elif all([self.can_be_int(x) for x in t]):
                return (int(t[0]), int(t[1]))
            else:
                print(self.INPUT_ERROR)

    def can_be_int(self, s):
        try:
            return isinstance(int(s), int)
        except TypeError:
            return False
        except ValueError:
            return False