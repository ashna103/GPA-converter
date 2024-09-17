#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Convert UK class honours to 4.0 GPA
#adapted from information supplied by the Fulbright Commission

# Define the UK percentage to US GPA conversion function
def uk_percentage_to_us_gpa(percentage):
    if 70 <= percentage <= 100:
        return 4.0  # First Class Honours (starting at 70%)
    elif 65 <= percentage < 70:
        return 3.7  # Upper Second Class Honours (2:1)
    elif 60<= percentage < 65:
        return 3.3 #Upper second Class Honours (2:1)
    elif 55 <= percentage < 60:
        return 3.0  # Lower Second Class Honours (2:2)
    elif 50 <= percentage <55: 
        return 2.7 #Lower Seond Class Honours (2:2)
    elif 40 <= percentage < 50:
        return 2.3  # Third Class Honours
    else:
        return 0.0  # Fail

# Function to collect user input and compute GPA
def calculate_gpa():
    courses = []

    # Ask for the number of courses
    num_courses = int(input("Enter the number of courses: "))

    # Collect course details
    for i in range(num_courses):
        course_name = input(f"Enter the name of course {i + 1}: ")
        credits = float(input(f"Enter the number of credits for {course_name}: "))
        grade = float(input(f"Enter the grade (percentage) for {course_name}: "))

        # Append course data to list
        courses.append({"name": course_name, "credits": credits, "grade": grade})

    # Initialize total grade points and total credits
    total_grade_points = 0
    total_credits = 0

    # Calculate GPA based on UK-to-US conversion
    for course in courses:
        gpa = uk_percentage_to_us_gpa(course["grade"])
        total_grade_points += gpa * course["credits"]
        total_credits += course["credits"]

    # Calculate final GPA
    gpa_final = total_grade_points / total_credits
    gpa_final = float(round(gpa_final,2))

    # Output the final GPA
    print(f"Your GPA is: {gpa_final:.2f}")

# Run the function to calculate GPA
calculate_gpa()


# In[ ]:





# In[ ]:




