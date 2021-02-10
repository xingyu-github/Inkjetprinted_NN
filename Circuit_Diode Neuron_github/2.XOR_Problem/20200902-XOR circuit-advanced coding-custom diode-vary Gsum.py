# -*- coding: utf-8 -*-
"""
Created on Mon Aug 31 21:12:32 2020

@author: duxingyu8
"""
import matplotlib.pyplot as plt
import PySpice.Logging.Logging as Logging
logger = Logging.setup_logging()
from PySpice.Doc.ExampleTools import find_libraries
from PySpice.Probe.Plot import plot
from PySpice.Spice.Library import SpiceLibrary
from PySpice.Spice.Netlist import Circuit, SubCircuit, SubCircuitFactory
from PySpice.Unit import *
import numpy as np
#the purpose of the following code is to clean all
#import os
#clear = lambda: os.system('cls')
#clear()


Input1=np.array([0,0])
Input2=np.array([0,1])
class SubCircuit1(SubCircuitFactory):
    __name__ = 'sub_circuit1'
    __nodes__ = ('In', 'Out')
    def __init__(self):
        super().__init__()
        self.D('1','Mid','Out',model='Diode')
        self.model('Diode','D',IS=0.000000006, n=3.12467)
        self.R('Rs','In','Mid',611.49897@u_Ω)
        self.R('Rsh','In','Out',188085.7139@u_Ω)
      
gamma=1000
lamda=0.001
#Circuit NO.1
circuit1_1 = Circuit('XOR Problem circuit')
circuit1_1.subcircuit(SubCircuit1())
circuit1_1.X('D1','Sub_circuit1','N1In','N1Out')
circuit1_1.X('D2','Sub_circuit1','N2In','N2out')
circuit1_1.V('input1', 'IN1_1', circuit1_1.gnd, 2*Input1[0]@u_V)
circuit1_1.V('input2', 'IN1_2', circuit1_1.gnd, -2*Input1[1]@u_V)
circuit1_1.V('input3', 'IN1_bias', circuit1_1.gnd, 0.9@u_V)
circuit1_1.V('input4', 'IN2_1', circuit1_1.gnd, -2*Input1[0]@u_V)
circuit1_1.V('input5', 'IN2_2', circuit1_1.gnd, 2*Input1[1]@u_V)
circuit1_1.V('input6', 'IN2_bias', circuit1_1.gnd, 0.9@u_V)
circuit1_1.R(1, 'IN1_1', 'N1In', Rin@u_kΩ)
circuit1_1.R(2, 'IN1_2', 'N1In', Rin@u_kΩ)
circuit1_1.R(3, 'IN1_bias', 'N1In', Rin@u_kΩ)
circuit1_1.R(4, 'IN2_1', 'N2In', Rin@u_kΩ)
circuit1_1.R(5, 'IN2_2', 'N2In', Rin@u_kΩ)
circuit1_1.R(6, 'IN2_bias','N2In',Rin@u_kΩ)
circuit1_1.R(7, 'N1Out','Output',Rin*lamda@u_kΩ)
circuit1_1.R(8, 'N2Out','Output',Rin*lamda@u_kΩ)
circuit1_1.R(9, 'N1Out',circuit1_1.gnd,Rin*gamma@u_kΩ)
circuit1_1.R(10, 'N2Out',circuit1_1.gnd,Rin*gamma@u_kΩ)
simulator1_1 = circuit1_1.simulator(temperature=25, nominal_temperature=25)
analysis1_1 = simulator1_1.operating_point()
for node in analysis1_1.nodes.values():#nodes不是node
    if str(node)=='output':
       print ('Node{}: {:4.6f} V'.format(str(node), float(node)))
       Output1_1=float(node)
       break
circuit1_2 = Circuit('XOR Problem circuit')
#diodes
circuit1_2.subcircuit(SubCircuit1())
circuit1_2.X('D1','Sub_circuit1','N1In','N1Out')
circuit1_2.X('D2','Sub_circuit1','N2In','N2out')
#voltage source
circuit1_2.V('input1', 'IN1_1', circuit1_2.gnd, 2*Input2[0]@u_V)
circuit1_2.V('input2', 'IN1_2', circuit1_2.gnd, -2*Input2[1]@u_V)
circuit1_2.V('input3', 'IN1_bias', circuit1_2.gnd, 0.9@u_V)
circuit1_2.V('input4', 'IN2_1', circuit1_2.gnd, -2*Input2[0]@u_V)
circuit1_2.V('input5', 'IN2_2', circuit1_2.gnd, 2*Input2[1]@u_V)
circuit1_2.V('input6', 'IN2_bias', circuit1_2.gnd, 0.9@u_V)
#resistors
#第一个数字是编号，第二三个数字代表位置，第四个数字代表大小
circuit1_2.R(1, 'IN1_1', 'N1In', Rin@u_kΩ)
circuit1_2.R(2, 'IN1_2', 'N1In', Rin@u_kΩ)
circuit1_2.R(3, 'IN1_bias', 'N1In', Rin@u_kΩ)
circuit1_2.R(4, 'IN2_1', 'N2In', Rin@u_kΩ)
circuit1_2.R(5, 'IN2_2', 'N2In', Rin@u_kΩ)
circuit1_2.R(6, 'IN2_bias','N2In',Rin@u_kΩ)
circuit1_2.R(7, 'N1Out','Output',Rin*lamda@u_kΩ)
circuit1_2.R(8, 'N2Out','Output',Rin*lamda@u_kΩ)
circuit1_2.R(9, 'N1Out',circuit1_2.gnd,Rin*gamma@u_kΩ)
circuit1_2.R(10, 'N2Out',circuit1_2.gnd,Rin*gamma@u_kΩ)
simulator1_2 = circuit1_2.simulator(temperature=25, nominal_temperature=25)
analysis1_2 = simulator1_2.operating_point()
for node in analysis1_2.nodes.values():#nodes不是node
    if str(node)=='output':
       print ('Node{}: {:4.6f} V'.format(str(node), float(node)))
       Output1_2=float(node)
       break

