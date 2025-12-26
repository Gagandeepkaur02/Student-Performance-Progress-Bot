import pandas as pd
import random
from datetime import datetime, timedelta

students = range(1, 151)   # 150 students
subjects = ["Math", "Science", "English", "Computer"]
records = []

start_date = datetime(2024, 1, 1)

for student in students:
    for subject in subjects:
        score = random.randint(40, 90)
        for test in range(3):  # 3 tests
            records.append([
                student,
                subject,
                score + random.randint(-5, 5),
                (start_date + timedelta(days=test*30)).strftime("%Y-%m-%d")
            ])

df = pd.DataFrame(records, columns=["StudentID", "Subject", "Score", "Date"])
df.to_csv("student_data.csv", index=False)

print("Dummy data for 150 students created!")