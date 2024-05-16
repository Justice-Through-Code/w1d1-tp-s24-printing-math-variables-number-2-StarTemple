# W1D1-Printing-Math-Variables-Number-2

**\# Grade Calculator**

This Python script calculates the average grade for a student based on their scores in three subjects: Math, Science, and English.

**\## Instructions**

1\. Accept the assignment invitation on GitHub Classroom.

2\. Clone the repository to your local machine.

3\. Open the `grade_calculator.py` file.

4\. Implement the grade calculator script according to the following steps:
   \- Prompt the user to enter their name using the `input()` function and store it in a variable called `student_name`.
   \- Prompt the user to enter their scores for three subjects: Math, Science, and English. Store each score in separate variables: `math_score`, `science_score`, and `english_score`.
   \- Convert the entered scores from strings to integers using the `int()` function.
   \- Calculate the average grade by adding the three scores and dividing the result by 3. Store the result in a variable called `average_grade`.
   \- Print the student's name and average grade using formatted strings.
   \- Add meaningful comments throughout the script to explain the purpose of each section or line of code.

5\. Test your script with different score inputs to ensure it calculates the average grade correctly.

6\. Run the provided unit tests using PyTest:
   ```
   pytest test_grade_calculator.py
   ```

7\. If the tests pass, commit and push your changes to the GitHub repository.

8\. Check the repository on GitHub. If your implementation is correct, you should see a green checkmark indicating that the tests have passed.

9\. If the tests fail, review and fix your code, then repeat steps 7 and 8.

10\. Once your implementation passes the tests and you see a green checkmark on GitHub, copy the link to your GitHub repository.

11\. Go to the Canvas assignment page and submit the link to your GitHub repository in the submission box.

**\## Getting Started**

1\. Install PyTest if you haven't already:
   ```
   pip install pytest
   ```

2\. Run the script to calculate the average grade:
   ```
   python grade_calculator.py
   ```

   Enter the student's name and scores for Math, Science, and English when prompted. The script will display the student's name and average grade.

**\## Files**

\- `grade_calculator.py`: The main script that implements the grade calculator functionality.
\- `test_grade_calculator.py`: The unit tests for the grade calculator script using PyTest.

**\## Requirements**

\- Python 3.x
\- PyTest (can be installed using `pip install pytest`)
\- GitHub account
\- GitHub Classroom invitation link

**\## Acknowledgments**

This project is based on the learning materials for the course "Introduction to Python Programming".
