import ipdb

class Anagram():

    def __init__(self, word):

        self.word = word
    
    def match(self, checklist):
        
        anagram_list = []
        matching_word = [letter for letter in self.word]

        for word in checklist:
            if (sorted(matching_word) == (sorted([letter for letter in word]))):
                anagram_list.append(word)

        return anagram_list