import secrets
import string

def generate_password(length=6):
    # Character sets
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    punctuation = string.punctuation

    # Ensure at least one character from each type
    password = [
        secrets.choice(lowercase),
        secrets.choice(uppercase),
        secrets.choice(digits),
        secrets.choice(punctuation)
    ]

    # Combine all characters
    all_characters = lowercase + uppercase + digits + punctuation

    # Fill the rest of the password
    password += [secrets.choice(all_characters) for _ in range(length - 4)]

    # Shuffle the password
    secrets.SystemRandom().shuffle(password)

    return ''.join(password)

# Generate and print password
print("Generated Password:")
print(generate_password())