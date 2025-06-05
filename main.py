from module1 import say_hello as h1, is_playing as p1
from module2 import say_hello as h2, is_playing as p2
from module3 import swarp 

def main():
    a, b = swarp(2, 3)
    print(a, b)
    h1()
    h2("Cyaba")
    p1()
    p2()
    
    
    
    
if __name__ == "__main__":
    main()