#Number of words
def num_of_words(x):
    num = 0
    
    for i in x:
        if i == ' ':
            num += 1
    print("number of words in your sentence is :" , num + 1)
    
sentence = input("please enter your sentence : ")
num_of_words(sentence)