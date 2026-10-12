
from pyscript import display, document

# Add your student names here
best_students = ['miguel piansay', 'mohammad calaca', 'miguel velarde']

def get_name(e):
    document.getElementById('div1').innerHTML = ''

    f_name = document.getElementById('fname').value.strip()
    l_name = document.getElementById('lname').value.strip()

    full_name = f"{f_name} {l_name}".strip().lower()

    student_names = [name.lower() for name in best_students]

    name_checker = full_name in student_names

    display_message = (
        f"Sorry {f_name} {l_name}, your name is not on the list.",
        f"Congratulations {f_name} {l_name}! "
        "You are one of the best grade students!"
    )

    display(display_message[name_checker], target='div1')