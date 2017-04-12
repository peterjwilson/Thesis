# -*- coding: utf-8 -*-
"""
Created on Mon Dec  5 21:30:56 2016

@author: wilson
"""


#===============================================
#
#       dome self weight
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

t = 0.01




# DSG results

y_dsg = []
n_theta_dsg = []

with open("n_theta_dsg.txt", "r") as fol:
  for line in fol:
    line = line.split(' ')
    y_dsg.append((float(line[0]))) 
    n_theta_dsg.append((float(line[1]))*0.01)
fol.close()


phi_dsg = []

for i in range(len((y_dsg))):
    phi_dsg.append(180*y_dsg[i]/np.pi/5)


# ANDES results

y_andes = []
n_theta_andes = []

with open("n_theta_andes.txt", "r") as fol:
  for line in fol:
    line = line.split(' ')
    y_andes.append((float(line[0]))) 
    n_theta_andes.append((float(line[1])))
fol.close()


phi_andes = []

for i in range(len((y_andes))):
    phi_andes.append(180*y_andes[i]/np.pi/5)   
    
#
#with open("tos_ex9_force_xx.txt", "r") as fol:
#  for line in fol:
#    line = line.split(' ')
#    force_phi_1.append((float(line[1])))
#fol.close()
#
#with open("tos_ex9_force_yy.txt", "r") as fol:
#  for line in fol:
#    line = line.split(' ')
#    force_phi_2.append((float(line[1])))
#fol.close()

#for i in range(len(force_phi_1)):
#    force_phi.append((force_phi_1[i]**2 + force_phi_2[i]**2)**0.5)




#custom_edit




force_theta_ref = []
phi_ref = []
with open("ref_n_theta.txt", "r") as fol:
  for line in fol:
    line = line.split('\t')
    phi_ref.append((float(line[0]))) 
    force_theta_ref.append((float(line[1])))
fol.close()


##77B5FE = nice blue

plt.plot(phi_andes,n_theta_andes, color = '#77B5FE', linewidth=3.0, label = 'ANDES-DKQ',antialiased=True)
plt.plot(phi_dsg,n_theta_dsg, color = '#FF91A4', linewidth=3.0, label = 'DSG',antialiased=True)
plt.plot(phi_ref,force_theta_ref,color = 'grey', linestyle='None', markerfacecolor= 'None', markersize = 7.0, marker='o', label = 'Ref',antialiased=True)
#plt.plot(disp_ref,load_ref,color = 'grey', linewidth=2.0, linestyle='--', label = 'Ref',antialiased=True)
plt.legend(loc=2,frameon=False,fontsize=labelfontsize+2)
#lg = plt.legend()
#lg.draw_frame(False)
#lg.loc(2)
plt.xlabel('Phi (degrees)')
plt.ylabel('n_theta [N/m]')
plt.grid()
plt.tick_params(labelsize=labelfontsize)
plt.savefig('Simply_support_dome_n_theta.pdf')
plt.show()

