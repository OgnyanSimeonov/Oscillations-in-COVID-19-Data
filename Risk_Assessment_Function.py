# -*- coding: utf-8 -*-
"""Ogy_Covid.ipynb

Ollatiosns in COVID-19 Data
For Figure 1 panels (b) and (c)
---------------------------------------------------------------------------
Created by: Ognyan Simeonov (Bates College)
Edited by: Prof. Carrie Diaz Eaton (Bates College)
Date: 05/24/2022
"""

#Include Needed Packages
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.integrate import odeint
#from lmfit import minimize, Parameters, report_fit

#Plot the initial data. Here we use the 2012 HvZ data. 
dataI = pd.read_csv("COVID_Tufts.csv")
#plt.plot(dataI['Hour'], dataI['Humans'], color='#2c7bb6', linestyle = "", marker = ".", label="Susceptible")
#plt.plot(dataI['Day'], dataI['Infected'], color = '#fdae61', linestyle = "", marker = ".", label="Infected")
#plt.plot(dataI['Hour'], dataI['Corpses'], color = '#d7191c', linestyle = "", marker = ".", label="Removed")

#Label the x and y axis.
plt.xlabel('Pandemic Day', fontsize=14)
plt.ylabel('COVID-19 Cases 7-day Average', fontsize=14)

"""# Define the Model"""

#First time period from t=0h to t=65h. We keep b=0, thus it is not included in the 
#parameter estimation. Here we use a combination of the warrior and the sleep cycle models.

def risk(I, Cmax,a): #define the risk assessment model
    if I <= 0:
      infection_rate = 1
    elif I > 20:
      infection_rate = 0
    else:
      infection_rate = (1-I/Cmax)**a
    
    return infection_rate


def ode_model(z, t, k1, k2, b = 0): #define the ODE model
    S, E, I, R = z
    #N = H + E + Z + C
    #p = np.random.uniform(0.00015, 0.0001)
    
    if S > 0 and I > 0: #System of ODEs to model the change in populations
        dSdt = -0.00015*S*I*risk(I, 20, 0.5)  + 1/90*R
        dEdt = 0.00015*S*I*risk(I, 20, 0.5) - 0.25*E 
        dIdt = 0.25*E - 1/14*I 
        dRdt = 1/14*I -1/90*R
    else:
        dSdt = 0
        dEdt = 0
        dIdt = - 1/14*I
        dRdt = 1/14*I
    return [dSdt, dEdt, dIdt, dRdt]

#DEFINE THE ODE SOLVER
# The ODE solver takes as inputs the time span, initial conditions, and parameter
#and uses them to solve the model of ODEs we defined
def ode_solver(t, initial_conditions, params):
    initS, initE, initI, initR = initial_conditions
    k1, k2, b = params['k1'].value, params['k2'].value, params['b'].value
    res = odeint(ode_model, [initS, initE, initI, initR], t, args=(k1,k2, b))
    return res

#Define initial conditions
initS = 5737
initE = 7
initI = 1
initR = 80
initial_conditions = [initS,initE, initI, initR]

#parameter initial estimates from simulation
k1 = 0.002
k2 = 0.001333645
b =  0.14

t0 = np.arange(1, 250, 1)
int_cond0 = [initS,initE, initI, initR]
sol0 = odeint(ode_model, int_cond0, t0, args=(k1,k2, b))

#plt.plot(t0,sol0[:,0],color='#2c7bb6', linestyle = "-", marker = "",label="Susceptible Fit")
plt.plot(t0,sol0[:,2],color ='green', linestyle = "-", marker = "",label="r = 0.5")
#plt.plot(t0,sol0[:,3],color = '#d7191c', linestyle = "-", marker = "",label="Removed Fit")

#------------------------------------------------------------------------------
       
def ode_model(z, t, k1, k2, b = 0): #define the ODE model
    S, E, I, R = z
    #N = H + E + Z + C
    #p = np.random.uniform(0.00015, 0.0001)

    if S > 0 and I > 0: #System of ODEs to model the change in populations
        dSdt = -0.00015*S*I*risk(I, 20, 1)  + 1/90*R
        dEdt = 0.00015*S*I*risk(I, 20, 1) - 0.25*E 
        dIdt = 0.25*E - 1/14*I 
        dRdt = 1/14*I -1/90*R
    else:
        dSdt = 0
        dEdt = 0
        dIdt = - 1/14*I
        dRdt = 1/14*I
    return [dSdt, dEdt, dIdt, dRdt]

#Define initial conditions
initS = 5737
initE = 7
initI = 1
initR = 80
initial_conditions = [initS,initE, initI, initR]

#parameter initial estimates from simulation
k1 = 0.002
k2 = 0.001333645
b =  0.14

t0 = np.arange(1, 250, 1)
int_cond0 = [initS,initE, initI, initR]
sol0 = odeint(ode_model, int_cond0, t0, args=(k1,k2, b))

