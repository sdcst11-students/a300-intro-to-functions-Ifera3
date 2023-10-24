#! python3

# SD Computing Studies Assignment
"""
Create a program with 3 function definitions: function A prints the message "Hello" function B prints the message "How are you" function C prints the message "Hi"

Ask the user to enter a letter from A to C Execute the function of the letter they use.
"""
def A():
    print("Hello")

def B():
    print("How are you")

def C():
    print("Hi")

if __name__ == "__main__":
    x = input("A, B, or C: ")
    if x == 'A' or x == 'a':
        A()
    elif x == 'B' or x == 'b':
        B()
    elif x == 'C' or x == 'c':
        C()