# -*- coding: utf-8 -*-
"""
Created on Fri Mar 17 18:37:12 2017

@author: Peter
"""

#===============================================
#
#       cantilever
#
#===============================================



import matplotlib.pyplot as plt
import numpy as np

myfontsize = 20
labelfontsize = 14
#===============================================================================
## Set style of plots
font = {'family' : 'sans-serif',
        'family' : 'Arial',
        'style'  : 'normal',
        'weight' : 'normal',
        'size'   : myfontsize}

plt.rc('font', **font)
plt.rc('font', serif='Helvetica Neue') 
#plt.rcParams['font.family'] = 'Arial'
#===============================================================================

time_andes = [0]
disp_andes = [0]

with open("cantilever_andes.txt", "r") as fol:
  for line in fol:
    line = line.split(' ')
    time_andes.append((float(line[0])))    
    disp_andes.append((float(line[1])))   
fol.close()





time_ref = [0]
disp_ref = [0]

with open("cantilever_ref.txt", "r") as fol:
  for line in fol:
    line = line.split(' ')
    time_ref.append((float(line[0])))    
    disp_ref.append((float(line[1])))   
fol.close()

#reference quantities

#Kn = 3.52
#pi=np.pi
#E = 2e11
#I = 286.583 / (10**4)
#g = 9.81
#mass = 44.745
#length = 3
#w = mass*g/length*1000
#
#f0 = 12.203 #Hz
#omega = 2*pi*f0
#staticDisp = -0.002295709913596511
#
#time_ref = []
#disp_ref = []
#dt = 0.0025
#for timestep in range(int(0.15 / dt)):
#    time_ref.append(dt*timestep)
#    disp_ref.append(staticDisp*(1-np.cos(omega*dt*timestep)))
    

#custom_edit

##77B5FE = nice blue
#plt.figure(figsize=(5.82,3.5))
plt.plot(time_andes,disp_andes, color = '#77B5FE', linewidth=2.0, label = 'ANDES-DKQ',antialiased=True)
#plt.plot(time_dsg,disp_dsg, color = '#FF91A4', linestyle='--', linewidth=2.0, label = 'DSG',antialiased=True)
plt.plot(time_ref,disp_ref,color = 'grey', linestyle='None', markerfacecolor= 'None', markersize = 7.0, marker='o', label = 'Ref',antialiased=True)
#plt.plot(disp_ref,load_ref,color = 'grey', linewidth=2.0, linestyle='--', label = 'Ref',antialiased=True)
plt.legend(loc=2,frameon=False,fontsize=labelfontsize+2)
#lg = plt.legend()
#lg.draw_frame(False)
#lg.loc(2)
plt.xlabel('Time [s]')
plt.ylabel('Vertical displacement [m]')
plt.xlim([0,0.15])
plt.grid()

plt.tick_params(labelsize=labelfontsize)
plt.savefig('swinging_plate_graph.pdf')
plt.show()

#