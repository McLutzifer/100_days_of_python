from question_model import Question
from open_trivia import question_data
from quiz_brain import QuizBrain

question_bank = []  
for element in question_data:   
    question_bank.append(Question(element["question"], element["correct_answer"]))  # FIX


quiz = QuizBrain(question_bank) 
while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz")
print(f"your score is {quiz.score}/{quiz.question_number}")
