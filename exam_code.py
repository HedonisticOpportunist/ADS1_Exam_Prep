import math


class ExamCode:
    """
    This code is related to any pseudo related
    questions found in previous exam papers and / or
    practice exams
    """

    def __init__(self):
        self.stack = []

    def make_stack(self, numbers):
        """
        Create a stack out of a given array
        :param numbers:
        :return:
        """
        array_length = len(numbers)

        for i in range(math.floor(array_length / 2)):
            self.stack.append(numbers[i])

        print("The stack is: " + str(self.stack))
        print("\ō͡≡o˞̶ \ō͡≡o˞̶ \ō͡≡o˞̶ \ō͡≡o˞̶")
        return self.stack
