class word_data:
    wordList = ["Green", "Apple", "Pear"]

    def isLetter(self, letter):
        if letter.isalpha() == True:
            return True
        else:
            return False

    file1 = open("mit.edu_~ecprice_wordlist.10000.txt", "r");
    file1.readlines();
