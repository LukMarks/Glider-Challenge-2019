import numpy as np
import matplotlib.pyplot as plt
class stab:
    def __init__(self, aircraft):
        self.rc = aircraft[0]#root chord
        self.tc = aircraft[1]
        self.t = self.tc/self.rc
        self.b = aircraft[2]  # wing san
        return

    def wing_area(self):
        self.S = (self.rc+self.tc)*(self.b/2)/2
        return self.S

    def average_chord(self):
        self.c = self.S/self.b
        return self.c

    def frange(start, stop, step):
         i = start
         while i < stop:
             yield i
             i += step

    def vertical_tail_area(self,Vvolume,Lv):
        K = Vvolume * self.S*self.b
        self.Sv = K/Lv
        return self.Sv

    def horizontal_tail_area(self,Hvolume,Lh):
        K = Hvolume * (self.S*self.c)
        self.Sh = K/Lh
        return self.Sh

    def mean_aerodynamic_chord(self):
        self.mac = (2/3)*self.rc*((1+self.t+self.t**2)/(1+self.t))
        return self.mac

    def dihedral_angle(self,B,Lv,Cl = 0.3):
        gamma = B*self.b*Cl/Lv
        return gamma

    def roll_control(self,B,Vvolume):
        control = B*Vvolume
        return control

    def vertical_tail_volume(self,Vv,lvi,lvf, step = 10e-3):
        sv = []
        lv = []
        for i in stab.frange(lvi,lvf,step):
            Sv = stab.vertical_tail_area(self,Vv,i)
            sv.append(Sv)
            lv.append(i)
        Label  = 'Vv = ' + str(Vv)
        plt.figure(100)
        plt.plot(lv,sv, label = Label)
        plt.grid()
        plt.xlabel('Vertical tail moment arm [m]')
        plt.ylabel('Vertical tail area [m^2]')
        plt.title('Vertical Tail Volume')
        plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
        return sv, lv

    def horizontal_tail_volume(self,Hv,lhi,lhf, step = 10e-3):
        sh = []
        lh = []
        for j in stab.frange(lhi,lhf,step):
            Sh = stab.horizontal_tail_area(self,Hv,j)
            sh.append(Sh)
            lh.append(j)
        Label  = 'Vh = ' + str(Hv)
        plt.figure(101)
        plt.plot(lh,sh,label = Label)
        plt.grid()
        plt.xlabel('Horizontal tail moment arm [m]')
        plt.ylabel('Horizontal tail area [m^2]')
        plt.title('Horizontal Tail Volume')
        plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
        return sh,lh

    def vertical_volume(self,threshold,lvi,lvf, step = 10e-3):
        for V in threshold:
            stab.vertical_tail_volume(self,V,lvi,lvf)
        #plt.show()
        return

    def horizontal_volume(self,threshold,lhi,lhf, step = 10e-3):
        for V in threshold:
            stab.horizontal_tail_volume(self,V,lhi,lhf)
        #plt.show()
        return
