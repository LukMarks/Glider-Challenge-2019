import numpy as np
import matplotlib.pyplot as plt
import platform
import os
sys = platform.system() # get the O.S
if sys =='Linux':
	from xfoil_linux import xfoil
else:
	from xfoil import xfoil


class flight:
    def __init__(self,g = 9.81):
        self.g = g
        self.u = 1.7894e-5#[N.s/m²] air dynamic viscosity
        self.p = 1.2 #[kg/m³] air density
        self.path  ='.\\xfoil_output'
        return

    def distance(self, V, m, Fd):
        D = -m*(V/Fd)
        return D

    def altitude(self):
        return H

    def flight_forces(self,v,airfoil,alpha,S,mac,inter= 300,np = 200):
        reynolds = mac * v * self.p/self.u # reynolds number
        mach = v/343 # mach number
        L = []
        D = []
        aero = xfoil(airfoil,alpha,reynolds,mach,inter,np,self.path,L,D)
        cl = aero[0]
        cd = aero[1]
        print('Aerodynimics Coefficiets')
        print('cd: ',cd,' cl: ',cl)
        lift = (1/2)*self.p*v**2*S*cl
        drag = (1/2)*self.p*v**2*S*cd
        return lift,drag,cl,cd
    def performance(self,v0,vf,T,step,airfoil,alpha,S,mac,w = 0.02,g = 9.81):
        v_step = v0
        d = []
        l = []
        rc = []
        v = []
        t = []
        W = []
        while v_step <= vf:
            Lift,Drag,cl,cd = flight.flight_forces(self,v_step,airfoil,alpha,S,mac)
            d.append(Drag)
            l.append(Lift)
            RC = (T*v_step-Drag*v_step)/w
            rc.append(RC)
            v.append(v_step)
            t.append(T)
            W.append(w*g)
            v_step+=step
        plt.figure(10)
        plt.plot(v,t, label = 'Thrust')
        plt.plot(v,d, label = 'Drag')
        plt.grid()
        plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
        plt.xlabel('Velocity (m/s)')
        plt.ylabel('Force (N)')
        plt.title('Thrust X Drag')

        plt.figure(11)
        plt.plot(v,l , label = 'Lift')
        #plt.plot(v,W , label = 'Weigth')
        plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
        plt.grid()
        plt.xlabel('velocity (m/s)')
        plt.ylabel('Lift (N)')
        plt.title('Wight x Lift')

        plt.figure(12)
        plt.plot(v,rc)
        plt.grid()
        plt.xlabel('velocity (m/s)')
        plt.ylabel('Rate of Climb (m/s)')
        plt.title('Rate of climb')


        return
