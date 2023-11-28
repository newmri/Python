from question_model import Question
from quiz_brain import QuizBrain
import requests
from ui import QuizInterface

URL = "https://opentdb.com/api.php?"

param = {"amount" : 10, "type" : "boolean"}
response = requests.get(URL,param)
response.raise_for_status()

question_data = response.json()["results"]

question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz_ui = QuizInterface(QuizBrain(question_bank))