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

thick = []
andes_cross_2 = []
dsg_cross_2 = []
ref_cross_2 = []

with open("cross2ply.txt", "r") as fol:
  for line in fol:
    line = line.split('\t')
    thick.append((float(line[0])))  
    andes_cross_2.append((float(line[1])))    
    dsg_cross_2.append((float(line[2])))   
    ref_cross_2.append((float(line[2])))   
fol.close()

fig = plt.figure(1)
plt.plot(thick,andes_cross_2, color = '#77B5FE', linewidth=2.0, label = 'ANDES-DKQ',antialiased=True)
plt.plot(thick,andes_cross_2, color = '#FF91A4', linestyle='--', linewidth=2.0, label = 'DSG',antialiased=True)
#plt.plot(time_strand,disp_strand,color = 'grey', linestyle='None', markerfacecolor= 'None', markersize = 3.0,  marker='o', label = 'Ref',antialiased=True)
plt.plot(thick,ref_cross_2,color = 'grey', linestyle='None', markerfacecolor= 'None', markersize = 7.0, marker='o', label = 'Ref',antialiased=True)
#plt.plot(disp_ref,load_ref,color = 'grey', linewidth=2.0, linestyle='--', label = 'Ref',antialiased=True)
plt.legend(loc=9,bbox_to_anchor=(0.5, -0.1), ncol=3, frameon=False,fontsize=labelfontsize+2)
#lg = plt.legend()
#lg.draw_frame(False)
#lg.loc(2)
plt.title('2 ply cross layup [0/90]',fontsize=myfontsize)
plt.xlabel('Shell thickness')
plt.ylabel('Vertical displacement')
#plt.xlim([0,2.5])
plt.grid()

plt.tick_params(labelsize=labelfontsize)
plt.savefig('cross2ply.pdf',bbox_inches="tight")


andes_cross_10 = []
dsg_cross_10 = []
ref_cross_10 = []

with open("cross10ply.txt", "r") as fol:
  for line in fol:
    line = line.split('\t')
    #thick.append((float(line[0])))  
    andes_cross_10.append((float(line[1])))    
    dsg_cross_10.append((float(line[2])))   
    ref_cross_10.append((float(line[2])))   
fol.close()

fig = plt.figure(2)
plt.plot(thick,andes_cross_10, color = '#77B5FE', linewidth=2.0, label = 'ANDES-DKQ',antialiased=True)
plt.plot(thick,dsg_cross_10, color = '#FF91A4', linestyle='--', linewidth=2.0, label = 'DSG',antialiased=True)
#plt.plot(time_strand,disp_strand,color = 'grey', linestyle='None', markerfacecolor= 'None', markersize = 3.0,  marker='o', label = 'Ref',antialiased=True)
plt.plot(thick,ref_cross_10,color = 'grey', linestyle='None', markerfacecolor= 'None', markersize = 7.0, marker='o', label = 'Ref',antialiased=True)
#plt.plot(disp_ref,load_ref,color = 'grey', linewidth=2.0, linestyle='--', label = 'Ref',antialiased=True)
plt.legend(loc=9,bbox_to_anchor=(0.5, -0.1), ncol=3, frameon=False,fontsize=labelfontsize+2)
#lg = plt.legend()
#lg.draw_frame(False)
#lg.loc(2)
plt.title('10 ply cross layup [0/90/0/90/...]',fontsize=myfontsize)
plt.xlabel('Shell thickness')
plt.ylabel('Vertical displacement')
#plt.xlim([0,2.5])
plt.grid()

plt.tick_params(labelsize=labelfontsize)
plt.savefig('cross10ply.pdf',bbox_inches="tight")



andes_angle_2 = []
dsg_angle_2 = []
ref_angle_2 = []

with open("angle2ply.txt", "r") as fol:
  for line in fol:
    line = line.split('\t')
    #thick.append((float(line[0])))  
    andes_angle_2.append((float(line[1])))    
    dsg_angle_2.append((float(line[2])))   
    ref_angle_2.append((float(line[2])))   
fol.close()

fig = plt.figure(3)
plt.plot(thick,andes_angle_2, color = '#77B5FE', linewidth=2.0, label = 'ANDES-DKQ',antialiased=True)
plt.plot(thick,dsg_angle_2, color = '#FF91A4', linestyle='--', linewidth=2.0, label = 'DSG',antialiased=True)
#plt.plot(time_strand,disp_strand,color = 'grey', linestyle='None', markerfacecolor= 'None', markersize = 3.0,  marker='o', label = 'Ref',antialiased=True)
plt.plot(thick,ref_angle_2,color = 'grey', linestyle='None', markerfacecolor= 'None', markersize = 7.0, marker='o', label = 'Ref',antialiased=True)
#plt.plot(disp_ref,load_ref,color = 'grey', linewidth=2.0, linestyle='--', label = 'Ref',antialiased=True)
plt.legend(loc=9,bbox_to_anchor=(0.5, -0.1), ncol=3, frameon=False,fontsize=labelfontsize+2)
#lg = plt.legend()
#lg.draw_frame(False)
#lg.loc(2)
plt.title('2 ply angle layup [-45/45]',fontsize=myfontsize)
plt.xlabel('Shell thickness')
plt.ylabel('Vertical displacement')
#plt.xlim([0,2.5])
plt.grid()

