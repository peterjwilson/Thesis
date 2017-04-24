# -*- coding: utf-8 -*-
"""
Created on Fri Apr 14 14:40:14 2017

@author: Peter
"""

#===============================================
#
#       simply supported plate analysis
#
#===============================================



import matplotlib.pyplot as plt
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
#===============================================================================

import numpy as np
import sympy as sp

      
      
# -----------------------------------------------------------------------------
#       READ KRATOS THRU THICKNESS RESULTS
# -----------------------------------------------------------------------------  

kratos_thru_z = [0.5,0.25,0.25,0,0,-0.25,-0.25,-0.5]
ticks =[-0.5,-0.25,0,0.25,0.5]

quad_thru_s_xx = []
with open("quad_thru_s_xx.txt", "r") as kratos_file:
  for line in kratos_file:
      line = line.split('\t')
      quad_thru_s_xx.append(float(line[0]))   
      
quad_thru_s_yy = []
with open("quad_thru_s_yy.txt", "r") as kratos_file:
  for line in kratos_file:
      line = line.split('\t')
      quad_thru_s_yy.append(float(line[0]))   
 
quad_thru_s_xy = []
with open("quad_thru_s_xy.txt", "r") as kratos_file:
  for line in kratos_file:
      line = line.split('\t')
      quad_thru_s_xy.append(float(line[0]))        

quad_thru_tsai = []
with open("quad_thru_tsai.txt", "r") as kratos_file:
  for line in kratos_file:
      line = line.split('\t')
      quad_thru_tsai.append(float(line[0]))           
          
# Thick tri
          
          
tri_thru_s_xx = []
with open("tri_thru_s_xx.txt", "r") as kratos_file:
  for line in kratos_file:
      line = line.split('\t')
      tri_thru_s_xx.append(float(line[0]))    

tri_thru_s_yy = []
with open("tri_thru_s_yy.txt", "r") as kratos_file:
  for line in kratos_file:
      line = line.split('\t')
      tri_thru_s_yy.append(float(line[0]))    
 
tri_thru_s_xy = []
with open("tri_thru_s_xy.txt", "r") as kratos_file:
  for line in kratos_file:
      line = line.split('\t')
      tri_thru_s_xy.append(float(line[0]))    
      
tri_thru_tsai = []
with open("tri_thru_tsai.txt", "r") as kratos_file:
  for line in kratos_file:
      line = line.split('\t')
      tri_thru_tsai.append(float(line[0]))   
          
      
# Reference thru tsai - from Strand7
strand_thru_tsai = []
with open("strand_thru_tsai.txt", "r") as kratos_file:
  for line in kratos_file:
      line = line.split('\t')
      strand_thru_tsai.append(float(line[0])) 
      
      
      
# -----------------------------------------------------------------------------
#       PLOT GRAPHS
# -----------------------------------------------------------------------------         
          









# Stress XX thru thickness @ plate center
fig = plt.figure(1)

