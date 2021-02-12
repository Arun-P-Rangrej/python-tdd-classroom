class StringExercise:

    def __init__(self):
        pass   # Do some initial setup in this constructor method, if needed

    def reverse_string(self, input_str):
        input_str = input_str[::-1] 
        return input_str 

    def is_english_vowel(self, ch):
        if(ch=='A' or ch=='a' or ch=='E' or ch =='e' or ch=='I' or ch=='i' or ch=='O' or ch=='o' or ch=='U' or ch=='u'):
            return True
        else:
            return False
        
        

    def find_longest_word(self, sentence):
        import re
        word_pattern = "\w+"
        regex = re.compile(word_pattern)
        words_found = regex.findall(sentence)

        if words_found:
            longest_word = max(words_found, key=lambda word: len(word))
            return longest_word
        return None

    def get_word_lengths(self, text):
        mytext = text.split(" ")
        word_len = []
        for n in mytext:
            word_len.append(len(n))
        return word_len
