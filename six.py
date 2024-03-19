#for generating all 6-letter combos given a 3-letter prefix

from itertools import product

def generate_combinations(first_three_letters):
    if len(first_three_letters) != 3:
        print("Please input exactly three letters.")
        return
      
    last_three_letters = [chr(i) for i in range(ord('a'), ord('z')+1)]
    combinations = [''.join(comb) for comb in product(last_three_letters, repeat=3)]
    result = [first_three_letters + comb for comb in combinations]   
    return result

input_letters = input("Enter the first three letters: ").strip().lower()
combinations = generate_combinations(input_letters)

with open("output.txt", "w") as output_file:
    for combo in combinations:
        output_file.write("https://www.neopets.com/pound/adopt.phtml?search=" + combo + "\n")

print("Generated combinations with links written to output.txt.")
