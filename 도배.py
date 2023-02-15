import pyautogui
import time

n = int(input('반복할 횟수를 입력해주세요. >>> '))  # 5번 반복을 원하시면 5를 입력.
sen = input('도배할 문장(단어)를 입력해주세요.\n(한국어는 지원하지 않기 때문에 영어로 한국어를 입력해주세요. \nEx.) 안녕하세요 -> dkssudgktpdy)\n>>> ')
print('20초 안에 도배할 곳을 클릭해주세요.')  # 카톡에 도배를 할 경우 카톡 입력창 클릭하고 대기.
for i in range(0,21):
    print(f'{20-i}초 뒤 도배 시작',end='\r')  # 남은 시간을 알려줌.
    time.sleep(1)
for i in range(0,n+1):  # 도배 시작
    pyautogui.write(sen)    # 입력한 글자를 누름.
    pyautogui.keyDown('enter')  # 엔터(return)키를 누름.
