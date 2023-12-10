def no_space (word) :
    new_string = ""
    for i in range (len(word)) :
        if word[i]!=" " :
            new_string += word[i]
    
    return new_string
            
def is_anagram(w1,w2):
    if sorted(w1.lower()) == sorted(w2.lower()):
        #return True
        print(word1," is a anagram of ",word2)
        
    else:
        print(word1," is not an angram of ", word2)
def phrase_check(w1,w2,phrase):
    is_anagram(w1,phrase)
    is_anagram(w2,phrase)
    
word1 = input("Enter the first word: ")
word2 = input("enter the second word")

 # test whether the sorted strings are the same as each other
 # if the sorted strings are the same then they must be anagrams
 
is_anagram(word1,word2)

phrase = input(" enter your phrase : ")
phrase_check(word1,word2,phrase)



    


