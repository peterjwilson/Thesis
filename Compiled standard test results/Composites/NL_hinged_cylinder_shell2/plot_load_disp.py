# -*- coding: utf-8 -*-
"""
Created on Mon Dec  5 21:30:56 2016

@author: wilson
"""

#===============================================
#
#       Composite hinged cylindrical roof
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



load_andes = [0]
disp_andes = [0]

disp_scale = 1000 #m to mm

with open("load_andes.txt", "r") as fol:
  for line in fol:
    load_andes.append(abs(float(line)))      
fol.close()

with open("displacement_andes.txt", "r") as fod:
  for line in fod:
    disp_andes.append(abs(float(line)))         
fod.close()

load_dsg = [0]
disp_dsg = [0]
with open("load_dsg.txt", "r") as fol:
  for line in fol:
    load_dsg.append(abs(float(line)))      
fol.close()

with open("displacement_dsg.txt", "r") as fod:
  for line in fod:
    disp_dsg.append(abs(float(line)))         
fod.close()

#https://www.researchgate.net/publication/222423070_Popular_benchmark_problems_for_geometric_nonlinear_analysis_of_shells
load_ref = [0]
disp_ref = [0]
max_load_ref = 3000
with open("load_benchmark.txt", "r") as fol:
  for line in fol:
    load_ref.append(abs(float(line))*max_load_ref)      
fol.close()

with open("displacement_benchmark.txt", "r") as fod:
  for line in fod:
    disp_ref.append(abs(float(line))/disp_scale)         
fod.close()


#custom_edit

##77B5FE = nice blue

plt.plot(disp_andes,load_andes, color = '#77B5FE', linewidth=3.0, label = 'ANDES-DKQ',antialiased=True)
plt.plot(disp_dsg,load_dsg, color = '#FF91A4', linewidth=3.0, label = 'DSG',antialiased=True)
plt.plot(disp_ref,load_ref,color = 'grey', linestyle='None', markerfacecolor= 'None', markersize = 7.0, marker='o', label = 'Ref',antialiased=True)
#plt.plot(disp_ref,load_ref,color = 'grey', linewidth=2.0, linestyle='--', label = 'Ref',antialiased=True)
plt.legend(loc=2,frameon=False,fontsize=labelfontsize+2)
#lg = plt.legend()
#lg.draw_frame(False)
#lg.loc(2)
plt.xlabel('Displacement [m]')
plt.ylabel('Load [N]')
plt.title('Load-displacement curve of hinged cylindrical roof [90/0/90]',fontsize=labelfontsize+2)
plt.grid()
plt.tick_params(labelsize=labelfontsize)
plt.savefig('Load_displacement_curve_composite_hinged_cylindrical_roof.pdf')
plt.show()

