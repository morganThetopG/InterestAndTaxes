from time import sleep
un=float(input("enter a number: "))
print("\n The Number You Entered Will Enter The Intrest Simulator \n")
I=0
while True:
    sleep(0.3)
    output=0.06*un
    outpu=un+output
    I+=1
    print("Year "+str(I))
    print(str(output)+"\n")
    print(str(outpu)+"\n")
    un=outpu
    if I>68:
        break
print("Thank You For Using Morgan's Tax Simulator")
