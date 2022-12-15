# Function to find the waiting time for all 
# processes
def findWaitingTime(processes, n, 
                    bt, wt):
    
    # waiting time for first process is 0
    wt[0] = 0
    
    # calculating waiting time
    for i in range(1, n):
        wt[i] = bt[i-1] + wt[i-1]
        
# Function to calculate turn around time
def findTurnAroundTime(processes, n, 
                        bt, wt, tat):
    
    # calculating turnaround time by adding
    # bt[i] + wt[i]
    for i in range(n):
        tat[i] = bt[i] + wt[i]

# Function to calculate average time
def findavgTime(processes, n, bt):
    wt = [0] * n
    tat = [0] * n
    
    # Function to find waiting time of all
    # processes
    findWaitingTime(processes, n, bt, wt)
    
    # Function to find turn around time for
    # all processes
    findTurnAroundTime(processes, n, bt, wt, tat)
    
    # Display processes along with all
    # details
    print("Processes   Burst time   Waiting"   "time   Turn around time")
    total_wt = 0
    total_tat = 0
    for i in range(n):
        
        total_wt = total_wt + wt[i]
        total_tat = total_tat + tat[i]
        print(" ", i + 1, "\t\t", bt[i],
              "\t\t", wt[i], "\t\t", tat[i])
        
    print("\nAverage waiting time = %.5f "%(total_wt /n))
    print("Average turn around time = ", total_tat / n)

# Driver code
if __name__ =="__main__":
    
    # process id's
    # processes = [1, 2, 3]
    print("Enter the number of processes: ")
    m = int(input())
    processes = []
    for i in range(m):
        processes.append(i+1)

    n = len(processes)
    
    # Burst time of all processes
    # burst_time = [10, 5, 8]
    print("Enter the burst time of processes: ")
    burst_time = []
    for i in range(m):
        burst_time.append(int(input()))
    
    findavgTime(processes, n, burst_time)
