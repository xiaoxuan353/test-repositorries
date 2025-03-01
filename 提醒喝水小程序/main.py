from time import sleep
from random import choice as ch
def drink_water():
    print(ch(["已经坐了一个小时了,快起来走走","为了你的屁股!我是认真de","动一动吧,花不了几分钟"]))
  
def main():
    while True:
        sleep(60*60)
        drink_water()

if __name__ == "__main__":
    main()