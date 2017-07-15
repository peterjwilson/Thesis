# -*- coding: utf-8 -*-
"""
Created on Fri Mar 17 18:37:12 2017

@author: Peter
"""

#===============================================
#
#       prinched cylinder static test
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
plt.ticklabel_format(style='sci', axis='y', scilimits=(1e-4,10000))
#===============================================================================

dofs = []
disp_dsg = []
disp_csdsg = []
disp_kratos_tri = []
ref = []

with open("cyl_tri_struc.txt", "r") as fol:
  for line in fol:
    line = line.split('\t')
    dofs.append(abs(float(line[0])))    
    disp_dsg.append(abs(float(line[1])))   
    disp_csdsg.append(abs(float(line[2])))
    ref.append(abs(float(line[3])))   
fol.close()

#colors
ANDESDKQ = '#77B5FE'        #blue
ANDESBasic = '#C5AAF5'      #purple
KRATOSQUAD = '#79BFA1'      #green

DSG = '#FF91A4'             #salmon
DSGBasic = '#F5A352'        #orange
KRATOSTRI = '#BB7365'       #brown

CSDSG = '#85d5ca'           #key lime

#Plot graph

plt.plot(dofs,disp_dsg, color = DSG, linewidth=2.0, 
         markersize = 7.0, marker='o', markeredgewidth = 2.0, markeredgecolor = DSG, 
         markerfacecolor= 'None', label = 'DSG',antialiased=True)

plt.plot(dofs,disp_csdsg, color = CSDSG, linewidth=2.0, 
         markersize = 7.0, marker='o', markeredgewidth = 2.0, markeredgecolor = CSDSG, 
         markerfacecolor= 'None', label = 'CS-DSG',antialiased=True)

plt.axhline(y=ref[0],color = 'grey', linestyle='--', linewidth=2.0, 
         label = 'Ref',antialiased=True)

plt.legend(loc=9,bbox_to_anchor=(0.5, -0.1), ncol=3, frameon=False,fontsize=labelfontsize+2)

plt.xlabel('Elements',fontsize=myfontsize)
plt.ylabel('|Displacement| [m]',fontsize=myfontsize)
plt.ylim([0,2e-5])
plt.grid()
plt.tick_params(labelsize=labelfontsize)
plt.savefig('pinched_cyl_structured_tri_results_csdsg.pdf',bbox_inches="tight")
plt.show()

#pylab.legend(loc=9, bbox_to_anchor=(0.5, -0.1), ncol=2)
