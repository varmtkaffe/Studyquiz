# quiz1.py

answer = input("When was the first known use of the word 'quiz'? ") # input() always returns a text string, even if that string contains only digits
if answer == "1781":
 print("Correct!")
else:
 print(f"The answer is '1781', not {answer!r}") # The f before your quoted string literal inside the else clause indicates that the string is a formatted string, called an f-string.

# Python evaluates expressions inside curly braces ({}) within f-strings and inserts them into the string.  
# !r indicates that answer should be inserted based on its repr() representation. 
# This means that strings are shown surrounded by single quotes, like '1871'

answer = input("Which built-in function can get information from the user? ")
if answer == "input":
 print("Correct!")
else: 
 print(f"The answer is 'input', not {answer!r}")  

# Don’t Repeat Yourself, you should avoid repeated code because it gets hard to maintain.
# or you can do it like this by using Lists and Tuples to Avoid Repetitive Code

#  Stores your questions and answers in the QUESTIONS data structure
QUESTIONS = [
 ("When was the first know use of the word 'quiz'", "1781"), # question element: two-tuple, question text and the answer, comma after each tuple. Comma after each element.
 ("Which built-in function can get information form the user", "input") # question element: two-tuple, the question text , the answer.
 ] # the brackets creates a list which holds the question elements

# loop over each question
for question, correct_answer in QUESTIONS: # for each question, you want access to both the question and answer.
 answer = input(f"{question}? ")
 if answer == correct_answer:
  print("Correct!")
 else:
  print(f"The answer is {correct_answer!r}, not {answer!r}")

# MULTIPLE CHOICE
QUESTIONS = {
 "When was the first known use of the word 'quiz'": [
  "1781", "1771", "1871", "1881"
 ],
 "Which built-in function can get information from the user": [
  "input", "get", "print", "write"
 ],
 "Which keyword do you use to loop over a given list of elements": [
  "for", "while", "each", "loop"
 ],
 "What's the purpose of the built-in zip() function": [
  "To iterate over two or more sequences at the same time",
  "To combine several strings into one",
  "To compress several files into one archive",
  "To get information from the user",
 ],
}

# Loop thru over each item in the QUESTIONS dictionary
# For each question, you pick out the correct answer from the alternatives, and you print out all the alternatives before asking the question:
for question, alternatives in QUESTIONS.items():   
 correct_answer = alternatives[0] # pick out the correct answer from the alternatives, (position 0)
 for alternative in sorted(alternatives):  # change the order of the alternatives by sorting them
  print(f"  - {alternative}") # print out all the alternatives before asking the question
 
 answer = input(f"{question}? ")
 if answer == correct_answer:
  print("Correct!")
 else:
  print(f"The answer is {correct_answer!r}, not {answer!r}")


# Add a label to each alternative and only ask the user to enter the label
# Use enumerate() to print the index of each answer alternative:

QUESTIONS = {
 "Which keyword do you use to loop over a given list of elements": [
  "for", "while", "each", "loop"
 ],
 "What's the purpose of the built-in zip() function": [
  "To iterate over two or more sequences at the same time",
  "To combine several strings into one",
  "To compress several files into one archive",
  "To get information from the user",
 ],
 "What's the name of Python's sorting algorithm": [
  "Timsort", "Quicksort", "Merge sort", "Bubble sort"
 ],
}

for question, alternatives in QUESTIONS.items():
 correct_answer = alternatives[0] # pick out the correct answer from the alternatives, (position 0)
 sorted_alternatives = sorted(alternatives) # store the reordered alternatives as sorted_alternatives
 for label, alternative in enumerate(sorted_alternatives): # Add a label to each alternative, enumerate the sorted alternatives
  print(f"  {label}) {alternative}")  # print the index for each answer alternative
 
 answer_label = int(input(f"{question}? ")) # convert input string to integer before treating it as a list index
 answer = sorted_alternatives[answer_label] # you can look up the full answer based on the answer label that the user enters.
 if answer == correct_answer:
  print("Correct!")
 else:
  print(f"The answer is {correct_answer!r}, not {answer!r}")