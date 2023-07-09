import random 

def updown_game(player_dic, turn):
    fst_num = random.randint(1, 101)
    print("UPDOWN 게임을 시작합니다. 범위는 1~100입니다. 패배자는 승리자의 직전 사람입니다.")

    players = list(player_dic.keys()) + [turn]
    total_players = len(players)
    gturn = 0
    
    loser = None
    
    while True:
        player = players[gturn % total_players]
        
        if player == turn:
            crt_num = int(input("당신의 차례입니다. 숫자를 입력하세요: "))
        else:
            crt_num = random.randint(1, 101)
            print(player + "의 차례입니다. 숫자를 자동으로 생성했습니다:", crt_num)
        
        if crt_num == fst_num:
            print("승자는", player)
            loser = players[(gturn - 1) % total_players]
            break
        
        if crt_num > fst_num:
            print("DOWN!")
        else:
            print("UP!")
        
        gturn += 1
    
    print("승자의 직전 턴 사람은", loser)
    return loser 