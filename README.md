This project was inspired by https://realpython.com/python-quiz-application/#prerequisites 

# Project Overview
This is a basic Python quiz application that's only capable of asking a question, collecting an answer, and checking whethere the answer is correct. 
From there, I added more features in order to make the app more interestin, user-friendly, and fun. 
The subject is study material the CompTIA Security+ Exam Sy0-601,

 - First we create a basic application that can ask multiple-choice questions.
 - Make the app more user-friendly by improving how it looks and how it handles user errors. 
 - Refactor the code to use functions.
 - Separate question data from source code by storing questions in a dedicated data file.
 - Expand the app to handle multiple correct answers, give hints, and provide explanations. 
 - Add interest by supporting different quiz topics to choose from.

# Organize Your Code With Functions
 - Create functions
 - Remove any questions from the code and organize them in a toml file

# Organize Your Questions With Multiple Toml Files
 - Create a toml file for each quiz topic

# Notes
 - First iteration of this app had the questions in the same file as the functions
 - I decided to not use a SQL database because it would be easier to scale the growing amount of questions

# Environment
 - Python 3.11