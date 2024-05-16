def calculate_average_grade():
    # Prompt the user to enter their name
    student_name = input("Please enter your name: ")

    # Prompt the user to enter their scores for Math, Science, and English
    math_score = int(input("Enter your Math score: "))
    science_score = int(input("Enter your Science score: "))
    english_score = int(input("Enter your English score: "))

    # Calculate the average grade
    total_score = math_score + science_score + english_score
    average_grade = total_score / 3

    return student_name, average_grade
