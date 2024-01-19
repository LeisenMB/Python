import pyautogui as pg ,webbrowser as web , time as tm
web.open("https://web.whatsapp.com/send?phone=54911239103993")
tm.sleep(1)


for i in range (10):
    pg.write("vamos a jugar")
    pg.press("enter")