#second
lamda=0.01
circuit2_1 = Circuit('XOR Problem circuit')
circuit2_1.subcircuit(SubCircuit1())
circuit2_1.X('D1','Sub_circuit1','N1In','N1Out')
circuit2_1.X('D2','Sub_circuit1','N2In','N2out')
circuit2_1.V('input1', 'IN1_1', circuit2_1.gnd, 2*Input1[0]@u_V)
circuit2_1.V('input2', 'IN1_2', circuit2_1.gnd, -2*Input1[1]@u_V)
circuit2_1.V('input3', 'IN1_bias', circuit2_1.gnd, 0.9@u_V)
circuit2_1.V('input4', 'IN2_1', circuit2_1.gnd, -2*Input1[0]@u_V)
circuit2_1.V('input5', 'IN2_2', circuit2_1.gnd, 2*Input1[1]@u_V)
circuit2_1.V('input6', 'IN2_bias', circuit2_1.gnd, 0.9@u_V)
circuit2_1.R(1, 'IN1_1', 'N1In', Rin@u_kΩ)
circuit2_1.R(2, 'IN1_2', 'N1In', Rin@u_kΩ)
circuit2_1.R(3, 'IN1_bias', 'N1In', Rin@u_kΩ)
circuit2_1.R(4, 'IN2_1', 'N2In', Rin@u_kΩ)
circuit2_1.R(5, 'IN2_2', 'N2In', Rin@u_kΩ)
circuit2_1.R(6, 'IN2_bias','N2In',Rin@u_kΩ)
circuit2_1.R(7, 'N1Out','Output',Rin*lamda@u_kΩ)
circuit2_1.R(8, 'N2Out','Output',Rin*lamda@u_kΩ)
circuit2_1.R(9, 'N1Out',circuit2_1.gnd,Rin*gamma@u_kΩ)
circuit2_1.R(10, 'N2Out',circuit2_1.gnd,Rin*gamma@u_kΩ)
simulator2_1 = circuit2_1.simulator(temperature=25, nominal_temperature=25)
analysis2_1 = simulator2_1.operating_point()
for node in analysis2_1.nodes.values():#nodes不是node
    if str(node)=='output':
       print ('Node{}: {:4.6f} V'.format(str(node), float(node)))
       Output2_1=float(node)
       break
circuit2_2 = Circuit('XOR Problem circuit')
#diodes
circuit2_2.subcircuit(SubCircuit1())
circuit2_2.X('D1','Sub_circuit1','N1In','N1Out')
circuit2_2.X('D2','Sub_circuit1','N2In','N2out')
#voltage source
circuit2_2.V('input1', 'IN1_1', circuit2_2.gnd, 2*Input2[0]@u_V)
circuit2_2.V('input2', 'IN1_2', circuit2_2.gnd, -2*Input2[1]@u_V)
circuit2_2.V('input3', 'IN1_bias', circuit2_2.gnd, 0.9@u_V)
circuit2_2.V('input4', 'IN2_1', circuit2_2.gnd, -2*Input2[0]@u_V)
circuit2_2.V('input5', 'IN2_2', circuit2_2.gnd, 2*Input2[1]@u_V)
circuit2_2.V('input6', 'IN2_bias', circuit2_2.gnd, 0.9@u_V)
#resistors
#第一个数字是编号，第二三个数字代表位置，第四个数字代表大小
circuit2_2.R(1, 'IN1_1', 'N1In', Rin@u_kΩ)
circuit2_2.R(2, 'IN1_2', 'N1In', Rin@u_kΩ)
circuit2_2.R(3, 'IN1_bias', 'N1In', Rin@u_kΩ)
circuit2_2.R(4, 'IN2_1', 'N2In', Rin@u_kΩ)
circuit2_2.R(5, 'IN2_2', 'N2In', Rin@u_kΩ)
circuit2_2.R(6, 'IN2_bias','N2In',Rin@u_kΩ)
circuit2_2.R(7, 'N1Out','Output',Rin*lamda@u_kΩ)
circuit2_2.R(8, 'N2Out','Output',Rin*lamda@u_kΩ)
circuit2_2.R(9, 'N1Out',circuit2_2.gnd,Rin*gamma@u_kΩ)
circuit2_2.R(10, 'N2Out',circuit2_2.gnd,Rin*gamma@u_kΩ)
simulator2_2 = circuit2_2.simulator(temperature=25, nominal_temperature=25)
analysis2_2 = simulator2_2.operating_point()
for node in analysis2_2.nodes.values():#nodes不是node
    if str(node)=='output':
       print ('Node{}: {:4.6f} V'.format(str(node), float(node)))
       Output2_2=float(node)
       break
   
#Circuit NO.3
lamda=0.1
circuit3_1 = Circuit('XOR Problem circuit')
circuit3_1.subcircuit(SubCircuit1())
circuit3_1.X('D1','Sub_circuit1','N1In','N1Out')
circuit3_1.X('D2','Sub_circuit1','N2In','N2out')
circuit3_1.V('input1', 'IN1_1', circuit3_1.gnd, 2*Input1[0]@u_V)
circuit3_1.V('input2', 'IN1_2', circuit3_1.gnd, -2*Input1[1]@u_V)
circuit3_1.V('input3', 'IN1_bias', circuit3_1.gnd, 0.9@u_V)
circuit3_1.V('input4', 'IN2_1', circuit3_1.gnd, -2*Input1[0]@u_V)
circuit3_1.V('input5', 'IN2_2', circuit3_1.gnd, 2*Input1[1]@u_V)
circuit3_1.V('input6', 'IN2_bias', circuit3_1.gnd, 0.9@u_V)
circuit3_1.R(1, 'IN1_1', 'N1In', Rin@u_kΩ)
circuit3_1.R(2, 'IN1_2', 'N1In', Rin@u_kΩ)
circuit3_1.R(3, 'IN1_bias', 'N1In', Rin@u_kΩ)
circuit3_1.R(4, 'IN2_1', 'N2In', Rin@u_kΩ)
circuit3_1.R(5, 'IN2_2', 'N2In', Rin@u_kΩ)
circuit3_1.R(6, 'IN2_bias','N2In',Rin@u_kΩ)
circuit3_1.R(7, 'N1Out','Output',Rin*lamda@u_kΩ)
circuit3_1.R(8, 'N2Out','Output',Rin*lamda@u_kΩ)
circuit3_1.R(9, 'N1Out',circuit3_1.gnd,Rin*gamma@u_kΩ)
circuit3_1.R(10, 'N2Out',circuit3_1.gnd,Rin*gamma@u_kΩ)
simulator3_1 = circuit3_1.simulator(temperature=25, nominal_temperature=25)
analysis3_1 = simulator3_1.operating_point()
for node in analysis3_1.nodes.values():#nodes不是node
    if str(node)=='output':
       print ('Node{}: {:4.6f} V'.format(str(node), float(node)))
       Output3_1=float(node)
       break
