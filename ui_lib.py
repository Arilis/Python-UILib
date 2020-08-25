import os, time, ctypes

start_time = time.time()
Center_Amount = 0

def Clear():
    os.system('cls')
    
def Title(value):
    new_title = value.center(Center_Amount)
    invisible = "".center(Center_Amount)
    print(f"|{new_title}|")
    print(f"|{invisible}|")

def CreateOption(option):
    new_option = option.center(Center_Amount)
    print(f"|{new_option}|")

def Credits(value):
    value = f"By {value}"
    new_credits = value.center(Center_Amount)
    invisible = "".center(Center_Amount)
    print(f"|{invisible}|")
    print(f"|{new_credits}|")

def TopLines():
    print("╔" + "-" * Center_Amount + "╗")

def BottomLines():
    print("╚" + "-" * Center_Amount + "╝")
    
def SetTitle(title):
    ctypes.windll.kernel32.SetConsoleTitleW(title)
    
def Debug():
    print(f"UILib finished in {time.time() - start_time} seconds.")
