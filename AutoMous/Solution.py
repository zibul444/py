import time

import pyautogui

print('__---__');
pyautogui.PAUSE = 1;
pyautogui.FAILSAFE = True;

try:
    scrinSize = pyautogui.size();
    print(scrinSize);

    print (scrinSize[0]);
    print (scrinSize[1]);

    pyautogui.moveTo(40, scrinSize[1]/2);
    # for x in range(scrinSize[1]):
    i = 0;
    while True:
        if i < 2:
            pyautogui.moveRel(20, 0);
            time.sleep(10);
            i = i+1;
        else:
            i=0;
            pyautogui.moveTo(40, scrinSize[1] / 2);
        #     break

    # todo  idea
    pyautogui.keyDown('ctrl');
    pyautogui.press('c');
    pyautogui.keyUp('ctrl');


except KeyboardInterrupt:
    print ('-_-_-_ Ctrl + c _-_-_-')

except pyautogui.FailSafeException:
    print ('-_-_-_Exception_-_-_-')

print ('-_-_-_Passed out_-_-_-')
