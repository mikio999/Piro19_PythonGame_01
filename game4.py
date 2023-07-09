import random
import time

def mouse_game(players):
    phrases = ['쥐', '를', '잡', '자', '쥐를', '잡자', '쥐를 잡자', '찍찍찍', '몇 마리?']
    loser = ''

    # for i in range(0, len(phrases)):
    #     if i < len(players): 
    #         phrase = phrases[i]
    #         print(players[i] + ':', phrase)
    #         time.sleep(0.5)
    #     else:
    #         phrase = phrases[i]
    #         print(players[i % len(players)] + ':', phrase)
    #         time.sleep(0.5)
    while True:
            caught_mice = 0
            play_turn = players[0]
            try:
                num_mice = int(input("몇 마리? > ' A ' < (최대 다섯 마리): "))
                if 1 <= num_mice <= 5:
                    print("user:", num_mice)
                    break
                else:
                    print("1,2,3,4,5 중 하나를 입력하시오.")
            except ValueError:
                    print("숫자를 입력하세요.")
                
    
    caught_mice = 0
    play_turn = players[0]

    if caught_mice < num_mice:
        play_turn = players[0]
        while True:
            if play_turn != 'user':
                phrase = random.choice(['잡았다', '놓쳤다', '풀었다'])
                if phrase == '잡았다':
                    caught_mice += 1
                    print(play_turn + ':' + phrase, caught_mice)
                    time.sleep(0.5)
                if phrase == '풀었다':
                    if caught_mice > 0:
                        caught_mice -= 1
                        print(play_turn + ':' + phrase, caught_mice)
                        time.sleep(0.5)
                if phrase == '놓쳤다':
                    print(play_turn + ':' + phrase, caught_mice)
                    time.sleep(0.5)
            else:
                user_phrase = input("행동을 선택해주세요: ['잡았다', '놓쳤다', '풀었다']: ")
                if user_phrase == '잡았다':
                    print(play_turn + ':' + user_phrase, caught_mice)
                    time.sleep(0.5)
                    caught_mice += 1

                if user_phrase == "놓쳤다":
                    print(play_turn + ':' + phrase, caught_mice)
                    time.sleep(0.5)

                if user_phrase == '풀었다':
                    if caught_mice > 0:
                        caught_mice -= 1
                        print(play_turn + ':' + phrase, caught_mice)
                        time.sleep(0.5)
                    else:
                        print(play_turn + ':' + phrase, caught_mice)
                        print("쥐는 음수가 될 수 없습니다. 찍찍 > ' A ' <")
                        loser = "user"
                        print(f"{loser} 의 패배!")
                        time.sleep(0.5)
                        return loser
                
                else:
                    print("박자는 생명!! 아 박자는 생명!!!")
                    loser="user"
                    print(f"{loser} 의 패배!")
                    time.sleep(0.5)
                    return loser
                
            play_turn = players[(players.index(play_turn) + 1) % len(players)]

            if caught_mice == num_mice:
                print("찍찍찍찍찍!!!> ' A ' <!!!:")
                start_time = time.time()
                result = input()
                end_time = time.time()

                if result == '야옹' and end_time - start_time <= 3:
                    players.remove("user")
                    loser = random.choice(players)
                    print(f"{loser} 의 패배!")
                    return loser

                else:
                    loser = "user"
                    print("user의 패배!")
                    return loser

    else: 
        print("쥐는 음수가 될 수 없습니다. 찍찍 > ' A ' <")
        loser = "user"
        print(f"{loser} 의 패배!")
        time.sleep(0.5)
        return loser

players = ['A', 'B', 'C', 'user']
loser = mouse_game(players)
print("쥐를 잡기 게임에서 패배자는!")
print(loser)
