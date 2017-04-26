# -*- coding: utf-8 -*-
"""
Created on Fri Mar 17 18:37:12 2017

@author: Peter
"""

#===============================================
#
#       composite clamped cylinder static test
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

circumferential_divisions0 = []
disp_andes0 = []
disp_dsg0 = []
disp_reddyq40 = []
disp_reddyq90 = []

with open("0.txt", "r") as fol:
  for line in fol:
    line = line.split('\t')
    circumferential_divisions0.append((float(line[0])))    
    disp_andes0.append((float(line[1])))   
    disp_dsg0.append((float(line[2])))
    disp_reddyq40.append((float(line[3])))   
    disp_reddyq90.append((float(line[4]))) 
fol.close()




circumferential_divisions090 = []
disp_andes090 = []
disp_dsg090 = []
disp_reddyq4090 = []
disp_reddyq9090 = []

with open("0_90.txt", "r") as fol:
  for line in fol:
    line = line.split('\t')
    circumferential_divisions090.append((float(line[0])))    
    disp_andes090.append((float(line[1])))   
    disp_dsg090.append((float(line[2])))
    disp_reddyq4090.append((float(line[3])))   
    disp_reddyq9090.append((float(line[4]))) 
fol.close()



#colors
ANDESDKQ = '#77B5FE'        #blue
ANDESBasic = '#C5AAF5'      #purple
KRATOSQUAD = '#79BFA1'      #green

DSG = '#FF91A4'             #salmon
DSGBasic = '#F5A352'        #orange
KRATOSTRI = '#BB7365'       #brown


#Plot graph
fig = plt.figure(1)
plt.plot(circumferential_divisions0,disp_andes0, color = ANDESDKQ, linewidth=2.0, 
         markersize = 7.0, marker='o', markeredgewidth = 2.0, markeredgecolor = ANDESDKQ, 
         markerfacecolor= 'None', label = 'ANDES-DKQ',antialiased=True)

plt.plot(circumferential_divisions0,disp_dsg0, color = DSG, linewidth=2.0, 
         markersize = 7.0, marker='o', markeredgewidth = 2.0, markeredgecolor = DSG, 
         markerfacecolor= 'None', label = 'DSG',antialiased=True)

#plt.axhline(y=disp_reddyq4[0],color = 'grey', linestyle='-.', linewidth=2.0, 
         #label = 'ReddyQ4',antialiased=True)

plt.axhline(y=disp_reddyq90[0],color = 'grey', linestyle='--', linewidth=2.0, 
         label = 'Ref',antialiased=True)

plt.legend(loc=9,bbox_to_anchor=(0.5, -0.1), ncol=3, frameon=False,fontsize=labelfontsize+2)

plt.xlabel('Circumferential divisions',fontsize=myfontsize)
plt.ylabel('Displacement [m]',fontsize=myfontsize)
plt.title('1 ply layup [0]',fontsize=myfontsize)
plt.ylim([0,0.4])
plt.xlim([0,80])
plt.grid()
plt.tick_params(labelsize=labelfontsize)
plt.savefig('composite_clamped_cyl_0layup.pdf',bbox_inches="tight")












#Plot graph
fig = plt.figure(2)
plt.plot(circumferential_divisions090,disp_andes090, color = ANDESDKQ, linewidth=2.0, 
         markersize = 7.0, marker='o', markeredgewidth = 2.0, markeredgecolor = ANDESDKQ, 
         markerfacecolor= 'None', label = 'ANDES-DKQ',antialiased=True)

plt.plot(circumferential_divisions090,disp_dsg090, color = DSG, linewidth=2.0, 
         markersize = 7.0, marker='o', markeredgewidth = 2.0, markeredgecolor = DSG, 
         markerfacecolor= 'None', label = 'DSG',antialiased=True)

#plt.axhline(y=disp_reddyq4[0],color = 'grey', linestyle='-.', linewidth=2.0, 
         #label = 'ReddyQ4',antialiased=True)

plt.axhline(y=disp_reddyq9090[0],color = 'grey', linestyle='--', linewidth=2.0, 
         label = 'Ref',antialiased=True)

plt.legend(loc=9,bbox_to_anchor=(0.5, -0.1), ncol=3, frameon=False,fontsize=labelfontsize+2)

plt.xlabel('Circumferential divisions',fontsize=myfontsize)
plt.ylabel('Displacement [m]',fontsize=myfontsize)
plt.title('2 ply layup [0/90]',fontsize=myfontsize)
plt.ylim([0,0.2])
plt.xlim([0,80])
plt.grid()
plt.tick_params(labelsize=labelfontsize)
plt.savefig('composite_clamped_cyl_090layup.pdf',bbox_inches="tight")
















plt.show()
