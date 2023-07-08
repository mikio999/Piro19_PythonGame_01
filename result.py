import random 

##############Example#############
guest_number = 2
player_dic = {'정곤':[4,2],'현지':[5,1],'민경':[4,3]}
player='정곤'
loser='정곤'

turn = player
while True :
    #guest 받기 
    #if turn= player:
        #input(turn + '(이)가 좋아하는 랜덤 게임~무슨게임?')
    #else:
        # ~님이 게임을 선택하셨습니다
    #game 싲가
    #game 종료
    
    for key, value in player_dic.items():
        if key == loser:    # 값이 20이면
            value[1] = value[1] -1      # 키-값 쌍 삭제 
    for key, value in player_dic.items():
        print(key + '은(는) 지금까지' + str(value[0]-value[1]) + '🍺! 치사량까지' + str(value[1]))
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

    i = random.randrange(1,guest_number+1)
    turn = list(player_dic.keys())[i]
    break
    

