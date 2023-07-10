import random
import time
# from main import my_name

my_name="은우"
players = [my_name, 'A', 'B', 'C']

# players = ['A', 'B', 'C', 'user']

def mouse_game(players):
    phrases = ['쥐…ᘛ⁐̤ᕐᐷ', '를', '잡', '자', '쥐를…ᘛ⁐̤ᕐᐷ', '잡자', '쥐를 잡자!…ᘛ⁐̤ᕐᐷ!', '찍찍찍…ᘛ⁐̤ᕐᐷ…ᘛ⁐̤ᕐᐷ…ᘛ⁐̤ᕐᐷ','쥐를 잡자!…ᘛ⁐̤ᕐᐷ!', '찍찍찍…ᘛ⁐̤ᕐᐷ…ᘛ⁐̤ᕐᐷ…ᘛ⁐̤ᕐᐷ', '몇 마리?']
    active_choice = ['잡았다', '놓쳤다', '풀었다']
    loser = ''

    for i in range(0, len(phrases)):
        if i < len(players): 
            phrase = phrases[i]
            print(players[i] + ':', phrase)
            time.sleep(0.5)
        else:
            phrase = phrases[i]
            print(players[i % len(players)] + ':', phrase)
            time.sleep(0.5)
    while True:
            caught_mice = 0
            play_turn = players[0]
            try:
                num_mice = int(input("몇 마리? > ' A ' < (최대 다섯 마리): "))
                if 1 <= num_mice <= 5:
                    print(play_turn,":", num_mice)
                    break
                else:
                    print("1,2,3,4,5 중 하나를 입력하시오.")
            except ValueError:
                    print("숫자를 입력하세요.")
                
    
    caught_mice = 0
    play_turn = players[0]
    if caught_mice < num_mice:
        while True:
            if play_turn != my_name:
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

                if user_phrase == "놓쳤다":
                    print(play_turn + ':' + user_phrase)
                    time.sleep(0.5)

                if user_phrase == '풀었다':
                    if caught_mice > 0:
                        caught_mice -= 1
                        print(play_turn + ':' + user_phrase)
                        time.sleep(0.5)
                    else:
                        print(play_turn + ':' + user_phrase)
                        print("쥐는 음수가 될 수 없습니다. 찍찍 🐭 술이 먹고 싶었어?")
                        loser=play_turn
                        print(loser, "의 패배!")
                        time.sleep(0.5)
                        return loser
                
                if user_phrase not in active_choice:
                    print("🐭🐭🐭🐭찍찍찍찍찍!!!🐭🐭🐭🐭")
                    print("술이 들어간다! 쭉쭉쭉쭉 쭉쭉쭉쭉")
                    loser=play_turn
                    print(f"{loser} 의 패배!")
                    time.sleep(0.5)
                    return loser
                
                
            play_turn = players[(players.index(play_turn) + 1) % len(players)]

            if caught_mice == num_mice:
                print("~(=^･ω･^)ﾍ >ﾟ)))彡 고양이가 나타났다!")
                time.sleep(0.5)
                start_time = time.time()
                result = input("hint) what does the cat say?:")
                end_time = time.time()

                if result == '야옹' and end_time - start_time <= 3:
                    players.remove(play_turn)
                    loser = random.choice(players)
                    print(loser, "의 패배!")
                    return loser

                else:
                    loser = play_turn
                    print(play_turn,"의 패배!")
                    print("동구밭~ 과수원 샷!")
                    return loser

    else: 
        print("쥐는 음수가 될 수 없습니다. 찍찍 > ' A ' <")
        loser = play_turn
        print(f"{loser} 의 패배!")
        time.sleep(0.5)
        return loser

# loser = mouse_game(players)
# print("쥐를 잡기 게임에서 패배자는!")
# print(loser)