ref_z = [0.5,0.25,0.25,-0.25,-0.25,-0.5]
ref_val =[44214,44214,5892,5892,44214,44214]
plt.plot(quad_thru_s_xx,kratos_thru_z, color = '#77B5FE', linewidth=3.0, label = 'ANDES-DKQ',antialiased=True)
plt.plot(tri_thru_s_xx,kratos_thru_z, color = '#FF91A4', linewidth=3.0, label = 'DSG',antialiased=True)
plt.plot(ref_val,ref_z,color = 'grey', linestyle='None', markerfacecolor= 'None', markersize = 7.0, marker='o', label = 'Ref',antialiased=True)
#plt.plot(disp_ref,load_ref,color = 'grey', linewidth=2.0, linestyle='--', label = 'Ref',antialiased=True)
plt.legend(loc=9,bbox_to_anchor=(0.5, -0.1), ncol=3, frameon=False,fontsize=labelfontsize+2)
#plt.legend()
#lg = plt.legend()
#lg.draw_frame(False)
#lg.loc(2)
plt.xlim([0,50000])
plt.ylim([-0.75,0.75])
plt.yticks(ticks)
plt.ylabel('Z coordinate = z/h',fontsize=myfontsize)
plt.xlabel('Stress_XX',fontsize=myfontsize)
plt.grid()
plt.tick_params(labelsize=labelfontsize)
plt.savefig('nasa3_thru_s_xx.pdf',bbox_inches="tight")
#
#
#
#
# Stress YY thru thickness @ plate center
fig = plt.figure(2)
ref_z = [0.5,0.25,0.25,-0.25,-0.25,-0.5]
ref_val =[-48,-48,66,66,-48,-48]
plt.plot(quad_thru_s_yy,kratos_thru_z, color = '#77B5FE', linewidth=3.0, label = 'ANDES-DKQ',antialiased=True)
plt.plot(tri_thru_s_yy,kratos_thru_z, color = '#FF91A4', linewidth=3.0, label = 'DSG',antialiased=True)
plt.plot(ref_val,ref_z,color = 'grey', linestyle='None', markerfacecolor= 'None', markersize = 7.0, marker='o', label = 'Ref',antialiased=True)
#plt.plot(disp_ref,load_ref,color = 'grey', linewidth=2.0, linestyle='--', label = 'Ref',antialiased=True)
plt.legend(loc=9,bbox_to_anchor=(0.5, -0.1), ncol=3, frameon=False,fontsize=labelfontsize+2)
#plt.legend()
#lg = plt.legend()
#lg.draw_frame(False)
#lg.loc(2)
plt.xlim([-80,80])
plt.ylim([-0.75,0.75])
plt.yticks(ticks)
plt.ylabel('Z coordinate = z/h',fontsize=myfontsize)
plt.xlabel('Stress_YY',fontsize=myfontsize)
plt.grid()
plt.tick_params(labelsize=labelfontsize)
plt.savefig('nasa3_thru_s_yy.pdf',bbox_inches="tight")
#
#
#
# Stress XY thru thickness @ plate center
fig = plt.figure(3)
ref_z = [0.5,0.25,0.25,-0.25,-0.25,-0.5]
ref_val =[-1151,-1151,1167,1167,-1151,-1151]
plt.plot(quad_thru_s_xy,kratos_thru_z, color = '#77B5FE', linewidth=3.0, label = 'ANDES-DKQ',antialiased=True)
plt.plot(tri_thru_s_xy,kratos_thru_z, color = '#FF91A4', linewidth=3.0, label = 'DSG',antialiased=True)
plt.plot(ref_val,ref_z,color = 'grey', linestyle='None', markerfacecolor= 'None', markersize = 7.0, marker='o', label = 'Ref',antialiased=True)
#plt.plot(disp_ref,load_ref,color = 'grey', linewidth=2.0, linestyle='--', label = 'Ref',antialiased=True)
plt.legend(loc=9,bbox_to_anchor=(0.5, -0.1), ncol=3, frameon=False,fontsize=labelfontsize+2)
#plt.legend()
#lg = plt.legend()
#lg.draw_frame(False)
#lg.loc(2)
plt.ylim([-0.75,0.75])
plt.yticks(ticks)
plt.ylabel('Z coordinate = z/h',fontsize=myfontsize)
plt.xlabel('Stress_XY',fontsize=myfontsize)
plt.grid()
plt.tick_params(labelsize=labelfontsize)
plt.savefig('nasa3_thru_s_xy.pdf',bbox_inches="tight")



