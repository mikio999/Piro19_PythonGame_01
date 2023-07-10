import math 
import random
import intro 
import result
import requests
from bs4 import BeautifulSoup as bs
from datetime import datetime
import time

# player_dic = {} # {'player': [life, left_life] }

def main_game ():
    my_name, my_life = intro.intro()
    result.result(my_name, my_life)

    
main_game()

#####




