# File Name: Bankers_algorithm.py
# n = int(input("Enter the number of processes: "))
# m = int(input("Enter the number of resources: "))
n = int(input())
m = int(input())
# print("Enter the allocated matrix: ")
allocated = [] # allocated matrix
for i in range(n):
    allocated.append(list(map(int, input().split()))) # Input the allocated matrix
# print("Enter the maximum matrix: ")
maximum = [] # Maximum matrix : maximum resources that can be allocated to processes
for i in range(n):
    maximum.append(list(map(int, input().split()))) # Input the maximum matrix
# print("Enter the available matrix: ") # Available matrix : resources that are available
available = list(map(int, input().split())) # Input the available matrix.
need = [] # Need matrix : resources that are needed to complete the processes
for i in range(n):
    need.append([]) 
    for j in range(m):
        need[i].append(maximum[i][j] - allocated[i][j]) # Calculate the need matrix
finish = [0] * n 
safeSeq = [0] * n # Safe sequence : Initially set to 0
# work = available # *Temporary matrix* Work matrix : Initially set to available matrix 
count = 0
while count < n:
    found = False # found is set to false because we will make it true if we find a safe sequence
    for i in range(n):
        if finish[i] == 0: # If the process is not finished then we will check if it is in safe state
            for j in range(m): # j in range of m means we are checking for all the processes
                if (need[i][j] > available[j]) or (need[i][j]<0): # If the need is greater than available then we will break becuase there is a deadlock
                        break # breaking the loop and returning back to the print function
            if j == m - 1: # checking if j is equal to m-1 because if it is then we will have to check for all the processes 
                for k in range(m): 
                    available[k] += allocated[i][k] # available = available + allocated
                safeSeq[count] = i # safe sequence is equal to i because it is in safe state
                count += 1 # incrementing the count because we have found that allocating resource to a process is safe
                finish[i] = 1 # finish is set to 1 because the current process is finished
                found = True # found is set to true because we have found a process in the safe sequence. After this we will check for the next process
    if found == False: # If found is false then we will print that the system is not in safe state
        print("System is not in safe state")
        exit(0)
print("\n")

print("PID\tAllocated\tMaximum\t\tNeed\t\tAvailable")
for i in range(n):
    print(i+1, end = "\t")
    for j in range(m):
        print(allocated[i][j], end = " ")
    print(end = "\t\t")
    for j in range(m):
        print(maximum[i][j], end = " ")
    print(end = "\t\t")
    for j in range(m):
        print(need[i][j], end = " ")
    print(end = "\t\t")
    if i == 0:
        for j in range(m):
            print(available[j], end = " ")
    print()

print("System is in safe state.")
print("Safe sequence is: ", end = " ")
for i in safeSeq:
    print(str(i+1), end = " ")
# print()
print("\n")

# if none of the requests can be granted, the loop will terminate after n iterations
