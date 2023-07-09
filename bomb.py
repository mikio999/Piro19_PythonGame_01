import requests
from bs4 import BeautifulSoup as bs
from datetime import datetime
import time
import random


# 게임 설명: 지하철 7호선 역 이름 말하기
# 역 이름을 말해야만 다음 사람에게 폭탄을 넘길 수 있다.
# 단, 보조 이름을 가진 역은 보조 이름까지 전부 말해야 한다. 예를 들어, 이수 (x) 이수(총신대입구) (o)
# 폭탄 터진 사람이 loser


# 임시 데이터
dict_players = {'A':[2,2], 'B':[4,4], 'C':[6,6]} # { player:[life, left_life] }
players = ['B', 'C']


# 스크래핑으로 지하철 7호선 역 정보 얻어오는 함수
def getStationInfoByScraping():
    url = "https://ko.wikipedia.org/wiki/%EC%84%9C%EC%9A%B8_%EC%A7%80%ED%95%98%EC%B2%A0_7%ED%98%B8%EC%84%A0"
    response = requests.get(url)
    soup = bs(response.text, "html.parser")

    stationArs = soup.select(".wikitable > tbody > tr > td:nth-of-type(1) > a")

    stations = []
    for stationAr in stationArs:
        stations.append(stationAr.text)

    return stations

def sleep1Sec():
    time.sleep(1)

def printMiniGameIntro():
    print('----------    지하철 7호선 역 이름 말하기    ----------')
    sleep1Sec()
    print('---------- 💣 30초 뒤에 폭탄이 터집니다. 💣 -----------')
    sleep1Sec()
    print('-------------------  [GAME START]  --------------------')

def printMiniGameOutro(loser):
    print('---------- 💣💣💣💣💣💣💣💣💣💣💣💣💣💣💣💣 -----------')
    print('---------- 💣💣💣 폭탄이 터졌습니다. 💣💣💣 -----------')
    print('---------- 💣💣💣💣💣💣💣💣💣💣💣💣💣💣💣💣 -----------')
    sleep1Sec()
    print('--------------------  [GAME OVER]  --------------------')
    sleep1Sec()
    print('--------------------- loser는 %s  ----------------------' %loser)

def checkBomb(start_time, player):
    current_time = datetime.now()
    if (current_time - start_time).seconds >= 30:
        printMiniGameOutro(player)
        exit()

def bomb():
    #폭탄돌리기 게임에 필요한 정보
    stations = getStationInfoByScraping()
    mention = [] # 언급된 지하철 역 이름

    printMiniGameIntro()
    start_time = datetime.now()

    while True:

        while True:
            station = input('A : ') #다시 입력받는 경우: 존재하지 않는 역 이름 언급, 이미 언급된 역 이름을 다시 언급
            checkBomb(start_time, 'A')
            if (station in stations) and (station not in mention):
                mention.append(station)
                break
        print('    💣 폭탄넘기기 성공!')

        for player in players:
            while True:
                time.sleep(random.random() * 3)
                station = stations[random.randint(0, 52)]  #다시 입력받는 경우: 이미 언급된 역 이름을 다시 언급
                print('%s : %s' %(player, station))
                checkBomb(start_time, player)
                if station not in mention:
                    mention.append(station)
                    break
            print('    💣 폭탄넘기기 성공!')