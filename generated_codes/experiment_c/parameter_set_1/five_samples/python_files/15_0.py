'''
Example 3 : Cops in house 10 can cover houses 1 to 17, and cops in house 51 can cover houses 41 to 66. So, in total 9 houses are safe.
'''

#importing numpy for array
import numpy as np

#importing matplotlib for plotting the graph
import matplotlib.pyplot as plt

def main():
    #taking number of test cases
    t=int(input())
    #for each test case
    for i in range(t):
        #taking number of cops(M), maximum speed of cops(x) and maximum time given to thief to hide(y)
        M,x,y=map(int,input().split())
        #taking house numbers where cops are residing
        cops=np.array(list(map(int,input().split())))
        #initializing an array with all the house numbers
        houses=np.arange(1,101)
        #initializing an empty array
        safe_houses=np.array([],dtype=np.int64)
        #for each cop
        for j in cops:
            #adding indices of safe houses to the array
            safe_houses=np.append(safe_houses,np.where((houses<(j-x*y))|(houses>(j+x*y)))[0])
        #printing number of safe houses
        print(len(safe_houses))
        #plotting the graph
        plt.plot(safe_houses,[0]*len(safe_houses),'go')
        plt.plot(houses,[0]*len(houses),'r.')
        plt.show()

if __name__=='__main__':
    main()