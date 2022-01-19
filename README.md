<img align="centre" src="extra/nedlogo.png" height="300px" width="300px"/>

<h1 align="centre">NED University of Engineering and Technology, Karachi, Pakistan.</h1>
<h2 align="centre">Course Codes and Content for Biomedical Engineering batch 2017.</h2>

Due to the unavailability of course contents from the department of Biomedical Engineering at NED University of Engineering and Technology, this series of markdowns were compiled by [Usairim Isani](https://www.linkedin.com/in/usairimisani/)

All Course Contents can be verified from other department websites from [NED University of Engineering and Technology](https://www.neduet.edu.pk/) and [HEC](https://hec.gov.pk/english/services/universities/RevisedCurricula/Documents/New%20Curricula/Biomedical%20EngineeringBS.pdf).

---

## PDFs 
[PDFs](pdf) for all courses

## Markdown
[Markdowns](course_content) for all courses

## Combined PDF
[course_content_bme_2017](course_content_bme_2017)


---
## Process to create a pdf/docx from markdown files.
### Prerequisites
- pandoc
- latex tools
- vscode
- linux

```bash
# To generate complete course contents using pandoc
pandoc --pdf-engine=xelatex --toc --toc-depth=2 -V geometry:margin=1in course_content/* -o pdf/course_content_bme_2017.pdf

# To generate pdf of CONTENTS
pandoc -f markdown+emoji --variable mainfont="DejaVu Sans"  --pdf-engine=xelatex  -V geometry:margin=1in CONTENT.md -o pdf/CONTENT.pdf

# To generate pdf of README
pandoc  -V geometry:margin=1in README.md -o pdf/README.pdf

# A python utility to create PDFs for each course.
python3 utils/create_pdfs.py
```

Please send in a PR if you find issues or inaccuracies.