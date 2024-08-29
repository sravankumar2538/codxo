import random
import string

def generate_password(length, use_upper, use_lower, use_digits, use_special):
    characters = ''
    
    if use_upper:
        characters += string.ascii_uppercase
    if use_lower:
        characters += string.ascii_lowercase
    if use_digits:
        characters += string.digits
    if use_special:
        characters += string.punctuation

    if not characters:
        print("Error: You must select at least one character type.")
        return None

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    
    try:
        length = int(input("Enter the desired length for the password: "))
        if length <= 0:
            print("Error: Password length must be a positive integer.")
            return
        
        use_upper = input("Include uppercase letters? (y/n): ").strip().lower() == 'y'
        use_lower = input("Include lowercase letters? (y/n): ").strip().lower() == 'y'
        use_digits = input("Include digits? (y/n): ").strip().lower() == 'y'
        use_special = input("Include special characters? (y/n): ").strip().lower() == 'y'

        # Generate and display the password based on user choices
        password = generate_password(length, use_upper, use_lower, use_digits, use_special)

        if password:
            print(f"Generated password: {password}")

    except ValueError:
        print("Error: Please enter a valid number for the password length.")

if __name__ == "__main__":
    main()
