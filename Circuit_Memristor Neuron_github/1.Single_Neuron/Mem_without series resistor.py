# -*- coding: utf-8 -*-
"""
Created on Thu Jan 21 23:16:48 2021

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
clear = lambda: os.system('cls')
clear()



libraries_path = "~/ngspice/PySpice/examples/libraries"
spice_library = SpiceLibrary(libraries_path)
circuit = Circuit('Memristor Characteristic Curve')
circuit.include(spice_library['MEM_VTEAMN1'])



circuit.X('M1', 'MEM_VTEAMN1', 'out', circuit.gnd, 'state')
ac_line = circuit.AcLine('input', 'out', circuit.gnd, rms_voltage=0.0707@u_V, frequency=0.0125@u_Hz)

simulator = circuit.simulator(temperature=25, nominal_temperature=25)
analysis = simulator.transient(step_time=ac_line.period/80000, end_time=ac_line.period*3)
##step time has to be equaled to the real timeo of 1 second
print(circuit)

##figure 1 plot voltage
figure, ax = plt.subplots(figsize=(20, 10))
ax.plot(analysis['out'])
#ax.plot(analysis['out_minus'])
ax.legend(('Vin [V]', 'Vout [V]'), loc=(.8,.8), fontsize=30)
ax.grid()
ax.set_xlabel('t [s]', fontsize=60)
ax.set_ylabel('[V]', fontsize=60)
plt.tick_params(labelsize=20)

plt.tight_layout()
plt.show()

##figure2 plot current
figure, ax = plt.subplots(figsize=(20, 10))
ax.plot(-u_uA(analysis.Vinput))
##u_uA(analysis.XXX) XXX has to be a voltage source
ax.legend(('Iinput [uA]'), loc=(.8,.8), fontsize=30)
ax.grid()
ax.set_xlabel('t [ms]', fontsize=60)
ax.set_ylabel('I[uA]', fontsize=60)
plt.tick_params(labelsize=20)

plt.tight_layout()
plt.show()

##figure plot current vs voltage
figure, ax = plt.subplots(figsize=(20, 10))
ax.plot(analysis['out'],-u_uA(analysis.Vinput))
##u_uA(analysis.XXX) XXX has to be a voltage source
ax.legend(('Iinput [uA]'), loc=(.8,.8), fontsize=30)
ax.grid()
ax.set_xlabel('t [ms]', fontsize=60)
ax.set_ylabel('I[uA]', fontsize=60)
plt.tick_params(labelsize=20)

plt.tight_layout()
plt.show()


