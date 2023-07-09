import random as r 
import game1
import game2
import game3
import game5
import gameover

##############Example#############
""" guest_number = 2
player_dic = {'정곤':[4,2],'현지':[5,1],'민경':[4,3]}
player='정곤'
loser='정곤' """
def result (my_name, my_life):
    player_dic = { my_name : [my_life,my_life] } # { host name : [life, left-life] }
    players_hj= ['정곤', '현지', '환희', '정한', '민경']

    
    # n 값 입력받기
    while True:
        n=input('함께 취할 친구들은 얼마나 필요하신가요?(사회적 거리두기는 끝났지만 최대 3명까지 초대할 수 있어요!) : ')
        if not n.isdigit() or (n<"1" or n>"3"):
            print('값을 다시 입력해주세요. 최소 1명 ~ 최대 3명까지 초대할 수 있습니다.')
        else:
            break

    # player 초대하기
    for i in range(int(n)):
        while True:
            players_idx = r.randint(0, 3)
            if players_hj[players_idx] not in player_dic: # 이미 초대된 player 제외
                player_dic[players_hj[players_idx]] = []
                break
        life = r.randint(1, 5) * 2
        player_dic[players_hj[players_idx]] = [life, life]
        print('오늘 함께 취할 친구는 %s입니다 ! (치사량 : %d)' %(players_hj[players_idx], life))
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

    for player, lifeAr in player_dic.items():
        print('%s은(는) 지금까지 %d🍺! 치사량까지 %d' %(player, lifeAr[0]-lifeAr[1], lifeAr[1]))
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

    print('~~~~~~~~~~~~~~~~ 🍺 오늘의 Alcohol GAME 🍺 ~~~~~~~~~~~~~~~~')
    print('             🍺 1. 아파트게임                       ')
    print('             🍺 2. updown 게임                            ')
    print('             🍺 3. 폭탄돌리기                          ')
    print('             🍺 4. 쥐를 잡자                        ')
    print('             🍺 5. 더게임오브데스                             ')
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
   
    import copy
    player_dic_forgame5 = copy.deepcopy(player_dic)

    players= []
    for key, value in player_dic.items():
        players.append(key)

    print(players)
    turn= players[0]


    loser=''
    for key, value in player_dic.items():
        if key != players[0] :
            value.append(0)
        if key == players[0] :
            value.append(1)
    game_choose=0
    print('test')
    print(player_dic_forgame5)

    while True :
        if turn == players[0]:
            game_choose = int(input(turn + '(이)가 좋아하는 랜덤 게임~무슨게임? : '))
        else:
            game_choose = r.randrange(1,6)
        print(game_choose)

        if game_choose == 1 :
            loser = game1.apart(players, len(players))
        elif game_choose ==2 :
            game2.updown_game(player_dic, turn)
        elif game_choose ==5 :
            print('adsfad')
            print(player_dic_forgame5 )
            game5.game5(player_dic_forgame5,players,turn)
        elif game_choose ==3 :
                loser = game3.bomb(turn, players, player_dic)
        elif game_choose ==4 :
            pass


        for key, value in player_dic.items():
            if key == loser:    # 값이 20이면
                value[1] = value[1] -1      # 키-값 쌍 삭제 
        for key, value in player_dic.items():
            print(key + '은(는) 지금까지' + str(value[0]-value[1]) + '🍺! 치사량까지' + str(value[1]))
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        i=0

        for key, value in player_dic.items():
            if value[2] == 1:
                i = i+1

        if i == len(player_dic):
            for key, value in player_dic.items():
                value[2]=0

        while_a = 0
        while while_a == 0 :
            i = r.randrange(0,len(player_dic))
            for key, value in player_dic.items():
                if value[2] == 0 and players[i] == key:
                    turn = key
                    value[2]= 1
                    while_a = 1

        for key, value in player_dic.items():
            if value[1]==0:
                gameover.game_over(key)
                exit()


