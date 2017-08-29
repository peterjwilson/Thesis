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

dsg = [0.086254367, 0.086254367, 0.047556947]
csdsg = [0.047556954, 0.047556954,0.047556954]

#colors
ANDESDKQ = '#77B5FE'        #blue
ANDESBasic = '#C5AAF5'      #purple
KRATOSQUAD = '#79BFA1'      #green

DSG = '#FF91A4'             #salmon
DSGBasic = '#F5A352'        #orange
KRATOSTRI = '#BB7365'       #brown

CSDSG = '#85d5ca'           #key lime


#Plot graph
n_groups = 3
fig, ax = plt.subplots()
index = np.arange(n_groups)
bar_width = 0.35
opacity = 0.8
 
rects1 = plt.bar(index, dsg, bar_width,
                 alpha=opacity,
                 color=DSG,
                 label='DSG',antialiased=True)
 
rects2 = plt.bar(index + bar_width, csdsg, bar_width,
                 alpha=opacity,
                 color=CSDSG,
                 label='CS-DSG',antialiased=True)
 
plt.xlabel('Node ordering arrangement',fontsize=myfontsize)
plt.ylabel('|Displacement| [m]',fontsize=myfontsize)
plt.xticks(index + bar_width, ('1', '2', '3'))

plt.legend(loc=9,bbox_to_anchor=(0.5, -0.1), ncol=2, frameon=False,fontsize=labelfontsize+2)


#plt.ylim([0,0.8])
#plt.grid()
plt.tick_params(labelsize=labelfontsize)
plt.savefig('node_ordering_study_single_tri.pdf',bbox_inches="tight")

















plt.show()