# players를 매개변수로 받아옴. 
# 층수는 5에서 30 사이의 숫자가 랜덤으로 배정됨 
# 한사람당 두개의 손을 가지고 있기 때문에 이름이 두개씩 담긴 playersHand라는 리스트를 만들어 뒤죽박죽 섞어줌
# playersHand list에서 끝사람이 빠지고 index 0으로 들어오는 것을 floor번 반복
# floor번째에 가장 마지막 index에 해당하는 사람이 loser
# loser 반환

import random
import time
def apart(players):
    # while True:
    #     start = input("아파트게임을 시작하시겠습니까? (y/n) : ")
    #     if (start == "y"):
    #         break
    #     else:
    #         print("게임을 시작하려면 y를 눌러주세요")

    print("아~파트아파트! 아~파트아파트! 몇층에 살까?")
    floor = random.randrange(5, 31)
    print(f"!!!!!!!! {floor}층!!!!!!!!")
    time.sleep(1)

    playersHand = []
    for p in range(0, len(players)):
        playersHand.append(players[p])
        playersHand.append(players[p])
    
    random.shuffle(playersHand)

    for f in range(1, floor + 1):
        print(f"\n~~~~~{f}층~~~~~")
        for i, h in enumerate(playersHand):
            if (i == len(players) * 2 - 1):
                print(f"|{h}| <= {f}층")
            else:
                print(f"|{h}|")
        time.sleep(0.7)
        turn = playersHand.pop(-1)
        playersHand.insert(0, turn)
        
    loser = playersHand[0]
    print(f"🚨🚨{loser} 패배🚨🚨")
    return loser
