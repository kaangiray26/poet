#!/usr/bin/python
#-*- encoding:utf-8 -*-
import os
import time
import random
chars="abcdefghjlnoprstuvyz"
length=input("Lines?\n:")
firstline=raw_input("First word?\n:")
times=input("Number of poems?\n:")
os.system("open /Applications/TextEdit.app/")
time.sleep(1)
os.system("""osascript -e 'tell application "System Events" to keystroke "n" using command down'""")
time.sleep(1)
for x in range(0,times):
    os.system("""osascript -e 'tell application "System Events" to keystroke "#########"'""")
    os.system(""" osascript -e 'tell application "System Events"
        key code 76
    end tell' """)
    os.system("""osascript -e 'tell application "System Events" to keystroke "%s"'""" %(firstline))
    for i in range(0,length):
        words=random.randint(2,5)
        for w in range(0,words):
            if random.randint(0,2) == 2:
                char=chars[random.randint(0,19)]
                os.system("""osascript -e 'tell application "System Events" to keystroke "%s"'""" %(char))
            os.system(""" osascript -e 'tell application "System Events"
            key code 53
    end tell' """)
            option=random.randint(1,20)
            for a in range (0,option):
                os.system("""osascript -e 'tell application "System Events" to key code 125 using option down'""")
            os.system(""" osascript -e 'tell application "System Events"
        	key code 76
        end tell' """)
            os.system(""" osascript -e 'tell application "System Events"
        	key code 49
        end tell' """)
        os.system(""" osascript -e 'tell application "System Events"
        key code 76
    end tell' """)
