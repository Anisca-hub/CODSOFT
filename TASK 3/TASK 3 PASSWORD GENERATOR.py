# TASK 3 - PASSWORD GENERATOR
import random
import string

def generate_password(length, use_uppercase, use_digits, use_symbols):
    if length < (use_uppercase + use_digits + use_symbols + 1):  
        return "⚠️ Error: Length too short for selected options."

    characters = string.ascii_lowercase
    password_chars = []

    # Guarantee at least one from each selected category
    if use_uppercase:
        characters += string.ascii_uppercase
        password_chars.append(random.choice(string.ascii_uppercase))
    if use_digits:
        characters += string.digits
        password_chars.append(random.choice(string.digits))
    if use_symbols:
        characters += string.punctuation
        password_chars.append(random.choice(string.punctuation))

    # Fill the rest with random choices
    while len(password_chars) < length:
        password_chars.append(random.choice(characters))

    # Shuffle the result to avoid predictable patterns
    random.shuffle(password_chars)

    return ''.join(password_chars)

def main():
    print("🔒🔑 WELCOME TO THE PASSWORD GENERATOR 🔒🔑\n")
    try:
        count = int (input ("🔢 How many passwords do you want to generate? : "))
        length = int (input ("\n🔑 Enter the desired password length : "))

        use_uppercase = input ("\n🔠 Include uppercase letters? (Y/N) : ").strip().lower() == 'y'
        use_digits = input ("🔢 Include digits? (Y/N) : ").strip().lower() == 'y'
        use_symbols = input ("🔒 Include symbols? (Y/N) : ").strip().lower() == 'y'

        for _ in range(count):
            pwd = generate_password(length, use_uppercase, use_digits, use_symbols)
            print ("\n🔑 Generated Password :", pwd)

    except ValueError:
        print ("❌ Invalid input. Please enter numbers for password length and count.")

if __name__ == "__main__":
    main()