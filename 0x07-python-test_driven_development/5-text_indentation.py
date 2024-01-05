#!/usr/bin/python3

def text_indentation(text):
    if not isinstance(text, string):
        raise TypeError("text must be a string")
    
def print_text(text):
    for char in text:
        print(char, end="")

        if char in ".?:":
            print("\n\n")

print("Hey. I am a noob")

