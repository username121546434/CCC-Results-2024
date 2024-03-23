"""
This file reads the pdf results and outputs a csv file
containing information about everyone who got a perfect
score on the CCC, or a 75 out of 75.

Note that this is not perfect and there is still some 
manual work required even after running the script.

The final csv can be found in table.csv
Statistics are available at statistics.ipynb
"""
import fitz
from csv import writer

ignore = [
    '2024',
    'Canadian',
    'Computing',
    'Competition',
    'Results',
    'Sponsors:',
    '1',
    'Student Honour Roll',
    'Palmar`',
    'es d\u2019\xb4',
    'es d\u2019',
    'etudiants',
    'Junior Competitors',
    'Students are listed in alphabetical order within each group.',
    'Dans chaque group, les \xb4',
    'el`',
    'eves sont nomm\xb4',
    'es en ordre alphabetiques.',
    'Name/Nom',
    'School/ \xb4',
    'Ecole',
    'Location/Endroit',
    'Group 1: Scores from 75 to 75',
    'es d�',
    "'es d\xb4'",
    "es d\xb4"
]

with fitz.open(r"C:\Users\athar\Downloads\2024CCCResults.pdf") as pdf, \
     open('table.csv', 'w', newline='') as f:
    csv = writer(f)
    csv.writerow(['Last Name', 'First Name', 'School', 'Location'])
    for pg, page in enumerate(pdf):
        if pg not in range(5):
            continue
        text: str = page.get_textpage().extractTEXT()
        row = []
        for line in text.splitlines():
            if len(row) == 4:
                csv.writerow(row)
                row.clear()
            if line in ignore or line.isdigit():
                continue
            row.append(line)