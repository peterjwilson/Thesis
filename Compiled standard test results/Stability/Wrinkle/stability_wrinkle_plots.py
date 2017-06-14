# -*- coding: utf-8 -*-
"""
Created on Fri Mar 17 18:37:12 2017

@author: Peter
"""

#===============================================
#
#       stability wrinkle plots
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

# Thin quad element -------------------------------------------
axialDispQT = []
latDispQT = []
latDispPointQT = []
loadQT = []

with open("displacementxQT.txt", "r") as doc:
  for line in doc:
    axialDispQT.append((float(line)))    
doc.close()

with open("displacementzQT.txt", "r") as doc:
  for line in doc:
    latDispQT.append((float(line)))    
doc.close()

with open("displacement_point_zQT.txt", "r") as doc:
  for line in doc:
    latDispPointQT.append((float(line)))    
doc.close()

with open("loadxQT.txt", "r") as doc:
  for line in doc:
    loadQT.append((float(line))/1e3)    
doc.close()



# Thin quad element BASIC -------------------------------------------
axialDispQTB = []
latDispQTB = []
latDispPointQTB = []
loadQTB = []

with open("displacementxQTB.txt", "r") as doc:
  for line in doc:
    axialDispQTB.append((float(line)))    
doc.close()

with open("displacementzQTB.txt", "r") as doc:
  for line in doc:
    latDispQTB.append((float(line)))    
doc.close()

with open("displacement_point_zQTB.txt", "r") as doc:
  for line in doc:
    latDispPointQTB.append((float(line)))    
doc.close()

with open("loadxQTB.txt", "r") as doc:
  for line in doc:
    loadQTB.append((float(line))/1e3)    
doc.close()


# Kratos quad element -------------------------------------------
axialDispQK = []
latDispQK = []
latDispPointQK = []
loadQK = []

with open("displacementxQK.txt", "r") as doc:
  for line in doc:
    axialDispQK.append((float(line)))    
doc.close()

with open("displacementzQK.txt", "r") as doc:
  for line in doc:
    latDispQK.append((float(line)))    
doc.close()

with open("displacement_point_zQK.txt", "r") as doc:
  for line in doc:
    latDispPointQK.append((float(line)))    
doc.close()

with open("loadxQK.txt", "r") as doc:
  for line in doc:
    loadQK.append((float(line))/1e3)    
doc.close()



# Thick tri element -------------------------------------------
axialDispTT = []
latDispTT = []
latDispPointTT = []
loadTT = []

with open("displacementxTT.txt", "r") as doc:
  for line in doc:
    axialDispTT.append((float(line)))    
doc.close()

with open("displacementzTT.txt", "r") as doc:
  for line in doc:
    latDispTT.append((float(line)))    
doc.close()

with open("displacement_point_zTT.txt", "r") as doc:
  for line in doc:
    latDispPointTT.append((float(line)))    
doc.close()

with open("loadxTT.txt", "r") as doc:
  for line in doc:
    loadTT.append((float(line))/1e3)    
doc.close()



# Thick tri element basic-------------------------------------------
axialDispTTB = []
latDispTTB = []
latDispPointTTB = []
loadTTB = []

with open("displacementxTTB.txt", "r") as doc:
  for line in doc:
    axialDispTTB.append((float(line)))    
doc.close()

with open("displacementzTTB.txt", "r") as doc:
  for line in doc:
    latDispTTB.append((float(line)))    
doc.close()

with open("displacement_point_zTTB.txt", "r") as doc:
  for line in doc:
    latDispPointTTB.append((float(line)))    
doc.close()

with open("loadxTTB.txt", "r") as doc:
  for line in doc:
    loadTTB.append((float(line))/1e3)    
doc.close()




# Thick tri element -------------------------------------------
axialDispTK = []
latDispTK = []
latDispPointTK = []
loadTK = []

with open("displacementxTK.txt", "r") as doc:
  for line in doc:
    axialDispTK.append((float(line)))    
doc.close()

with open("displacementzTK.txt", "r") as doc:
  for line in doc:
    latDispTK.append((float(line)))    
doc.close()

with open("displacement_point_zTK.txt", "r") as doc:
  for line in doc:
    latDispPointTK.append((float(line)))    
doc.close()

with open("loadxTK.txt", "r") as doc:
  for line in doc:
    loadTK.append((float(line))/1e3)    
doc.close()



# Reference calc -------------------------------------------
n = 4.0
E = 206900000000
I = 14568645/1000**4 #mm4 to m4
L = 3
A = 3063.053/1000**2 #mm2 to m2
k = E*A/L

loadRef = [0]
axialDispRef = [0]
loadRef.append(-n*np.pi**2*E*I/L**2/1000) #N to kN
axialDispRef.append(loadRef[1]/k*1000)

