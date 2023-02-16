# integrate the TOML file into your quiz application
# change how you read the questions from the TOML file

import random
from string import ascii_lowercase

import pathlib
try:
 import tomllib
except ModuleNotFoundError:
 import tomli as tomllib

NUM_QUESTIONS_PER_QUIZ = 5
QUESTIONS_PATH = pathlib.Path(__file__).parent / "questions.toml"
# QUESTIONS = tomllib.loads(QUESTIONS_PATH.read_text())


def run_quiz():
 questions = prepare_questions(
  QUESTIONS_PATH, num_questions=NUM_QUESTIONS_PER_QUIZ
  )
 

 num_correct = 0
 for num, question in enumerate(questions, start=1): # keep a counter that numbers the questions you ask
  print(f"\nQuestion {num}:")
  num_correct += ask_question(question)
 
 print(f"\nYou got {num_correct} correct out of {num} questions")



# implement the necessary preprocessing
# prepare the QUESTIONS data structure so that it's ready to be used in your main loop

def prepare_questions(path, num_questions):  
 questions = tomllib.loads(path.read_text())["questions"] # do the reading of the TOML file and pick out the questions list
 num_questions = min(num_questions, len(questions))
 return random.sample(questions, k=num_questions)



def ask_question(question):
 correct_answer = question["answer"]
 alternatives = [question["answer"]] + question["alternatives"]
 ordered_alternatives = random.sample(alternatives, k=len(alternatives)) # randomly reorder the answer alternatives

 answer = get_answer(question["question"], ordered_alternatives) # handles all details about getting an answer from the user
 if answer == correct_answer: # check the correctness of the answer
  print("⭐ Correct! ⭐")
  return 1  #  indicates to the calling function whether the answer was correct
 else:
  print(f"The answer is {correct_answer!r}, not {answer!r}")
  return 0  #  indicates to the calling function whether the answer was not correct



# This function accepts a question text and a list of alternatives
def get_answer(question, alternatives):
 print(f"{question}?")
 labeled_alternatives = dict(zip(ascii_lowercase, alternatives))
 for label, alternative in labeled_alternatives.items(): # label the alternatives 
  print(f"  {label}) {alternative}")
 
 while (answer_label := input("\nChoice? ")) not in labeled_alternatives: 
  print(f"Please answer one of {', '.join(labeled_alternatives)}") #  ask the user to enter a valid label

 return labeled_alternatives[answer_label] # return the user’s answer


# at the end outside of any function, is called when you run quiz.py as a script, not called when you import quiz as a module
if __name__ == " __main__":
 NUM_QUESTIONS_PER_QUIZ = 5
 QUESTIONS_PATH = pathlib.Path(__file__).parent / "questions.toml"
 QUESTIONS = tomllib.loads(QUESTIONS_PATH.read_text())
run_quiz()