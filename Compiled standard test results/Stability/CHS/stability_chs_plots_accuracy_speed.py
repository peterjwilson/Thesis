# -*- coding: utf-8 -*-
"""
Created on Fri Mar 17 18:37:12 2017

@author: Peter
"""

#===============================================
#
#       stability chs plots
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

DSG_r = [92.33,13.57]
Basic_T3 = [96.94,21.04]
KRATOS_T3 = [125.59,10.12]

ANDES_DKQ = [251.59,10.99]
BASIC_DKQ = [231.87,12.99]
kratos_q4 = [264.41,	12.18]


#colors
ANDESDKQ = '#77B5FE'        #blue
ANDESBasic = '#C5AAF5'      #purple
KRATOSQUAD = '#79BFA1'      #green

DSG = '#FF91A4'             #salmon
DSGBasic = '#F5A352'        #orange
KRATOSTRI = '#BB7365'       #brown


#Plot graph ------------------------------------------------------------------

fig = plt.figure(1)
plt.plot(ANDES_DKQ[0],ANDES_DKQ[1],
         markeredgecolor = ANDESDKQ, linestyle='None', markerfacecolor= 'None', 
         markersize = 15.0, marker='s', markeredgewidth = 2.0,
         label = 'ANDES-DKQ',antialiased=True)

plt.plot(BASIC_DKQ[0],BASIC_DKQ[1],
         markeredgecolor = ANDESBasic, linestyle='None', markerfacecolor= 'None', 
         markersize = 15.0, marker='s', markeredgewidth = 2.0,
         label = 'Basic-DKQ',antialiased=True)

plt.plot(kratos_q4[0],kratos_q4[1],
         markeredgecolor = KRATOSQUAD, linestyle='None', markerfacecolor= 'None', 
         markersize = 15.0, marker='s', markeredgewidth = 2.0,
         label = 'KRATOS Q4',antialiased=True)

plt.plot(DSG_r[0],DSG_r[1],
         markeredgecolor = DSG, linestyle='None', markerfacecolor= 'None', 
         markersize = 15.0, marker='^', markeredgewidth = 2.0,
         label = 'DSG',antialiased=True)

plt.plot(Basic_T3[0],Basic_T3[1],
         markeredgecolor = DSGBasic, linestyle='None', markerfacecolor= 'None', 
         markersize = 15.0, marker='^', markeredgewidth = 2.0,
         label = 'Basic-T3',antialiased=True)

plt.plot(KRATOS_T3[0],KRATOS_T3[1],
         markeredgecolor = KRATOSTRI, linestyle='None', markerfacecolor= 'None', 
         markersize = 15.0, marker='^', markeredgewidth = 2.0,
         label = 'KRATOS T3',antialiased=True)

plt.legend(loc=9,bbox_to_anchor=(0.5, -0.1), ncol=3, frameon=False,fontsize=labelfontsize+2)
#plt.legend(loc = 1,frameon=False,fontsize=labelfontsize)
plt.xlabel('Element construction time [ns]',fontsize=myfontsize)
plt.ylabel('|Critical load| [MN]',fontsize=myfontsize)
plt.ylim([9,25])
plt.xlim([0,350])
plt.grid()
plt.tick_params(labelsize=labelfontsize)
#plt.savefig('stability_chs_ACCURACY_COST.pdf',bbox_inches="tight")




fig = plt.figure(2)
plt.plot(DSG_r[0],DSG_r[1],
         markeredgecolor = DSG, linestyle='None', markerfacecolor= 'None', 
         markersize = 15.0, marker='^', markeredgewidth = 2.0,
         label = 'DSG',antialiased=True)

plt.plot(Basic_T3[0],Basic_T3[1],
         markeredgecolor = DSGBasic, linestyle='None', markerfacecolor= 'None', 
         markersize = 15.0, marker='^', markeredgewidth = 2.0,
         label = 'Basic-T3',antialiased=True)

plt.plot(KRATOS_T3[0],KRATOS_T3[1],
         markeredgecolor = KRATOSTRI, linestyle='None', markerfacecolor= 'None', 
         markersize = 15.0, marker='^', markeredgewidth = 2.0,
         label = 'KRATOS T3',antialiased=True)

plt.legend(loc=9,bbox_to_anchor=(0.5, -0.1), ncol=3, frameon=False,fontsize=labelfontsize+2)
#plt.legend(loc = 1,frameon=False,fontsize=labelfontsize)
plt.xlabel('Element construction time [ns]',fontsize=myfontsize)
plt.ylabel('|Critical load| [MN]',fontsize=myfontsize)
plt.ylim([9,22])
plt.xlim([0,200])
plt.grid()
plt.tick_params(labelsize=labelfontsize)
#plt.savefig('stability_chs_ACCURACY_COST_tri.pdf',bbox_inches="tight")



fig = plt.figure(3)
plt.plot(ANDES_DKQ[0],ANDES_DKQ[1],
         markeredgecolor = ANDESDKQ, linestyle='None', markerfacecolor= 'None', 
         markersize = 15.0, marker='s', markeredgewidth = 2.0,
         label = 'ANDES-DKQ',antialiased=True)

plt.plot(BASIC_DKQ[0],BASIC_DKQ[1],
         markeredgecolor = ANDESBasic, linestyle='None', markerfacecolor= 'None', 
         markersize = 15.0, marker='s', markeredgewidth = 2.0,
         label = 'Basic-DKQ',antialiased=True)

plt.plot(kratos_q4[0],kratos_q4[1],
         markeredgecolor = KRATOSQUAD, linestyle='None', markerfacecolor= 'None', 
         markersize = 15.0, marker='s', markeredgewidth = 2.0,
         label = 'KRATOS Q4',antialiased=True)

plt.legend(loc=9,bbox_to_anchor=(0.5, -0.1), ncol=3, frameon=False,fontsize=labelfontsize+2)
#plt.legend(loc = 1,frameon=False,fontsize=labelfontsize)
plt.xlabel('Element construction time [ns]',fontsize=myfontsize)
plt.ylabel('|Critical load| [MN]',fontsize=myfontsize)
plt.ylim([10.5,13.5])
plt.xlim([200,300])
plt.grid()
plt.tick_params(labelsize=labelfontsize)
plt.savefig('stability_chs_ACCURACY_COST_quad.pdf',bbox_inches="tight")





plt.show()