circuit3_2 = Circuit('XOR Problem circuit')
#diodes
circuit3_2.subcircuit(SubCircuit1())
circuit3_2.X('D1','Sub_circuit1','N1In','N1Out')
circuit3_2.X('D2','Sub_circuit1','N2In','N2out')
#voltage source
circuit3_2.V('input1', 'IN1_1', circuit3_2.gnd, 2*Input2[0]@u_V)
circuit3_2.V('input2', 'IN1_2', circuit3_2.gnd, -2*Input2[1]@u_V)
circuit3_2.V('input3', 'IN1_bias', circuit3_2.gnd, 0.9@u_V)
circuit3_2.V('input4', 'IN2_1', circuit3_2.gnd, -2*Input2[0]@u_V)
circuit3_2.V('input5', 'IN2_2', circuit3_2.gnd, 2*Input2[1]@u_V)
circuit3_2.V('input6', 'IN2_bias', circuit3_2.gnd, 0.9@u_V)
#resistors
#第一个数字是编号，第二三个数字代表位置，第四个数字代表大小
circuit3_2.R(1, 'IN1_1', 'N1In', Rin@u_kΩ)
circuit3_2.R(2, 'IN1_2', 'N1In', Rin@u_kΩ)
circuit3_2.R(3, 'IN1_bias', 'N1In', Rin@u_kΩ)
circuit3_2.R(4, 'IN2_1', 'N2In', Rin@u_kΩ)
circuit3_2.R(5, 'IN2_2', 'N2In', Rin@u_kΩ)
circuit3_2.R(6, 'IN2_bias','N2In',Rin@u_kΩ)
circuit3_2.R(7, 'N1Out','Output',Rin*lamda@u_kΩ)
circuit3_2.R(8, 'N2Out','Output',Rin*lamda@u_kΩ)
circuit3_2.R(9, 'N1Out',circuit3_2.gnd,Rin*gamma@u_kΩ)
circuit3_2.R(10, 'N2Out',circuit3_2.gnd,Rin*gamma@u_kΩ)
simulator3_2 = circuit3_2.simulator(temperature=25, nominal_temperature=25)
analysis3_2 = simulator3_2.operating_point()
for node in analysis3_2.nodes.values():#nodes不是node
    if str(node)=='output':
       print ('Node{}: {:4.6f} V'.format(str(node), float(node)))
       Output3_2=float(node)
       break
   
    
#Circuit NO.4
lamda= 1      
circuit4_1 = Circuit('XOR Problem circuit')
circuit4_1.subcircuit(SubCircuit1())
circuit4_1.X('D1','Sub_circuit1','N1In','N1Out')
circuit4_1.X('D2','Sub_circuit1','N2In','N2out')
circuit4_1.V('input1', 'IN1_1', circuit4_1.gnd, 2*Input1[0]@u_V)
circuit4_1.V('input2', 'IN1_2', circuit4_1.gnd, -2*Input1[1]@u_V)
circuit4_1.V('input3', 'IN1_bias', circuit4_1.gnd, 0.9@u_V)
circuit4_1.V('input4', 'IN2_1', circuit4_1.gnd, -2*Input1[0]@u_V)
circuit4_1.V('input5', 'IN2_2', circuit4_1.gnd, 2*Input1[1]@u_V)
circuit4_1.V('input6', 'IN2_bias', circuit4_1.gnd, 0.9@u_V)
circuit4_1.R(1, 'IN1_1', 'N1In', Rin@u_kΩ)
circuit4_1.R(2, 'IN1_2', 'N1In', Rin@u_kΩ)
circuit4_1.R(3, 'IN1_bias', 'N1In', Rin@u_kΩ)
circuit4_1.R(4, 'IN2_1', 'N2In', Rin@u_kΩ)
circuit4_1.R(5, 'IN2_2', 'N2In', Rin@u_kΩ)
circuit4_1.R(6, 'IN2_bias','N2In',Rin@u_kΩ)
circuit4_1.R(7, 'N1Out','Output',Rin*lamda@u_kΩ)
circuit4_1.R(8, 'N2Out','Output',Rin*lamda@u_kΩ)
circuit4_1.R(9, 'N1Out',circuit4_1.gnd,Rin*gamma@u_kΩ)
circuit4_1.R(10, 'N2Out',circuit4_1.gnd,Rin*gamma@u_kΩ)
simulator4_1 = circuit4_1.simulator(temperature=25, nominal_temperature=25)
analysis4_1 = simulator4_1.operating_point()
for node in analysis4_1.nodes.values():#nodes不是node
    if str(node)=='output':
       print ('Node{}: {:4.6f} V'.format(str(node), float(node)))
       Output4_1=float(node)
       break