plt.tick_params(labelsize=labelfontsize)
plt.savefig('angle2ply.pdf',bbox_inches="tight")





andes_angle_10 = []
dsg_angle_10 = []
ref_angle_10 = []

with open("angle10ply.txt", "r") as fol:
  for line in fol:
    line = line.split('\t')
    #thick.append((float(line[0])))  
    andes_angle_10.append((float(line[1])))    
    dsg_angle_10.append((float(line[2])))   
    ref_angle_10.append((float(line[2])))   
fol.close()
#
fig = plt.figure(4)
plt.plot(thick,andes_angle_10, color = '#77B5FE', linewidth=2.0, label = 'ANDES-DKQ',antialiased=True)
plt.plot(thick,dsg_angle_10, color = '#FF91A4', linestyle='--', linewidth=2.0, label = 'DSG',antialiased=True)
#plt.plot(time_strand,disp_strand,color = 'grey', linestyle='None', markerfacecolor= 'None', markersize = 3.0,  marker='o', label = 'Ref',antialiased=True)
plt.plot(thick,ref_angle_10,color = 'grey', linestyle='None', markerfacecolor= 'None', markersize = 7.0, marker='o', label = 'Ref',antialiased=True)
#plt.plot(disp_ref,load_ref,color = 'grey', linewidth=2.0, linestyle='--', label = 'Ref',antialiased=True)
plt.legend(loc=9,bbox_to_anchor=(0.5, -0.1), ncol=3, frameon=False,fontsize=labelfontsize+2)
#lg = plt.legend()
#lg.draw_frame(False)
#lg.loc(2)
plt.title('10 ply angle layup [-45/45/-45/45/...]',fontsize=myfontsize)
plt.xlabel('Shell thickness')
plt.ylabel('Vertical displacement')
#plt.xlim([0,2.5])
plt.grid()

plt.tick_params(labelsize=labelfontsize)
plt.savefig('angle10ply.pdf',bbox_inches="tight")











#
#
#
#
#fig = plt.figure(1)
##plt.plot(thick,andes_cross_2, color = '#77B5FE', linewidth=2.0, label = 'ANDES-DKQ',antialiased=True)
##plt.plot(thick,dsg, color = '#FF91A4', linestyle='--', linewidth=2.0, label = 'DSG',antialiased=True)
#
#plt.plot(thick,andes_cross_2,markeredgecolor = '#77B5FE', linestyle='None',
#         markerfacecolor= 'None', markersize = 14.0, marker='^', 
#         markeredgewidth=2.0, label = 'ANDES-DKQ',antialiased=True)
#
#plt.plot(thick,dsg_cross_2,markeredgecolor = '#FF91A4', linestyle='None', 
#         markeredgewidth=2.0, markerfacecolor= 'None', markersize = 14.0, 
#         marker='^', label = 'DSG',antialiased=True)
#
#plt.plot(thick,ref_cross_2,markeredgecolor = 'grey', linestyle='None', 
#         markeredgewidth=2.0,markerfacecolor= 'None', markersize = 14.0, 
#         marker='^', label = 'Ref',antialiased=True)
#
#plt.plot(thick,andes_angle_2,markeredgecolor = '#77B5FE', linestyle='None',
#         markerfacecolor= 'None', markersize = 14.0, marker='s', 
#         markeredgewidth=2.0, label = 'ANDES-DKQ',antialiased=True)
#
#plt.plot(thick,dsg_angle_2,markeredgecolor = '#FF91A4', linestyle='None', 
#         markeredgewidth=2.0, markerfacecolor= 'None', markersize = 14.0, 
#         marker='s', label = 'DSG',antialiased=True)
#
#plt.plot(thick,ref_angle_2,markeredgecolor = 'grey', linestyle='None', 
#         markeredgewidth=2.0,markerfacecolor= 'None', markersize = 14.0, 
#         marker='s', label = 'Ref',antialiased=True)
#
#
##plt.plot(disp_ref,load_ref,color = 'grey', linewidth=2.0, linestyle='--', label = 'Ref',antialiased=True)
#plt.legend(loc=9,bbox_to_anchor=(0.5, -0.1), ncol=3, frameon=False,fontsize=labelfontsize+2)
##lg = plt.legend()
##lg.draw_frame(False)
##lg.loc(2)
#plt.title('10 ply angle layup [-45/45/-45/45/...]',fontsize=myfontsize)
#plt.xlabel('Shell thickness')
#plt.ylabel('Vertical displacement')
##plt.xlim([0,2.5])
#plt.grid()
#
#plt.tick_params(labelsize=labelfontsize)
#plt.savefig('scordelis_composite_2ply.pdf',bbox_inches="tight")





plt.show()
