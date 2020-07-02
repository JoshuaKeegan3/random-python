

import random


# The easiest
def shuffle1(word):
    word_list = list(word)
    random.shuffle(word_list)
    word = ''
    for char in word_list:
        word += char
    return word

def shuffle2(word):
    new_word = ''
    word_list = list(word)
    while len(word_list) >0:
        random_indici = random.randint(0,len(word_list)-1)
        new_word+=word_list[random_indici]
        del word_list[random_indici]
    return new_word

def shuffle3(word):
    new_word = ''
    swaps = []
    for i in range(random.randint(0,len(word)*2)):
        swap1=random.randint(0,len(word)-1)
        swap2=random.randint(0,len(word)-1)
        swaps.append((swap1,swap2))
    word = list(word)
    
    for swap in swaps:
        temp_var = word[swap[0]]
        word[swap[0]] = word[swap[1]]
        word[swap[1]] = temp_var
    
    for char in word:
        new_word +=char

    return new_word

# Shuffle with insert

def shuffle4(word):
    word=list(word)
    new_word = ''
    for i in range(len(word)):
        word.insert(random.randint(0,len(word)),word.pop(random.randint(0,len(word)-1)))
    for char in word:
        new_word +=char
    return new_word

                    

