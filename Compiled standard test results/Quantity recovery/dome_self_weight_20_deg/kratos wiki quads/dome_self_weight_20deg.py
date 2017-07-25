# -*- coding: utf-8 -*-
"""
Created on Mon Dec  5 21:30:56 2016

@author: wilson
"""


#===============================================
#
#       dome self weight 20 deg
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




# DSG results --------------------------------------------------------------

y_dsg = []
n_theta_dsg = []
n_yy_dsg = []
n_zz_dsg = []

#with open("n_theta_dsg.txt", "r") as fol:
#  for line in fol:
#    line = line.split(' ')
#    y_dsg.append((float(line[0]))) 
#    n_theta_dsg.append((float(line[1])))
#fol.close()
    
n_phi_dsg = []
with open("n_phi_dsg.txt", "r") as fol:
  for line in fol:
    line = line.split(' ')
    y_dsg.append((float(line[0]))) 
    n_phi_dsg.append((float(line[1])))
fol.close()

#von_mises_dsg = []
#with open("von_mises_mid_dsg.txt", "r") as fol:
#  for line in fol:
#    line = line.split(' ')
#    #y_dsg.append((float(line[0]))) 
#    von_mises_dsg.append((float(line[1]))/1e3)
#fol.close()

phi_dsg = []
for i in range(len((y_dsg))):
    phi_dsg.append(20+180*y_dsg[i]/np.pi/5)


# ANDES results  -------------------------------------------------------------

y_andes = []
n_theta_andes = []

with open("n_theta_andes.txt", "r") as fol:
  for line in fol:
    line = line.split(' ')
    y_andes.append((float(line[0]))) 
    n_theta_andes.append((float(line[1])))
fol.close()

n_phi_andes = []
with open("n_phi_andes.txt", "r") as fol:
  for line in fol:
    line = line.split(' ')
    #y_dsg.append((float(line[0]))) 
    n_phi_andes.append((float(line[1])))
fol.close()

von_mises_andes = []
with open("von_mises_mid_andes.txt", "r") as fol:
  for line in fol:
    line = line.split(' ')
    #y_dsg.append((float(line[0]))) 
    von_mises_andes.append((float(line[1]))/1e3)
fol.close()


phi_andes = []
for i in range(len((y_andes))):
    phi_andes.append(20+180*y_andes[i]/np.pi/5)   
    
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




# Excel results

n_theta_ref = []
phi_ref = []
with open("ref_n_theta.txt", "r") as fol:
  for line in fol:
    line = line.split('\t')
    phi_ref.append((float(line[0]))) 
    n_theta_ref.append((float(line[1])))
fol.close()

n_phi_ref = []
with open("ref_n_phi.txt", "r") as fol:
  for line in fol:
    line = line.split('\t')
    #phi_ref.append((float(line[0]))) 
    n_phi_ref.append((float(line[1])))
fol.close()



#ansys results
s_ansys = []
von_mises_ansys = []
with open("von_mises_mid_ansys.txt", "r") as fol:
  for line in fol:
    line = line.split('\t')
    s_ansys.append((float(line[0]))) 
    von_mises_ansys.append((float(line[1]))/1e3)
fol.close()

phi_ansys = []
for i in range(len((y_andes))):
    phi_ansys.append(90-180*s_ansys[i]/np.pi/5)   





#theoretical shell resuls
density = 7850
g = 9.8
gamma = density*g
R = 5
n_phi_hand = []
n_theta_hand = []

for i in range(len(phi_ref)):
    phi = phi_ref[i]/180*np.pi
    n_phi_hand.append(R*gamma*t*(np.cos(phi)-0.9397)/np.sin(phi)/np.sin(phi))
    n_theta_hand.append(-R*gamma*t*np.cos(phi)-n_phi_hand[i])





