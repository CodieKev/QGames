"""
Created on Sun Dec 22 23:56:32 2019

@author: codie
"""


from qiskit import QuantumRegister, ClassicalRegister
from qiskit import QuantumCircuit, execute, Aer
import numpy as np

###########<User_Input>###########

n = int(input("Number of player:-"))                                            # Number of player(alive)
m = int(input("Number of Source of Damage:-"))                                  # Total number of sources that can deal damage    
l = int(input("Total number of Constraint:-"))                                  # Total constraints on all the source


Dam = list(map(float,input("Enter the Base damage with space between them : ").strip().split()))[:m]    # Base damage from each of the source
Health = [100]*n                                                                # Initial Health
###########</User_Input>###########

###########<Circuit_Algorithm>###########

def Event(A):
    Damage = [0]*n
    qc = QuantumCircuit()
    q = QuantumRegister(2*(n+l+m)+1+n, 'q')
    c = ClassicalRegister(n, 'c')    
    qc.add_register(q)
    qc.add_register(c)
    for i in range (2*n+m+l+1):
        if i <n:                                                               
            qc.u3(A[i]*np.pi, 0, 0, q[i])
            qc.x(q[i+n])
            qc.u3(A[i+n]*np.pi, 0, 0, q[i+n])
        if n<=i<n+m:                                                            
            qc.x(q[i+n])
            qc.u3(A[i+n]*Dam[i-n]*np.pi, 0, 0, q[i+n])
        if n+m<=i<n+m+l:
            qc.x(q[i+n])
            qc.u3(A[i+n]*np.pi, 0, 0, q[i+n])
        if i == n+m+l:
            qc.mct(q[2*n:2*n+l+m], q[2*n+m+l+1], q[3*n+m+l+2:3*n+2*l+2*m+1])
        if n+m+l<i<2*n+m+l+1:        
            qc.ccx(q[i-(n+m+l+1)], q[i-(m+l+1)], q[2*n+m+l])           
            qc.ccx(q[2*n+m+l], q[2*n+m+l+1], q[i+n+1])
            qc.ccx(q[i-(n+m+l+1)], q[i-(m+l+1)], q[2*n+m+l])
            qc.measure(q[i+1+n], c[2*n+m+l-i])
    backend = Aer.get_backend('qasm_simulator')
    job = execute(qc, backend=backend)
    job_result = job.result()
    A = list(job_result.get_counts(qc).keys())
    for i in A:
        B = list(i)
        for j in range (n):
            if B[j] == '1':
                Damage[j]+= int(job_result.get_counts(qc).get(i))/1024
    return Damage

###########</Circuit_Algorithm>###########

###########<Health_Calc_Loop>###########

while n>1:                                                                      # Makes it self adjesting for plyers more then 1
    control = 0                                                                 # Control for while loop
    k=2*n+m+l
    while control==0:
        remake = []
        Health_new =[]
        print('give',k,'input with space between them')
        E_C = list(map(float,input("Enter the Event conditions: ").strip().split()))[:k]
        print(E_C)
        Event_Output = Event(E_C)
        for i in range (n):
            Health[i] -= (Event_Output[i])*100
            if Health[i]<=0:
                control=1                                                       # If some players dies Control stops while loop and redesign the circuit
                remake.append(Health[i])                                        # Takes those died player data and stores it to be removed
        if control==1:                                                          # Checks if any player died then removes its data from the storage
            for i in range (len(remake)):
                Health.remove(remake[i])
        n = len(Health)                                                         # Total no of alive player left
        print(Health)
        
###########</Health_Calc_Loop>###########
