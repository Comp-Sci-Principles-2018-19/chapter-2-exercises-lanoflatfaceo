P=10000
n=12
r=0.08
t=input("How many years?")
t=int(t)
A=P*(1+r/n)**(n*t)
A=A*100
A=int(A)
A=A/100
print(A,"dollars")
