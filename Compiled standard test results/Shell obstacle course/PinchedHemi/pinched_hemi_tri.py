# -*- coding: utf-8 -*-
"""
Created on Fri Mar 17 18:37:12 2017

@author: Peter
"""

#===============================================
#
#       pinched hemisphere static test
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

dofs = []
disp_dsg = []
disp_dsg_basic = []
disp_kratos_tri = []
ref = []

with open("pinched_hemi_tri.txt", "r") as fol:
  for line in fol:
    line = line.split('\t')
    dofs.append(abs(float(line[0])))    
    disp_dsg.append(abs(float(line[1])))   
    disp_dsg_basic.append(abs(float(line[2])))
    disp_kratos_tri.append(abs(float(line[3])))   
    ref.append(abs(float(line[4])))   
fol.close()

#colors
ANDESDKQ = '#77B5FE'        #blue
ANDESBasic = '#C5AAF5'      #purple
KRATOSQUAD = '#79BFA1'      #green

DSG = '#FF91A4'             #salmon
DSGBasic = '#F5A352'        #orange
KRATOSTRI = '#BB7365'       #brown


#Plot graph

plt.plot(dofs,disp_dsg, color = DSG, linewidth=2.0, 
         markersize = 7.0, marker='o', markeredgewidth = 2.0, markeredgecolor = DSG, 
         markerfacecolor= 'None', label = 'DSG',antialiased=True)

plt.plot(dofs,disp_dsg_basic, color = DSGBasic, linewidth=2.0, 
         markersize = 7.0, marker='o', markeredgewidth = 2.0, markeredgecolor = DSGBasic, 
         markerfacecolor= 'None', label = 'Basic-T3',antialiased=True)

plt.plot(dofs,disp_kratos_tri, color = KRATOSTRI, linewidth=2.0, 
         markersize = 7.0, marker='o', markeredgewidth = 2.0, markeredgecolor = KRATOSTRI, 
         markerfacecolor= 'None', label = 'KRATOS T3',antialiased=True)

plt.axhline(y=ref[0],color = 'grey', linestyle='--', linewidth=2.0, 
         label = 'Ref',antialiased=True)

plt.legend(loc=9,bbox_to_anchor=(0.5, -0.1), ncol=2, frameon=False,fontsize=labelfontsize+2)

plt.xlabel('Elements')
plt.ylabel('|Displacement| [m]')
plt.ylim(ymin=0)
plt.grid()

plt.tick_params(labelsize=labelfontsize)
plt.savefig('pinched_hemi_tri_results.pdf',bbox_inches="tight")
plt.show()

#pylab.legend(loc=9, bbox_to_anchor=(0.5, -0.1), ncol=2)
