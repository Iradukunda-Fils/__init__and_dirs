from module1 import say_hello as h1, is_playing as p1
from module2 import say_hello as h2, is_playing as p2
from module3 import swarp 
import module1
import module2
import module3

def main():
    a, b = swarp(2, 3)
    print(a, b)
    h1()
    h2("Cyaba")
    p1()
    p2()
        
    print("The module found and imported successfully!" if hasattr(module1, 'hello') else "Module1 not found or 'p1' not defined.")
    
    print("The module found and imported successfully!" if hasattr(module2, 'say_hello') else "Module2 not found or 'p2' not defined.")
    print("The module found and imported successfully!" if hasattr(module3, 'swarp') else "Module3 not found or 'swarp' not defined.", end="\n\n")
    
if __name__ == "__main__":
    main()