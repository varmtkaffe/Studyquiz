# Expand Your Quiz Functionality
# Questions with multiple correct answers
# Hints that can point toward the correct answer
# Explanations that can act as teaching moments

import random
from string import ascii_lowercase

import pathlib
try:
 import tomllib
except ModuleNotFoundError:
 import tomli as tomllib

NUM_QUESTIONS_PER_QUIZ = 5
QUESTIONS_PATH = pathlib.Path(__file__).parent / "questions.toml"


def run_quiz():
  questions = prepare_questions(
    QUESTIONS_PATH, num_questions=NUM_QUESTIONS_PER_QUIZ
  )

  num_correct = 0
  for num, question in enumerate(questions, start=1): # keep a counter that numbers the questions you ask
    print(f"\nQuestion {num}:")
    num_correct += ask_question(question)
  print(f"\nYou got {num_correct} correct out of {num} questions")


def prepare_questions(path, num_questions):
  topic_info = tomllib.loads(path.read_text()) # reads to topic label from the toml file
  topics = {
    topic["label"]: topic["questions"] for topic in topic_info.values() #  
  }

  questions = tomllib.loads(path.read_text())["questions"] # reads the TOML file and picks out the questions from list
  num_questions = min(num_questions, len(questions))
  return random.sample(questions, k=num_questions)



def ask_question(question):
 #print(f"START{question['answer']}END")
 correct_answers = question["answer"]
 alternatives = [question["answer"]] + question["alternatives"]
 ordered_alternatives = random.sample(alternatives, k=len(alternatives))

 answers = get_answers(
  question=question["question"],
  alternatives=ordered_alternatives,
  num_choices=len(correct_answers),
 )
 if set(answers) == set(correct_answers):
  print("⭐ Correct! ⭐")
  return 1
 else:
  is_or_are = " is" if len(correct_answers) == 1 else "s are"
  print("\n- ".join([f"No, the answer{is_or_are}:"] + correct_answers))
  return 0


# Allow Multiple Correct Answers
def get_answers(question, alternatives, num_choices=1):
 print(f"{question}?")
 labeled_alternatives = dict(zip(ascii_lowercase, alternatives))
 for label, alternative in labeled_alternatives.items():
  print(f"  {label}) {alternative}")

 while True:
  plural_s = "" if num_choices == 1 else f"s (choose {num_choices})"
  answer = input(f"\nChoice{plural_s}? ")
  answers = set(answer.replace(",", " ").split())

  # Handle invalid answers
  if len(answers) != num_choices:
   plural_s = "" if num_choices == 1 else "s, separated by comma"
   print(f"Please answer {num_choices} alternative{plural_s}")
   continue

  if any(
   (invalid := answer) not in labeled_alternatives
   for answer in answers
   ):
    print(
     f"{invalid!r} is not a valid choice. "
     f"Please use {', '.join(labeled_alternatives)}"
    )
    continue
   
  return [labeled_alternatives[answer] for answer in answers]

if __name__ == " __main__":
 NUM_QUESTIONS_PER_QUIZ = 5
 QUESTIONS_PATH = pathlib.Path(__file__).parent / "questions.toml"
 QUESTIONS = tomllib.loads(QUESTIONS_PATH.read_text())
run_quiz()