circuit4_2 = Circuit('XOR Problem circuit')
#diodes
circuit4_2.subcircuit(SubCircuit1())
circuit4_2.X('D1','Sub_circuit1','N1In','N1Out')
circuit4_2.X('D2','Sub_circuit1','N2In','N2out')
#voltage source
circuit4_2.V('input1', 'IN1_1', circuit4_2.gnd, 2*Input2[0]@u_V)
circuit4_2.V('input2', 'IN1_2', circuit4_2.gnd, -2*Input2[1]@u_V)
circuit4_2.V('input3', 'IN1_bias', circuit4_2.gnd, 0.9@u_V)
circuit4_2.V('input4', 'IN2_1', circuit4_2.gnd, -2*Input2[0]@u_V)
circuit4_2.V('input5', 'IN2_2', circuit4_2.gnd, 2*Input2[1]@u_V)
circuit4_2.V('input6', 'IN2_bias', circuit4_2.gnd, 0.9@u_V)
#resistors
#第一个数字是编号，第二三个数字代表位置，第四个数字代表大小
circuit4_2.R(1, 'IN1_1', 'N1In', Rin@u_kΩ)
circuit4_2.R(2, 'IN1_2', 'N1In', Rin@u_kΩ)
circuit4_2.R(3, 'IN1_bias', 'N1In', Rin@u_kΩ)
circuit4_2.R(4, 'IN2_1', 'N2In', Rin@u_kΩ)
circuit4_2.R(5, 'IN2_2', 'N2In', Rin@u_kΩ)
circuit4_2.R(6, 'IN2_bias','N2In',Rin@u_kΩ)
circuit4_2.R(7, 'N1Out','Output',Rin*lamda@u_kΩ)
circuit4_2.R(8, 'N2Out','Output',Rin*lamda@u_kΩ)
circuit4_2.R(9, 'N1Out',circuit4_2.gnd,Rin*gamma@u_kΩ)
circuit4_2.R(10, 'N2Out',circuit4_2.gnd,Rin*gamma@u_kΩ)
simulator4_2 = circuit4_2.simulator(temperature=25, nominal_temperature=25)
analysis4_2 = simulator4_2.operating_point()
for node in analysis4_2.nodes.values():#nodes不是node
    if str(node)=='output':
       print ('Node{}: {:4.6f} V'.format(str(node), float(node)))
       Output4_2=float(node)
       break
   
#Circuit NO.5
lamda= 10      
circuit5_1 = Circuit('XOR Problem circuit')
circuit5_1.subcircuit(SubCircuit1())
circuit5_1.X('D1','Sub_circuit1','N1In','N1Out')
circuit5_1.X('D2','Sub_circuit1','N2In','N2out')
circuit5_1.V('input1', 'IN1_1', circuit5_1.gnd, 2*Input1[0]@u_V)
circuit5_1.V('input2', 'IN1_2', circuit5_1.gnd, -2*Input1[1]@u_V)
circuit5_1.V('input3', 'IN1_bias', circuit5_1.gnd, 0.9@u_V)
circuit5_1.V('input4', 'IN2_1', circuit5_1.gnd, -2*Input1[0]@u_V)
circuit5_1.V('input5', 'IN2_2', circuit5_1.gnd, 2*Input1[1]@u_V)
circuit5_1.V('input6', 'IN2_bias', circuit5_1.gnd, 0.9@u_V)
circuit5_1.R(1, 'IN1_1', 'N1In', Rin@u_kΩ)
circuit5_1.R(2, 'IN1_2', 'N1In', Rin@u_kΩ)
circuit5_1.R(3, 'IN1_bias', 'N1In', Rin@u_kΩ)
circuit5_1.R(4, 'IN2_1', 'N2In', Rin@u_kΩ)
circuit5_1.R(5, 'IN2_2', 'N2In', Rin@u_kΩ)
circuit5_1.R(6, 'IN2_bias','N2In',Rin@u_kΩ)
circuit5_1.R(7, 'N1Out','Output',Rin*lamda@u_kΩ)
circuit5_1.R(8, 'N2Out','Output',Rin*lamda@u_kΩ)
circuit5_1.R(9, 'N1Out',circuit5_1.gnd,Rin*gamma@u_kΩ)
circuit5_1.R(10, 'N2Out',circuit5_1.gnd,Rin*gamma@u_kΩ)
simulator5_1 = circuit5_1.simulator(temperature=25, nominal_temperature=25)
analysis5_1 = simulator5_1.operating_point()
for node in analysis5_1.nodes.values():#nodes不是node
    if str(node)=='output':
       print ('Node{}: {:4.6f} V'.format(str(node), float(node)))
       Output5_1=float(node)
       break
circuit5_2 = Circuit('XOR Problem circuit')
#diodes
circuit5_2.subcircuit(SubCircuit1())
circuit5_2.X('D1','Sub_circuit1','N1In','N1Out')
circuit5_2.X('D2','Sub_circuit1','N2In','N2out')
#voltage source
circuit5_2.V('input1', 'IN1_1', circuit5_2.gnd, 2*Input2[0]@u_V)
circuit5_2.V('input2', 'IN1_2', circuit5_2.gnd, -2*Input2[1]@u_V)
circuit5_2.V('input3', 'IN1_bias', circuit5_2.gnd, 0.9@u_V)
circuit5_2.V('input4', 'IN2_1', circuit5_2.gnd, -2*Input2[0]@u_V)
circuit5_2.V('input5', 'IN2_2', circuit5_2.gnd, 2*Input2[1]@u_V)
circuit5_2.V('input6', 'IN2_bias', circuit5_2.gnd, 0.9@u_V)
#resistors
#第一个数字是编号，第二三个数字代表位置，第四个数字代表大小
circuit5_2.R(1, 'IN1_1', 'N1In', Rin@u_kΩ)
circuit5_2.R(2, 'IN1_2', 'N1In', Rin@u_kΩ)
circuit5_2.R(3, 'IN1_bias', 'N1In', Rin@u_kΩ)
circuit5_2.R(4, 'IN2_1', 'N2In', Rin@u_kΩ)
circuit5_2.R(5, 'IN2_2', 'N2In', Rin@u_kΩ)
circuit5_2.R(6, 'IN2_bias','N2In',Rin@u_kΩ)
circuit5_2.R(7, 'N1Out','Output',Rin*lamda@u_kΩ)
circuit5_2.R(8, 'N2Out','Output',Rin*lamda@u_kΩ)
circuit5_2.R(9, 'N1Out',circuit5_2.gnd,Rin*gamma@u_kΩ)
circuit5_2.R(10, 'N2Out',circuit5_2.gnd,Rin*gamma@u_kΩ)
simulator5_2 = circuit5_2.simulator(temperature=25, nominal_temperature=25)
analysis5_2 = simulator5_2.operating_point()
for node in analysis5_2.nodes.values():#nodes不是node
    if str(node)=='output':
       print ('Node{}: {:4.6f} V'.format(str(node), float(node)))
       Output5_2=float(node)
       break
    
