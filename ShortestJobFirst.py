# File Name: ShortestJobFirst.py
# Date: 2022-12-15
# Date: December 15, 2022
# Time: 17:09:45
# Author : Sajid (git : sajidshahriar72543)

# Idea is to sort the processes according to their burst time and then execute them in that order
# This is a non-preemptive algorithm, tha is why arrival time is not considered
# This is just FCFS with a sorted list of processes

n = int(input("Enter the number of processes: "))
top = 0
bt = []
ct = []
tat = []
wt = []
avgwt = 0
avgtat = 0
for i in range (n):
    inp = int(input("Enter the burst time of process " + str(i+1) + ": "))
    bt.append(inp)
    print()

for i in range (n):
    if i==0: #first process
        top += bt[i] 
        ct.append(top) #completion time
    elif i>0: #other processes
        top += bt[i] 
        ct.append(top) #completion time

print("Burst Time Calculated\n")

for i in range (n):
    temp = ct[i] #- at[i]
    tat.append(temp) #turn around time
    temp = tat[i] - bt[i]
    wt.append(temp) #waiting time

print("Turn Around Time Calculated\n Waiting Time Calculated\n")

print("PID\tBT\tCT\tTAT\tWT")
for i in range (n):
    print(str(i+1) + "\t" + str(bt[i]) + "\t" + str(ct[i]) + "\t" + str(tat[i]) + "\t" + str(wt[i]))
    avgwt += wt[i]
    avgtat += tat[i]

avgwt = avgwt/n
avgtat = avgtat/n

print("Average Waiting Time: " + str(avgwt))
print("Average Turn Around Time: " + str(avgtat))