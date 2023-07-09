import random as r

# 임시 데이터
player_dic = { 'lisa' : [4,4] } # { host name : [life, left-life] }
players = ['jisoo', 'lisa', 'jennie', 'rose']

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
        if players[players_idx] not in player_dic: # 이미 초대된 player 제외
            player_dic[players[players_idx]] = []
            break
    life = r.randint(1, 5) * 2
    player_dic[players[players_idx]] = [life, life]
    print('오늘 함께 취할 친구는 %s입니다 ! (치사량 : %d)' %(players[players_idx], life))
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

for player, lifeAr in player_dic.items():
    print('%s은(는) 지금까지 %d🍺! 치사량까지 %d' %(player, lifeAr[0]-lifeAr[1], lifeAr[1]))
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

print('~~~~~~~~~~~~~~~~ 🍺 오늘의 Alcohol GAME 🍺 ~~~~~~~~~~~~~~')
print('                 🍺 1. 더게임오브데스                       ')
print('                 🍺 2. 쥐를잡자                            ')
print('                 🍺 3. 폭탄돌리기                          ')
print('                 🍺 4. 아파트게임                          ')
print('                 🍺 5. (정한)                             ')
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')