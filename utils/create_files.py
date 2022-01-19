import pandas as pd

with open('course_codes/course_credit_hours-semi-delimited.csv') as csv_file:
    courses = pd.read_csv(csv_file, dtype=object, delimiter=";")
    courses.columns = courses.columns.str.strip()
    for course_index, course in courses.iterrows():
        name = "_".join(course['name'].lower().strip().split(" "))
        file_name = f"course_content/{course['code'].strip()}_{name}.md"
        open(file_name, "w")
