import random

updown_player_dic = {"Mellissa": 0, "JhonWich": 0, "Maverick": 0, "Rebecca": 0}

def updown_game():
    fst_num = random.randint(1, 101)
    print("UPDOWN 게임을 시작합니다. 범위는 1~100입니다.")

    players = list(updown_player_dic.keys()) + ["player"]
    total_players = len(players)
    turn = 0
    
    while True:
        player = players[turn % total_players]
        
        if player == "player":
            crt_num = int(input("당신의 차례입니다. 숫자를 입력하세요: "))
        else:
            crt_num = random.randint(1, 101)
            print(player + "의 차례입니다. 숫자를 자동으로 생성했습니다:", crt_num)
        
        if crt_num == fst_num:
            print("승자는", player)
            losers = [p for p in players if p != player]
            return losers
        
        if crt_num > fst_num:
            print("DOWN!")
        else:
            print("UP!")
        
        turn += 1
updown_game()