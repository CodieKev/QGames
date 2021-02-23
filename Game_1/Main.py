# -*- coding: utf-8 -*-
"""
Created on Tue Feb 23 00:16:36 2021

@author: codie
"""
from qiskit import QuantumRegister, ClassicalRegister
from qiskit import QuantumCircuit, execute, Aer
import numpy as np

n = 2                                            # Number of player(alive)
m = 1                                  # Total number of sources that can deal damage    
l = 0
Dam = [1]  
k=2*n+m+l
const_1= 0.668
A = [1,1,const_1,1,1]

def Event(A):
    Damage = [0]*n
    counts = 10000
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
            qc.u3(A[i+n]*(1-Dam[i-n])*np.pi, 0, 0, q[i+n])
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
    qc.draw()
    backend = Aer.get_backend('qasm_simulator')
    job = execute(qc, backend=backend,shots = counts)
    job_result = job.result()
    A = list(job_result.get_counts(qc).keys())
    for i in A:
        print(i)
        B = list(i)
        for j in range (n):
            if B[j] == '1':
                Damage[j]+= int(job_result.get_counts(qc).get(i)) /counts
    return Damage

print(Event(A))