#Circuit NO.6
lamda= 100       
circuit6_1 = Circuit('XOR Problem circuit')
circuit6_1.subcircuit(SubCircuit1())
circuit6_1.X('D1','Sub_circuit1','N1In','N1Out')
circuit6_1.X('D2','Sub_circuit1','N2In','N2out')
circuit6_1.V('input1', 'IN1_1', circuit6_1.gnd, 2*Input1[0]@u_V)
circuit6_1.V('input2', 'IN1_2', circuit6_1.gnd, -2*Input1[1]@u_V)
circuit6_1.V('input3', 'IN1_bias', circuit6_1.gnd, 0.9@u_V)
circuit6_1.V('input4', 'IN2_1', circuit6_1.gnd, -2*Input1[0]@u_V)
circuit6_1.V('input5', 'IN2_2', circuit6_1.gnd, 2*Input1[1]@u_V)
circuit6_1.V('input6', 'IN2_bias', circuit6_1.gnd, 0.9@u_V)
circuit6_1.R(1, 'IN1_1', 'N1In', Rin@u_kΩ)
circuit6_1.R(2, 'IN1_2', 'N1In', Rin@u_kΩ)
circuit6_1.R(3, 'IN1_bias', 'N1In', Rin@u_kΩ)
circuit6_1.R(4, 'IN2_1', 'N2In', Rin@u_kΩ)
circuit6_1.R(5, 'IN2_2', 'N2In', Rin@u_kΩ)
circuit6_1.R(6, 'IN2_bias','N2In',Rin@u_kΩ)
circuit6_1.R(7, 'N1Out','Output',Rin*lamda@u_kΩ)
circuit6_1.R(8, 'N2Out','Output',Rin*lamda@u_kΩ)
circuit6_1.R(9, 'N1Out',circuit6_1.gnd,Rin*gamma@u_kΩ)
circuit6_1.R(10, 'N2Out',circuit6_1.gnd,Rin*gamma@u_kΩ)
simulator6_1 = circuit6_1.simulator(temperature=25, nominal_temperature=25)
analysis6_1 = simulator6_1.operating_point()
for node in analysis6_1.nodes.values():#nodes不是node
    if str(node)=='output':
       print ('Node{}: {:4.6f} V'.format(str(node), float(node)))
       Output6_1=float(node)
       break
circuit6_2 = Circuit('XOR Problem circuit')
#diodes
circuit6_2.subcircuit(SubCircuit1())
circuit6_2.X('D1','Sub_circuit1','N1In','N1Out')
circuit6_2.X('D2','Sub_circuit1','N2In','N2out')
#voltage source
circuit6_2.V('input1', 'IN1_1', circuit6_2.gnd, 2*Input2[0]@u_V)
circuit6_2.V('input2', 'IN1_2', circuit6_2.gnd, -2*Input2[1]@u_V)
circuit6_2.V('input3', 'IN1_bias', circuit6_2.gnd, 0.9@u_V)
circuit6_2.V('input4', 'IN2_1', circuit6_2.gnd, -2*Input2[0]@u_V)
circuit6_2.V('input5', 'IN2_2', circuit6_2.gnd, 2*Input2[1]@u_V)
circuit6_2.V('input6', 'IN2_bias', circuit6_2.gnd, 0.9@u_V)
#resistors
#第一个数字是编号，第二三个数字代表位置，第四个数字代表大小
circuit6_2.R(1, 'IN1_1', 'N1In', Rin@u_kΩ)
circuit6_2.R(2, 'IN1_2', 'N1In', Rin@u_kΩ)
circuit6_2.R(3, 'IN1_bias', 'N1In', Rin@u_kΩ)
circuit6_2.R(4, 'IN2_1', 'N2In', Rin@u_kΩ)
circuit6_2.R(5, 'IN2_2', 'N2In', Rin@u_kΩ)
circuit6_2.R(6, 'IN2_bias','N2In',Rin@u_kΩ)
circuit6_2.R(7, 'N1Out','Output',Rin*lamda@u_kΩ)
circuit6_2.R(8, 'N2Out','Output',Rin*lamda@u_kΩ)
circuit6_2.R(9, 'N1Out',circuit6_2.gnd,Rin*gamma@u_kΩ)
circuit6_2.R(10, 'N2Out',circuit6_2.gnd,Rin*gamma@u_kΩ)
simulator6_2 = circuit6_2.simulator(temperature=25, nominal_temperature=25)
analysis6_2 = simulator6_2.operating_point()
for node in analysis6_2.nodes.values():#nodes不是node
    if str(node)=='output':
       print ('Node{}: {:4.6f} V'.format(str(node), float(node)))
       Output6_2=float(node)
       break    
    
#Circuit NO.7
lamda= 1000
circuit7_1 = Circuit('XOR Problem circuit')
circuit7_1.subcircuit(SubCircuit1())
circuit7_1.X('D1','Sub_circuit1','N1In','N1Out')
circuit7_1.X('D2','Sub_circuit1','N2In','N2out')
circuit7_1.V('input1', 'IN1_1', circuit7_1.gnd, 2*Input1[0]@u_V)
circuit7_1.V('input2', 'IN1_2', circuit7_1.gnd, -2*Input1[1]@u_V)
circuit7_1.V('input3', 'IN1_bias', circuit7_1.gnd, 0.9@u_V)
circuit7_1.V('input4', 'IN2_1', circuit7_1.gnd, -2*Input1[0]@u_V)
circuit7_1.V('input5', 'IN2_2', circuit7_1.gnd, 2*Input1[1]@u_V)
circuit7_1.V('input6', 'IN2_bias', circuit7_1.gnd, 0.9@u_V)
circuit7_1.R(1, 'IN1_1', 'N1In', Rin@u_kΩ)
circuit7_1.R(2, 'IN1_2', 'N1In', Rin@u_kΩ)
circuit7_1.R(3, 'IN1_bias', 'N1In', Rin@u_kΩ)
circuit7_1.R(4, 'IN2_1', 'N2In', Rin@u_kΩ)
circuit7_1.R(5, 'IN2_2', 'N2In', Rin@u_kΩ)
circuit7_1.R(6, 'IN2_bias','N2In',Rin@u_kΩ)
circuit7_1.R(7, 'N1Out','Output',Rin*lamda@u_kΩ)
circuit7_1.R(8, 'N2Out','Output',Rin*lamda@u_kΩ)
circuit7_1.R(9, 'N1Out',circuit7_1.gnd,Rin*gamma@u_kΩ)
circuit7_1.R(10, 'N2Out',circuit7_1.gnd,Rin*gamma@u_kΩ)
simulator7_1 = circuit7_1.simulator(temperature=25, nominal_temperature=25)
analysis7_1 = simulator7_1.operating_point()
for node in analysis7_1.nodes.values():#nodes不是node
    if str(node)=='output':
       print ('Node{}: {:4.6f} V'.format(str(node), float(node)))
       Output7_1=float(node)
       break
