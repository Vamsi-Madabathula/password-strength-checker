import re

def check_password_strength(password):
    score = 0
    suggestions = []

    if len(password) >= 8:
        score += 1
    else:
        suggestions.append("Use at least 8 characters")

    if re.search(r"[A-Z]", password):
        score += 1
    else:
        suggestions.append("Add uppercase letters")

    if re.search(r"[a-z]", password):
        score += 1
    else:
        suggestions.append("Add lowercase letters")

    if re.search(r"[0-9]", password):
        score += 1
    else:
        suggestions.append("Include numbers")

    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        suggestions.append("Use special characters")

    return score, suggestions

def main():
    password = input("Enter your password: ")
    score, suggestions = check_password_strength(password)

    print(f"\nStrength Score: {score}/5")

    if score == 5:
        print("Strong Password!")
    elif score >= 3:
        print("Medium Password")
    else:
        print("Weak Password")

    if suggestions:
        print("\nSuggestions:")
        for s in suggestions:
            print("-", s)

if __name__ == "__main__":
    main() 