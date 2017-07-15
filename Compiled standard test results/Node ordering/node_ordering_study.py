# -*- coding: utf-8 -*-
"""
Created on Fri Mar 17 18:37:12 2017

@author: Peter
"""

#===============================================
#
#       node ordering study
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
        'size'   : labelfontsize}

plt.rc('font', **font)
plt.rc('font', serif='Helvetica Neue') 
#plt.rcParams['font.family'] = 'Arial'
#plt.ticklabel_format(style='sci', axis='y', scilimits=(1e-4,10000))
#===============================================================================


#ref = []

elements = [2,8,16,32]
dsg_bottom = [0.73938,0.25177,0.23623,0.23108]
dsg_left = [0.30618,0.24366,0.2324,0.22932]
csdsg = [0.35066,0.25393,0.23702,0.23127]

#colors
ANDESDKQ = '#77B5FE'        #blue
ANDESBasic = '#C5AAF5'      #purple
KRATOSQUAD = '#79BFA1'      #green

DSG = '#FF91A4'             #salmon
DSGBasic = '#F5A352'        #orange
KRATOSTRI = '#BB7365'       #brown

CSDSG = '#85d5ca'           #key lime


#Plot graph

fig = plt.figure(1)
plt.plot(elements,dsg_bottom, color = DSG, linewidth=2.0, 
         markersize = 7.0, marker='o', markeredgewidth = 2.0, markeredgecolor = DSG, 
         markerfacecolor= 'None', label = 'DSG (bottom clamped)',antialiased=True)

plt.plot(elements,dsg_left, color = DSG, linewidth=2.0, linestyle='--',
         markersize = 7.0, marker='o', markeredgewidth = 2.0, markeredgecolor = DSG, 
         markerfacecolor= 'None', label = 'DSG (left clamped)',antialiased=True)


plt.plot(elements,csdsg, color = CSDSG, linewidth=2.0, 
         markersize = 7.0, marker='o', markeredgewidth = 2.0, markeredgecolor = CSDSG, 
         markerfacecolor= 'None', label = 'CS-DSG',antialiased=True)

plt.axhline(y=0.22058,color = 'grey', linestyle='--', linewidth=2.0, 
         label = 'Ref',antialiased=True)

plt.legend(loc=9,bbox_to_anchor=(0.5, -0.1), ncol=2, frameon=False,fontsize=labelfontsize+2)

plt.xlabel('Elements',fontsize=myfontsize)
plt.ylabel('|Displacement| [m]',fontsize=myfontsize)
plt.ylim([0,0.8])
plt.grid()
plt.tick_params(labelsize=labelfontsize)
plt.savefig('node_ordering_study.pdf',bbox_inches="tight")

CSDSG_Bmatrix_setup = 13.438 #ns
DSG_Bmatrix_setup = 12.000 #ns
CSDSGtime = []
DSGtime = []
CSDSG_error = []
DSG_bottom_error = []
DSG_left_error = []
for i in range(len(elements)):
    CSDSGtime.append(elements[i]*CSDSG_Bmatrix_setup)
    DSGtime.append(elements[i]*DSG_Bmatrix_setup)
    CSDSG_error.append((csdsg[i]-0.22058)/0.22058*100)
    DSG_bottom_error.append((dsg_bottom[i]-0.22058)/0.22058*100)
    DSG_left_error.append((dsg_left[i]-0.22058)/0.22058*100)

fig = plt.figure(2)
plt.semilogy(DSGtime,DSG_bottom_error, color = DSG, linewidth=2.0, 
         markersize = 7.0, marker='o', markeredgewidth = 2.0, markeredgecolor = DSG, 
         markerfacecolor= 'None', label = 'DSG (bottom clamped)',antialiased=True)

plt.semilogy(DSGtime,DSG_left_error, color = DSG, linewidth=2.0, linestyle='--',
         markersize = 7.0, marker='o', markeredgewidth = 2.0, markeredgecolor = DSG, 
         markerfacecolor= 'None', label = 'DSG (left clamped)',antialiased=True)


plt.semilogy(CSDSGtime,CSDSG_error, color = CSDSG, linewidth=2.0, 
         markersize = 7.0, marker='o', markeredgewidth = 2.0, markeredgecolor = CSDSG, 
         markerfacecolor= 'None', label = 'CS-DSG',antialiased=True)

plt.legend(loc=9,bbox_to_anchor=(0.5, -0.1), ncol=3, frameon=False,fontsize=labelfontsize+2)

plt.xlabel('Cumulative element shear B Matrix construction time [ns]',fontsize=myfontsize)
plt.ylabel('% Error',fontsize=myfontsize)
#plt.ylim([0,0.8])
plt.grid()
plt.tick_params(labelsize=labelfontsize)
plt.savefig('node_ordering_study_error.pdf',bbox_inches="tight")





















plt.show()