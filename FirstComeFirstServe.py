n = int(input("Enter the number of processes: "))
top = 0
at = []
bt = []
ct = []
tat = []
wt = []
avgwt = 0
avgtat = 0
for i in range (n):
    inp = int(input("Enter the arrival time of process " + str(i+1) + ": "))
    at.append(inp)
    inp = int(input("Enter the burst time of process " + str(i+1) + ": "))
    bt.append(inp)
    print()

for i in range (n):
    if i==0: #first process
        top += bt[i] 
        ct.append(top) #completion time
    elif i>0: #other processes
        if at[i] > top: # if arrival time is greater than completion time
            top = at[i]+bt[i] 
            ct.append(top) #completion time
        else: #if arrival time is less than completion time
            top += bt[i]
            ct.append(top)
print("Arrival Time Calculated\n")

for i in range (n):
    temp = ct[i] - at[i]
    tat.append(temp) #turn around time
    temp = tat[i] - bt[i]
    wt.append(temp) #waiting time

print("Turn Around Time Calculated\n Waiting Time Calculated\n")

print("PID\tAT\tBT\tCT\tTAT\tWT")
for i in range (n):
    print(str(i+1) + "\t" + str(at[i]) + "\t" + str(bt[i]) + "\t" + str(ct[i]) + "\t" + str(tat[i]) + "\t" + str(wt[i]))
    avgwt += wt[i]
    avgtat += tat[i]

avgwt = avgwt/n
avgtat = avgtat/n

print("Average Waiting Time: " + str(avgwt))
print("Average Turn Around Time: " + str(avgtat))