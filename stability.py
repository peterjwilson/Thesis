# -*- coding: utf-8 -*-
"""
Created on Sat May 20 20:10:33 2017

@author: Peter
"""

import numpy as np
import sympy as sp
import matplotlib.pyplot as plt
from mpmath import *

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



def calcK(disp):
    return EA/L**3*(3*disp**2 - 6*b*disp+2*b**2)
    
def calcEgl(disp):
    return (disp**2 - 2*b*disp)/2/L**2

def calcFunc(func,u,w,EA,a,b,P):
    L = np.sqrt(a**2 + b**2)
    returnvalue = ((((((func.subs(u_s,u)).subs(w_s,w)).subs(EA_s,EA)).subs(a_s,a)).subs(b_s,b)).subs(P_s,P)).subs(L_s,L)
    return returnvalue

#a = 1
#b = 1
#EA = 1
#P = 1
#L = np.sqrt(2)
#u_lim = 2.5
#u_div = 100
#u = []
#lamda = []
#K = []
#
#
#
#
#lamda_lpb = 0.05
#u_lpb = 0.0801
#e_lpb = calcEgl(u_lpb)
#Kg_lpb = 2*EA/L*e_lpb
#K_e = calcK(0)
#
#crit_lim = -K_e/Kg_lpb




# Two dof system --------------------------------------------------------------
lamda_lpb = 0
u_lpb = 0
u_c1 = 0
u_c2 = 0
lamda_c1 = 0
lamda_c2 = 0
u = []
lamda = []

k_mat_22 = []
lam_2 = []
u_nl_buck = []

a = 1
b_lim = 5
b_div = 50
ba = []
lpb_ratio = []
for k in range(b_div+1):
    b = a+k*(b_lim-a)/b_div
    ba.append(b/a)
    #b = 1
    EA = 1
    P = 1
    b_over_a = b/a
    L = np.sqrt(a**2 + b**2)
    
    
    u_lim = 2.5*b
    u_div = 50
    
    a_s = sp.Symbol('a')
    b_s = sp.Symbol('b')
    EA_s = sp.Symbol('EA')
    P_s = sp.Symbol('P')
    L_s = sp.Symbol('L')
    
    u_s = sp.Symbol('u')
    w_s = sp.Symbol('w')
    lamda_s = sp.Symbol('lamda')
    
    # GL1
    l_1 = sp.sqrt(L_s**2 + u_s**2 + 2*a_s*u_s + w_s**2 - 2*b_s*w_s)
    e_gl_1 = 0.5*(l_1**2 - L_s**2)/L_s**2
    d_e_gl_1_du = sp.diff(e_gl_1,u_s)
    d_e_gl_1_dw = sp.diff(e_gl_1,w_s)
    
    
    # GL1
    l_2= sp.sqrt(L_s**2 + u_s**2 - 2*a_s*u_s + w_s**2 - 2*b_s*w_s)
    e_gl_2 = 0.5*(l_2**2 - L_s**2)/L_s**2
    d_e_gl_2_du = sp.diff(e_gl_2,u_s)
    d_e_gl_2_dw = sp.diff(e_gl_2,w_s)
    
    # system residual
    r = sp.zeros(2,1)
    # r0 - du
    r[0] = EA_s*L_s*e_gl_1*d_e_gl_1_du + EA_s*L_s*e_gl_2*d_e_gl_2_du
    # r1 - dw
    r[1] = EA_s*L_s*e_gl_1*d_e_gl_1_dw + EA_s*L_s*e_gl_2*d_e_gl_2_dw

    
    # system tangent stiffness
    K_mat = sp.zeros(2,2)
    K_mat[0,0] = r[0].diff(u_s)
    K_mat[0,1] = r[0].diff(w_s)
    K_mat[1,0] = r[1].diff(u_s)
    K_mat[1,1] = r[1].diff(w_s)
    
    
    # system tangent stiffness roots
    detK = K_mat[0,0]*K_mat[1,1] - K_mat[0,1]*K_mat[1,0]
    detK2 = calcFunc(detK,0.0,w_s,EA,a,b,P)
    #sp.pprint(detK2)
    roots_w = sp.solve(detK2,w_s)
    roots_lamda = []
    roots_lamda.append(calcFunc(r[1],0.0,roots_w[0],EA,a,b,P))
    roots_lamda.append(calcFunc(r[1],0.0,roots_w[1],EA,a,b,P))
    #print(roots_lamda[0])
    
    u_nl_buck.append(roots_w[0])
    
    # Linear pre-buckling
    K_e_mat = calcFunc(K_mat,0.0,0.0,EA,a,b,P)
    K_g_mat = sp.zeros(2,2)
    K_g_mat[0,0] = lamda_s/b
    K_g_mat[1,1] = lamda_s/b
    K_buck = K_e_mat - K_g_mat
    detK_buck = K_buck[0,0] * K_buck[1,1]
    roots_buck = sp.solve(detK_buck,lamda_s)
    #print("roots buck = ",roots_buck)
    lamda_2_lpb = EA*b**2*b/L**3
    lamda_2_lpb = EA*a**2*b/L**3
    lamda_2_lpb = roots_buck[0]
    #print(lamda_2_lpb)
    
    
    #results
    lpb_ratio.append(lamda_2_lpb/roots_lamda[0])

