# 절차지향적 프로그래밍

# 1. 상대방으로부터 문자열을 받기.

import random

def get_player_choice():
    """
    get_player_choice() --> string 반환
    반환값 : "가위" or "바위" or "보"
    """
    li=("가위","바위","보")
    mine=input("선택해라 휴먼 : ")
    while mine not in li:
        mine=input("똑바로 선택해라 휴먼 : ")
    return mine 

def get_computer_choice():
    """
    get_computer_choice() --> string 반환
    반환값: "가위" | "바위" | "보"
    """
    li=("가위","바위","보")
    computer=random.randint(0,2)
    computer=li[computer]
    return computer

def who_wins(player, com):
    """
    who_wins(player, com) --> string
    반환값 : 플레이어가 이기면 문자로 "player"
            컴퓨터가 이기면 문자로 "computer"
            비기면 None
    """
    if player == com:
        return None
    elif (player == "가위" and com == "보")or \
        (player == "바위" and com == "가위")or \
        (player == "보" and com == "바위"):
        return "player"
    elif (player == "가위" and com == "바위")or \
        (player == "바위" and com == "보")or \
        (player == "보" and com == "가위"):
        return "computer"

def play_one():
    """
    who_wins(player, com) --> string
    반환값 : 플레이어가 이기면 문자로 "player"
    컴퓨터가 이기면 문자로 "computer"
    """
    while True:
        player=get_player_choice()
        com=get_computer_choice()
        result = who_wins(player, com)
        print(f"player:{player}, computer: {com}")
        if result == "player":
            print("이겼다")
            return "player"
        elif result == "computer":
            print("졌다")
            return "computer"
        else:
            print("비겼다")
            continue
        
def check_final_winner(result):
    """
    check_final_winner(result) --> string
    result : ex) ['player', 'player']
    반환값 : 만약 result 안에 'player' 가 두 개 이상이면 : 'player'
            'computer' 가 두 개 이상이면 : 'computer'
            otherwise : none
    """
    print(f"player: {result.count('player')}승, computer: {result.count('computer')}승")
    if result.count('player') >= 2:
        return "player"
    elif result.count('computer') >= 2:
        return "computer"
    else:
        None
    

def play():
    """
    play() --> none
    3판 2선승 가위바위보 게임
    """
    result_list=[]
    while True:
        result_list.append(play_one())
        checked=check_final_winner(result_list)
        if checked=="player":
            print("당신이 이겼다")
            break
        elif checked=="computer":
            print("당신이 졌다")
            break
        else:
            continue
    


if __name__ == "__main__":
    play()