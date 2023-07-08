player_dic = {'정곤':[4,2],'현지':[5,1],'민경':[4,3]}
loser='정곤'

def result():
    for key, value in player_dic.items():
        print(key + '은(는) 지금까지' + str(value[0]-value[1]) + '🍺! 치사량까지' + str(value[1]))
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
result()