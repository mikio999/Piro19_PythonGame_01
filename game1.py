# 층수는 랜덤(5~30)으로 주어진다. 
# 한 층씩 세면서 아래에서 손을 빼서 위에 올리다가 말한 층수에 걸린 사람이 당첨

# player 수를 매개변수로 받아옴. 
# 이름은 아직 모르기때문에 p1, p2, p3.. 이런식으로 임의로 이름매김
# loser 반환

import random
def apart(pNum):
    print("아~파트아파트! 아~파트아파트! 몇층에 살까?")
    floor = random.randrange(5, 30)
    print(f"!!!!!!!! {floor}층!!!!!!!!")

    playersHand = []
    for p in range(1, pNum+1):
        playersHand.append(f"p{p}")
        playersHand.append(f"p{p}")
    
    random.shuffle(playersHand)

    for f in range(1, floor + 1):
        print(f"\n~~~~~{f}층~~~~~")
        for i, h in enumerate(playersHand):
            if (i == pNum * 2 - 1):
                print(f"|{h}| <= {f}층")
            else:
                print(f"|{h}|")
    
        turn = playersHand.pop(-1)
        playersHand.insert(0, turn)
        
    loser = playersHand[0]
    print(f"🚨🚨{loser} 패배🚨🚨")
    return loser