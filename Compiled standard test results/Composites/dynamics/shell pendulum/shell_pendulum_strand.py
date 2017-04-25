# -*- coding: utf-8 -*-
"""
Created on Fri Mar 17 18:37:12 2017

@author: Peter
"""

#===============================================
#
#       swinging plate
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


time_kratos = [0]
composite_thin_quad_pendulum_lumped = [0]
with open("composite_thin_quad_pendulum_lumped.txt", "r") as fol:
  for line in fol:
    line = line.split(' ')
    time_kratos.append((float(line[0])))    
    composite_thin_quad_pendulum_lumped.append((float(line[1])))   
fol.close()

#thin_quad_consistent = [0]
#with open("thin_quad_consistent.txt", "r") as fol:
#  for line in fol:
#    line = line.split(' ')
#    #time_kratos.append((float(line[0])))    
#    thin_quad_consistent.append((float(line[1])))   
#fol.close()


composite_thick_tri_pendulum_lumped = [0]
with open("composite_thick_tri_pendulum_lumped.txt", "r") as fol:
  for line in fol:
    line = line.split(' ')
    #time_kratos.append((float(line[0])))    
    composite_thick_tri_pendulum_lumped.append((float(line[1])))   
fol.close()



#thick_tri_consistent = [0]
#with open("thick_tri_consistent.txt", "r") as fol:
#  for line in fol:
#    line = line.split(' ')
#    #time_kratos.append((float(line[0])))    
#    thick_tri_consistent.append((float(line[1])))   
#fol.close()






time_strand = [0]
strand_composite_pendulum_lumped = [0]
counter = 0
with open("strand_composite_pendulum_lumped.txt", "r") as fol:
  for line in fol:
    counter += 1
    if counter%4 == 0:
        line = line.split('\t')
        time_strand.append((float(line[1])))    
        strand_composite_pendulum_lumped.append((float(line[2])))   
fol.close()

#time_strand_con = [0]
#strand_shell_pendulum_consistent = [0]
#counter = 0
#with open("strand_shell_pendulum_consistent.txt", "r") as fol:
#  for line in fol:
#    counter += 1
#    if counter%4 == 2:
#        line = line.split('\t') 
#        #print(line)
#        time_strand_con.append((float(line[1])))   
#        strand_shell_pendulum_consistent.append((float(line[2])))   
#fol.close()  

##77B5FE = nice blue
##plt.figure(figsize=(5.82,3.5))
#fig = plt.figure(1)
#plt.plot(time_kratos,thin_quad_consistent, color = '#77B5FE', linewidth=2.0, label = 'ANDES-DKQ (Consistent)',antialiased=True)
#
#plt.plot(time_kratos,thick_tri_consistent, color = '#FF91A4', linestyle='--', linewidth=2.0, label = 'DSG (Consistent)',antialiased=True)
#
#plt.plot(time_strand,strand_shell_pendulum_lumped,color = 'grey', linestyle='None', markerfacecolor= 'None', markersize = 7.0, marker='o', label = 'Strand7 (Lumped)',antialiased=True)
#
#plt.plot(time_strand_con,strand_shell_pendulum_consistent,color = 'grey', linestyle='None', markerfacecolor= 'None', markersize = 7.0, marker='^', label = 'Strand7 (Consistent)',antialiased=True)
##plt.plot(disp_ref,load_ref,color = 'grey', linewidth=2.0, linestyle='--', label = 'Ref',antialiased=True)
#plt.legend(loc=9,bbox_to_anchor=(0.5, -0.1), ncol=2, frameon=False,fontsize=labelfontsize+2)
##lg = plt.legend()
##lg.draw_frame(False)
##lg.loc(2)
#plt.xlabel('Time [s]')
#plt.ylabel('Vertical displacement [m]')
#plt.xlim([0,2.5])
#plt.grid()
#plt.tick_params(labelsize=labelfontsize)
#plt.savefig('shell_pendulum_consistent.pdf',bbox_inches="tight")





fig = plt.figure(2)
plt.plot(time_kratos,composite_thin_quad_pendulum_lumped, color = '#77B5FE', linewidth=2.0, label = 'ANDES-DKQ (Lumped)',antialiased=True)

plt.plot(time_kratos,composite_thick_tri_pendulum_lumped, color = '#FF91A4', linestyle='--', linewidth=2.0, label = 'DSG (Lumped)',antialiased=True)

plt.plot(time_strand,strand_composite_pendulum_lumped,color = 'grey', linestyle='None', markerfacecolor= 'None', markersize = 7.0, marker='o', label = 'Strand7 (Lumped)',antialiased=True)

#plt.plot(time_strand_con,strand_shell_pendulum_consistent,color = 'grey', linestyle='None', markerfacecolor= 'None', markersize = 7.0, marker='^', label = 'Strand7 (Consistent)',antialiased=True)
#plt.plot(disp_ref,load_ref,color = 'grey', linewidth=2.0, linestyle='--', label = 'Ref',antialiased=True)
plt.legend(loc=9,bbox_to_anchor=(0.5, -0.1), ncol=2, frameon=False,fontsize=labelfontsize+2)
#lg = plt.legend()
#lg.draw_frame(False)
#lg.loc(2)
plt.xlabel('Time [s]')
plt.ylabel('Vertical displacement [m]')
plt.xlim([0,2.5])
plt.grid()
plt.tick_params(labelsize=labelfontsize)
plt.savefig('composite_shell_pendulum_lumped.pdf',bbox_inches="tight")













plt.show()

