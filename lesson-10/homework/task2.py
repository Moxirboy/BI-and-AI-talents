import csv

# Read data from grades.csv
with open('grades.csv', 'r') as file:
    reader = csv.DictReader(file)
    data = list(reader)

# Process data to calculate average grades per subject
subject_grades = {}

for row in data:
    subject = row['Subject']
    grade = int(row['Grade'])
    if subject not in subject_grades:
        subject_grades[subject] = []
    subject_grades[subject].append(grade)

# Prepare the averages list
averages = []
for subject, grades in subject_grades.items():
    total = sum(grades)
    count = len(grades)
    average = total / count
    # Check if the average is a whole number to format correctly
    if average.is_integer():
        average = int(average)
    else:
        average = round(average, 1)
    averages.append({'Subject': subject, 'Average Grade': average})

# Write the averages to average_grades.csv
with open('average_grades.csv', 'w', newline='') as file:
    fieldnames = ['Subject', 'Average Grade']
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(averages)

print("Average grades have been written to average_grades.csv")
