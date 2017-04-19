# -*- coding: utf-8 -*-
"""
Created on Wed Apr 19 14:35:48 2017

@author: Peter
"""

import matplotlib.pyplot as plt
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
#===============================================================================

factor = 1e6

# MID SURFACE STRESSES --------------------------------------------------------

kratos_x = []    
kratos_s_xz_middle = []
with open("kratos_s_xz.txt", "r") as kratos_file:
  for line in kratos_file:
      line = line.split(' ')
      kratos_x.append(line[0])
      kratos_s_xz_middle.append(float(line[1])/factor)   
      
      
ansys_x = []    
ansys_s_xz_middle = []
with open("ansys_s_xz.txt", "r") as kratos_file:
  for line in kratos_file:
      line = line.split('\t')
      ansys_x.append(line[0])
      ansys_s_xz_middle.append(float(line[1])/factor)           
      
      
# BOT SURFACE STRESSES --------------------------------------------------------      
         
kratos_s_xx_bot = []
with open("kratos_s_xx_bot.txt", "r") as kratos_file:
  for line in kratos_file:
      line = line.split(' ')
      #kratos_x.append(line[0])
      kratos_s_xx_bot.append(float(line[1])/factor)      
      
ansys_s_xx_bot = []
with open("ansys_s_xx_bot.txt", "r") as kratos_file:
  for line in kratos_file:
      line = line.split('\t')
      #ansys_x.append(line[0])
      ansys_s_xx_bot.append(float(line[1])/factor)          
            
 
kratos_diag =[]  
kratos_s_xy_bot_diag = []
with open("kratos_s_xy_bot_diag.txt", "r") as kratos_file:
  for line in kratos_file:
      line = line.split(' ')
      kratos_diag.append(line[0])
      kratos_s_xy_bot_diag.append(float(line[1])/factor)      
      
ansys_diag =[]        
ansys_s_xy_bot_diag = []
with open("ansys_s_xy_bot_diag.txt", "r") as kratos_file:
  for line in kratos_file:
      line = line.split('\t')
      ansys_diag.append(line[0])
      ansys_s_xy_bot_diag.append(float(line[1])/factor)            
      
 
kratos_vm_bot_diag = []
with open("kratos_vm_bot_diag.txt", "r") as kratos_file:
  for line in kratos_file:
      line = line.split(' ')
      #kratos_diag.append(line[0])
      kratos_vm_bot_diag.append(float(line[1])/factor)      
      
       
ansys_vm_bot_diag = []
with open("ansys_vm_bot_diag.txt", "r") as kratos_file:
  for line in kratos_file:
      line = line.split('\t')
      #ansys_diag.append(line[0])
      ansys_vm_bot_diag.append(float(line[1])/factor)            
           
      
      
      
      
      
      
# Stress XZ middle surface
fig = plt.figure(40)
#plt.plot(kratos_x,kratos_s_xz_middle, color = '#77B5FE', linewidth=3.0, label = 'PYTHON',antialiased=True)
plt.plot(kratos_x,kratos_s_xz_middle, color = '#FF91A4', linewidth=3.0, label = 'DSG',antialiased=True)
plt.plot(ansys_x,ansys_s_xz_middle,color = 'grey', linestyle='None', markerfacecolor= 'None', markersize = 7.0, marker='o', label = 'ANSYS',antialiased=True)
#plt.plot(disp_ref,load_ref,color = 'grey', linewidth=2.0, linestyle='--', label = 'Ref',antialiased=True)
plt.legend(loc=9,bbox_to_anchor=(0.5, -0.1), ncol=3, frameon=False,fontsize=labelfontsize+2)
#plt.legend()
#lg = plt.legend()
#lg.draw_frame(False)
#lg.loc(2)
plt.xlim([0,100])
plt.xlabel('X coordinate [m]')
plt.ylabel('XZ shear stress @ mid-surface [MPa]')
plt.grid()
plt.tick_params(labelsize=labelfontsize)
plt.savefig('navier_plate_tri_s_xz.pdf',bbox_inches="tight")







      
      
