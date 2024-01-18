import string

def letter_count(file) -> dict | int:
    """
    Counts the English letters in the file
    Input: .txt file
    Output: dictionary of {letter:count} pairs, total letter count
    """
    # create & initialize letter count dictionary
    letter_count = {}
    
    for letter in string.ascii_lowercase:
        letter_count[letter] = 0
        
    # create initial total letter count
    total_letters = 0
    
    f = open(file)

    # iterate through the letters of each line and update letter count
    for line in f:
        for letter in line:
            if letter.lower() in string.ascii_lowercase:
                letter_count[letter.lower()] += 1
                total_letters += 1
                
    f.close()
    
    # output {letter:count} dict
    return letter_count, total_letters

def letter_frequency(dict_letters: dict, letter_total: int) -> dict:
    """
    Finds the frequeny of each letter in the letter_count dictionary
    Input: {letter:count} dict, letter total
    Output: dictionary of {letter:frequency} pairs
    """
    # create & initialize frequency count using dictionary
    frequency_count = {}
    
    for letter in string.ascii_lowercase:
        frequency_count[letter] = 0

    # compute frequency and update dictionary
    for k, v in dict_letters.items():
        freq = v / letter_total
        frequency_count[k] = freq
    return frequency_count


if __name__ == "__main__":
    # letterCountDict, totalLetters = letter_count('frost.txt')
    letterCountDict, totalLetters = letter_count('The_Hunger_Games.txt')
    print('Letter counts->')
    for k,v in letterCountDict.items():
        print(f'{k}: {v}')
    letterFrequency = letter_frequency(letterCountDict, totalLetters)
    print('Letter frequency->')
    for k,v in letterFrequency.items():
        print(f'{k}: {v}')
