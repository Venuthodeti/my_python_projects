import random
import hanging_man_pictures
movie=['bahubali','rrr','maryadharamanna','studentno1']
guessed=random.choice(movie)
game=True
lives=6
kaali=[]
k="_ "*len(guessed)
print(guessed)
print(k)
while game:
    ans=''
    guess=input('enter any guess: ')

    for i in guessed:
        if guess==i:
            ans+=guess
            kaali.append(guess)
        elif i in kaali:
            ans+=i
        else:
            ans+="_"
    if "_" not in ans:
        print("you won!")
        game=False
    elif guess not in guessed:
        lives-=1
        print("not there")
        if lives==0:
            print("you lost!")
            
            game=False
    print(hanging_man_pictures.a[lives])
        