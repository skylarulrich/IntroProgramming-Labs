#File: chaos.py
#A simple program illustrating chaotic behavior

def main():
    print("This program illustrates a chaotic function")
    x= eval(input("Enter a number between 0 and 1: "))
    k= eval(input("Enter a second number between 0 and 1: "))
    print("input 1", "           input 2")
    for i in range(10):
        x= 3.9 * x * (1-x)
        k= 3.9 * k * (1-k)
        print(x , k)

main()
