# -*- coding: utf-8 -*-
"""
Created on Sat May 20 20:10:33 2017

@author: Peter
"""

import numpy as np
import matplotlib.pyplot as plt

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

a = 1
b = 1
EA = 1
P = 1

L = np.sqrt(2)

def calcK(disp):
    return EA/L**3*(3*disp**2 - 6*b*disp+2*b**2)
    
def calcEgl(disp):
    return (disp**2 - 2*b*disp)/2/L**2


u_lim = 2.5
u_div = 100
u = []
lamda = []
K = []
for i in range(u_div):
    u.append(i*u_lim/u_div)
    u_i = u[i]
    lamda.append(EA/L**3*(u_i**3 - 3*b*u_i**2 + 2*b**2*u_i)/P)
    K.append(calcK(u_i))

u_c1 = 0.423
u_c2 = 1.577
lamda_c1 = 0.136
lamda_c2 = -0.136

lamda_lpb = 0.05
u_lpb = 0.0801
e_lpb = calcEgl(u_lpb)
Kg_lpb = 2*EA/L*e_lpb
K_e = calcK(0)

crit_lim = -K_e/Kg_lpb

lamda_lpb = [0,0.354,0.354]
u_lpb = [0,0.354/K_e,2.5]

    
##77B5FE = nice blue
fig = plt.figure(1)
#plt.plot(phi_andes,n_theta_andes, color = '#77B5FE', linewidth=3.0, label = 'ANDES-DKQ',antialiased=True)
#plt.plot(phi_dsg,n_theta_dsg, color = '#FF91A4', linestyle='--',linewidth=3.0, label = 'DSG',antialiased=True)
plt.plot(u,K,color = 'blue', label = 'Ref',antialiased=True)
plt.plot(u,lamda,color = 'grey', label = 'Ref',antialiased=True)
plt.plot(u_lpb,lamda_lpb,color = 'green', label = 'Ref',antialiased=True)
plt.plot(u_c1,lamda_c1,color = 'red', linestyle='None', markerfacecolor= 'None',markeredgecolor= 'red', markersize = 7.0, marker='o', label = 'Ref',antialiased=True)
plt.plot(u_c2,lamda_c2,color = 'red', linestyle='None', markerfacecolor= 'None',markeredgecolor= 'red', markersize = 7.0, marker='o', label = 'Ref',antialiased=True)
#plt.plot(phi_ref,n_theta_hand,color = 'grey', linewidth=2.0, linestyle='--', label = 'Ref',antialiased=True)
#plt.legend(loc=9,bbox_to_anchor=(0.5, -0.1), ncol=3, frameon=False,fontsize=labelfontsize+2)
#lg = plt.legend()
#lg.draw_frame(False)
#lg.loc(2)
#plt.xlim([0,90])
plt.xlabel('Displacement')
plt.ylabel('Load factor')
plt.grid()
plt.tick_params(labelsize=labelfontsize)
#plt.savefig('Simply_support_dome_n_theta.pdf',bbox_inches="tight")

plt.show()