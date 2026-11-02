import random
import hanging_man_pictures
movie=['bahubali','rrr','maryadharamanna','studentno1']
guessed=random.choice(movie)

lives=6
ans=['_']*len(guessed)
print(ans)
while lives>0:
    guess=input('enter any alphabet: ')
    if guess in guessed:
        for i in range (len(guessed)):
            if guess == guessed[i]:
                ans[i]=guess
            
        print(ans)
    elif '_'not in ans:
        print("you won!")
        
    else:
        print('not there')
        lives-=1
        if lives==0:
            print("you lost")
            
    print(hanging_man_pictures.a[lives])

        