circuit7_2 = Circuit('XOR Problem circuit')
#diodes
circuit7_2.subcircuit(SubCircuit1())
circuit7_2.X('D1','Sub_circuit1','N1In','N1Out')
circuit7_2.X('D2','Sub_circuit1','N2In','N2out')
#voltage source
circuit7_2.V('input1', 'IN1_1', circuit7_2.gnd, 2*Input2[0]@u_V)
circuit7_2.V('input2', 'IN1_2', circuit7_2.gnd, -2*Input2[1]@u_V)
circuit7_2.V('input3', 'IN1_bias', circuit7_2.gnd, 0.9@u_V)
circuit7_2.V('input4', 'IN2_1', circuit7_2.gnd, -2*Input2[0]@u_V)
circuit7_2.V('input5', 'IN2_2', circuit7_2.gnd, 2*Input2[1]@u_V)
circuit7_2.V('input6', 'IN2_bias', circuit7_2.gnd, 0.9@u_V)
#resistors
#第一个数字是编号，第二三个数字代表位置，第四个数字代表大小
circuit7_2.R(1, 'IN1_1', 'N1In', Rin@u_kΩ)
circuit7_2.R(2, 'IN1_2', 'N1In', Rin@u_kΩ)
circuit7_2.R(3, 'IN1_bias', 'N1In', Rin@u_kΩ)
circuit7_2.R(4, 'IN2_1', 'N2In', Rin@u_kΩ)
circuit7_2.R(5, 'IN2_2', 'N2In', Rin@u_kΩ)
circuit7_2.R(6, 'IN2_bias','N2In',Rin@u_kΩ)
circuit7_2.R(7, 'N1Out','Output',Rin*lamda@u_kΩ)
circuit7_2.R(8, 'N2Out','Output',Rin*lamda@u_kΩ)
circuit7_2.R(9, 'N1Out',circuit7_2.gnd,Rin*gamma@u_kΩ)
circuit7_2.R(10, 'N2Out',circuit7_2.gnd,Rin*gamma@u_kΩ)
simulator7_2 = circuit7_2.simulator(temperature=25, nominal_temperature=25)
analysis7_2 = simulator7_2.operating_point()
for node in analysis7_2.nodes.values():#nodes不是node
    if str(node)=='output':
       print ('Node{}: {:4.6f} V'.format(str(node), float(node)))
       Output7_2=float(node)
       break    


#Circuit NO.8
lamda= 10000       
circuit8_1 = Circuit('XOR Problem circuit')
circuit8_1.subcircuit(SubCircuit1())
circuit8_1.X('D1','Sub_circuit1','N1In','N1Out')
circuit8_1.X('D2','Sub_circuit1','N2In','N2out')
circuit8_1.V('input1', 'IN1_1', circuit8_1.gnd, 2*Input1[0]@u_V)
circuit8_1.V('input2', 'IN1_2', circuit8_1.gnd, -2*Input1[1]@u_V)
circuit8_1.V('input3', 'IN1_bias', circuit8_1.gnd, 0.9@u_V)
circuit8_1.V('input4', 'IN2_1', circuit8_1.gnd, -2*Input1[0]@u_V)
circuit8_1.V('input5', 'IN2_2', circuit8_1.gnd, 2*Input1[1]@u_V)
circuit8_1.V('input6', 'IN2_bias', circuit8_1.gnd, 0.9@u_V)
circuit8_1.R(1, 'IN1_1', 'N1In', Rin@u_kΩ)
circuit8_1.R(2, 'IN1_2', 'N1In', Rin@u_kΩ)
circuit8_1.R(3, 'IN1_bias', 'N1In', Rin@u_kΩ)
circuit8_1.R(4, 'IN2_1', 'N2In', Rin@u_kΩ)
circuit8_1.R(5, 'IN2_2', 'N2In', Rin@u_kΩ)
circuit8_1.R(6, 'IN2_bias','N2In',Rin@u_kΩ)
circuit8_1.R(7, 'N1Out','Output',Rin*lamda@u_kΩ)
circuit8_1.R(8, 'N2Out','Output',Rin*lamda@u_kΩ)
circuit8_1.R(9, 'N1Out',circuit8_1.gnd,Rin*gamma@u_kΩ)
circuit8_1.R(10, 'N2Out',circuit8_1.gnd,Rin*gamma@u_kΩ)
simulator8_1 = circuit8_1.simulator(temperature=25, nominal_temperature=25)
analysis8_1 = simulator8_1.operating_point()
for node in analysis8_1.nodes.values():#nodes不是node
    if str(node)=='output':
       print ('Node{}: {:4.6f} V'.format(str(node), float(node)))
       Output8_1=float(node)
       break
