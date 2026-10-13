from pyscript import document


Grade8_Members = {"SAMANTHA BAUTISTA", "VIKTOR PENA"}
Grade9_Members = {"JILLIAN EUSEBIO", "KHLOE GUTIERREZ", "STEPHANIE TAMBIO", "ALEYNAH REDILLAS", "CHELSI SIBAL", "CHLOE ADLAWAN", "ELEAZAR SALUDEZ", "ELISHA IGLOSO"}
Grade10_Members = {"GEORGINA BANAL", "GEORGINA CAJANDING", "JULIA BERMUDEZ", "ERIN RIOFLORIDO", "MARC CATU", "DANIELLE SANDOVAL"}
Grade11_Members = {"AUDREY TAN", "ENZO MACARANAS", "MAYER CRUZ"}

All_Members = Grade8_Members.union(Grade9_Members).union(Grade10_Members).union(Grade11_Members)

# function for adding a new member
def add_candidate(e):


    # calls first name and last name
    first_name = document.getElementById("first_name").value
    last_name = document.getElementById("last_name").value

    # combines first name and last name, converting it to uppercase to compare it the list
    full_name = (first_name + " " + last_name).upper()

    #add full_name into the list of members
    All_Members.add(full_name)

    messages = [

        "Congratulations " + full_name.title() + 
        "is now added to Dance Club! 🕺"
    ]

    #gets result of all members
    result = messages[0]
    result += f"<br><br>Members List: {', '.join(All_Members)}"
    result += f"<br>Total members: {len(All_Members)}"


    document.getElementById("result").innerHTML = result