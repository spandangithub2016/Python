import win_unicode_console

win_unicode_console.enable()
try:
    inp=open("bengali.txt",'r')
    for word in inp.readlines():
        print(word)
finally:
    win_unicode_console.disable()
