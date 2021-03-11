from queue import Queue


class Exercises:
    """
    These exercises are from the revision sheet
    shared in the lecture
    """

    def __init__(self):
        self.threshold = 10
        self.is_divisible = False

        self.output = None
        self.queue = None
        self.queue_is_empty = True

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

    def get_number_of_elements_in_queue(self, integer: int, other_integer: int):
        """
        A simple queue implementation
        :param integer:
        :param other_integer:
        :return: the number of elements in the queue
        """
        self.queue = Queue(maxsize=4)
        self.queue.put(integer)
        self.queue.put(other_integer)
        self.queue.get()
        size_of_queue = self.queue.qsize()
        print(size_of_queue)
        print("🐈🐈🐈🐈🐈🐈🐈🐈🐈🐈🐈🐈")
        return size_of_queue

    def calculate_sum(self, queue):
        """
        Calculates the sum of all elements
        in a queue
        :param queue:
        :return: the sum if the queue
        is not empty
        """
        if len(queue) is None:
            print("The queue is empty: ")
            print("( >ω<)♡(>ω< ✿)")
            return self.queue_is_empty
        sum_of_queue = 0
        for i in range(0, len(queue)):
            sum_of_queue = sum_of_queue + queue[i]
        print("The sum of the queue is: " + str(sum_of_queue))
        print("(=•́ܫ•̀=)")
        return sum_of_queue


