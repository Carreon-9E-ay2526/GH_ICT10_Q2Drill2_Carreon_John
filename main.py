#Drill2: Set Operators
from pyscript import display, document

grade_7 = {'Jarence Manacap', 'Isabelle Cabatu'}
grade_8 = {'Joel Gonzales', 'Gabrielle Cortez'}
grade_9 = {'Amanda Bower', 'Hans Baquiran'}
grade_10 = {'John Carreon', 'Nathan Bautista', 'Jaden Galvez', 'Chester Roxas'}

all_members = grade_7 | grade_8 | grade_9 | grade_10

def submit(e):
    club_applicant = str(document.getElementById('firstname').value)
    club_applicant1 = str(document.getElementById('lastname').value)

    new_applicant = club_applicant + " " + club_applicant1

    all_members.add(new_applicant)

    display_message = f"All members:<br>{'<br>'.join(sorted(all_members))}"

    document.getElementById('output').innerHTML = display_message
    display(f"Total Members: {len(all_members)}", target='output')
