# -*- coding: utf-8 -*-
"""
Created on Wed Sep  2 12:35:08 2020

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
import math
#the purpose of the following code is to clean all
#clear = lambda: os.system('cls')
#clear()
#input
Input=np.array([[-3.33333333e-01,  1.33333333e+00, -1.86440678e+00,        -1.83333333e+00],       [-1.11111111e+00, -1.16666667e+00, -6.44067797e-01,        -3.33333333e-01],       [ 5.55555556e-01, -3.33333333e-01,  3.05084746e-01,         1.66666667e-01],       [-7.77777778e-01,  1.16666667e+00, -1.79661017e+00,        -1.50000000e+00],       [ 2.00000000e+00,  1.00000000e+00,  1.66101695e+00,         1.16666667e+00],       [ 2.22222222e-01,  1.66666667e-01,  5.08474576e-01,         5.00000000e-01],       [ 8.88888889e-01, -1.66666667e-01,  7.79661017e-01,         1.66666667e+00],       [-1.11111111e+00,  1.00000000e+00, -1.38983051e+00,        -1.50000000e+00],
       [-1.55555556e+00,  0.00000000e+00, -1.59322034e+00,        -1.83333333e+00],       [ 8.88888889e-01,  0.00000000e+00,  1.18644068e+00,         1.66666667e+00],       [-5.55555556e-01, -8.33333333e-01,  1.69491525e-01,         4.44089210e-16],       [-7.77777778e-01,  1.16666667e+00, -1.52542373e+00,        -1.50000000e+00],       [ 1.11111111e+00, -3.33333333e-01,  1.32203390e+00,         1.33333333e+00],       [ 3.33333333e-01,  0.00000000e+00,  3.72881356e-01,         3.33333333e-01],       [-1.11111111e-01, -5.00000000e-01,  3.72881356e-01,         3.33333333e-01],       [-1.88888889e+00,  0.00000000e+00, -1.79661017e+00,        -1.83333333e+00],
       [-3.33333333e-01, -1.00000000e+00,  3.38983051e-02,        -1.66666667e-01],       [-5.55555556e-01, -3.33333333e-01,  3.72881356e-01,         3.33333333e-01],       [-7.77777778e-01,  3.33333333e-01, -1.66101695e+00,        -1.50000000e+00],       [-1.22222222e+00,  0.00000000e+00, -1.86440678e+00,        -1.83333333e+00],       [-6.66666667e-01, -1.00000000e+00,  3.05084746e-01,        -1.66666667e-01],       [-7.77777778e-01, -3.33333333e-01,  3.72881356e-01,         3.33333333e-01],       [ 6.66666667e-01, -3.33333333e-01,  7.11864407e-01,         6.66666667e-01],       [-1.22222222e+00,  5.00000000e-01, -1.79661017e+00,        -1.66666667e+00],
       [ 1.22222222e+00,  0.00000000e+00,  1.38983051e+00,         8.33333333e-01],       [-4.44444444e-01, -6.66666667e-01,  1.01694915e-01,         4.44089210e-16],       [-6.66666667e-01,  1.66666667e+00, -1.72881356e+00,        -1.83333333e+00],       [-1.11111111e+00,  1.00000000e+00, -1.66101695e+00,        -1.66666667e+00],       [-8.88178420e-16, -6.66666667e-01,  5.08474576e-01,        -1.66666667e-01],       [ 2.22222222e-01, -1.16666667e+00,  7.11864407e-01,         1.00000000e+00],       [-8.88178420e-16, -3.33333333e-01,  4.40677966e-01,         1.66666667e-01],       [ 1.77777778e+00, -3.33333333e-01,  1.45762712e+00,         1.66666667e+00],
       [-5.55555556e-01, -1.16666667e+00, -3.38983051e-02,        -3.33333333e-01],       [ 3.33333333e-01, -6.66666667e-01,  1.11864407e+00,         1.33333333e+00],       [-3.33333333e-01, -6.66666667e-01,  7.79661017e-01,         1.83333333e+00],       [-8.88888889e-01,  8.33333333e-01, -1.66101695e+00,        -1.83333333e+00],       [-6.66666667e-01, -1.50000000e+00,  3.38983051e-02,         4.44089210e-16],       [-1.00000000e+00,  3.33333333e-01, -1.72881356e+00,        -1.83333333e+00],       [ 4.44444444e-01, -6.66666667e-01,  4.40677966e-01,         3.33333333e-01],       [ 6.66666667e-01, -1.16666667e+00,  1.25423729e+00,         8.33333333e-01],
       [ 7.77777778e-01, -3.33333333e-01,  1.05084746e+00,         1.33333333e+00],       [-1.11111111e+00,  5.00000000e-01, -1.72881356e+00,        -1.66666667e+00],       [-1.11111111e-01, -1.66666667e+00,  7.11864407e-01,         3.33333333e-01],       [ 2.22222222e-01, -5.00000000e-01,  1.11864407e+00,         8.33333333e-01],       [ 5.55555556e-01, -5.00000000e-01,  4.40677966e-01,         4.44089210e-16],       [ 1.77777778e+00, -1.00000000e+00,  2.00000000e+00,         1.66666667e+00],       [-4.44444444e-01,  1.00000000e+00, -1.52542373e+00,        -1.66666667e+00],       [-1.22222222e+00,  6.66666667e-01, -1.72881356e+00,        -1.83333333e+00],
       [-1.44444444e+00, -3.33333333e-01, -1.72881356e+00,        -1.66666667e+00],       [-1.00000000e+00, -8.33333333e-01, -3.38983051e-02,         1.66666667e-01],       [-1.11111111e+00,  3.33333333e-01, -1.66101695e+00,        -1.83333333e+00],       [-6.66666667e-01,  5.00000000e-01, -1.79661017e+00,        -1.83333333e+00],       [ 1.77777778e+00,  1.00000000e+00,  1.86440678e+00,         1.50000000e+00],       [ 8.88888889e-01, -1.66666667e-01,  9.83050847e-01,         1.33333333e+00],       [ 1.33333333e+00, -5.00000000e-01,  1.59322034e+00,         8.33333333e-01],       [ 3.33333333e-01, -6.66666667e-01,  1.11864407e+00,         1.50000000e+00],
       [ 1.11111111e-01, -6.66666667e-01,  5.76271186e-01,         8.33333333e-01],       [-1.11111111e-01,  3.33333333e-01,  3.72881356e-01,         5.00000000e-01],       [ 1.77777778e+00, -6.66666667e-01,  1.86440678e+00,         1.16666667e+00],       [-4.44444444e-01, -3.33333333e-01,  1.69491525e-01,        -1.66666667e-01],       [-1.44444444e+00,  3.33333333e-01, -1.59322034e+00,        -1.83333333e+00],       [-4.44444444e-01, -1.16666667e+00,  7.11864407e-01,         1.16666667e+00],       [ 2.22222222e-01, -8.33333333e-01,  6.44067797e-01,         8.33333333e-01],       [-1.44444444e+00, -3.33333333e-01, -1.72881356e+00,        -2.00000000e+00],
       [-1.55555556e+00,  0.00000000e+00, -1.79661017e+00,        -1.83333333e+00],       [ 4.44444444e-01, -3.33333333e-01,  1.25423729e+00,         1.50000000e+00],       [-1.66666667e+00,  3.33333333e-01, -1.72881356e+00,        -1.66666667e+00],       [-8.88178420e-16, -3.33333333e-01,  6.44067797e-01,         8.33333333e-01],       [ 4.44444444e-01,  0.00000000e+00,  7.79661017e-01,         1.16666667e+00],       [ 6.66666667e-01, -1.66666667e-01,  3.05084746e-01,         1.66666667e-01],       [-4.44444444e-01, -6.66666667e-01,  3.72881356e-01,         4.44089210e-16],       [ 6.66666667e-01,  1.66666667e-01,  1.18644068e+00,         2.00000000e+00],
       [-1.11111111e-01, -3.33333333e-01,  5.76271186e-01,         8.33333333e-01],       [-1.11111111e+00,  1.00000000e+00, -1.59322034e+00,        -1.83333333e+00],       [-1.11111111e-01, -1.66666667e+00,  3.38983051e-02,        -5.00000000e-01],       [ 3.33333333e-01, -5.00000000e-01,  2.37288136e-01,         4.44089210e-16],       [ 4.44444444e-01, -3.33333333e-01,  1.05084746e+00,         8.33333333e-01],       [-1.22222222e+00, -1.50000000e+00, -4.40677966e-01,        -5.00000000e-01],       [ 2.22222222e-01,  1.66666667e-01,  1.38983051e+00,         2.00000000e+00],       [-6.66666667e-01, -1.16666667e+00,  3.38983051e-02,         4.44089210e-16],
       [-7.77777778e-01,  8.33333333e-01, -1.66101695e+00,        -1.83333333e+00],       [-1.33333333e+00, -1.66666667e-01, -1.66101695e+00,        -2.00000000e+00],       [-1.00000000e+00,  1.50000000e+00, -1.66101695e+00,        -2.00000000e+00],       [ 6.66666667e-01,  1.66666667e-01,  1.18644068e+00,         1.33333333e+00],       [-1.88888889e+00, -3.33333333e-01, -1.79661017e+00,        -1.83333333e+00],       [-1.11111111e-01, -8.33333333e-01,  7.79661017e-01,         5.00000000e-01],       [ 3.33333333e-01, -8.33333333e-01,  9.15254237e-01,         1.00000000e+00],       [-2.22222222e-01, -3.33333333e-01,  7.79661017e-01,         8.33333333e-01],       [-1.00000000e+00,  5.00000000e-01, -1.66101695e+00,        -1.83333333e+00],
       [-1.11111111e+00,  1.66666667e-01, -1.52542373e+00,        -1.33333333e+00]])
#Parameters
W=np.array([[-1.4800873 ,  0.5056782 ,  2.945876  ,  0.7192196 , -0.65940505],
       [-0.20633703, -1.2039925 , -1.5020272 , -0.9310725 ,  2.6416876 ],
       [ 0.87476736,  0.5556942 , -3.3199759 ,  0.30431792, -2.4884613 ],
       [ 1.3599266 ,  0.71431535,  0.3470606 , -0.7626541 , -3.4138155 ]])
B=np.array([ 0.2       , -0.2       ,  0.2       ,  0.2       , -0.19995317])
W_O=np.array([[-3.7562346 ,  1.4907584 , -1.504717  ],       [-3.855074  , -4.6448703 ,  4.675792  ],
       [-0.11584902,  4.7378235 , -4.8694863 ],       [-2.6841202 ,  4.2753496 , -4.2679796 ],
       [ 1.8600078 , -3.475445  , -0.54265946]])
y_label=np.array([[1, 0, 0],       [0, 1, 0],       [0, 1, 0],       [1, 0, 0],       [0, 0, 1],       [0, 1, 0],       [0, 0, 1],       [1, 0, 0],       [1, 0, 0],       [0, 0, 1],       [0, 1, 0],       [1, 0, 0],       [0, 0, 1],       [0, 1, 0],       [0, 1, 0],       [1, 0, 0],       [0, 1, 0],       [0, 1, 0],       [1, 0, 0],       [1, 0, 0],       [0, 1, 0],       [0, 1, 0],       [0, 1, 0],       [1, 0, 0],       [0, 0, 1],       [0, 1, 0],       [1, 0, 0],       [1, 0, 0],       [0, 1, 0],       [0, 0, 1],       [0, 1, 0],       [0, 0, 1],
       [0, 1, 0],       [0, 0, 1],       [0, 0, 1],       [1, 0, 0],       [0, 1, 0],       [1, 0, 0],       [0, 1, 0],       [0, 0, 1],       [0, 0, 1],       [1, 0, 0],       [0, 0, 1],       [0, 0, 1],       [0, 1, 0],       [0, 0, 1],       [1, 0, 0],       [1, 0, 0],       [1, 0, 0],       [0, 1, 0],       [1, 0, 0],       [1, 0, 0],       [0, 0, 1],       [0, 0, 1],       [0, 0, 1],       [0, 0, 1],       [0, 0, 1],       [0, 1, 0],       [0, 0, 1],       [0, 1, 0],       [1, 0, 0],       [0, 0, 1],       [0, 0, 1],       [1, 0, 0],
       [1, 0, 0],       [0, 0, 1],       [1, 0, 0],       [0, 0, 1],       [0, 0, 1],       [0, 1, 0],       [0, 1, 0],       [0, 0, 1],       [0, 0, 1],       [1, 0, 0],       [0, 1, 0],       [0, 1, 0],       [0, 0, 1],       [0, 1, 0],       [0, 0, 1],       [0, 1, 0],       [1, 0, 0],       [1, 0, 0],       [1, 0, 0],       [0, 0, 1],       [1, 0, 0],       [0, 1, 0],       [0, 0, 1],       [0, 0, 1],
       [1, 0, 0],       [1, 0, 0]])
#Tunning PARAMETERS
#lamda=np.array([1,10])
##gamma=np.array([10,100])
#lamda=np.array([0.001,0.01,0.1,1,10,100,1000,10000,100000,1000000])
#gamma=np.array([0.001,0.01,0.1,1,10,100,1000,10000,100000,1000000])
lamda=np.array([10,20,40,60,80,100,120,140,160,180])
gamma=np.array([10,20,30,40,50,60,70,80,90,100])
RinRef=1
Bias=0.4

#Prepossessing:
#hidden_output connections
W_P=np.zeros((5,3))
mmin=-np.amin(W_O)
for ix,iy in np.ndindex(W_O.shape):
    W_P[ix,iy]=W_O[ix,iy]+mmin
W_P_column_sums= W_P.sum(axis=0)
#print('Summation of hidden_output connections weights column:',W_P_column_sums)
Kprime=W_P_column_sums.max()
print('Kprime is', Kprime)
#input_hidden connections
W__abs=abs(W)
W_column_sums= W__abs.sum(axis=0)
#print('Summation of input_hidden connections weights column:',W_column_sums)
K=math.ceil(W_column_sums.max())
print('K is', K)
SIGN=np.sign(W)
G=np.zeros((4,5))
#overall
Kv=K*Kprime
print('Kv is',Kv)
#print(VAR)
#Function:
prediction=np.zeros((90,3))
VAR=np.zeros((1,90))
average=np.zeros((10,10))
accuracy=np.zeros((10,10))
GB=np.zeros((5))
VB=np.zeros((5))
circuit_list=[]
simulator_list=[]
analysis_list=[]
def classification_accuracy(classification_scores, true_scores):
    """
    Returns the fractional classification accuracy for a batch of N predictions.
    Parameters
    ----------
    classification_scores : numpy.ndarray, shape=(N, K)
        The scores for K classes, for a batch of N pieces of data
        (e.g. images).
    true_labels : numpy.ndarray, shape=(N,)
        The true label for each datum in the batch: each label is an
        integer in the domain [0, K).

    Returns
    -------
    float
        (num_correct) / N
    """
    return np.mean(np.argmax(classification_scores, axis=1) == np.argmax(true_scores, axis=1))
class SubCircuit1(SubCircuitFactory):
    __name__ = 'sub_circuit1'
    __nodes__ = ('In', 'Out')
    def __init__(self):
        super().__init__()
        self.D('1','Mid','Out',model='Diode')
        self.model('Diode','D',IS=0.000000006, n=3.12467)
        self.R('Rs','In','Mid',611.49897@u_Ω)
        self.R('Rsh','In','Out',188085.7139@u_Ω)
a=0
for ix in range(0,10):
    for iy in range(0,10) :
        for num_cycle in range(0,90):
            locals()["circuit"+str(a)] = Circuit('IRIS problem circuit')
            circuit_list.append(locals()["circuit"+str(a)])
            a=a+1
a=0
#%%
for ia in range(0,10):
    for ib in range(0,10) :
        #Parameter   
#        lamda=1 
#        gamma=2
#        Goutput=Gsum/lamda
#        Gground=Gsum/gamma
        Gsum=5/RinRef
        Goutput=Gsum/lamda[ia]  
        Gground=Gsum/gamma[ib]
        for num_cycle in range(0,90):
            #Diode
#            num_cycle=1
#            a=0
            circuit_list[a].subcircuit(SubCircuit1())       
            for i in range(0,5):
                circuit_list[a].X('neuron{}'.format(i),'Sub_circuit1','neuron{}In'.format(i),'neuron{}Out'.format(i))
            #input voltage&bias
            #Input voltage=Input*SIGN
            for ix,iy in np.ndindex(SIGN.shape):
                circuit_list[a].V('Vinput{}_{}'.format(ix,iy),'input{}_{}'.format(ix,iy),circuit_list[a].gnd,(SIGN[ix,iy]*Input[num_cycle,ix])@u_V)
            #input synpases&bias resistors
            #GCOLSUM is the summation of G matrix's columns
            for ix,iy in np.ndindex(W__abs.shape):
                G[ix,iy]=Gsum*W__abs[ix,iy]/K
                circuit_list[a].R('Rinput{}_{}'.format(ix,iy),'input{}_{}'.format(ix,iy),'neuron{}In'.format(iy),(1/G[ix,iy])@u_kΩ)
            GCOLSUM=G.sum(axis=0)
            for i in range(0,5):
                GB[i]=Gsum-GCOLSUM[i]
                circuit_list[a].R('Rbias{}'.format(i),'bias{}'.format(i),'neuron{}In'.format(i),(1/GB[i])@u_kΩ)
            #input bias voltage 
            for i in range(0,5):
                VB[i]=Gsum*((Kprime*B[i]/Kv/GB[i])*1.9+(Bias/GB[i]))
                circuit_list[a].V('Vbias{}'.format(i),'bias{}'.format(i),circuit_list[a].gnd,(VB[i])@u_V)
            #Output synapses
            for ix,iy in np.ndindex(W_P.shape):
                if W_P[ix,iy]!=0:
                   circuit_list[a].R('Rout{}_{}'.format(ix,iy),'neuron{}Out'.format(ix),'output{}'.format(iy),(1/(Goutput*W_P[ix,iy]/Kprime))@u_kΩ) 
            #Ground Resistors
            for i in range(0,5):   
                circuit_list[a].R('Rground{}'.format(i),'neuron{}Out'.format(i),circuit_list[a].gnd,(1/Gground)@u_kΩ)
                #    print(circuit_list[a])
            locals()["simulator" + str(a)] = circuit_list[a].simulator(temperature=25, nominal_temperature=25)
            simulator_list.append(locals()["simulator" + str(a)])
            locals()["analysis" + str(a)]  = simulator_list[a].operating_point()
            analysis_list.append(locals()["analysis" + str(a)])
            #    for node in analysis.nodes.values():#nodes不是node
            #        print('Node{}: {:4.6f} V'.format(str(node), float(node)))
            for node in analysis_list[a].nodes.values():#nodes不是node
                if str(node)=='output1':
        #            print('Node{}: {:4.6f} V'.format(str(node), float(node)))
                    out1=float(node)
                    break
            for node in analysis_list[a].nodes.values():#nodes不是node
                if str(node)=='output2':
        #            print('Node{}: {:4.6f} V'.format(str(node), float(node)))
                    out2=float(node)
            for node in analysis_list[a].nodes.values():#nodes不是node
                if str(node)=='output0':
        #            print('Node{}: {:4.6f} V'.format(str(node), float(node)))
                    out0=float(node)    
                    break
            prediction[num_cycle][0]=out0
            prediction[num_cycle][1]=out1
            prediction[num_cycle][2]=out2
            Median= np.median(prediction[num_cycle,:])
            Max=np.max(prediction[num_cycle,:])
            VAR[0][num_cycle]=Max-Median
#            print(circuit1)
            a=a+1
        average[ia][ib]=np.mean(VAR)
        print(average[ia][ib])
        accuracy[ia][ib]=classification_accuracy(prediction,y_label)        
        print(accuracy[ia][ib])

#%%%
#
##print(circuit3)
#    for node in analysis1.nodes.values():#nodes不是node
#        print('Node{}: {:4.6f} V'.format(str(node), float(node)))
