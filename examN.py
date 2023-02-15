import random
from string import ascii_lowercase

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