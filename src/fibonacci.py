import datetime


ts = datetime.datetime.now().timestamp()
print(ts)
# A very resource consuming way of implementing


def recur_fib(n):
    if n <= 1:
        return n
    else:
        return(recur_fib(n-2) + recur_fib(n-1))


print("Fibonacci sequence")
for i in range(17):
    print(recur_fib(i))

t1 = datetime.datetime.now().timestamp() - ts
print(t1)
ts = datetime.datetime.now().timestamp()

# A more memory efficient way of implementing it

fiblist = [0, 1]
print("Fibonacci sequence again")
print("0")
for i in range(17):
    print(fiblist[1])
    temp = fiblist[1]
    fiblist[1] = fiblist[0] + fiblist[1]
    fiblist[0] = temp

t2 = datetime.datetime.now().timestamp() - ts
print(t2)


print("Execution efficiency difference")
print(t2/t1)
