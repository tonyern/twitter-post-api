import random

# Function that takes a text and randomly capitalizes a string.
def randomCaptialization(text):
    newText = []

    for c in text:
        # Random number generator 0 or 1.
        randomBinary = random.randint(0, 1)
        
        # If 0 then lowercase character. If 1 then uppercase character.
        if randomBinary:
            newText.append(c.lower())
        else:
            newText.append(c.upper())

    return ''.join(newText)

# Main method.
if __name__ == "__main__":
    print(randomCaptialization('Hello World!'))