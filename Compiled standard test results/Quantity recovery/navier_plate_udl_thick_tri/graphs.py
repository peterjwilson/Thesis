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
      

   
kratos_x_unstruc = []    
kratos_s_xz_unstruc = []
with open("kratos_s_xz_unstruc.txt", "r") as kratos_file:
  for line in kratos_file:
      line = line.split(' ')
      kratos_x_unstruc.append(line[0])
      kratos_s_xz_unstruc.append(float(line[1])/factor)         
      


kratos_x_rot90 = []    
kratos_s_xz_rot90 = []
with open("kratos_s_xz_rot90.txt", "r") as kratos_file:
  for line in kratos_file:
      line = line.split(' ')
      kratos_x_rot90.append(line[0])
      kratos_s_xz_rot90.append(float(line[1])/factor) 
      
kratos_y = []    
kratos_s_yz_middle = []
with open("kratos_s_yz.txt", "r") as kratos_file:
  for line in kratos_file:
      line = line.split(' ')
      kratos_y.append(line[0])
      kratos_s_yz_middle.append(float(line[1])/factor)       
      
      
ansys_y = []    
ansys_s_yz_middle = []
with open("ansys_s_yz.txt", "r") as kratos_file:
  for line in kratos_file:
      line = line.split('\t')
      ansys_y.append(line[0])
      ansys_s_yz_middle.append(float(line[1])/factor)   
      
      
      
      
      


kratos_y_unstruc = []    
kratos_s_yz_unstruc = []
with open("kratos_s_yz_unstruc.txt", "r") as kratos_file:
  for line in kratos_file:
      line = line.split(' ')
      kratos_y_unstruc.append(line[0])
      kratos_s_yz_unstruc.append(float(line[1])/factor)    
      
      
kratos_y_8x8 = []    
kratos_s_yz_8x8 = []
with open("kratos_s_yz_8x8.txt", "r") as kratos_file:
  for line in kratos_file:
      line = line.split(' ')
      kratos_y_8x8.append(line[0])
      kratos_s_yz_8x8.append(float(line[1])/factor)         
      
kratos_y_rot90 = []    
kratos_s_yz_rot90 = []
with open("kratos_s_yz_rot90.txt", "r") as kratos_file:
  for line in kratos_file:
      line = line.split(' ')
      y = float(line[0])
      y = 100 - y
      kratos_y_rot90.append(y)
      kratos_s_yz_rot90.append(float(line[1])/factor*-1)         
            
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
            

kratos_s_yy_bot = []
with open("kratos_s_yy_bot.txt", "r") as kratos_file:
  for line in kratos_file:
      line = line.split(' ')
      #kratos_x.append(line[0])
      kratos_s_yy_bot.append(float(line[1])/factor)      
      
ansys_s_yy_bot = []
with open("ansys_s_yy_bot.txt", "r") as kratos_file:
  for line in kratos_file:
      line = line.split('\t')
      #ansys_x.append(line[0])
      ansys_s_yy_bot.append(float(line[1])/factor)         
      
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
DSG = '#FF91A4'             #salmon
DSGBasic = '#F5A352'        #orange
KRATOSTRI = '#BB7365'       #brown

fig = plt.figure(40)
plt.plot(kratos_x_rot90,kratos_s_xz_rot90, color = '#F5A352', linewidth=3.0, label = 'DSG mesh rotated 90',antialiased=True)
plt.plot(kratos_x_unstruc,kratos_s_xz_unstruc, color = '#BB7365', linewidth=3.0, label = 'DSG Unstructured',antialiased=True)
plt.plot(kratos_x,kratos_s_xz_middle, color = '#FF91A4', linewidth=3.0, label = 'DSG 24x24',antialiased=True)
plt.plot(ansys_x,ansys_s_xz_middle,color = 'grey', linestyle='None', markerfacecolor= 'None', markersize = 7.0, marker='o', label = 'ANSYS',antialiased=True)
#plt.plot(disp_ref,load_ref,color = 'grey', linewidth=2.0, linestyle='--', label = 'Ref',antialiased=True)
plt.legend(loc=9,bbox_to_anchor=(0.5, -0.1), ncol=2, frameon=False,fontsize=labelfontsize+2)
#plt.legend()
#lg = plt.legend()
#lg.draw_frame(False)
#lg.loc(2)
plt.xlim([0,100])
plt.xlabel('X coordinate [m]')
plt.ylabel('Stress_XZ @ mid-surface [MPa]')
plt.grid()
plt.tick_params(labelsize=labelfontsize)
plt.savefig('navier_plate_tri_s_xz.pdf',bbox_inches="tight")



