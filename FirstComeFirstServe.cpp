// File Name: FirstComeFirstServe.cpp
// Date: December 15, 2022
// Time: 01:10:17
// Author : Sajid (git : sajidshahriar72543)

#include <bits/stdc++.h>
using namespace std;
void withoutArrival(int n);
void withArrival(int n);
int main()
{
    cout << "Enter no of processes: ";
    int n;
    cin >> n;
    cout << "Enter 1 if arrival time is given else 0: ";
    int choice;
    cin >> choice;
    if (choice == 1)
    {
        withArrival(n);
        // your code here
    }
    else
    {
        withoutArrival(n);
    }
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
    int sum = 0;
    for (int i = 0; i < n; i++)
    {
        sum += wt[i]; // sum of waiting time
    }
    cout << "Average waiting time: " << sum / n;
    sum = 0;
    for (int i = 0; i < n; i++)
    {
        sum += tat[i]; // sum of turn around time
    }
    cout << "Average turn around time: " << sum / n;
}
void withArrival(int n)
{
    int at[n], bt[n], wt[n], tat[n];
    cout << "Enter arrival time of processes: ";
    for (int i = 0; i < n; i++)
    {
        cin >> at[i]; // input arrival time
    }
    cout << "Enter burst time of processes: ";
    for (int i = 0; i < n; i++)
    {
        cin >> bt[i]; // input burst time
    }
    wt[0] = 0; // waiting time of first process is 0
    int ct[n];
    ct[0] = 0;
    for (int i = 0; i < n; i++)
    {
        wt[i] = 0;
        tat[i] = 0;
        ct[i + 1] = ct[i] + bt[i]; // completion time of processes
        wt[i] = ct[i] - at[i];     // waiting time of processes
        tat[i] = wt[i] + bt[i];    // turn around time of processes
    }
    cout << "Process\tAT\tBT\tCT\tWT\tTAT" << endl;
    for (int i = 0; i < n; i++)
    {
        cout << i + 1 << "\t" << at[i] << "\t" << bt[i] << "\t" << ct[i] << "\t" << wt[i] << "\t" << tat[i] << endl;
    }
    int sum = 0;
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