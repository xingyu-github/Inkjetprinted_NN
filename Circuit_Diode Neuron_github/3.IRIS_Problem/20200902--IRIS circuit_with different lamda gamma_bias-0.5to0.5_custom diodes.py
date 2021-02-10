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
#the purpose of the following code is to clean all
#clear = lambda: os.system('cls')
#clear()
#input
Input=np.array([[0.41666667, 0.83333333, 0.03389831, 0.04166667],       [0.22222222, 0.20833333, 0.33898305, 0.41666667],       [0.63888889, 0.41666667, 0.57627119, 0.54166667],
                [0.30555556, 0.79166667, 0.05084746, 0.125     ],       [1.        , 0.75      , 0.91525424, 0.79166667],       [0.55555556, 0.54166667, 0.62711864, 0.625     ],
                [0.72222222, 0.45833333, 0.69491525, 0.91666667],       [0.22222222, 0.75      , 0.15254237, 0.125     ],       [0.11111111, 0.5       , 0.10169492, 0.04166667],
                [0.72222222, 0.5       , 0.79661017, 0.91666667],       [0.36111111, 0.29166667, 0.54237288, 0.5       ],       [0.30555556, 0.79166667, 0.11864407, 0.125     ],
                [0.77777778, 0.41666667, 0.83050847, 0.83333333],       [0.58333333, 0.5       , 0.59322034, 0.58333333],       [0.47222222, 0.375     , 0.59322034, 0.58333333], 
                [0.02777778, 0.5       , 0.05084746, 0.04166667],       [0.41666667, 0.25      , 0.50847458, 0.45833333],       [0.36111111, 0.41666667, 0.59322034, 0.58333333],
                [0.30555556, 0.58333333, 0.08474576, 0.125     ],       [0.19444444, 0.5       , 0.03389831, 0.04166667],       [0.33333333, 0.25      , 0.57627119, 0.45833333],
                [0.30555556, 0.41666667, 0.59322034, 0.58333333],       [0.66666667, 0.41666667, 0.6779661 , 0.66666667],       [0.19444444, 0.625     , 0.05084746, 0.08333333],
                [0.80555556, 0.5       , 0.84745763, 0.70833333],       [0.38888889, 0.33333333, 0.52542373, 0.5       ],       [0.33333333, 0.91666667, 0.06779661, 0.04166667],
                [0.22222222, 0.75      , 0.08474576, 0.08333333],       [0.5       , 0.33333333, 0.62711864, 0.45833333],       [0.55555556, 0.20833333, 0.6779661 , 0.75      ],
                [0.5       , 0.41666667, 0.61016949, 0.54166667],       [0.94444444, 0.41666667, 0.86440678, 0.91666667],       [0.36111111, 0.20833333, 0.49152542, 0.41666667],
                [0.58333333, 0.33333333, 0.77966102, 0.83333333],       [0.41666667, 0.33333333, 0.69491525, 0.95833333],       [0.27777778, 0.70833333, 0.08474576, 0.04166667],
                [0.33333333, 0.125     , 0.50847458, 0.5       ],       [0.25      , 0.58333333, 0.06779661, 0.04166667],       [0.61111111, 0.33333333, 0.61016949, 0.58333333],
                [0.66666667, 0.20833333, 0.81355932, 0.70833333],       [0.69444444, 0.41666667, 0.76271186, 0.83333333],       [0.22222222, 0.625     , 0.06779661, 0.08333333],
                [0.47222222, 0.08333333, 0.6779661 , 0.58333333],       [0.55555556, 0.375     , 0.77966102, 0.70833333],       [0.63888889, 0.375     , 0.61016949, 0.5       ]])
#Parameters
W=np.array([[-1.,  1.,  1., -1.,  1.,  1., -1., -1., -1., -1., -1., -1.,  1.,        -1., -1.,  1., -1., -1., -1., -1.],
       [-1., -1., -1.,  1., -1., -1., -1., -1., -1., -1.,  1., -1.,  1.,         1.,  1.,  1.,  1., -1., -1., -1.],
       [-1.,  1.,  1., -1.,  1., -1.,  1.,  1., -1., -1.,  1., -1., -1.,        -1., -1., -1., -1., -1., -1., -1.],
       [-1., -1.,  1., -1.,  1., -1., -1., -1., -1., -1., -1., -1., -1.,        -1., -1., -1., -1., -1., -1., -1.]])
B=np.array([-0.5       ,  0.5       , -0.5       ,  0.5       , -0.42057827,        0.        ,  0.        , -0.5       , -0.5       , -0.47523797,
        0.5       , -0.5       ,  0.5       ,  0.5       ,  0.5       ,        0.5       ,  0.5       , -0.4880538 , -0.01908754, -0.5       ])
