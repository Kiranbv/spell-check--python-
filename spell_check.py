

""" OBJECTIVE: This program reads words from stdin, and prints either the best
spelling suggestion, or "NO SUGGESTION" if no suggestion can be found.
"""



# this function finds all the consonants in a given word
def find_consonants(word):
    consonants = [] 
    for i in range(0,len(word)):
        if(word[i] != "a" and word[i] != "e" and word[i] != "i" and word[i] != "o" and word[i] != "u"):
            consonants.append(word[i])
    return consonants 




def main():
    # importing libraries
    import enchant
    import nltk
    from nltk.metrics import edit_distance
    import re


    # importing dictionary from enchant
    dictionary = enchant.Dict("en_US")


    # Reading the words from the standard input
    print("please enter the word you want checked. If you wish to stop enter quit")
    while 1:
        word_input = input('> ')
        flag_repeated = 0
        flag_consonant = 0
        response = int(input("do you want to find words with the same consonants, 1 for yes,0 for no"))
        if(response):
            flag_consonant = 1
        
        

    # The word is first checked to see if it has mixed case. If so it is converted to lower case. 
        if(not word_input.isupper() and not word_input.islower()):
            word_new = word_input.lower()
        else:
            word_new = word_input


    # checking to see if the word has repeated letters
        word_temp = "".join(set(word_new))
        if(len(word_temp) < len(word_new)):
            flag_repeated = 1    
        


    # finding suggestions for the original word
        suggestions = dictionary.suggest(word_new)    
        distance_words = []
        for i in range(0,len(suggestions)):
            distance_words.append(edit_distance(word_new,suggestions[i]))

        
    # Now to find and print the best match 
    # If the word matches perfectly with zero edit distance in which case its
    # just the actual word with a few letters with different case, that is the
    # final suggestion. 
        if(min(distance_words) == 0):
            min_index = distance_words.index(min(distance_words))
            final_answer = suggestions[min_index]
            print("final suggestion is:",suggestions[min_index])
            


    # if there are repeat characters we look for suggestions both for original word
    # and word formed by unique letters of the original word. Choose the list which
    # has the word closest.
        if(flag_repeated):
            suggestions1 = dictionary.suggest(word_temp)
            distance_words1 = []
            for i in range(0,len(suggestions1)):
                distance_words1.append(edit_distance(word_temp,suggestions1[i]))
            if(min(distance_words1)<min(distance_words)):
                suggestions_selected = suggestions1
                distances_sel = distance_words1
            else:
                suggestions_selected = suggestions
                distances_sel = distance_words

            
    # depending on the response of the user to keep the consonants, final word suggestion is made
    # only words with low distance is kept and consonants of those words with that of original word compared
    # to find the final suggestion.
    # The program gives different answer if you want consoant or not
        if(flag_consonant):
             min1 = min(distances_sel)
             suggestions_temp = []
             for i in range(0,len(distances_sel)):
                 if(distances_sel[i] == min1):
                     suggestions_temp.append(suggestions_selected[i])
             consonants_original = find_consonants(word_new)

             for i in range(0,len(suggestions_temp)):
                 if(consonants_original == find_consonants(suggestions_temp[i])):
                    print("final suggestion is:",suggestions_temp[i])
                 else:
                    print("no suggestion")
        else:
            min_index = distances_sel.index(min(distances_sel))
            final_answer = suggestions_selected[min_index]
            print("final suggestion is:",suggestions_selected[min_index])

        if word_input == "quit":
            break

if __name__ == "__main__":
    main()






            
    

