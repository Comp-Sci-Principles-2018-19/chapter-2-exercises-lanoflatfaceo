time=int(input("what time is it?"))
time_to_wait=int(input("How long do you want to wait?"))
actual_time=time+time_to_wait
time_v2=actual_time%24
if time_v2<12:
    print(time_v2,"A.M")
else:
    print(time_v2-12,"P.M.")
    
