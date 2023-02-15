from string import ascii_lowercase

# number the questions themselves 
# present the question text above the answer alternatives. 
# Additionally, you’ll use lowercase letters instead of numbers to identify answers

QUESTIONS = {
 "What's the purpose of the built-in zip() function": [
  "To iterate over two or more sequences at the same time",
  "To combine several strings into one",
  "To compress several files into one archive",
  "To get information from the user",
 ],
 "What's the name of Python's sorting algorithm": [
  "Timsort", "Quicksort", "Merge sort", "Bubble sort"
 ],
 "What does dict.get(key) return if key isn't found in dict": [
  "None", "key", "True", "False",
 ]
}

for num, (question, alternatives) in enumerate(QUESTIONS.items(), start=1):
 print(f"\nQuestion {num}:")
 print(f"{question}?")
 correct_answer = alternatives[0]
 labeled_alternatives = dict(zip(ascii_lowercase, sorted(alternatives)))
 for label, alternative in labeled_alternatives.items():
  print(f"  {label}) {alternative}")

 answer_label = input("\nChoice? ")
 answer = labeled_alternatives.get(answer_label)
 if answer == correct_answer:
  print("⭐ Correct! ⭐")
 else:
  print(f"The answer is {correct_answer!r}, not {answer!r}")

# Use string.ascii_lowercase to get letters that label your answer alternatives.
# Combine letters and alternatives with zip() and store them in a dictionary as follows:
""" 
>>> import string
>>> dict(zip(string.ascii_lowercase, ["1771", "1781", "1871", "1881"]))
{'a': '1771', 'b': '1781', 'c': '1871', 'd': '1881'}
"""

QUESTIONS = {
 "What does dict.get(key) return if key isn't found in dict": [
  "None", "key", "True", "False",
 ],
 "How do you iterate over both indices and elements in an iterable": [
  "enumerate(iterable)",
  "enumerate(iterable, start=1)",
  "range(iterable)",
  "range(iterable, start=1)",
 ],
}

# Keep Score
# Now that you’re numbering the questions, it would also be nice to keep track of how many questions the user answers correctly. 
# You can add a variable, num_correct, to take care of this:

num_correct = 0  # keeps track of how many questions the user answers correctly
for num, (question, alternatives) in enumerate(QUESTIONS.items(), start=1):  # num loop variable counts the total number of questions
 print(f"\nQuestion {num}:")
 print(f"{question}?")
 correct_answer = alternatives[0]
 labeled_alternatives = dict(zip(ascii_lowercase, sorted(alternatives))) # Combine letters and alternatives with zip() and store them in a dictionary
 for label, alternative in labeled_alternatives.items():
  print(f"  {label}) {alternative}")
 
 answer_label = input("\nChoice? ")
 answer = labeled_alternatives.get(answer_label)
 if answer == correct_answer:
  num_correct += 1          # increase num_correct for each correct answer
  print("⭐ Correct! ⭐")
 else:
  print(f"The answer is {correct_answer!r}, not {answer!r}")
 
 print(f"\nYou got {num_correct} correct out of {num} questions")  # use num loop variable to report the user’s result

