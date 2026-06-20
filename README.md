# 🧮 Calculator — Python

> A fully functional terminal-based calculator supporting basic to advanced arithmetic operations — built with pure Python.

![Python](https://img.shields.io/badge/Python-3.x-blue?style=flat&logo=python)
![Type](https://img.shields.io/badge/Type-CLI%20Calculator-green?style=flat)
![Operations](https://img.shields.io/badge/Operations-10+-orange?style=flat)
![Status](https://img.shields.io/badge/Status-Active-brightgreen?style=flat)

---

## 📸 Demo

> _(Terminal screenshot yahan add karo)_

```
============================
     Python Calculator
============================
Select Operation:
  1. Addition       (+)
  2. Subtraction    (-)
  3. Multiplication (*)
  4. Division       (/)
  5. Power          (**)
  6. Square Root    (√)
  7. Modulus        (%)
  8. Exit

Enter choice (1-8): 1
Enter first number : 25
Enter second number: 17
Result: 25 + 17 = 42

Continue? (yes/no): yes
```

---

## 📋 About The Project

A **clean and interactive Python calculator** that runs in the terminal, supporting a wide range of arithmetic operations. Built using core Python — no external libraries needed. Designed with a menu-driven interface for easy use.

**Key Highlights:**
- 10+ arithmetic operations supported
- Input validation — handles invalid inputs and division by zero gracefully
- Continuous calculation mode — no need to restart for multiple calculations
- History feature — view your last 5 calculations
- 100% pure Python — zero dependencies

---

## ✨ Features

- ✅ Basic operations — Addition, Subtraction, Multiplication, Division
- ✅ Advanced operations — Power, Square Root, Modulus, Floor Division
- ✅ Division by zero error handling
- ✅ Invalid input handling with helpful messages
- ✅ Continuous calculation — calculate multiple times in one session
- ✅ Calculation history — view last 5 results
- ✅ Clean menu-driven interface

---

## 🛠️ Tech Stack

| Component | Technology |
|-----------|-----------|
| Language | Python 3.x |
| Libraries | `math` (built-in), `os` (built-in) |
| Interface | Command Line (CLI) |
| Version Control | Git & GitHub |

---

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- Git

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/tomerarvind195-byte/python-calculator.git
cd python-calculator

# 2. Run the calculator
python calculator.py
```

No `pip install` needed — pure Python only!

---

## 🔢 Supported Operations

| # | Operation | Symbol | Example |
|---|-----------|--------|---------|
| 1 | Addition | `+` | 10 + 5 = 15 |
| 2 | Subtraction | `-` | 10 - 5 = 5 |
| 3 | Multiplication | `*` | 10 * 5 = 50 |
| 4 | Division | `/` | 10 / 5 = 2.0 |
| 5 | Power / Exponent | `**` | 2 ** 8 = 256 |
| 6 | Square Root | `√` | √144 = 12.0 |
| 7 | Modulus | `%` | 10 % 3 = 1 |
| 8 | Floor Division | `//` | 10 // 3 = 3 |

---

## 💡 Code Highlights

```python
import math

def calculator():
    history = []

    while True:
        print("\n============================")
        print("     Python Calculator")
        print("============================")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")
        print("5. Power (**)")
        print("6. Square Root (√)")
        print("7. Modulus (%)")
        print("8. View History")
        print("9. Exit")

        choice = input("\nEnter choice (1-9): ")

        if choice == '9':
            print("Goodbye!")
            break

        elif choice == '6':
            num = float(input("Enter number: "))
            if num < 0:
                print("Error: Cannot find square root of negative number!")
            else:
                result = math.sqrt(num)
                print(f"Result: √{num} = {result}")
                history.append(f"√{num} = {result}")

        elif choice in ['1','2','3','4','5','7']:
            num1 = float(input("Enter first number : "))
            num2 = float(input("Enter second number: "))

            if choice == '1':
                result = num1 + num2
                history.append(f"{num1} + {num2} = {result}")
            elif choice == '2':
                result = num1 - num2
                history.append(f"{num1} - {num2} = {result}")
            elif choice == '3':
                result = num1 * num2
                history.append(f"{num1} * {num2} = {result}")
            elif choice == '4':
                if num2 == 0:
                    print("Error: Division by zero is not allowed!")
                    continue
                result = num1 / num2
                history.append(f"{num1} / {num2} = {result}")
            elif choice == '5':
                result = num1 ** num2
                history.append(f"{num1} ** {num2} = {result}")
            elif choice == '7':
                result = num1 % num2
                history.append(f"{num1} % {num2} = {result}")

            print(f"\nResult: {result}")

        elif choice == '8':
            if not history:
                print("No history yet!")
            else:
                print("\n--- Last Calculations ---")
                for h in history[-5:]:
                    print(f"  {h}")

        else:
            print("Invalid choice! Please enter 1-9.")

calculator()
```

---

## 📁 Project Structure

```
python-calculator/
│
├── calculator.py        # Main calculator — run this
└── README.md
```

---

## 🔮 Future Improvements

- [ ] Add GUI using `tkinter`
- [ ] Scientific calculator mode (sin, cos, tan, log)
- [ ] Save history to a `.txt` file
- [ ] Build a web-based calculator using Django
- [ ] Add keyboard shortcut support

---

## 🤝 Contributing

1. Fork the repository
2. Create a new branch (`git checkout -b feature/scientific-mode`)
3. Commit your changes (`git commit -m 'Add scientific calculator mode'`)
4. Push and open a Pull Request

---

## 👨‍💻 Author

**Arvind Kumar**

- 🌐 [LinkedIn](https://www.linkedin.com/in/arvind-kumar-399a60338)
- 💻 [GitHub](https://github.com/tomerarvind195-byte)
- 📧 tomerarvind195@gmail.com

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

> ⭐ Agar helpful laga toh **star** zaroor karo!
