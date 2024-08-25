marks = int(input("Enter The Marks: "))  # Convert input to integer
if marks >= 90:
    grade = "A"
elif marks >= 80 and marks < 90:
    grade = "B"
elif marks >= 70 and marks < 80:  # Add 'and' here
    grade = "C"
elif marks >= 60 and marks < 70:  # Add 'and' here
    grade = "D"
else:
    grade = "F"

print("Grade:", grade)


