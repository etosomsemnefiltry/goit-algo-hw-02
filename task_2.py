from collections import deque

def is_palindrome(s):
    s = ''.join(char.lower() for char in s if char.isalnum())
    s_deque = deque(s)

    while len(s_deque) > 1:
        if s_deque.popleft() != s_deque.pop():
            return False
        return True
    
test = "Казак"
if is_palindrome(test):
    print(f"'{test}' - палиндром.")
else:
    print(f"'{test}' - не палиндром.")