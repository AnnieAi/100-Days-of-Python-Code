from question_model import Question
# from data import question_data
from opentdb_data import question_data
from quiz_brain import QuizBrain

question_bank = []

# data preprocessing
for dictionary in question_data:
    ### --- For processing data.py 's question_data --- ###
    # question_text = dictionary["text"]
    # question_answer = dictionary["answer"]
    # new_question = Question(question_text,question_answer)

    # new_question = Question(dictionary["text"], dictionary["answer"])  # Above 3 lines of code just equal to this line
    # question_bank.append(new_question)

    ### --- For processing opentdb_data.py 's question_data --- ###
    new_question = Question(dictionary["question"], dictionary["correct_answer"])
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()


# print("You've completed the quiz.")
# print(f"You final score was: {quiz.score}/{quiz.question_number}")

quiz.show_the_result()