# Stress XX bot surface
fig = plt.figure(30)
#plt.plot(kratos_x,kratos_s_xz_middle, color = '#77B5FE', linewidth=3.0, label = 'PYTHON',antialiased=True)
plt.plot(kratos_x,kratos_s_xx_bot, color = '#FF91A4', linewidth=3.0, label = 'DSG',antialiased=True)
plt.plot(ansys_x,ansys_s_xx_bot,color = 'grey', linestyle='None', markerfacecolor= 'None', markersize = 7.0, marker='o', label = 'ANSYS',antialiased=True)
#plt.plot(disp_ref,load_ref,color = 'grey', linewidth=2.0, linestyle='--', label = 'Ref',antialiased=True)
plt.legend(loc=9,bbox_to_anchor=(0.5, -0.1), ncol=3, frameon=False,fontsize=labelfontsize+2)
#plt.legend()
#lg = plt.legend()
#lg.draw_frame(False)
#lg.loc(2)
plt.xlim([0,100])
plt.xlabel('X coordinate [m]')
plt.ylabel('XX stress @ bottom surface [MPa]')
plt.grid()
plt.tick_params(labelsize=labelfontsize)
plt.savefig('navier_plate_tri_s_xx.pdf',bbox_inches="tight")   



# Stress XY bot surface
fig = plt.figure(32)
#plt.plot(kratos_x2,kratos_s_xy_bot2, color = '#77B5FE', linewidth=3.0, label = 'kratos refined',antialiased=True)
plt.plot(kratos_diag,kratos_s_xy_bot_diag, color = '#FF91A4', linewidth=3.0, label = 'DSG',antialiased=True)
plt.plot(ansys_diag,ansys_s_xy_bot_diag,color = 'grey', linestyle='None', markerfacecolor= 'None', markersize = 7.0, marker='o', label = 'ANSYS',antialiased=True)
#plt.plot(disp_ref,load_ref,color = 'grey', linewidth=2.0, linestyle='--', label = 'Ref',antialiased=True)
plt.legend(loc=9,bbox_to_anchor=(0.5, -0.1), ncol=3, frameon=False,fontsize=labelfontsize+2)
#plt.legend()
#lg = plt.legend()
#lg.draw_frame(False)
#lg.loc(2)
plt.xlim([0,150])
plt.xlabel('Diagonal distance [m]')
plt.ylabel('XY shear stress @ bottom surface [MPa]')
plt.grid()
plt.tick_params(labelsize=labelfontsize)
plt.savefig('navier_plate_tri_s_xy.pdf',bbox_inches="tight")    



# Stress VM bot surface
fig = plt.figure(33)
#plt.plot(kratos_x2,kratos_s_xy_bot2, color = '#77B5FE', linewidth=3.0, label = 'kratos refined',antialiased=True)
plt.plot(kratos_diag,kratos_vm_bot_diag, color = '#FF91A4', linewidth=3.0, label = 'DSG',antialiased=True)
plt.plot(ansys_diag,ansys_vm_bot_diag,color = 'grey', linestyle='None', markerfacecolor= 'None', markersize = 7.0, marker='o', label = 'ANSYS',antialiased=True)
#plt.plot(disp_ref,load_ref,color = 'grey', linewidth=2.0, linestyle='--', label = 'Ref',antialiased=True)
plt.legend(loc=9,bbox_to_anchor=(0.5, -0.1), ncol=3, frameon=False,fontsize=labelfontsize+2)
#plt.legend()
#lg = plt.legend()
#lg.draw_frame(False)
#lg.loc(2)
plt.xlim([0,150])
plt.xlabel('Diagonal distance [m]')
plt.ylabel('Von Mises stress @ bottom surface [MPa]')
plt.grid()
plt.tick_params(labelsize=labelfontsize)
plt.savefig('navier_plate_tri_vm.pdf',bbox_inches="tight")    




plt.show()