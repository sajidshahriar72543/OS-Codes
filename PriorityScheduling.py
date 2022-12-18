w = 0 # waiting time
B = [] # burst time
P = [] # priority

n = int(input("Enter the no of processes:\n"))
pMax = 100 # max priority
Wt = [0]*n
for i in range(int(n)):
        b, p = input( # input burst time and priority
            "Enter The BurstTime and Priority for Process : " + str(i+1)+"\n").split() # split the input to take multiple inputs
        B.append(int(b)) # append the burst time to the list
        P.append(int(p)) # append the priority to the list
        if pMax < int(p): # check if the priority is greater than the max priority
            pMax = int(p) # if yes then assign the max priority to the priority

# print(B) # print the burst time (testing purpose)
# print(P) # print the priority (testing purpose)
# print(pMax) # print the max priority (testing purpose)

for j in range(pMax): # loop through the max priority. explanation: max priority is being used as the no of iterations
        for i in range(0, n): # loop through the no of processes. 
            if P[i] == j: # check if the priority is equal to the max priority
                Wt[i] = w # assign the waiting time to the waiting time list
                w = w+B[i] # increment the waiting time

print("Process\tBurstTime\tPriority\tWaitingTime\tTurnaroundTime")
for i in range(0, int(n)):
        print("p"+str(i)+"\t"+str(B[i])+"\t\t"+str(P[i]) +
              "\t\t"+str(Wt[i])+"\t\t"+str(Wt[i]+B[i]))

totalTAT = 0
totalWT = 0
for i in range(0, int(n)):
        totalTAT = totalTAT + Wt[i]+B[i]
        totalWT = totalWT + Wt[i]

print("Total Turnaround Time: "+str(totalTAT))
print("Total Waiting Time: "+str(totalWT))        
print("Average Turnaround Time: "+str(totalTAT/int(n)))
print("Average Waiting Time: "+str(totalWT/int(n)))
