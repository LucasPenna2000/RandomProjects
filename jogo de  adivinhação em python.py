import os #biblioteca de sistema operacional
import random
import time

live = 5 #number of lives 
while live > 0: 
    if live == 0:
        print('GAME OVER')
        break
        
    print(f'You have ({live}) lives')
    x = int(input('choose a number from 1 to 5: ')) 
    print('loading...')
    print('-='*15)
    time.sleep(2)

    escolha = random.randint(1,5)
    print('The computer chose: ',escolha)
    print('-='*15)

    if x == escolha:
        print(f'You win! with {live} lives \nGame Over!')
        break
    elif x > 5:
        print('You chose a number greater than five!!!!\nTry Again.') 
        live = live - 1       
    else:
        print('Try Again')  
        live = live - 1 
    time.sleep(5)
    
    if os.name == "nt":#retorna o nome do sistema operacional, nt são sistemas operacionais da microsoft.  
        os.system("cls") #irá limpar o terminal no sistema operacional microsoft
    else:
        os.system("clear") #ira limpar terminal no sistema operacional linux