import random

colors = ['Red', 'Green', 'Yellow', 'Blue', 'Purple', 'Orange']
code_lenght = 4
max_attempts = 10

code = random.choices(colors, k=code_lenght)
attempts = 0

print('Welcom to the mastermind game!')
print(f'Available colors: {','.join(colors)}')
print(f'Code lenght: {code_lenght}, Max attempts: {max_attempts}')

while attempts < max_attempts:
    guess = input(f'Attempt {attempts + 1} / {max_attempts}. Enter your guess: ').strip().split
    if len(guess) != code_lenght or not all(color in colors for color in guess):
        print('Invalid guess! Make sure you have four colors.')
        continue

    correct_position = sum(g == c for g, c in zip(guess, code))
    correct_color = sum(min(guess.count(c), code.count(c)) for c in set(code))
    correct_color -= correct_position

    print(f'{correct_position} colors placed correctly!')
    print(f'{correct_color} correct colors placed in wrong positions!')

    if correct_position == correct_color:
        print('Correct! Congratulations.')
        exit()

attempts += 1
