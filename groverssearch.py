import matplotlib.pyplot as plt
import numpy as np
from qiskit import IBMQ, Aer, QuantumCircuit, ClassicalRegister, QuantumRegister, execute, transpile, assemble
from qiskit.providers.ibmq import least_busy
from qiskit.quantum_info import Statevector
from qiskit.visualization import plot_histogram

#setup the quantum circuit with n qubits and place all qubits in superposition
n = 2
grover = QuantumCircuit(n)
grover.h(range(n))

marked_element = '101'  # For example, we want to find the element '101' in an unsorted database

# Grover's iterations
iterations = int(round(3.14 / 4 * (2 ** (n / 2))))
for i in range(iterations):
    # Oracle: apply a phase flip to the marked element
    for j in range(n):
        if marked_element[i] == '1':
            grover.z(i)
    grover.mct(list(range(n)), n-1)  # multi-controlled Toffoli gate
    for i in range(n):
        if marked_element[i] == '1':
            grover.z(i)

# Amplification: apply Hadamard and X gates
grover.h(range(n))
grover.x(range(n))
grover.mct(list(range(n-1)), n-1)  # multi-controlled Toffoli gate
grover.x(range(n))
grover.h(range(n))

# Measure the qubits
grover.measure(range(n), range(n))
