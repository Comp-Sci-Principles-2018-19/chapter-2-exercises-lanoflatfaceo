total_secs = int(input("How many seconds, in total?"))
hours = total_secs // 3600
secs_still_remaining = total_secs / 60
minutes = secs_still_remaining // 60
secs_finally_remaining = secs_still_remaining / 60

print("Hrs=", hours, " mines=", minutes,
                                  "secs=", secs_finally_remaining)

name=int(input("What is your name?"))
print("okey", name)