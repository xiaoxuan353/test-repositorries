import random
def other_input():
    enemy = random.randint(1,3)
    return enemy
#1=石头 2=剪刀 3=布

def your():
    while True:
        my_decision =input("请输入石头剪刀布")
        if my_decision == "石头":
            my_decision = 1
            break
        elif my_decision == "剪刀":
            my_decision = 2
            break
        elif my_decision == "布":
            my_decision = 3
            break
        else:
            print("输入有误,请重新输入")
    return my_decision

def judgment(my_decision, enemy,b):
    number = my_decision - enemy
    if number == -1 or number == 2:
        print("you win")
        b = 1
    elif number == 1 or number == -2:
        print("you lose,please try again")
        b = 0
    else:
        print("平局,再试一次吧")
        b = 0
    return b

def main():
    a = True
    while a:
        enemy = other_input()
        my_decision = your()
        b = 0
        if judgment(my_decision,enemy,b) == 1:
            a = False

if __name__ == "__main__":
    main()