# Stress YZ middle surface
fig = plt.figure(41)
plt.plot(kratos_y_rot90,kratos_s_yz_rot90, color = '#F5A352', linewidth=3.0, label = 'DSG mesh rotated 90',antialiased=True)
#plt.plot(kratos_y_8x8,kratos_s_yz_8x8, color = 'red', linewidth=3.0, label = 'DSG 8x8',antialiased=True)
plt.plot(kratos_y_unstruc,kratos_s_yz_unstruc, color = '#BB7365', linewidth=3.0, label = 'DSG Unstructured',antialiased=True)
plt.plot(kratos_y,kratos_s_yz_middle, color = '#FF91A4', linewidth=3.0, label = 'DSG 24x24',antialiased=True)
plt.plot(ansys_y,ansys_s_yz_middle,color = 'grey', linestyle='None', markerfacecolor= 'None', markersize = 7.0, marker='o', label = 'ANSYS',antialiased=True)
#plt.plot(kratos_y_unstruc,kratos_s_yz_unstruc,color = 'grey', linewidth=2.0, linestyle='--', label = 'Ref',antialiased=True)
plt.legend(loc=9,bbox_to_anchor=(0.5, -0.1), ncol=2, frameon=False,fontsize=labelfontsize+2)
#plt.legend()
#lg = plt.legend()
#lg.draw_frame(False)
#lg.loc(2)
plt.xlim([0,100])
plt.xlabel('Y coordinate [m]')
plt.ylabel('Stress_YZ @ mid-surface [MPa]')
plt.grid()
plt.tick_params(labelsize=labelfontsize)
plt.savefig('navier_plate_tri_s_yz.pdf',bbox_inches="tight")



      
      
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
plt.ylabel('Stress_XX @ bottom surface [MPa]')
plt.grid()
plt.tick_params(labelsize=labelfontsize)
plt.savefig('navier_plate_tri_s_xx.pdf',bbox_inches="tight")   



# Stress YY bot surface
fig = plt.figure(31)
#plt.plot(kratos_x,kratos_s_xz_middle, color = '#77B5FE', linewidth=3.0, label = 'PYTHON',antialiased=True)
plt.plot(kratos_x,kratos_s_yy_bot, color = '#FF91A4', linewidth=3.0, label = 'DSG',antialiased=True)
plt.plot(ansys_x,ansys_s_yy_bot,color = 'grey', linestyle='None', markerfacecolor= 'None', markersize = 7.0, marker='o', label = 'ANSYS',antialiased=True)
#plt.plot(disp_ref,load_ref,color = 'grey', linewidth=2.0, linestyle='--', label = 'Ref',antialiased=True)
plt.legend(loc=9,bbox_to_anchor=(0.5, -0.1), ncol=3, frameon=False,fontsize=labelfontsize+2)
#plt.legend()
#lg = plt.legend()
#lg.draw_frame(False)
#lg.loc(2)
plt.xlim([0,100])
plt.xlabel('X coordinate [m]')
plt.ylabel('Stress_YY @ bottom surface [MPa]')
plt.grid()
plt.tick_params(labelsize=labelfontsize)
plt.savefig('navier_plate_tri_s_yy.pdf',bbox_inches="tight")   






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
plt.ylabel('Stress_XY @ bottom surface [MPa]')
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