##77B5FE = nice blue
fig = plt.figure(1)
plt.plot(phi_andes,n_theta_andes, color = '#77B5FE', linewidth=3.0, label = 'ANDES-DKQ',antialiased=True)
#plt.plot(phi_dsg,n_theta_dsg, color = '#FF91A4', linestyle='--',linewidth=3.0, label = 'DSG',antialiased=True)
#plt.plot(phi_ref,n_theta_ref,color = 'grey', linestyle='None', markerfacecolor= 'None', markersize = 7.0, marker='o', label = 'Ref',antialiased=True)
plt.plot(phi_ref,n_theta_hand,color = 'grey', linestyle='None', markerfacecolor= 'None', markersize = 7.0, marker='o', label = 'Ref',antialiased=True)
#plt.plot(phi_ref,n_theta_hand,color = 'grey', linewidth=2.0, linestyle='--', label = 'Ref',antialiased=True)
plt.legend(loc=9,bbox_to_anchor=(0.5, -0.1), ncol=3, frameon=False,fontsize=labelfontsize+2)
#lg = plt.legend()
#lg.draw_frame(False)
#lg.loc(2)
plt.xlim([0,90])
plt.xlabel('Phi (degrees)')
plt.ylabel('Circumferential shell force [N/m]')
plt.grid()
plt.tick_params(labelsize=labelfontsize)
plt.savefig('Simply_support_dome_n_theta.pdf',bbox_inches="tight")



fig = plt.figure(2)
plt.plot(phi_andes,n_phi_andes, color = '#77B5FE', linewidth=3.0, label = 'ANDES-DKQ',antialiased=True)
plt.plot(phi_dsg,n_phi_dsg, color = '#FF91A4', linestyle='--',linewidth=3.0, label = 'Kratos thick quad',antialiased=True)
#plt.plot(phi_ref,n_phi_ref,color = 'grey', linestyle='None', markerfacecolor= 'None', markersize = 7.0, marker='o', label = 'Ref',antialiased=True)
plt.plot(phi_ref,n_phi_hand,color = 'grey', linestyle='None', markerfacecolor= 'None', markersize = 7.0, marker='o', label = 'Ref',antialiased=True)
#plt.plot(phi_ref,n_phi_hand,color = 'grey', linewidth=2.0, linestyle='--', label = 'Ref',antialiased=True)
plt.legend(loc=9,bbox_to_anchor=(0.5, -0.1), ncol=3, frameon=False,fontsize=labelfontsize+2)
#lg = plt.legend()
#lg.draw_frame(False)
#lg.loc(2)
plt.xlim([0,90])
plt.xlabel('Phi (degrees)')
plt.ylabel('Meridional shell force [N/m]')
plt.grid()
plt.tick_params(labelsize=labelfontsize)
plt.savefig('Simply_support_dome_n_phi_quads.png',bbox_inches="tight")




fig = plt.figure(3)
plt.plot(phi_andes,von_mises_andes, color = '#77B5FE', linewidth=3.0, label = 'ANDES-DKQ',antialiased=True)
#plt.plot(phi_dsg,von_mises_dsg, color = '#FF91A4', linestyle='--',linewidth=3.0, label = 'DSG',antialiased=True)
plt.plot(phi_ansys,von_mises_ansys,color = 'grey', linestyle='None', markerfacecolor= 'None', markersize = 7.0, marker='o', label = 'ANSYS',antialiased=True)
#plt.plot(disp_ref,load_ref,color = 'grey', linewidth=2.0, linestyle='--', label = 'Ref',antialiased=True)
plt.legend(loc=9,bbox_to_anchor=(0.5, -0.1), ncol=3, frameon=False,fontsize=labelfontsize+2)
#lg = plt.legend()
#lg.draw_frame(False)
#lg.loc(2)
plt.xlim([0,90])
plt.ylim([0,1000])
plt.xlabel('Phi (degrees)')
plt.ylabel('Von Mises mid-surface stress [kPa]')
plt.grid()
plt.tick_params(labelsize=labelfontsize)
plt.savefig('Simply_support_dome_von_mises_quads.png',bbox_inches="tight")














plt.show()

