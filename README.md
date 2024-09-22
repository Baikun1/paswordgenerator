# Password Generator

This Python script generates random passwords based on user-defined criteria. It allows users to specify the desired length of the password, whether to include special characters, and minimum requirements for digits, uppercase letters, lowercase letters, and special characters.

## Features

- **Customizable Password Length:** Specify the desired length of the generated password.
- **Character Requirements:** Define minimum requirements for:
  - Digits
  - Uppercase letters
  - Lowercase letters
  - Special characters (optional)
- **Randomized Output:** The generated password is a random mix of the specified character types.

## Installation

Ensure you have Python 3.x installed on your system.

## Usage

1. Clone this repository or download the script file.
2. Run the script using Python:

   ```bash
   python password_generator.py
   ```
## Follow the prompts to enter the desired password specifications:
```bash
Password length
Include special characters (yes/no)
Minimum number of digits
Minimum number of uppercase letters
Minimum number of lowercase letters
Minimum number of special characters (if applicable)
The generated password will be displayed based on your specifications.
```

## Example
```bash
Enter the desired password length: 16
Include special characters? (yes/no): yes
Minimum number of digits: 2
Minimum number of uppercase letters: 2
Minimum number of lowercase letters: 2
Minimum number of special characters: 2
Generated password: Ab1$cde2#FgH!34
```
## Error Handling
The script includes error handling to manage invalid inputs and ensure the specified password requirements are feasible given the chosen length.
