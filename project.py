import random          #imported random module   
import hangman         #imported hangman file through import module
import matplotlib.pyplot as plt   #imported matplotlib to show graph of finding probability of appearing of each word
word_list=["orange","velvet","colour",'apple','lavender'] 
plt.plot(word_list)
chosen_word=random.choice(word_list) #choice function present in random
life=6   #have 6 lives before starting game
# print(chosen_word) #it will print randomly chosen word from list
display=[]  
for i in range(len(chosen_word)):  #display spaces over the length of randomly chosen word
    display+='_'  #display underscore as a blank when no words are guessed
print(display)
gameover=False   #opposing gameover condition
while not gameover:                 #while game is running 
     letter_guessed=input("guess a letter:").lower()  #capital input will be converted into lower
     for position in range(len(chosen_word)):  
         letter=chosen_word[position]      #position of chosen word is stored in letter
         if letter==letter_guessed:      #if guessed letter position is correct to the letter
             display[position]=letter_guessed    #guessed letter will be stored in its original position
     print(display)
     if letter_guessed not in chosen_word:    #if guessed letter not present
         life-=1                         #life will be deducted
         if life==0:                 
             gameover=True              
             print("you lose :(")
     if '_' not in display:          #when all underscores are filled
         gameover=True               #gameover condition will be true
         print("you win!!!! :)")
     print(hangman.stages[life])      #imported hangman stages
plt.xlabel("Percentage of appearing that word",fontsize=16,color='red')
plt.ylabel("Random words",fontsize=16,color='red')
plt.title("Graph to find probability of appearing that word")
plt.show()