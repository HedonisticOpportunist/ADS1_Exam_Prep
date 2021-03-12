import math


class ExamCode:
    """
    This code is related to any pseudo related
    questions found in previous exam papers and / or
    practice exams
    """

    def __init__(self):
        self.message = ""

    def make_stack(self, numbers):
        """
        Create a stack out of a given array
        :param numbers:
        :return:
        """
        array_length = len(numbers)
        new_stack = []

        for i in range(math.floor(array_length / 2)):
            new_stack.append(numbers[i])

        self.message = "The stack is: " + str(new_stack)
        print(self.message)
        print("\ō͡≡o˞̶ \ō͡≡o˞̶ \ō͡≡o˞̶ \ō͡≡o˞̶")
        return new_stack

    def is_palindrome(self, array) -> bool:
        """
        Checks whether a given array is a palindrome
        :param array:
        :return: true if the array is a palindrome, false otherwise
        """
        if len(array) == 1:
            print("We have a palindrome here of length 1:")
            print("∪･ｪ･∪ ∪･ｪ･∪ ∪･ｪ･∪ ∪･ｪ･∪")
            return True
        else:
            palindrome_stack = self.make_stack(array)
            range_of_stack = math.floor(len(array)) + 1
            for i in range(0, range_of_stack):
                if palindrome_stack[-1] != array[i]:
                    print("This array is not a palindrome.")
                    print("(－_－) zzZ (－_－) zzZ (－_－) zzZ")
                    return True
                else:
                    print("This array is a palindrome.")
                    print("ʕ •̀ ω •́ ʔ ʕ •̀ ω •́ ʔ ʕ •̀ ω •́ ʔ ʕ •̀ ω •́ ʔ")
                    return False