circuit8_2 = Circuit('XOR Problem circuit')
#diodes
circuit8_2.subcircuit(SubCircuit1())
circuit8_2.X('D1','Sub_circuit1','N1In','N1Out')
circuit8_2.X('D2','Sub_circuit1','N2In','N2out')
#voltage source
circuit8_2.V('input1', 'IN1_1', circuit8_2.gnd, 2*Input2[0]@u_V)
circuit8_2.V('input2', 'IN1_2', circuit8_2.gnd, -2*Input2[1]@u_V)
circuit8_2.V('input3', 'IN1_bias', circuit8_2.gnd, 0.9@u_V)
circuit8_2.V('input4', 'IN2_1', circuit8_2.gnd, -2*Input2[0]@u_V)
circuit8_2.V('input5', 'IN2_2', circuit8_2.gnd, 2*Input2[1]@u_V)
circuit8_2.V('input6', 'IN2_bias', circuit8_2.gnd, 0.9@u_V)
#resistors
#第一个数字是编号，第二三个数字代表位置，第四个数字代表大小
circuit8_2.R(1, 'IN1_1', 'N1In', Rin@u_kΩ)
circuit8_2.R(2, 'IN1_2', 'N1In', Rin@u_kΩ)
circuit8_2.R(3, 'IN1_bias', 'N1In', Rin@u_kΩ)
circuit8_2.R(4, 'IN2_1', 'N2In', Rin@u_kΩ)
circuit8_2.R(5, 'IN2_2', 'N2In', Rin@u_kΩ)
circuit8_2.R(6, 'IN2_bias','N2In',Rin@u_kΩ)
circuit8_2.R(7, 'N1Out','Output',Rin*lamda@u_kΩ)
circuit8_2.R(8, 'N2Out','Output',Rin*lamda@u_kΩ)
circuit8_2.R(9, 'N1Out',circuit8_2.gnd,Rin*gamma@u_kΩ)
circuit8_2.R(10, 'N2Out',circuit8_2.gnd,Rin*gamma@u_kΩ)
simulator8_2 = circuit8_2.simulator(temperature=25, nominal_temperature=25)
analysis8_2 = simulator8_2.operating_point()
for node in analysis8_2.nodes.values():#nodes不是node
    if str(node)=='output':
       print ('Node{}: {:4.6f} V'.format(str(node), float(node)))
       Output8_2=float(node)
       break

#Circuit NO.9
lamda=100000      
circuit9_1 = Circuit('XOR Problem circuit')
circuit9_1.subcircuit(SubCircuit1())
circuit9_1.X('D1','Sub_circuit1','N1In','N1Out')
circuit9_1.X('D2','Sub_circuit1','N2In','N2out')
circuit9_1.V('input1', 'IN1_1', circuit9_1.gnd, 2*Input1[0]@u_V)
circuit9_1.V('input2', 'IN1_2', circuit9_1.gnd, -2*Input1[1]@u_V)
circuit9_1.V('input3', 'IN1_bias', circuit9_1.gnd, 0.9@u_V)
circuit9_1.V('input4', 'IN2_1', circuit9_1.gnd, -2*Input1[0]@u_V)
circuit9_1.V('input5', 'IN2_2', circuit9_1.gnd, 2*Input1[1]@u_V)
circuit9_1.V('input6', 'IN2_bias', circuit9_1.gnd, 0.9@u_V)
circuit9_1.R(1, 'IN1_1', 'N1In', Rin@u_kΩ)
circuit9_1.R(2, 'IN1_2', 'N1In', Rin@u_kΩ)
circuit9_1.R(3, 'IN1_bias', 'N1In', Rin@u_kΩ)
circuit9_1.R(4, 'IN2_1', 'N2In', Rin@u_kΩ)
circuit9_1.R(5, 'IN2_2', 'N2In', Rin@u_kΩ)
circuit9_1.R(6, 'IN2_bias','N2In',Rin@u_kΩ)
circuit9_1.R(7, 'N1Out','Output',Rin*lamda@u_kΩ)
circuit9_1.R(8, 'N2Out','Output',Rin*lamda@u_kΩ)
circuit9_1.R(9, 'N1Out',circuit9_1.gnd,Rin*gamma@u_kΩ)
circuit9_1.R(10, 'N2Out',circuit9_1.gnd,Rin*gamma@u_kΩ)
simulator9_1 = circuit9_1.simulator(temperature=25, nominal_temperature=25)
analysis9_1 = simulator9_1.operating_point()
for node in analysis9_1.nodes.values():#nodes不是node
    if str(node)=='output':
       print ('Node{}: {:4.6f} V'.format(str(node), float(node)))
       Output9_1=float(node)
       break
circuit9_2 = Circuit('XOR Problem circuit')
#diodes
circuit9_2.subcircuit(SubCircuit1())
circuit9_2.X('D1','Sub_circuit1','N1In','N1Out')
circuit9_2.X('D2','Sub_circuit1','N2In','N2out')
#voltage source
circuit9_2.V('input1', 'IN1_1', circuit9_2.gnd, 2*Input2[0]@u_V)
circuit9_2.V('input2', 'IN1_2', circuit9_2.gnd, -2*Input2[1]@u_V)
circuit9_2.V('input3', 'IN1_bias', circuit9_2.gnd, 0.9@u_V)
circuit9_2.V('input4', 'IN2_1', circuit9_2.gnd, -2*Input2[0]@u_V)
circuit9_2.V('input5', 'IN2_2', circuit9_2.gnd, 2*Input2[1]@u_V)
circuit9_2.V('input6', 'IN2_bias', circuit9_2.gnd, 0.9@u_V)
#resistors
#第一个数字是编号，第二三个数字代表位置，第四个数字代表大小
circuit9_2.R(1, 'IN1_1', 'N1In', Rin@u_kΩ)
circuit9_2.R(2, 'IN1_2', 'N1In', Rin@u_kΩ)
circuit9_2.R(3, 'IN1_bias', 'N1In', Rin@u_kΩ)
circuit9_2.R(4, 'IN2_1', 'N2In', Rin@u_kΩ)
circuit9_2.R(5, 'IN2_2', 'N2In', Rin@u_kΩ)
circuit9_2.R(6, 'IN2_bias','N2In',Rin@u_kΩ)
circuit9_2.R(7, 'N1Out','Output',Rin*lamda@u_kΩ)
circuit9_2.R(8, 'N2Out','Output',Rin*lamda@u_kΩ)
circuit9_2.R(9, 'N1Out',circuit9_2.gnd,Rin*gamma@u_kΩ)
circuit9_2.R(10, 'N2Out',circuit9_2.gnd,Rin*gamma@u_kΩ)
simulator9_2 = circuit9_2.simulator(temperature=25, nominal_temperature=25)
analysis9_2 = simulator9_2.operating_point()
for node in analysis9_2.nodes.values():#nodes不是node
    if str(node)=='output':
       print ('Node{}: {:4.6f} V'.format(str(node), float(node)))
       Output9_2=float(node)
       break


