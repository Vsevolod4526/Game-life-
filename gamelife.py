import random
import time
import numpy as np
import matplotlib.pyplot as plt

kadrov=500
k=50
spreadsheet=np.zeros((k,k),dtype=int)
memory_sheet=np.zeros([k,k],dtype=int)
big_fucking_data=np.zeros((kadrov+2,k,k),dtype=int)

for i in range(k):
    for j in range(k):
        cell=random.choice([1,0,0,0])
        spreadsheet[i][j]=cell
        
        
    
def print_first_4_kadr():
    for l in range(4):
        for i in range(k):
            for j in range(k):
                print(spreadsheet[l][i][j],end=' ')
            print()
        print()

def now_print_spreadsheet():
        for i in range(k):
            for j in range(k):
                print(spreadsheet[i][j],end=' ')
            print()
        print()



def podschet_ysloviy():
    for i in range(k):
        for j in range(k):
            memory_sheet[i][j]=0
            sum_life=0
            if i-1>=0 and j-1>=0:
                if spreadsheet[i-1][j-1]==1:
                    sum_life+=1
            if i-1>=0:
                if spreadsheet[i-1][j]==1:
                    sum_life+=1
            if i-1>=0 and j+1<=k-1:
                if spreadsheet[i-1][j+1]==1:
                    sum_life+=1
            if j+1<=k-1:
                if spreadsheet[i][j+1]==1:
                    sum_life+=1
            if j+1<=k-1 and i+1<=k-1:
                if spreadsheet[i+1][j+1]==1:
                    sum_life+=1
            if i+1<=k-1:
                if spreadsheet[i+1][j]==1:
                    sum_life+=1
            if i+1<=k-1 and j-1>=0:
                if spreadsheet[i+1][j-1]==1:
                    sum_life+=1
            if j-1>=0:
                if spreadsheet[i][j-1]==1:
                    sum_life+=1
            memory_sheet[i][j]=sum_life
def izmenenie():
    for i in range(k):
        for j in range(k):
            if memory_sheet[i][j]>3 or memory_sheet[i][j]<2:
                spreadsheet[i][j]=0
            if memory_sheet[i][j]==3:
                spreadsheet[i][j]=1
            
                
                
            
            
                
def sborka_programmi():
    for i in range(kadrov):
        
        podschet_ysloviy()
        
        izmenenie()
        big_fucking_data[i]=spreadsheet.copy()

#print_first_4_kadr()


sborka_programmi()



fig, ax = plt.subplots()

for i in range(kadrov-2):
    ax.cla()
    ax.imshow(big_fucking_data[i])
    ax.set_title("frame {}".format(i))
    # Note that using time.sleep does *not* work here!
    plt.pause(0.1)  
