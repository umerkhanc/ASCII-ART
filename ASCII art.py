from art import text2art
from termcolor import colored

# Get input text from user
input_text = input("Enter your text: ")

# Generate ASCII art from input text
ascii_art = text2art(input_text)

# Print ASCII art in green font
print(colored(ascii_art, 'green'))