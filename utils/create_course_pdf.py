import pandas as pd
import os
with open('course_codes/course_credit_hours.csv') as csv_file:
    courses = pd.read_csv(csv_file, dtype=object, delimiter=";")
    courses.columns = courses.columns.str.strip()
    for course_index, course in courses.iterrows():
        name = "_".join(course['name'].lower().strip().split(" "))
        full_name = f"{course['code'].strip()}_{name}"
        os.system(
            f"pandoc --pdf-engine=xelatex -V geometry:margin=1in course_content/{full_name}.md -o pdf/{full_name}.pdf")
