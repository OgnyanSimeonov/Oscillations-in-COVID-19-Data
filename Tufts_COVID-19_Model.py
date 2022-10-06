# -*- coding: utf-8 -*-
"""Copy of Ogy_Covid.ipynb


Ollatiosns in COVID-19 Data
For Figure 2 panels (a) and (b)
---------------------------------------------------------------------------
Created by: Ognyan Simeonov (Bates College)
Edited by: Prof. Carrie Diaz Eaton (Bates College)
Date: 05/24/2022
"""

#Include Needed Packages
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import math
from scipy.integrate import odeint
#from lmfit import minimize, Parameters, report_fit

"""# New Section"""
plt.figure(0)
#Plot the initial data. Here we use the 2012 HvZ data. 
dataI = pd.read_csv("Tufts_Covid.csv")
dataI = dataI
#plt.plot(dataI['Hour'], dataI['Humans'], color='#2c7bb6', linestyle = "", marker = ".", label="Susceptible")
plt.plot(dataI['Day'], dataI['Infected'], color = '#fdae61', linestyle = "", marker = ".", label="Infected")
#plt.plot(dataI['Hour'], dataI['Corpses'], color = '#d7191c', linestyle = "", marker = ".", label="Removed")
plt.rcParams["figure.figsize"] = [7.5, 5]
#Label the x and y axis.
plt.xlabel('Pandemic Day')
plt.ylabel('COVID-19 Cases 7-day Average')
plt.savefig('Tufts_Data.png', bbox_inches='tight', dpi=300)
"""# Define the Model"""

#First time period from t=0h to t=65h. We keep b=0, thus it is not included in the 
#parameter estimation. Here we use a combination of the warrior and the sleep cycle models.

def risk(I, Cmax,a): #define the risk assessment model
    if I <= 0:
      infection_rate = 1
    elif I > 35:
      infection_rate = 0
    else:
      infection_rate = (1-I/Cmax)**a
    
    return infection_rate


def ode_model(z, t): #define the ODE model
    S, E, I, R = z
    #N = H + E + Z + C
    #p = np.random.uniform(0,1)
    # initial peak Halloween 
    if t < 75:
        p = 0.00015
        k = 0.0001
        m = 0.25
    elif t < 77: #post break arrival 
        p = 0.00025
        k = 0.00001
        m = 0.008
    elif t < 140:
        p = 0.00015
        k = 0.0001
        m = 0.25
    elif t < 142: #ease COVID-19 restrictions
        p = 0.00025
        k = 0.00001
        m = 0.008
    elif t < 200:
        p = 0.00015
        k = 0.0001
        m = 0.25
    else:
        p = 0.0005
        k = 0.0001
        m = 0.008
    if S > 0 and I > 0: #System of ODEs to model the change in populations
        dSdt = -p*S*I*risk(I, 35,10)  + 1/90*R 
        dEdt = p*S*I*risk(I, 35,10) - m*E 
        dIdt = m*E - 1/14*I 
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
    res = odeint(ode_model, [initS, initE, initI, initR], t)
    return res

#Define initial conditions
initS = 5737
initE = 7
initI = 4
initR = 80
initial_conditions = [initS,initE, initI, initR]

t0 = np.arange(1, 175, 1)
int_cond0 = [initS,initE, initI, initR]
sol0 = odeint(ode_model, int_cond0, t0)
plt.figure(1)
#plt.plot(t0,sol0[:,0],color='#2c7bb6', linestyle = "-", marker = "",label="Susceptible Fit")
plt.plot(t0,sol0[:,2],color ='#fdae61', linestyle = "-", marker = "",label="Infected Fit")
#plt.plot(t0,sol0[:,3],color = '#d7191c', linestyle = "-", marker = "",label="Removed Fit")

plt.rcParams["figure.figsize"] = [7.5, 5]
plt.xlabel('Pandemic Day')
plt.ylabel('Infected')
plt.savefig('Tufts_Oscil.png', bbox_inches='tight', dpi=300)


#plt.figure(2)
#plt.plot(sol0[:,1],sol0[:,2],color ='#fdae61', linestyle = "-", marker = "",label="Infected Fit")
#plt.xlabel('Exposed')
#plt.ylabel('Infected')
#plt.savefig('PhasePortrait.png', bbox_inches='tight', dpi=300)



