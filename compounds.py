#for compounds generating all variations of the words in word1.txt + word2.txt with and without underscores

def read_word_list(file_name):
    with open(file_name, 'r') as file:
        return [word.strip() for word in file.readlines()]

def generate_combinations(word_list1, word_list2):
    combinations = []
    for word1 in word_list1:
        for word2 in word_list2:
            combinations.append(word1 + word2)
            combinations.append(word1 + "_" + word2)
    return combinations

def write_combinations_to_file(combinations, output_file):
    with open(output_file, 'w') as file:
        for combination in combinations:
            file.write("https://www.neopets.com/pound/adopt.phtml?search=" + combination + "\n")

if __name__ == "__main__":
    word_list1 = read_word_list("word1.txt")
    word_list2 = read_word_list("word2.txt")
    combinations = generate_combinations(word_list1, word_list2)
    write_combinations_to_file(combinations, "output.txt")
