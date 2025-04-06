import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-10,10,400)
while True:
    print("MENU")
    print("1. y= 2x")
    print("2. y= x^2")
    print("3. y= e^x")
    print("4. y= sqrt(x)")
    print("5. exit")
    ch = int(input("enter your choice : "))
    if ch ==1:
        y =2*x
        plt.ylim(-100,100)
        plt.plot(x,y,label="f(x)=2x",color="blue")
        plt.title("plot of f(x)=2x")
        plt.xlabel("x")
        plt.ylabel("f(x)")
        plt.grid(True,alpha=0.25)
        plt.legend()
        plt.show()
    elif ch==2:
        y =x**2
        plt.ylim(-100,100)
        plt.plot(x,y,label="f(x)=x^2",color = "blue")
        plt.xlabel("x")
        plt.ylabel("f(x)")
        plt.title("plot for f(x)= x^2")
        plt.grid(True,alpha =0.25)
        plt.legend()
        plt.show()
    elif ch==3:
        y =np.exp(x)
        plt.ylim(-100,100)
        plt.plot(x,y,label="f(x)=e^x",color = "blue")
        plt.xlabel("x")
        plt.ylabel("f(x)")
        plt.title("plot for f(x)= e^x")
        plt.grid(True,alpha =0.25)
        plt.legend()
        plt.show()
    elif ch==4:
        y =np.sqrt(x)
        x= np.linspace(0,10,400)
        plt.ylim(0,100)
        plt.plot(x,y,label="f(x)=sqrt(x)",color = "blue")
        plt.xlabel("x")
        plt.ylabel("f(x)")
        plt.title("plot for f(x)= sqrt(x)")
        plt.grid(True,alpha =0.25)
        plt.legend()
        plt.show()
    elif ch==5:
        break
    else:
        print("invalid choice!!")
