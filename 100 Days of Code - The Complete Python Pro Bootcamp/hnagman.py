import random
bible_words =['moses', 'jesus', 'faith', 'joshua', 'commandments', 'mary', 'righteousness', 'saviour', 'easter']

chosen_word=random.choice(bible_words)
mystery =''
for i in chosen_word:
    i = '_'
    mystery+=i
print(mystery)
print(chosen_word)
user_complete_guess=''
full_guess=''

while not user_complete_guess == chosen_word:
    user_complete_guess = ''
    user_letter=input('Guess Your letter:')
    for i in chosen_word:
        if user_letter == i:
            user_complete_guess+=user_letter
            full_guess += i
        else:
            user_complete_guess+='_'
    print(user_complete_guess)
    print(full_guess)