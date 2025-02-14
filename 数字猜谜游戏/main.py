import random
goal_number=random.randint(0,100)#包含0到100
for i in range(7):#只能猜7次
    try:
        number = int(input('请输入[0,100]间的整数'))
        if number > goal_number:
            print(f'大了,还能猜{6-i}次')
        if i == 6:
            print('game over!')
        elif number < goal_number:
            print(f'小了,还能猜{6-i}次')
        if i == 6:
            print('game over!')
        else:
           print(f'答对了,正确答案是{goal_number}')
        break
    except:
        print('请输入正确整数')
    
    