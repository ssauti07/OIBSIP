import random
import string

print("===== PASSWORD GENERATOR =====")

# Ask the user for password length
length = int(input("Enter password length: "))

# Create a collection of characters
characters = string.ascii_letters + string.digits + string.punctuation

# Generate the password
password = ""

for i in range(length):
    password += random.choice(characters)

# Display the generated password
print("\nYour Generated Password is:", password)
print("Thank you for using Password Generator!")
