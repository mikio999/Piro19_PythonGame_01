import random 
from time import *

##############Example#############


#player_dic = {이름,[life,left_life], 내 숫자, 고른 숫자}
 ##총 number
##게임을 시작한 사람 입력##

def game5(player_dic,players,turn):
    host = turn
    player=players[0]
    guest_number = len(players) - 1
    i=0
    number ='0' ##현재 number
    count = '0'
    for key, value in player_dic.items():
        value.append(i)
        i=i+1
    print(len(player_dic))
    print(player_dic)
    while True:
        try:
            for key, value in player_dic.items():
                if key != player:
                    print(key + ' : ' + str(value[2]))
            choose = int(input('지목할 사람을 고르세요 : '))
        except ValueError:
            print('\n정수를 입력하세요.')
        else :
            if (choose <= 0 or choose >= len(player_dic) ):
                print('\n자기 자신을 제외한 다른 사람의 번호를 입력하세요.')
            else : 
                for key, value in player_dic.items():
                    if key == player :
                        value.append(choose)
                    if value[2] == choose:
                        choose = key
                break

    if host == player :
        while True:
            try:
                count = int(input('\n2 이상의 숫자를 부르세요 : '))
            except ValueError:
                print('정수가 아닙니다.')
            else :
                if count < 2 :
                    print('2 이하의 정수를 입력했습니다.')  
                else : 
                    break
                        
    print('\n\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print('아싸 신난다 ~ 아싸 재미난다 ~ 더 게임 오브데스 !!')
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')



    print(player + ' ----> ' + choose)
    for key, value in player_dic.items():
        if key != player:
            a_key  = key
            while True :
                b_random= random.randrange(0,len(player_dic)) 
                if b_random != value[2] : 
                    value.append(b_random)
                    for key, value in player_dic.items():
                        if value[2] == b_random :
                            print(a_key + ' ----> ' + key)
                    break    


    print('\n\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print('게임 시작!!')
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

    for key, value in player_dic.items():
        if key == host:
            turn = value[2]
            next_turn = value[3]

    player_list= []
    for key, value in player_dic.items():
        player_list.append(key)

    a='   '
    b='   '
    c='   '
    d='   '
    e='   '
    f='   '
    n='   '


    i=1
    while (i<=count):
        sleep(2)
        for key, value in player_dic.items():
            if value[2] == turn:
                turn = key
            if value[2] == next_turn:
                next_turn = key
        print (i)

        if len(player_list)==4 :
            p_0=player_list[0]
            p_1=player_list[1]
            p_2=player_list[2]
            p_3=player_list[3]
            if turn == player_list[0] :
                if next_turn == player_list[1] : 
                    c = ' → '
                if next_turn == player_list[2] : 
                    d = ' ↓ '
                if next_turn == player_list[3] : 
                    b = ' ↘ '
            if turn == player_list[1] :
                if next_turn == player_list[0] : 
                    c = ' ← '
                if next_turn == player_list[2] : 
                    a = ' ↙ '
                if next_turn == player_list[3] : 
                    f = ' ↓ '
            if turn == player_list[2] :
                if next_turn == player_list[0] : 
                    d = ' ↑ '
                if next_turn == player_list[1] : 
                    a = ' ↗ '
                if next_turn == player_list[3] : 
                    e = ' → '
            if turn == player_list[3] :
                if next_turn == player_list[0] : 
                    b = ' ↖ '
                if next_turn == player_list[1] : 
                    f = ' ↑ '
                if next_turn == player_list[2] : 
                    e = ' ← '
            print(f'''


        {p_0} {c} {c} {c} {c} {p_1}
        {d}  {b} {n} {n} {a}  {f}               
        {d}  {n} {b} {a} {n}  {f}  
        {d}  {n} {a} {b} {n}  {f}           
        {d}  {a} {n} {n} {b}  {f}  
        {p_1} {e} {e} {e} {e} {p_1}
        ''')
            

        if len(player_list)==3 :
            p_0=player_list[0]
            p_1=player_list[1]
            p_2=player_list[2]
            if turn == player_list[0] :
                if next_turn == player_list[1] : 
                    b = ' ↙ '
                if next_turn == player_list[2] : 
                    c = ' ↘ '
            if turn == player_list[1] :
                if next_turn == player_list[0] : 
                    b = ' ↗ '
                if next_turn == player_list[2] : 
                    a = ' → '
            if turn == player_list[2] :
                if next_turn == player_list[0] : 
                    c = ' ↖ '
                if next_turn == player_list[1] : 
                    a = ' ← '
            print(f'''
                {p_0}
                {b}  {c} 
            {b}  {n}  {c}   
        {p_1} {a} {a} {p_2}
        ''')
            
        if len(player_list)==2 :
            p_0=player_list[0]
            p_1=player_list[1]
            if turn == player_list[0] :
                a = ' → '
            if turn == player_list[1] :
                a = ' ← '

            print(f'''
        {p_0} {a} {a} {a} {p_1}
        ''')
            
        a='   '
        b='   '
        c='   '
        d='   '
        e='   '
        f='   '
        n='   '


        turn = next_turn
        for key, value in player_dic.items():
            if key == turn:
                turn = value[2]
                next_turn = value[3]
        i = i+1


    for key, value in player_dic.items():
        if value[2] == turn:
            loser = key
        del value[3]    
        del value[2]

    print(loser)
    print(player_dic)