#    print("LPB lamda roots = ",roots_buck)
#    print("NL lamda roots = ",roots_lamda)
#    print("NL disp roots = ",roots_w)
#    print("Ratio of lpb to NL = ",lamda_2_lpb/roots_lamda[0],"\n")
    
    if b==1.0:
        lamda_lpb = [0,lamda_2_lpb]
        u_lpb = [0,lamda_2_lpb/K_e_mat[1,1]]
        u_c1 = roots_w[0]
        u_c2 = roots_w[1]
        lamda_c1 = roots_lamda[0]
        lamda_c2 = roots_lamda[1]
        for i in range(u_div):
            u.append(i*u_lim/u_div)
            u_i = u[i]
            lam_2.append(calcFunc(r[1],0.0,u[i],EA,a,b,P))
            k_mat_22.append(calcFunc(K_mat[1,1],0.0,u[i],EA,a,b,P))

            
#77B5FE = nice blue
fig = plt.figure(1)


plt.plot(u,lam_2,color = 'grey',linewidth=3.0, label = 'Equilibrium path',antialiased=True)

plt.plot(u,k_mat_22,color = '#77B5FE', linewidth=3.0,label = 'det[K]',antialiased=True)

#plt.plot(u_lpb,lamda_lpb,color = '#79BFA1', label = 'LPB',antialiased=True)
plt.axhline(y=lamda_lpb[1],color = '#79BFA1', linestyle='--', linewidth=3.0, 
         label = 'LPB',antialiased=True)


plt.plot(u_lpb[1],lamda_lpb[1],color = '#79BFA1', linestyle='None', markerfacecolor= 'None',markeredgecolor= '#79BFA1', markersize = 7.0, marker='o', label = None,antialiased=True)

plt.plot(u_c1,lamda_c1,color = 'red', linestyle='None', markerfacecolor= 'None',markeredgecolor= 'red', markersize = 7.0, marker='o', label = None,antialiased=True)
plt.plot(u_c2,lamda_c2,color = 'red', linestyle='None', markerfacecolor= 'None',markeredgecolor= 'red', markersize = 7.0, marker='o', label = None,antialiased=True)


plt.plot(u_c1,0,color = 'red', linestyle='None', markerfacecolor= 'None',markeredgecolor= 'red', markersize = 7.0, marker='o', label = None,antialiased=True)
plt.plot(u_c2,0,color = 'red', linestyle='None', markerfacecolor= 'None',markeredgecolor= 'red', markersize = 7.0, marker='o', label = None,antialiased=True)
plt.plot([u_c1,u_c1],[0,lamda_c1],color = 'red', linestyle='--',label = None,antialiased=True)
plt.plot([u_c2,u_c2],[0,lamda_c2],color = 'red', linestyle='--',label = None,antialiased=True)
#plt.plot(phi_ref,n_theta_hand,color = 'grey', linewidth=2.0, linestyle='--', label = 'Ref',antialiased=True)
plt.legend(loc=9,bbox_to_anchor=(0.5, -0.1), ncol=3, frameon=False,fontsize=labelfontsize+2)
#lg = plt.legend()
#lg.draw_frame(False)
#lg.loc(2)
#plt.xlim([0,90])
plt.xlabel('Vertical displacement w')
plt.ylabel('Load factor and det[K]')
plt.grid()
plt.tick_params(labelsize=labelfontsize)
plt.savefig('stability_analysis_mises_truss_1x1.pdf',bbox_inches="tight")




fig = plt.figure(2)

plt.plot(ba,lpb_ratio,color = '#79BFA1', linewidth=3.0, label = None,antialiased=True)

#plt.plot(phi_ref,n_theta_hand,color = 'grey', linewidth=2.0, linestyle='--', label = 'Ref',antialiased=True)
#plt.legend(loc=9,bbox_to_anchor=(0.5, -0.1), ncol=3, frameon=False,fontsize=labelfontsize+2)
lg = plt.legend()
#lg.draw_frame(False)
#lg.loc(2)
#plt.xlim([0,90])
plt.xlabel('b/a')
plt.ylabel('$λ_{LPB}$ / $λ_{NL}$')
plt.grid()
plt.tick_params(labelsize=labelfontsize)
plt.savefig('stability_analysis_mises_truss_lpb.pdf',bbox_inches="tight")





plt.show()