print(loadRef)
print(axialDispRef)


#colors
ANDESDKQ = '#77B5FE'        #blue
ANDESBasic = '#C5AAF5'      #purple
KRATOSQUAD = '#79BFA1'      #green

DSG = '#FF91A4'             #salmon
DSGBasic = '#F5A352'        #orange
KRATOSTRI = '#BB7365'       #brown


#Plot graph ------------------------------------------------------------------

fig = plt.figure(1)
plt.plot(latDispQT,loadQT, color = ANDESDKQ, linewidth=2.0, 
         label = 'ANDES-DKQ',antialiased=True)

plt.plot(latDispTT,loadTT, color = DSG, linewidth=2.0, 
         label = 'DSG',antialiased=True)

plt.plot(latDispQTB,loadQTB, color = ANDESBasic, linewidth=2.0, 
         label = 'Basic-DKQ',antialiased=True)

#plt.plot(latDispTTB,loadTTB, color = DSGBasic, linewidth=2.0, 
#         label = 'Basic-T3',antialiased=True)

plt.plot(latDispQK,loadQK, color = KRATOSQUAD, linewidth=2.0, 
         label = 'KRATOS Q4',antialiased=True)

plt.plot(latDispTK,loadTK, color = KRATOSTRI, linewidth=2.0, 
         label = 'KRATOS T3',antialiased=True)

plt.legend(loc=9,bbox_to_anchor=(0.5, -0.1), ncol=3, frameon=False,fontsize=labelfontsize+2)

plt.xlabel('Lateral displacement [m]',fontsize=myfontsize)
plt.ylabel('Load [kN]',fontsize=myfontsize)
#plt.ylim([0,2e-5])
plt.grid()
plt.tick_params(labelsize=labelfontsize)
plt.savefig('stability_wrinkle_abstrans_disp.pdf',bbox_inches="tight")




fig = plt.figure(2)
plt.plot(latDispPointQT,loadQT, color = ANDESDKQ, linewidth=2.0, 
         label = 'ANDES-DKQ',antialiased=True)

plt.plot(latDispPointTT,loadTT, color = DSG, linewidth=2.0, 
         label = 'DSG',antialiased=True)

plt.plot(latDispPointQTB,loadQTB, color = ANDESBasic, linewidth=2.0, 
         label = 'Basic-DKQ',antialiased=True)

plt.plot(latDispPointTTB,loadTTB, color = DSGBasic, linewidth=2.0, 
         label = 'Basic-T3',antialiased=True)

plt.plot(latDispPointQK,loadQK, color = KRATOSQUAD, linewidth=2.0, 
         label = 'KRATOS Q4',antialiased=True)

plt.plot(latDispPointTK,loadTK, color = KRATOSTRI, linewidth=2.0, 
         label = 'KRATOS T3',antialiased=True)

plt.legend(loc=9,bbox_to_anchor=(0.5, -0.1), ncol=3, frameon=False,fontsize=labelfontsize+2)

plt.xlabel('Point lateral displacement [m]',fontsize=myfontsize)
plt.ylabel('Load [kN]',fontsize=myfontsize)
plt.ylim([0,2e4])
plt.xlim([-0.015,0.015])
plt.grid()
plt.tick_params(labelsize=labelfontsize)
plt.savefig('stability_wrinkle_pointtrans_disp.pdf',bbox_inches="tight")





fig = plt.figure(3)
plt.plot(axialDispQT,loadQT, color = ANDESDKQ, linewidth=2.0, 
         label = 'ANDES-DKQ',antialiased=True)

plt.plot(axialDispTT,loadTT, color = DSG, linewidth=2.0, 
         label = 'DSG',antialiased=True)

plt.plot(axialDispQTB,loadQTB, color = ANDESBasic, linewidth=2.0, 
         label = 'Basic-DKQ',antialiased=True)

#plt.plot(axialDispTTB,loadTTB, color = DSGBasic, linewidth=2.0, 
#         label = 'Basic-T3',antialiased=True)

plt.plot(axialDispQK,loadQK, color = KRATOSQUAD, linewidth=2.0, 
         label = 'KRATOS Q4',antialiased=True)

plt.plot(axialDispTK,loadTK, color = KRATOSTRI, linewidth=2.0, 
         label = 'KRATOS T3',antialiased=True)



plt.legend(loc=9,bbox_to_anchor=(0.5, -0.1), ncol=3, frameon=False,fontsize=labelfontsize+2)

plt.xlabel('Axial displacement [m]',fontsize=myfontsize)
plt.ylabel('Load [kN]',fontsize=myfontsize)
#plt.ylim([0,2e-5])
plt.grid()
plt.tick_params(labelsize=labelfontsize)
plt.savefig('stability_wrinkle_axial_disp.pdf',bbox_inches="tight")





















plt.show()

