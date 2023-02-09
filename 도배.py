import pyautogui
import time

n = int(input('반복할 횟수를 입력해주세요. >>> '))
sen = input('도배할 문장(단어)를 입력해주세요.\n(한국어는 지원하지 않기 때문에 영어로 한국어를 입력해주세요. \nEx.) 안녕하세요 -> dkssudgktpdy)\n>>> ')
print('20초 안에 도배할 곳을 클릭해주세요.')
for i in range(0,21):
    print(f'{20-i}초 뒤 도배 시작',end='\r')
    time.sleep(1)
for i in range(0,n+1):
    pyautogui.write(sen)
    pyautogui.keyDown('enter')


# 도배 테스트
'''

'''