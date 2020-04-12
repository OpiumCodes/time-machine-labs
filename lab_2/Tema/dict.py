def letter_count(sentence):
    count = dict()
    for letter in sentence.lower():
        if not letter.isspace():
            if not letter in count:
                count[letter]=1
            else:
                count[letter]+=1
    return count 
print(letter_count("Ana are mere"))