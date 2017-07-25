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
disp_andes = []
disp_andes_basic = []
disp_kratos_quad = []
ref = []

with open("cyl_quad_struc.txt", "r") as fol:
  for line in fol:
    line = line.split('\t')
    dofs.append(abs(float(line[0])))    
    disp_andes.append(abs(float(line[1])))   
    disp_andes_basic.append(abs(float(line[2])))
    disp_kratos_quad.append(abs(float(line[3])))   
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

plt.plot(dofs,disp_andes, color = ANDESDKQ, linewidth=2.0, 
         markersize = 7.0, marker='o', markeredgewidth = 2.0, markeredgecolor = ANDESDKQ, 
         markerfacecolor= 'None', label = 'Kratos thin quad',antialiased=True)

#plt.plot(dofs,disp_andes_basic, color = ANDESBasic, linewidth=2.0, 
#         markersize = 7.0, marker='o', markeredgewidth = 2.0, markeredgecolor = ANDESBasic, 
#         markerfacecolor= 'None', label = 'Basic-DKQ',antialiased=True)

plt.plot(dofs,disp_kratos_quad, color = KRATOSQUAD, linewidth=2.0, 
         markersize = 7.0, marker='o', markeredgewidth = 2.0, markeredgecolor = KRATOSQUAD, 
         markerfacecolor= 'None', label = 'Kratos thick quad',antialiased=True)

plt.axhline(y=ref[0],color = 'grey', linestyle='--', linewidth=2.0, 
         label = 'Reference',antialiased=True)

plt.legend(loc=9,bbox_to_anchor=(0.5, -0.1), ncol=3, frameon=False,fontsize=labelfontsize+2)

plt.xlabel('Elements',fontsize=myfontsize)
plt.ylabel('|Displacement| [m]',fontsize=myfontsize)
plt.ylim([0,2e-5])
plt.grid()
plt.tick_params(labelsize=labelfontsize)
plt.savefig('pinched_cyl_structured_quad_results.png',bbox_inches="tight")
plt.show()

#pylab.legend(loc=9, bbox_to_anchor=(0.5, -0.1), ncol=2)
