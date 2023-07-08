import random
import time

def mouse_game(players):
    phrases = ['쥐', '를', '잡', '자', '쥐를', '잡자', '쥐를 잡자', '찍찍찍', '몇 마리?']

    for i in range(0, len(phrases)):
        if i < len(players): 
            phrase = phrases[i]
            print(players[i] + ':', phrase)
            time.sleep(0.5)
        else:
            phrase = phrases[i]
            print(players[i % len(players)] + ':', phrase)
            time.sleep(0.5)
            
    num_mice = int(input("몇 마리? (최대 다섯 마리): "))
    print("user:", num_mice)
    caught_mice = 0
    play_turn = players[0]

    while caught_mice < num_mice:
        play_turn = players[0]
        while True:
            if play_turn != 'user':
                phrase = random.choice(['잡았다', '놓쳤다', '풀었다'])
                if phrase == '잡았다':
                    caught_mice += 1
                    print(play_turn + ':' + phrase)
                    time.sleep(0.5)
                if phrase == '풀었다':
                    if caught_mice > 0:
                        caught_mice -= 1
                        print(play_turn + ':' + phrase)
                        time.sleep(0.5)
                if phrase == '놓쳤다':
                    print(play_turn + ':' + phrase)
                    time.sleep(0.5)
            else:
                user_phrase = input("행동을 선택해주세요: ['잡았다', '놓쳤다', '풀었다']: ")
                if user_phrase == '잡았다':
                    print(play_turn + ':' + user_phrase)
                    time.sleep(0.5)
                    caught_mice += 1

                if user_phrase == '풀었다':
                    if caught_mice > 0:
                        print(play_turn + ':' + user_phrase)
                        time.sleep(0.5)
                        caught_mice -= 1

                if user_phrase == "놓쳤다":
                       print(play_turn + ':' + phrase)
                       time.sleep(0.5)
               
            play_turn = players[(players.index(play_turn) + 1) % len(players)]

            if caught_mice < 0:
                print("쥐는 음수가 될 수 없습니다. 찍찍 > ' A ' <")
                print(play_turn,"의 패배!")
                time.sleep(0.5)
                break

            if caught_mice == num_mice:
                print("찍찍찍찍찍!!ㅂ!!!:")
                start_time = time.time()
                result = input()
                end_time = time.time()

                if result == '야옹' and end_time - start_time <= 3:
                    print("user의 승리!")
                else:
                    print("user의 패배!")
                break

        print("게임 종료")

players = ['A', 'B', 'C', 'user']
mouse_game(players)