#plt.plot(t0,sol0[:,0],color='#2c7bb6', linestyle = "-", marker = "",label="Susceptible Fit")
plt.plot(t0,sol0[:,2],color ='red', linestyle = "-", marker = "",label="r = 1")
#plt.plot(t0,sol0[:,3],color = '#d7191c', linestyle = "-", marker = "",label="Removed Fit")
       
#------------------------------------------------------------------------------

#------------------------------------------------------------------------------        
def ode_model(z, t, k1, k2, b = 0): #define the ODE model
    S, E, I, R = z
    #N = H + E + Z + C
    #p = np.random.uniform(0.00015, 0.0001)

    if S > 0 and I > 0: #System of ODEs to model the change in populations
        dSdt = -0.00015*S*I*risk(I, 20, 2)  + 1/90*R
        dEdt = 0.00015*S*I*risk(I, 20, 2) - 0.25*E 
        dIdt = 0.25*E - 1/14*I 
        dRdt = 1/14*I -1/90*R
    else:
        dSdt = 0
        dEdt = 0
        dIdt = - 1/14*I
        dRdt = 1/14*I
    return [dSdt, dEdt, dIdt, dRdt]

#Define initial conditions
initS = 5737
initE = 7
initI = 1
initR = 80
initial_conditions = [initS,initE, initI, initR]

#parameter initial estimates from simulation
k1 = 0.002
k2 = 0.001333645
b =  0.14

t0 = np.arange(1, 250, 1)
int_cond0 = [initS,initE, initI, initR]
sol0 = odeint(ode_model, int_cond0, t0, args=(k1,k2, b))

#plt.plot(t0,sol0[:,0],color='#2c7bb6', linestyle = "-", marker = "",label="Susceptible Fit")
plt.plot(t0,sol0[:,2],color ='blue', linestyle = "-", marker = "",label="r = 2")
#plt.plot(t0,sol0[:,3],color = '#d7191c', linestyle = "-", marker = "",label="Removed Fit")
       
#------------------------------------------------------------------------------

#------------------------------------------------------------------------------        
def ode_model(z, t, k1, k2, b = 0): #define the ODE model
    S, E, I, R = z
    #N = H + E + Z + C
    #p = np.random.uniform(0.00015, 0.0001)

    if S > 0 and I > 0: #System of ODEs to model the change in populations
        dSdt = -0.00015*S*I*risk(I, 20, 5)  + 1/90*R
        dEdt = 0.00015*S*I*risk(I, 20, 5) - 0.25*E 
        dIdt = 0.25*E - 1/14*I 
        dRdt = 1/14*I -1/90*R
    else:
        dSdt = 0
        dEdt = 0
        dIdt = - 1/14*I
        dRdt = 1/14*I
    return [dSdt, dEdt, dIdt, dRdt]

#Define initial conditions
initS = 5737
initE = 7
initI = 1
initR = 80
initial_conditions = [initS,initE, initI, initR]

#parameter initial estimates from simulation
k1 = 0.002
k2 = 0.001333645
b =  0.14

t0 = np.arange(1, 250, 1)
int_cond0 = [initS,initE, initI, initR]
sol0 = odeint(ode_model, int_cond0, t0, args=(k1,k2, b))

#plt.plot(t0,sol0[:,0],color='#2c7bb6', linestyle = "-", marker = "",label="Susceptible Fit")
plt.plot(t0,sol0[:,2],color ='purple', linestyle = "-", marker = "",label="r = 5")
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)
#plt.plot(t0,sol0[:,3],color = '#d7191c', linestyle = "-", marker = "",label="Removed Fit")
plt.savefig('DifferentRisk1.png', bbox_inches='tight', dpi=300)
plt.show()
#------------------------------------------------------------------------------



def f(x):
   return (1-x/20)**0.5

x = np.linspace(0, 20, 100)

plt.plot(x, f(x), color='g', label ="r=0.5")
def f(x):
   return (1-x/20)**1
plt.plot(x, f(x), color='r', label ="r=1")

def f(x):
   return (1-x/20)**2
plt.plot(x, f(x), color='b', label ="r=2")

def f(x):
   return (1-x/20)**5
plt.plot(x, f(x), color='purple', label ="r=5")

plt.xlabel('Number of Infected Individuals (I)', fontsize=14)
plt.ylabel('f(I; Cmax = 20)', fontsize=14)
         
plt.savefig('Risk_Function.png', bbox_inches='tight', dpi=300)

#plt.figure(2)
#plt.plot(sol0[:,1],sol0[:,2],color ='#fdae61', linestyle = "-", marker = "",label="Infected Fit")
#plt.xlabel('Exposed')
#plt.ylabel('Infected')
#plt.savefig('PhasePortrait.png', bbox_inches='tight', dpi=300)