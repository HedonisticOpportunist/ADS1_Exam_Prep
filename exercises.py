class Exercises:
    """
    These exercises are from the revision sheet
    shared in the lecture
    """
    def __init__(self):
        self.threshold = 10
        self.is_divisible = False
        self.output = None

    def smaller_than(self, number: int):
        """
        Checks whether a number is above or
        below a certain threshold
        :param number:
        :return: The threshold number if it
        has been, otherwise the number itself
        is returned
        """
        if number < self.threshold:
            print("The number is smaller as the threshold.")
            print("ฅ(*ΦωΦ*) ฅ")
            return number
        else:
            print("The number is larger or the same as the threshold.")
            print("(*Φ皿Φ*)")
            return self.threshold

    def divisible_by_three(self, integer: int):
        """
        Checks whether a number is divisible by
        three
        :param integer:
        :return: true if the number is divisibly by three,
        false otherwise
        """
        if integer % 3 == 0:
            self.is_divisible = True
            print("The number is divisible by three.")
            print("^ↀᴥↀ^")
            return self.is_divisible
        else:
            print("The number is not divisible by three.")
            print("ლ(●ↀωↀ●)ლ")
            return self.is_divisible

    def greatest_common_divisor(self, integer_one: int, integer_two: int):
        """
        :param integer_one:
        :param integer_two:
        :return: The greatest common divisor
        """
        self.output = integer_one
        while self.output != integer_two:
            if self.output > integer_two:
                self.output = self.output - integer_two
            else:
                integer_two = integer_two - self.output
        if self.output == integer_two:
            print("The greatest common divisor is: " + str(self.output))
            print("(^・ω・^ )")
            return self.output

