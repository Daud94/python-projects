# Write your code here
print("Input the number of cards:")
num_of_cards = int(input())

words_and_def = {}
i = 1
while i <= num_of_cards:
    print(f"The term for card #{i}:")
    term = input()
    print(f"The definition for card #{i}:")
    defi = input()
    words_and_def[term] = defi
    i = i + 1
# print(words_and_def)
for x, y in words_and_def.items():
    print(f"Print the definition of \"{x}\":")
    ans = input()
    if ans == y:
        print("Correct!")
    else:
        print(f"Wrong. The right answer is {y}")
