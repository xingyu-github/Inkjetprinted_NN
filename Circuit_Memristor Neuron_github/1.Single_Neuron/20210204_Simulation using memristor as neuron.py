# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 17:09:09 2021

@author: duxingyu8
"""

import matplotlib.pyplot as plt
import PySpice.Logging.Logging as Logging
logger = Logging.setup_logging()
from PySpice.Doc.ExampleTools import find_libraries
from PySpice.Probe.Plot import plot
from PySpice.Spice.Library import SpiceLibrary
from PySpice.Spice.Netlist import Circuit,SubCircuit, SubCircuitFactory
from PySpice.Unit import *
import numpy as np
import os
#the purpose of the following code is to clean all
clear = lambda: os.system('cls')
clear()

Vamp=1200##in mV
Vin1=Vamp
Bias=0
Rin=1000#in ohms
Rground=1000 ##in ohms
step_time=0.1
end=np.array([5,10,20,40,80])
circuit_list=[]
simulator_list=[]
analysis_list=[]
results=np.zeros((5,2,2400))
libraries_path = "~/ngspice/PySpice/examples/libraries"
spice_library = SpiceLibrary(libraries_path)

for a in range(0,13000):  
    locals()["circuit"+str(a)] = Circuit('simulation')
    circuit_list.append(locals()["circuit"+str(a)])

a=0
for i in range (0,5):
    V1=-1*Vamp
    end_time=end[i]
    print(".")
    for b in range(0,2400):
        
        circuit_list[a].include(spice_library['MEM_VTEAMN1'])
        ##neurons
        circuit_list[a].X('N1', 'MEM_VTEAMN1', 'Neuron1_In', 'Neuron1_Out', 'state')
        ##Voltage input
        circuit_list[a].V('Vin1','Input1',circuit_list[a].gnd,V1@u_mV)
        circuit_list[a].V('Vin2','Input2',circuit_list[a].gnd,0@u_mV)
        circuit_list[a].V('Bias','Bias',circuit_list[a].gnd,Bias@u_mV)
        ###Input synapses
        circuit_list[a].R('Rinput1','Input1','Neuron1_In',Rin@u_Ω)
        circuit_list[a].R('Rinput2','Input2','Neuron1_In',Rin@u_Ω)
        circuit_list[a].R('Rbias','Bias','Neuron1_In',Rin@u_Ω)
        ##Ground resistors
        circuit_list[a].R('Rground','Neuron1_Out',circuit_list[a].gnd,Rground@u_Ω)
        
        ###simulation
        locals()["simulator" + str(a)] = circuit_list[a].simulator(temperature=25, nominal_temperature=25)
        simulator_list.append(locals()["simulator" + str(a)])
        locals()["analysis" + str(a)]  = simulator_list[a].transient(step_time=step_time, end_time=end_time)
        analysis_list.append(locals()["analysis" + str(a)])
        
        #store the data
        index=V1+1200
        lens=len(analysis_list[a]['Neuron1_Out'])-1
        results[i][0][index]=analysis_list[a]['Neuron1_Out'][lens]
#        results[i][1][index]=V1
        results[i][1][index]=analysis_list[a]['Neuron1_In'][lens]
        V1=V1+1
        
        a=a+1

#%%
#plot the figure for the voltage changes at a single point
a=5590  
figure, ax = plt.subplots(figsize=(20, 10))
ax.plot(analysis_list[a]._time,analysis_list[a]['Neuron1_Out'])
ax.legend(('Vout [V]'), loc=(.8,.8), fontsize=30)
ax.grid()
ax.set_xlabel('t [s]', fontsize=60)
ax.set_ylabel('V[V]', fontsize=60)
plt.tick_params(labelsize=20)
plt.tight_layout()
plt.show()


#%%plot the figure for the voltage changes for different time duration
figure, ax = plt.subplots(figsize=(20, 10))
colors=np.array(['b', 'g', 'r', 'c', 'm', 'y', 'k'])

legends=np.array(['Time=5seconds','Time=10seconds','Time=20seconds',
                  'Time=40seconds','Time=80seconds'])
for i in range (0,5):
#    ax.plot(results[i][1]/1000, results[i][0],color = colors[i], label=legends[i]) #To plot Input1 vs. V2
    ax.plot(results[i][1], results[i][0], color = colors[i], label=legends[i]) # To plot V1 vs. V2.
    ax.legend(loc=(0.1,.6), fontsize=30)
ax.grid()
ax.set_xlabel('V1[V]', fontsize=60)
ax.set_ylabel('V2(output)[V]', fontsize=60)
plt.tick_params(labelsize=20)
plt.tight_layout()
plt.show()

#%%plot the figure for the voltage changes for different time duration
figure, ax = plt.subplots(figsize=(20, 15))
#colors=np.array(['b', 'g', 'r', 'c', 'm', 'y', 'k'])
#end=np.array([5,10,20,40,60,80,100])
#legends=np.array(['Time=5seconds','Time=10seconds','Time=20seconds',
#                  'Time=40seconds','Time=80seconds'])
#for i in range (0,5):
#    ax.plot(results[i][1]/1000, results[i][0],color = colors[i], label=legends[i]) #To plot Input1 vs. V2
ax.plot(results[3][1], results[3][0], color = 'b', label='Time=40seconds',linewidth=7.0) # To plot V1 vs. V2.
ax.legend(loc=(0.1,.8), fontsize=30)
ax.grid()
ax.set_xlabel('Input1[V]', fontsize=60)
ax.set_ylabel('V2(output)[V]', fontsize=60)
plt.tick_params(labelsize=20)
plt.tight_layout()
plt.show()
#%%find the derivative
derivative=np.zeros((5,2,2399))
for i in range(0,5):
    for j in range (0,2399):
        derivative[i][0][j]=(results[i][0][j+1]-results[i][0][j])/(results[i][1][j+1]-results[i][1][j])
        derivative[i][1][j]=results[i][1][j]
#%%
figure, ax = plt.subplots(figsize=(20, 10))

for i in range (0,5):
#    ax.plot(results[i][1]/1000, results[i][0],color = colors[i], label=legends[i]) #To plot Input1 vs. V2
    ax.plot(derivative[i][1], derivative[i][0], color = colors[i], label=legends[i]) # To plot V1 vs. V2.
    ax.legend(loc=(0.1,.6), fontsize=30)
ax.grid()
ax.set_xlabel('V1[V]', fontsize=60)
ax.set_ylabel('dV2(output)/dt[V]', fontsize=60)
plt.tick_params(labelsize=20)
plt.tight_layout()
plt.show()
