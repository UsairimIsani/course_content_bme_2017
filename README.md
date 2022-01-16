![NED University of Engineering and Technology](./extra/nedlogo.png){ width=300px height=300px style="margin: auto;" }

# Course Codes and Content for Biomedical Engineering
## NED University of Engineering and Technology, Karachi, Pakistan.

Due to the unavailability of course contents from the department of Biomedical Engineering at NED University of Engineering and Technology, this series of markdown were compiled by 

## Process to create a pdf/docx from markdown files.
### Prerequisites
- pandoc
- latex tools
- vscode
- linux

```bash
pandoc --pdf-engine=xelatex --toc --toc-depth=2 -V geometry:margin=1in \
    course_content/* -o course_content_bme_2017.pdf
pandoc  -V geometry:margin=1in README.md -o README.pdf


```