#Circuit NO.10
lamda=1000000
circuit10_1 = Circuit('XOR Problem circuit')
circuit10_1.subcircuit(SubCircuit1())
circuit10_1.X('D1','Sub_circuit1','N1In','N1Out')
circuit10_1.X('D2','Sub_circuit1','N2In','N2out')
circuit10_1.V('input1', 'IN1_1', circuit10_1.gnd, 2*Input1[0]@u_V)
circuit10_1.V('input2', 'IN1_2', circuit10_1.gnd, -2*Input1[1]@u_V)
circuit10_1.V('input3', 'IN1_bias', circuit10_1.gnd, 0.9@u_V)
circuit10_1.V('input4', 'IN2_1', circuit10_1.gnd, -2*Input1[0]@u_V)
circuit10_1.V('input5', 'IN2_2', circuit10_1.gnd, 2*Input1[1]@u_V)
circuit10_1.V('input6', 'IN2_bias', circuit10_1.gnd, 0.9@u_V)
circuit10_1.R(1, 'IN1_1', 'N1In', Rin@u_kΩ)
circuit10_1.R(2, 'IN1_2', 'N1In', Rin@u_kΩ)
circuit10_1.R(3, 'IN1_bias', 'N1In', Rin@u_kΩ)
circuit10_1.R(4, 'IN2_1', 'N2In', Rin@u_kΩ)
circuit10_1.R(5, 'IN2_2', 'N2In', Rin@u_kΩ)
circuit10_1.R(6, 'IN2_bias','N2In',Rin@u_kΩ)
circuit10_1.R(7, 'N1Out','Output',Rin*lamda@u_kΩ)
circuit10_1.R(8, 'N2Out','Output',Rin*lamda@u_kΩ)
circuit10_1.R(9, 'N1Out',circuit10_1.gnd,Rin*gamma@u_kΩ)
circuit10_1.R(10, 'N2Out',circuit10_1.gnd,Rin*gamma@u_kΩ)
simulator10_1 = circuit10_1.simulator(temperature=25, nominal_temperature=25)
analysis10_1 = simulator10_1.operating_point()
for node in analysis10_1.nodes.values():#nodes不是node
    if str(node)=='output':
       print ('Node{}: {:4.6f} V'.format(str(node), float(node)))
       Output10_1=float(node)
       break
circuit10_2 = Circuit('XOR Problem circuit')
#diodes
circuit10_2.subcircuit(SubCircuit1())
circuit10_2.X('D1','Sub_circuit1','N1In','N1Out')
circuit10_2.X('D2','Sub_circuit1','N2In','N2out')
#voltage source
circuit10_2.V('input1', 'IN1_1', circuit10_2.gnd, 2*Input2[0]@u_V)
circuit10_2.V('input2', 'IN1_2', circuit10_2.gnd, -2*Input2[1]@u_V)
circuit10_2.V('input3', 'IN1_bias', circuit10_2.gnd, 0.9@u_V)
circuit10_2.V('input4', 'IN2_1', circuit10_2.gnd, -2*Input2[0]@u_V)
circuit10_2.V('input5', 'IN2_2', circuit10_2.gnd, 2*Input2[1]@u_V)
circuit10_2.V('input6', 'IN2_bias', circuit10_2.gnd, 0.9@u_V)
#resistors
#第一个数字是编号，第二三个数字代表位置，第四个数字代表大小
circuit10_2.R(1, 'IN1_1', 'N1In', Rin@u_kΩ)
circuit10_2.R(2, 'IN1_2', 'N1In', Rin@u_kΩ)
circuit10_2.R(3, 'IN1_bias', 'N1In', Rin@u_kΩ)
circuit10_2.R(4, 'IN2_1', 'N2In', Rin@u_kΩ)
circuit10_2.R(5, 'IN2_2', 'N2In', Rin@u_kΩ)
circuit10_2.R(6, 'IN2_bias','N2In',Rin@u_kΩ)
circuit10_2.R(7, 'N1Out','Output',Rin*lamda@u_kΩ)
circuit10_2.R(8, 'N2Out','Output',Rin*lamda@u_kΩ)
circuit10_2.R(9, 'N1Out',circuit10_2.gnd,Rin*gamma@u_kΩ)
circuit10_2.R(10, 'N2Out',circuit10_2.gnd,Rin*gamma@u_kΩ)
simulator10_2 = circuit10_2.simulator(temperature=25, nominal_temperature=25)
analysis10_2 = simulator10_2.operating_point()
for node in analysis10_2.nodes.values():#nodes不是node
    if str(node)=='output':
       print ('Node{}: {:4.6f} V'.format(str(node), float(node)))
       Output10_2=float(node)
       break
    
result=np.ndarray(shape=(1,10), dtype=float)
result[0,0]=Output1_2-Output1_1
result[0,1]=Output2_2-Output2_1
result[0,2]=Output3_2-Output3_1
result[0,3]=Output4_2-Output4_1
result[0,4]=Output5_2-Output5_1
result[0,5]=Output6_2-Output6_1
result[0,6]=Output7_2-Output7_1
result[0,7]=Output8_2-Output8_1
result[0,8]=Output9_2-Output9_1
result[0,9]=Output10_2-Output10_1

print(result)

result2=np.ndarray(shape=(1,10), dtype=float)
result2[0,0]=Output1_2/Output1_1
result2[0,1]=Output2_2/Output2_1
result2[0,2]=Output3_2/Output3_1
result2[0,3]=Output4_2/Output4_1
result2[0,4]=Output5_2/Output5_1
result2[0,5]=Output6_2/Output6_1
result2[0,6]=Output7_2/Output7_1
result2[0,7]=Output8_2/Output8_1
result2[0,8]=Output9_2/Output9_1
result2[0,9]=Output10_2/Output10_1

print(result2)


