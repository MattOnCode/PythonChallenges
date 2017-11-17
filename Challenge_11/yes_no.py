import re


def yesno(user_input):
    """
    Validates whether the input is correct or not.
    :param user_input: The users input.
    :return: Returns false to exit the application, true to continue.
    """
    if re.search(r"\bY\b|\bN\b|\bYES\b|\bNO\b", user_input.upper()):
        return False
    else:
        return True


while yesno(input("Enter Response: ")):
    print("Try again")
print("Finally...")
