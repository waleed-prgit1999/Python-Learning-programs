'''import time
current_time = time.asctime(time.localtime())
print(current_time)

a=time.localtime()
for item in a:
    print(item)
###############################   different time functions    ###########################

f= 5; k=8
a = time.perf_counter()      # performance counter returns float value of time in seconds            
i=1
while i<=70:
    res = f*f*i+(k/4)
    print(res)
    i=i+1
    time.sleep(0.1)

b = time.perf_counter()                    #   it also incudes the sleep time
print("Time Elapsed =",b-a)'''

list = ["waleed","hassan","hareem","hamza","rameen","ayan","abdul rehman","rayan"]
tup = ("waleed","hassan","hareem","hamza","rameen","ayan","abdul rehman","rayan")
for index,items in enumerate(tup):     #enumerate function usage
    if index % 2 != 0:
        print(items)
