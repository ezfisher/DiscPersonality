
class UserInput:

#function to record user answers from test

    def __init__(self, tester_answer):
        self.tester_answer = input()

    def __str__(self):
        return f"user input is {self.tester_answer}"