W_O=np.array([[ 1., -1., -1.],       [-1.,  1., -1.],       [-1.,  1.,  1.],       [ 1., -1., -1.],
       [-1., -1.,  1.],       [ 1., -1.,  1.],       [-1., -1.,  1.],       [-1., -1., -1.],
       [-1., -1.,  1.],       [ 1.,  1., -1.],       [-1.,  1., -1.],       [ 1., -1., -1.],
       [ 1., -1., -1.],       [ 1., -1., -1.],       [ 1., -1., -1.],       [ 1.,  1., -1.],
       [ 1., -1., -1.],       [ 1., -1., -1.],       [-1.,  1.,  1.],       [ 1., -1., -1.]])
y_label=np.array([[1, 0, 0],       [0, 1, 0],       [0, 1, 0],       [1, 0, 0],       [0, 0, 1],
                  [0, 1, 0],       [0, 0, 1],       [1, 0, 0],       [1, 0, 0],       [0, 0, 1],
                  [0, 1, 0],       [1, 0, 0],       [0, 0, 1],       [0, 1, 0],       [0, 1, 0],
                  [1, 0, 0],       [0, 1, 0],       [0, 1, 0],       [1, 0, 0],       [1, 0, 0],
                  [0, 1, 0],       [0, 1, 0],       [0, 1, 0],       [1, 0, 0],       [0, 0, 1],
                  [0, 1, 0],       [1, 0, 0],       [1, 0, 0],       [0, 1, 0],       [0, 0, 1],
                  [0, 1, 0],       [0, 0, 1],       [0, 1, 0],       [0, 0, 1],       [0, 0, 1],
                  [1, 0, 0],       [0, 1, 0],       [1, 0, 0],       [0, 1, 0],       [0, 0, 1],
                  [0, 0, 1],       [1, 0, 0],       [0, 0, 1],       [0, 0, 1],       [0, 1, 0]])
#Resistance
Rin=1
K=5
Kprime=4
Kv=20
Bias=0.3
prediction=np.zeros((45,3))
VAR=np.zeros((1,45))
average=np.zeros((10,10))
accuracy=np.zeros((10,10))
W_1=np.zeros((20,3))
circuit_list=[]
simulator_list=[]
analysis_list=[]
#lamda=10 #Routput over Rinput
#gamma=100 #Rground over Rinput
#lamda=np.array([1,10])
#gamma=np.array([10,100])
lamda=np.array([0.001,0.01,0.1,1,10,100,1000,10000,100000,1000000])
gamma=np.array([0.001,0.01,0.1,1,10,100,1000,10000,100000,1000000])
#print(VAR)
#Function:
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
        for num_cycle in range(0,45):
            locals()["circuit"+str(a)] = Circuit('IRIS problem circuit')
            circuit_list.append(locals()["circuit"+str(a)])
            a=a+1
#print(circuit_list)    
#print(circuit_9_9_44)
        
a=0
#%%
for ia in range(0,10):
    for ib in range(0,10) :
        for num_cycle in range(0,45):
        #Diode
        #    circuit = Circuit('IRIS Problem circuit')
            circuit_list[a].subcircuit(SubCircuit1())       
            for i in range(0,20):
                circuit_list[a].X('neuron{}'.format(i),'Sub_circuit1','neuron{}In'.format(i),'neuron{}Out'.format(i))
            #input voltage&bias
            #Input voltage=Input*Weight(1 or -1)*K*K'*Kv
            for ix,iy in np.ndindex(W.shape):
                circuit_list[a].V('Vinput{}_{}'.format(ix,iy),'input{}_{}'.format(ix,iy),circuit_list[a].gnd,(W[ix,iy]*Input[num_cycle,ix]*K*Kprime/Kv)@u_V)
            #input bias voltage 
            for i in range(0,20):
                circuit_list[a].V('Vbias{}'.format(i),'bias{}'.format(i),circuit_list[a].gnd,(B[i]*0.6*Kprime/Kv+5*Bias)@u_V)
            #input synpases&bias resistors
            for ix,iy in np.ndindex(W.shape):
                circuit_list[a].R('Rinput{}_{}'.format(ix,iy),'input{}_{}'.format(ix,iy),'neuron{}In'.format(iy),Rin@u_kΩ)
            for i in range(0,20):
                circuit_list[a].R('Rbias{}'.format(i),'bias{}'.format(i),'neuron{}In'.format(i),Rin@u_kΩ)
            #Output synapses
            for ix,iy in np.ndindex(W_O.shape):
                W_1[ix,iy]=W_O[ix,iy]+1
                if W_1[ix,iy]!=0:
                   circuit_list[a].R('Rout{}_{}'.format(ix,iy),'neuron{}Out'.format(ix),'output{}'.format(iy),(Rin*lamda[ia])@u_kΩ)
            #Ground Resistors
            for i in range(0,20):   
                circuit_list[a].R('Rground{}'.format(i),'neuron{}Out'.format(i),circuit_list[a].gnd,(Rin*gamma[ib])@u_kΩ)
                #    print(circuit_list[a])
            locals()["simulator" + str(a)] = circuit_list[a].simulator(temperature=25, nominal_temperature=25)
            simulator_list.append(locals()["simulator" + str(a)])
            locals()["analysis" + str(a)]  = simulator_list[a].operating_point()
            analysis_list.append(locals()["analysis" + str(a)])
            #print(analysis.nodes.values())
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
