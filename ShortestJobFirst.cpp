// File Name: FirstComeFirstServe.cpp
// Date: December 15, 2022
// Time: 01:10:17
// Author : Sajid (git : sajidshahriar72543)

/*
    Idea is to sort the processes according to their burst time then apply FCFS
*/

#include <bits/stdc++.h>
using namespace std;
void withoutArrival(int n);
void withArrival(int n);
int main()
{
    cout << "Enter no of processes: ";
    int n;
    cin >> n;
    withoutArrival(n);
    // return 0;
}
void withoutArrival(int n)
{
    int bt[n], wt[n], tat[n];
    cout << "Enter burst time of processes: ";
    for (int i = 0; i < n; i++)
    {
        cin >> bt[i]; // input burst time
    }

    for (int i = 0; i < n; i++)
    {
        for (int j = i + 1; j < n; j++)
        {
            if (bt[i] > bt[j])
            {
                swap(bt[i], bt[j]);
            }
        }
    }

    wt[0] = 0; // waiting time of first process is 0
    for (int i = 1; i < n; i++)
    {
        wt[i] = bt[i - 1] + wt[i - 1]; // waiting time of other processes
    }
    for (int i = 0; i < n; i++)
    {
        tat[i] = bt[i] + wt[i]; // turn around time of processes
    }
    cout << "Process\tBT\tWT\tTAT" << endl;
    for (int i = 0; i < n; i++)
    {
        cout << i + 1 << "\t" << bt[i] << "\t" << wt[i] << "\t" << tat[i] << endl;
    }
    float sum = 0;
    for (int i = 0; i < n; i++)
    {
        sum += wt[i]; // sum of waiting time
    }
    cout << "Average waiting time: " << float(sum / n) << endl;
    sum = 0;
    for (int i = 0; i < n; i++)
    {
        sum += tat[i]; // sum of turn around time
    }
    cout << "Average turn around time: " << float(sum / n);
}