# Tsai wu reserve factor thru thickness @ plate center
fig = plt.figure(4)
plt.plot(quad_thru_tsai,kratos_thru_z, color = '#77B5FE', linewidth=3.0, label = 'ANDES-DKQ',antialiased=True)
plt.plot(tri_thru_tsai,kratos_thru_z, color = '#FF91A4', linewidth=3.0, label = 'DSG',antialiased=True)
plt.plot(strand_thru_tsai,kratos_thru_z,color = 'grey', linestyle='None', markerfacecolor= 'None', markersize = 7.0, marker='o', label = 'Ref',antialiased=True)
#plt.plot(disp_ref,load_ref,color = 'grey', linewidth=2.0, linestyle='--', label = 'Ref',antialiased=True)
plt.legend(loc=9,bbox_to_anchor=(0.5, -0.1), ncol=3, frameon=False,fontsize=labelfontsize+2)
#plt.legend()
#lg = plt.legend()
#lg.draw_frame(False)
#lg.loc(2)
plt.xlim([0,2])
plt.ylim([-0.75,0.75])
plt.yticks(ticks)
plt.ylabel('Z coordinate = z/h',fontsize=myfontsize)
plt.xlabel('Tsai-Wu reserve factor',fontsize=myfontsize)
plt.grid()
plt.tick_params(labelsize=labelfontsize)
plt.savefig('nasa3_thru_tsai.pdf',bbox_inches="tight")
#
#
## Strain YY thru thickness @ plate center
#fig = plt.figure(52)
#plt.plot(kratos_thru_e_yy,kratos_thru_z, color = '#77B5FE', linewidth=3.0, label = 'ANDES-DKQ',antialiased=True)
##plt.plot(phi_dsg,n_theta_dsg, color = '#FF91A4', linewidth=3.0, label = 'DSG',antialiased=True)
##plt.plot(kratos_x,analytical_s_x_top,color = 'grey', linestyle='None', markerfacecolor= 'None', markersize = 7.0, marker='o', label = 'Ref',antialiased=True)
##plt.plot(disp_ref,load_ref,color = 'grey', linewidth=2.0, linestyle='--', label = 'Ref',antialiased=True)
#plt.legend(loc=9,bbox_to_anchor=(0.5, -0.1), ncol=3, frameon=False,fontsize=labelfontsize+2)
##plt.legend()
##lg = plt.legend()
##lg.draw_frame(False)
##lg.loc(2)
#plt.ylim([-0.75,0.75])
#plt.yticks(ticks)
#plt.ylabel('Z coordinate = z/h',fontsize=myfontsize)
#plt.xlabel('Strain_YY',fontsize=myfontsize)
#plt.grid()
#plt.tick_params(labelsize=labelfontsize)
#plt.savefig('navier_plate_composite_quad_e_yy.pdf',bbox_inches="tight")
#
#
## Strain XY thru thickness @ plate center
#fig = plt.figure(53)
#plt.plot(kratos_thru_e_xy,kratos_thru_z, color = '#77B5FE', linewidth=3.0, label = 'ANDES-DKQ',antialiased=True)
##plt.plot(phi_dsg,n_theta_dsg, color = '#FF91A4', linewidth=3.0, label = 'DSG',antialiased=True)
##plt.plot(kratos_x,analytical_s_x_top,color = 'grey', linestyle='None', markerfacecolor= 'None', markersize = 7.0, marker='o', label = 'Ref',antialiased=True)
##plt.plot(disp_ref,load_ref,color = 'grey', linewidth=2.0, linestyle='--', label = 'Ref',antialiased=True)
#plt.legend(loc=9,bbox_to_anchor=(0.5, -0.1), ncol=3, frameon=False,fontsize=labelfontsize+2)
##plt.legend()
##lg = plt.legend()
##lg.draw_frame(False)
##lg.loc(2)
#plt.ylim([-0.75,0.75])
#plt.yticks(ticks)
#plt.ylabel('Z coordinate = z/h',fontsize=myfontsize)
#plt.xlabel('Strain_XY',fontsize=myfontsize)
#plt.grid()
#plt.tick_params(labelsize=labelfontsize)
#plt.savefig('navier_plate_composite_quad_e_xy.pdf',bbox_inches="tight")
#
#
#
plt.show()