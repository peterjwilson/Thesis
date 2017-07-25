# -*- coding: utf-8 -*-
"""
Created on Mon Dec  5 21:30:56 2016

@author: wilson
"""


#===============================================
#
#       open cylinder pullout
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



load_andes = [0]
disp_andes = [0]

disp_scale = 1 #m to mm

with open("load_andes.txt", "r") as fol:
  for line in fol:
    load_andes.append(abs(float(line))*4)      
fol.close()

with open("displacement_andes.txt", "r") as fod:
  for line in fod:
    disp_andes.append(abs(float(line)))         
fod.close()

load_kratos_quad = [0]
disp_kratos_quad = [0]
with open("load_kratos_quad.txt", "r") as fol:
  for line in fol:
    load_kratos_quad.append(abs(float(line))*4)      
fol.close()

with open("displacement_kratos_quad.txt", "r") as fod:
  for line in fod:
    disp_kratos_quad.append(abs(float(line)))         
fod.close()

#https://www.researchgate.net/publication/222423070_Popular_benchmark_problems_for_geometric_nonlinear_analysis_of_shells
load_ref = [0]
disp_ref = [0]
max_load_ref = 40000
with open("load_benchmark.txt", "r") as fol:
  for line in fol:
    load_ref.append(abs(float(line))*max_load_ref)      
fol.close()

with open("displacement_benchmark.txt", "r") as fod:
  for line in fod:
    disp_ref.append(abs(float(line))/disp_scale)         
fod.close()


#custom_edit

#colors
ANDESDKQ = '#77B5FE'        #blue
ANDESBasic = '#C5AAF5'      #purple
KRATOSQUAD = '#79BFA1'      #green

DSG = '#FF91A4'             #salmon
DSGBasic = '#F5A352'        #orange
KRATOSTRI = '#BB7365'       #brown

plt.plot(disp_andes,load_andes, color = '#77B5FE', linewidth=3.0, label = 'Kratos thin quad',antialiased=True)
plt.plot(disp_kratos_quad,load_kratos_quad, color = KRATOSQUAD, linestyle='--', linewidth=3.0, label = 'Kratos thick quad',antialiased=True)
plt.plot(disp_ref,load_ref,color = 'grey', linestyle='None', markerfacecolor= 'None', markersize = 7.0, marker='o', label = 'Reference',antialiased=True)
#plt.plot(disp_ref,load_ref,color = 'grey', linewidth=2.0, linestyle='--', label = 'Ref',antialiased=True)
plt.legend(loc=9,bbox_to_anchor=(0.5, -0.1), ncol=3, frameon=False,fontsize=labelfontsize+2)
#lg = plt.legend()
#lg.draw_frame(False)
#lg.loc(2)
plt.xlabel('Displacement [m]')
plt.ylabel('Load [N]')
plt.grid()
plt.tick_params(labelsize=labelfontsize)
plt.savefig('Load_displacement_curve_open_cylinder_pullout_quad.png',bbox_inches="tight")
plt.show()

