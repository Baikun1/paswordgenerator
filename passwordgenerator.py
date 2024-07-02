import random
import string

class PasswordGenerator:
    def __init__(self, length=12, include_special_chars=True, min_digits=0, min_uppercase=0, min_lowercase=0, min_special_chars=0):
        self.length = length
        self.include_special_chars = include_special_chars
        self.min_digits = min_digits
        self.min_uppercase = min_uppercase
        self.min_lowercase = min_lowercase
        self.min_special_chars = min_special_chars
        self.characters = string.ascii_letters + string.digits
        if self.include_special_chars:
            self.characters += string.punctuation

    def generate_password(self):
        if self.length < self.min_digits + self.min_uppercase + self.min_lowercase + self.min_special_chars:
            raise ValueError("Password length is too short for the given requirements.")

        password = []

        password.extend(random.choices(string.digits, k=self.min_digits))
        password.extend(random.choices(string.ascii_uppercase, k=self.min_uppercase))
        password.extend(random.choices(string.ascii_lowercase, k=self.min_lowercase))
        if self.include_special_chars:
            password.extend(random.choices(string.punctuation, k=self.min_special_chars))

        remaining_length = self.length - len(password)
        password.extend(random.choices(self.characters, k=remaining_length))
        random.shuffle(password)
        
        return ''.join(password)

    def set_length(self, length):
        if length < 1:
            raise ValueError("Password length must be at least 1.")
        self.length = length

    def set_requirements(self, min_digits, min_uppercase, min_lowercase, min_special_chars):
        self.min_digits = min_digits
        self.min_uppercase = min_uppercase
        self.min_lowercase = min_lowercase
        self.min_special_chars = min_special_chars


# Example usage with user input
if __name__ == "__main__":
    while True:
        try:
            length = int(input("Enter the desired password length: "))
            break
        except ValueError:
            print("Please enter a valid number.")

    include_special_chars = input("Include special characters? (yes/no): ").strip().lower() == "yes"
    min_digits = int(input("Minimum number of digits: "))
    min_uppercase = int(input("Minimum number of uppercase letters: "))
    min_lowercase = int(input("Minimum number of lowercase letters: "))
    min_special_chars = int(input("Minimum number of special characters: ")) if include_special_chars else 0

    generator = PasswordGenerator(
        length=length,
        include_special_chars=include_special_chars,
        min_digits=min_digits,
        min_uppercase=min_uppercase,
        min_lowercase=min_lowercase,
        min_special_chars=min_special_chars
    )

    try:
        print("Generated password:", generator.generate_password())
    except ValueError as e:
        print(e)
