class QuisGAME:
    def __init__(self):

        self.questions = [
            {"question": "The capital of France is Paris.", "answer": True},
            {"question": "2 + 3 equals 7.", "answer": False},
            {"question": "Ibn Sina is a philosopher.", "answer": True}
        ]
        self.score = 0

    def start(self):
        print("Welcome to the True or False Quiz!")

        for i, q in enumerate(self.questions):

            user_answer = input(f"Q{i + 1}: {q['question']} (True/False): ")

            if user_answer.lower() == str(q['answer']).lower():
                print("Correct!")
                self.score += 1
            else:
                print("Wrong!")


        print(f"\nYour final score is: {self.score}/{len(self.questions)}")


        if self.score == len(self.questions):
            print("Congratulations! You won the quiz!")
        else:
            print("Sorry, you lost the quiz. Better luck next time!")
