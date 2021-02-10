# -*- coding: utf-8 -*-
"""
Created on Thu Jan 28 20:49:43 2021

@author: duxingyu8
"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import PySpice.Logging.Logging as Logging
logger = Logging.setup_logging()
from PySpice.Spice.Netlist import Circuit
from PySpice.Spice.Library import SpiceLibrary
from PySpice.Unit import *
import PySpice
import os
#the purpose of the following code is to clean all
#clear = lambda: os.system('cls')
#clear()

##dataset
Input=np.array([[0,0],[0,1],[1,0],[1,1]])

##circuit parameter
Rin=0.1   
gamma=1000
lamda=1
step_time=0.1
end_time=30

##include memristor
libraries_path = "~/ngspice/PySpice/examples/libraries"
spice_library = SpiceLibrary(libraries_path)

##create circuit
a=0
results=np.zeros((1,4))


circuit_list=[]
simulator_list=[]
analysis_list=[]
for num_cycle in range(0,4):
    locals()["circuit"+str(a)] = Circuit('XOR problem circuit')
    circuit_list.append(locals()["circuit"+str(a)])
    a=a+1
a=0

##build the circuit and do the simulation
for num_cycle in range(0,4):
    circuit_list[a].include(spice_library['MEM_VTEAMN1'])
    circuit_list[a].X('D1', 'MEM_VTEAMN1', 'N1In', 'N1Out', 'state1')
    circuit_list[a].X('D2', 'MEM_VTEAMN1', 'N2In', 'N2Out', 'state2')
    
    circuit_list[a].PulseVoltageSource('input1', 'IN1_1', circuit_list[a].gnd,initial_value=0@u_V, pulsed_value=0.2*Input[num_cycle,0]@u_V, pulse_width=20@u_s,  period=80@u_s, rise_time=1@u_ns, fall_time=1@u_ns, delay_time=3@u_s)
    circuit_list[a].PulseVoltageSource('input2', 'IN1_2', circuit_list[a].gnd, initial_value=0@u_V, pulsed_value=-0.2*Input[num_cycle,1]@u_V, pulse_width=20@u_s,  period=80@u_s, rise_time=1@u_ns, fall_time=1@u_ns, delay_time=3@u_s)
    circuit_list[a].V('input3', 'IN1_bias', circuit_list[a].gnd, 0.07@u_V)
    circuit_list[a].PulseVoltageSource('input4', 'IN2_1', circuit_list[a].gnd, initial_value=0@u_V, pulsed_value=-0.2*Input[num_cycle,0]@u_V, pulse_width=20@u_s,  period=80@u_s, rise_time=1@u_ns, fall_time=1@u_ns, delay_time=3@u_s)
    circuit_list[a].PulseVoltageSource('input5', 'IN2_2', circuit_list[a].gnd, initial_value=0@u_V, pulsed_value=0.2*Input[num_cycle,1]@u_V, pulse_width=20@u_s,  period=80@u_s, rise_time=1@u_ns, fall_time=1@u_ns, delay_time=3@u_s)
    circuit_list[a].V('input6', 'IN2_bias', circuit_list[a].gnd, 0.05@u_V)
    circuit_list[a].R(1, 'IN1_1', 'N1In', 110@u_Ω)
    circuit_list[a].R(2, 'IN1_2', 'N1In', 110@u_Ω)
    circuit_list[a].R(3, 'IN1_bias', 'N1In', 70@u_Ω)
    circuit_list[a].R(4, 'IN2_1', 'N2In', 120@u_Ω)
    circuit_list[a].R(5, 'IN2_2', 'N2In', 120@u_Ω)
    circuit_list[a].R(6, 'IN2_bias','N2In',80@u_Ω)
    circuit_list[a].R(7, 'N1Out','Output',118@u_Ω)
    circuit_list[a].R(8, 'N2Out','Output',120.6@u_Ω)
    circuit_list[a].R(9, 'N1Out',circuit_list[a].gnd,90@u_kΩ)
    circuit_list[a].R(10, 'N2Out',circuit_list[a].gnd,90@u_kΩ)
    
    locals()["simulator" + str(a)] = circuit_list[a].simulator(temperature=25, nominal_temperature=25)
    simulator_list.append(locals()["simulator" + str(a)])
    locals()["analysis" + str(a)]  = simulator_list[a].transient(step_time=step_time, end_time=end_time)
    analysis_list.append(locals()["analysis" + str(a)])
#    print(circuit_list[a])
    
#    figure, ax = plt.subplots(figsize=(20, 10))
#    ax.plot(analysis_list[a]._time,analysis_list[a]['Output'])
#    ax.legend(('Vin [V]', 'Vout [V]'), loc=(.8,.8), fontsize=30)
#    ax.grid()
#    ax.set_xlabel('t [s]', fontsize=60)
#    ax.set_ylabel('[V]', fontsize=60)
#    plt.tick_params(labelsize=20)
#    plt.tight_layout()
#    plt.show()
    results[0][num_cycle]=analysis_list[a]['Output'][271]
    
    a=a+1
    