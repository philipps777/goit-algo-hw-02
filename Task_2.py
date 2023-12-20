from collections import deque


def is_palindrome(input_str):

    cleaned_str = ''.join(input_str.lower().split())
    d = deque(cleaned_str)
    print(d)
    while len(d) > 1:
        if d.popleft() != d.pop():
            return False
    return True


input_str = input("Напишіть рядок для перевірки: ")
result = is_palindrome(input_str)

if result:
    print(f'Рядок "{input_str}" - це паліндром.')
else:
    print(f'Рядок "{input_str}" - це не паліндром.')
