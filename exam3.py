# Handle User Errors
# Handle user errors by allowing the user to re-enter their answer when they enter something invalid. 
# One way to do this is to wrap input() in a while loop:

from string import ascii_lowercase

QUESTIONS = {
 "How do you iterate over both indices and elements in an iterable": [
  "enumerate(iterable)",
  "enumerate(iterable, start=1)",
  "range(iterable)",
  "range(iterable, start=1)",
 ],
 "What's the official name of the := operator": [
  "Assignment expression",
  "Named expression",
  "Walrus operator",
  "Colon equals operator",
 ],
}

num_correct = 0 # keeps track of how many questions the user answers correctly
for num, (question, alternatives) in enumerate(QUESTIONS.items(), start=1): # num loop variable counts the total number of questions
 print(f"\nQuestion {num}:")
 print(f"{question}?")
 correct_answer = alternatives[0]
 labeled_alternatives = dict(zip(ascii_lowercase, sorted(alternatives))) # # Combine letters and alternatives with zip() and store them in a dictionary 
 for label, alternative in labeled_alternatives.items():
  print(f"  {label}) {alternative}")
 
 while (answer_label := input("\nChoice? ")) not in labeled_alternatives: # wrap input() in while loop to allow the user to re-enter their answer when they enter something invalid
  print(f"Please answer one of {', '.join(labeled_alternatives)}") # this provides the alternative answers
 
 answer = labeled_alternatives[answer_label]
 if answer == correct_answer:
  num_correct += 1  # increase num_correct for each correct answer
  print("⭐ Correct! ⭐")
 else:
  print(f"The answer is {correct_answer!r}, not {answer!r}")

print(f"\nYou got {num_correct} correct out of {num} questions")  # use num loop variable to report the user’s result