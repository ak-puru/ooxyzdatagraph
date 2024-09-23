# Copyright Paul Lu, 2023

"""
Name: Akhshra Puru
SID: 1775349
CCID: akhshra
AnonID: 1000382193
CMPUT 274, Fall 2023
"""

import matplotlib.pyplot as xyzplt
import matplotlib.cm as cm
from xydata import *

class XYZDatagraph(XYData):
    def __init__(self,name=""):
        super().__init__(name)
        self.__z = []

    def __str__(self):
        s = "XYZData: " + self.name()
        return s

    def __repr__(self):
        s = super().__repr__(self)
        return s

    def dumplist(self):
        return list((zip(self.x(),self.y(),self.z())))

    def dump(self):
        my_list = self.dumplist()
        for i in my_list:
            print(list(i))
        return

    def swapxy(self):
        new_x = self.y().copy()
        new_y = self.x().copy()
        self.x(new_x)
        self.y(new_y)
        return

    def swapxz(self):
        new_x = self.__z.copy()
        new_z = self.x().copy()
        self.x(new_x)
        self.z(new_z) 
        return

    def swapyz(self):
        new_y = self.__z.copy()
        new_z = self.y().copy()
        self.y(new_y) 
        self.z(new_z)
        return

    def z(self,data=[]):
        if len(data) < 1:
            return(self.__z)
        elif type(data) is list:
            self.__z = data.copy()
            return(len(data))
        return None

    # Expects list of 3-element [x,y,z] lists
    def xyz(self,data=[]):
        if len(data) < 1:
            xyz_list = []
            for i in range(len(self.x())):
                xyz_list.append(list([self.x()[i],self.y()[i],self.z()[i]]))
            return str(xyz_list)
        elif type(data) is list:
            new_x = []
            new_y = []
            new_z = []
            for i in range(len(data)):
                new_x.append(data[i][0])
                new_y.append(data[i][1])
                new_z.append(data[i][2])
            self.x(new_x.copy()) 
            self.y(new_y.copy()) 
            self.z(new_z.copy())
            return(len(data))
        return None

    def plot3dpng(self):
        fig = xyzplt.figure()
        ax = fig.add_subplot(projection='3d')
        sc = ax.scatter(self.x(), self.y(), self.z(), c=self.z(), cmap=cm.turbo)
        fig.colorbar(sc, pad=0.2)
        ax.set_xlabel('Fingerprint Size (bytes)')
        ax.set_ylabel('Min Chunk Size (bytes)')
        ax.set_zlabel('Deduplication Ratio')
        ax.set_title('Deduplication Ratio vs.\nFingerprint Size and Min Chunk Size')
        xyzplt.savefig(self.name() + ".png")
        return
