n = int(input("Enter the number of processes: ")) # number of processes
ch = input("consider arrival tile? (y/n): ")
if ch == 'y': # if arrival time is considered
    at = [] # arrival time array
    print("Enter the arrival time of processes: ") 
    for i in range(n): 
        at.append(int(input())) # input arrival time
else:
    at = [0]*n # if arrival time is not considered
bt = [] # burst time array
print("Enter the burst time of processes: ")
for i in range(n):
    bt.append(int(input())) # input burst time
wt = [0]*n # waiting time array
tat = [0]*n # turnaround time array
ct = [0]*n # completion time array
rt = [0]*n # remaining time array
tq = int(input("Time quantum: ")) # time quantum
rt = bt[:] # copy burst time to remaining time
t = 0 # time
flag = 0 # flag
while True: # loop until all processes are completed
    for i in range(n): # loop for each process
        if rt[i] > 0: # if remaining time is greater than 0
            if rt[i] > tq: # if remaining time is greater than time quantum
                t += tq # add time quantum to time
                rt[i] -= tq # subtract time quantum from remaining time
            else: # if remaining time is less than time quantum
                t += rt[i] # add remaining time to time
                tat[i] = t - at[i] # calculate turnaround time
                wt[i] = tat[i] - bt[i] # calculate waiting time
                rt[i] = 0 # remaining time is 0
    if sum(rt) == 0: # if all processes are completed
        break # break the loop
print("Process\t\tBurst Time\tArrival Time\tWaiting Time\tTurnaround Time") 
for i in range(n):
    print(i+1, "\t\t", bt[i], "\t\t", at[i], "\t\t", wt[i], "\t\t", tat[i])
print("Average waiting time: ", sum(wt)/n) # print average waiting time
print("Average turnaround time: ", sum(tat)/n) # print average turnaround time
