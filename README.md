# 🔐 Password Strength Checker

A Python project that evaluates the strength of a password based on common security rules and provides suggestions for improvement.

---

## 📌 Overview

This project helps users create stronger passwords by analyzing input based on multiple criteria such as length, character variety, and complexity. It is designed to demonstrate basic Python concepts and real-world problem solving.

---

## 🚀 Features

* Checks password strength using 5 key criteria:

  * Minimum length (8 characters)
  * Uppercase letters (A–Z)
  * Lowercase letters (a–z)
  * Numbers (0–9)
  * Special characters (!@#$%^&* etc.)
* Generates a strength score (0–5)
* Classifies password as:

  * Weak 
  * Medium 
  * Strong 
* Provides suggestions to improve weak passwords

---

## 🛠️ Technologies Used

* Python
* `re` module (Regular Expressions)

---

## 📂 Project Structure

password-checker/
│── main.py
│── README.md

---

## ▶️ How to Run

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/password-checker.git
   ```

2. Navigate to the project folder:

   ```bash
   cd password-checker
   ```

3. Run the program:

   ```bash
   python main.py
   ```

---

## 🧪 Example Output

Enter your password: Hello123

Strength Score: 3/5
Medium Password

Suggestions:

* Use special characters

---

## 🎯 Learning Outcomes

* Understanding of conditional statements
* Working with functions in Python
* Using regular expressions for pattern matching
* Basic user input handling

---

## 🔮 Future Improvements

* Hide password input using `getpass`
* Add a graphical user interface (GUI)
* Store password strength history
* Add more advanced security checks

---

## 👨‍💻 Author

Vamsi-Madabathula

---

## 📄 License

This project is open-source and available under the MIT License.
