import re

def check_password_strength(password):
    score = 0
    feedback = []

    if len(password) < 6:
        feedback.append("Too short! Use at least 8 characters.")
    elif len(password) < 10:
        feedback.append("Decent length, but try 10+ characters.")
        score += 1
    else:
        feedback.append("Good length.")
        score += 2

    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Add some lowercase letters.")

    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Add some uppercase letters.")

    if re.search(r"[0-9]", password):
        score += 1
    else:
        feedback.append("Add at least one number.")

    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        feedback.append("Add some special characters (e.g. @, #, $, !).")

    common = ['password', '1234', 'qwerty', 'admin', 'letmein']
    if any(c in password.lower() for c in common):
        feedback.append("Avoid common words or patterns (e.g. 'password', '1234').")
        score -= 1

    if score <= 2:
        strength = "🟥 Weak"
    elif score == 3 or score == 4:
        strength = "🟨 Moderate"
    elif score >= 5:
        strength = "🟩 Strong"

    print("\nPassword Strength:", strength)
    print("Score:", score, "/ 6")
    print("\nSuggestions:")
    for item in feedback:
        print("-", item)


if __name__ == "__main__":
    print("Password Strength Tester")
    user_password = input("Enter a password to test: ")
    check_password_strength(user_password)
