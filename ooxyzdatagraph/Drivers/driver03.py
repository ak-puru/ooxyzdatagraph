from xyzdatagraph import *

# Only output is a .png file
def main():
    s = XYZDatagraph("Output/driver03")

    l = [
          [ 5,8,0.22460520019001806 ],
          [ 5,16,0.19083905808249857 ],
          [ 5,32,0.14876604376668032 ],
          [ 5,64,0.11138691439597544 ],
          [ 5,128,0.08921724482721335 ],
          [ 5,256,0.08252849840618463 ],
          [ 5,512,0.09389384489661114 ],
          [ 5,1024,0.1291728822423577 ]
        ]

    s.xyz(l)
    s.swapxz()
    s.swapxy()
    s.plotpng()

if __name__ == "__main__":
    main()
