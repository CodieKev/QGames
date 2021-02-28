#!/usr/bin/env python
# coding: utf-8

# # Imports

# In[1]:


from qiskit import QuantumRegister, ClassicalRegister
from qiskit import QuantumCircuit, execute, Aer
import numpy as np
import pygame
from math import *
import random
import os


# # Intializarion of Data and Constant

# In[2]:


xmin = ymin = 0

ymax = 700
p_y = 0.05*ymax
d_x = ymax/2-p_y#450
xmax = d_x*3
r_1 = 0.320*ymax                                        # Constant for the division between the circuit and gates
s_d = 0.112*ymax                                           # Constatnt for grids in the first 2 box 
Gate = 0
x_temp= y_temp = 0

x_c = []
y_c1 = []
y_c2 = []
x_gate = []
y_gate_1 = []
y_gate_2 = []
for i in range (4):
    y_c1.append(0.09*ymax+0.08*ymax*i)
    x_c.append((0.965+0.1*i)*ymax)
    y_c2.append(0.59*ymax+0.08*ymax*i)
for i in range(3):
    x_gate.append((0.965+0.1*i)*ymax)
    y_gate_1.append(ymax*0.435)
    y_gate_2.append(ymax*0.935)
y_c = [y_c1,y_c2]
y_gate=[y_gate_1,y_gate_2]
x_cancle = 1.265*ymax
y_cancle = [ymax*0.435,ymax*0.935]

### Image_Import###

H = pygame.image.load(os.path.join('Resource', 'H.jpg'))
X = pygame.image.load(os.path.join('Resource','X.jpg'))
D = pygame.image.load(os.path.join('Resource','D.jpg'))
C = pygame.image.load(os.path.join('Resource','C.png'))
coin = pygame.image.load(os.path.join('Resource','coin.jpg'))
player1_image = pygame.image.load(os.path.join('Resource','player.png'))
player2_image = pygame.image.load(os.path.join('Resource','player.jpg'))
one_image = pygame.image.load(os.path.join('Resource','1.jpg'))
two_image = pygame.image.load(os.path.join('Resource','2.jpg'))
three_image = pygame.image.load(os.path.join('Resource','3.jpg'))
blur_full = pygame.image.load(os.path.join('Resource','Blur_Full.jpg'))
blur_half = pygame.image.load(os.path.join('Resource','Blur_Half.jpg'))
bomb = pygame.image.load(os.path.join('Resource','bomb.jpg'))
blast = pygame.image.load(os.path.join('Resource','blast.jpg'))
p1_w = pygame.image.load(os.path.join('Resource','p1_w.jpg'))
p2_w = pygame.image.load(os.path.join('Resource','p2_w.jpg'))
player_one_text = pygame.image.load(os.path.join('Resource','player_one.jpg'))
player_two_text = pygame.image.load(os.path.join('Resource','player_two.jpg'))
heart = pygame.image.load(os.path.join('Resource','heart.jpg'))
board = pygame.image.load(os.path.join('Resource','Board.jpg'))


### Image_Resize

edge = int(0.07*ymax)
H = pygame.transform.scale(H, (edge, edge))
X = pygame.transform.scale(X, (edge, edge))
D = pygame.transform.scale(D, (edge, edge))
C = pygame.transform.scale(C, (edge, edge))
coin = pygame.transform.scale(coin, (floor(edge/2), floor(edge/2)))
player1_image = pygame.transform.scale(player1_image, (edge, edge))
player2_image = pygame.transform.scale(player2_image, (edge, edge))
one_image = pygame.transform.scale(one_image, (2*edge, 2*edge))
two_image = pygame.transform.scale(two_image, (2*edge, 2*edge))
three_image = pygame.transform.scale(three_image, (2*edge, 2*edge))
blur_full = pygame.transform.scale(blur_full, (int(xmax), int(ymax)))
blur_half = pygame.transform.scale(blur_half, (int(xmax), int(ymax/2)))
bomb = pygame.transform.scale(bomb, (edge, edge))
blast = pygame.transform.scale(blast, (edge, edge))
p1_w = pygame.transform.scale(p1_w, (edge*8, edge*8))
p2_w = pygame.transform.scale(p2_w, (edge*8, edge*8))
player_one_text = pygame.transform.scale(player_one_text, (int(0.25*ymax), int(0.035*ymax)))
player_two_text = pygame.transform.scale(player_two_text, (int(0.25*ymax), int(0.035*ymax)))
heart = pygame.transform.scale(heart, (int(0.03*ymax), int(0.03*ymax)))
board = pygame.transform.scale(board, (int(edge*6.5), int(edge*6.5)))


### Making List/tupels/grids So that its easire to get the image corrosponding to specific player
p_w = [p2_w,p1_w]
countdown_image = [three_image,two_image,one_image]
player_image = [player1_image,player2_image]
Gates_image = [H,X,D]
def grid_pos(x,y):
        temp_x_pos = []
        temp_y_pos = []
        for i in range(0,4):
            temp_x_pos.append(s_d*i+x)
            temp_y_pos.append(s_d*i+y)
        temp_x_pos.sort()
        temp_y_pos.sort()
        return(temp_x_pos,temp_y_pos)
coord_grid= [[[],[]],[[],[]]]
for i in range(2):
        for j in range(2):
            coord_grid[i][j] = grid_pos(d_x*i,j*ymax/2+p_y)


# # Structure of the Board

# In[23]:


def Structure():
    
    ### Comment out these 4 codes to remove the state show in each blocks ###
    
    #win.blit(board, (0, 0.05*ymax))
    #win.blit(board, (0.45*ymax, 0.05*ymax))
    #win.blit(board, (0, 0.55*ymax))
    #win.blit(board, (0.45*ymax, 0.55*ymax))
    
    ### Comment out above 4 codes to remove the state show in each blocks ###
    
    
    pygame.draw.line(win, (0,0,0), (0, ymax/2),(xmax,ymax/2), 2)   
    pygame.draw.line(win, (0,0,0), (d_x,p_y),(d_x,ymax/2), 5)
    pygame.draw.line(win, (0,0,0), (d_x*2,p_y),(d_x*2,ymax/2), 5)  
    pygame.draw.line(win, (0,0,0), (d_x,ymax/2+p_y),(d_x,ymax), 5)  
    pygame.draw.line(win, (0,0,0), (d_x*2,ymax/2+p_y),(d_x*2,ymax), 5)  

    pygame.draw.line(win, (0,0,0), (0,p_y),(xmax,p_y), 2)
    pygame.draw.line(win, (0,0,0), (0,ymax/2+p_y),(xmax,ymax/2+p_y), 2)
    # Division between the last box
    pygame.draw.line(win, (0,0,0), (d_x*2,r_1+p_y),(xmax,r_1+p_y), 2)
    pygame.draw.line(win, (0,0,0), (d_x*2,r_1+p_y+ymax/2),(xmax,r_1+p_y+ymax/2), 2)
    
    
    # Section in First and second Box 
    def grid(x,y):
        for i in range(1,4):
            pygame.draw.line(win, (0,0,0), (x,s_d*i+y),(x+d_x,s_d*i+y), 2)
            pygame.draw.line(win, (0,0,0), (s_d*i+x,y),(s_d*i+x,y+d_x), 2)
        return()
    
    for i in range(2):
        for j in range(2):
            grid(d_x*i,j*ymax/2+p_y)
            
            
    
    #Gates Position
    def gates(x,y):
        win.blit(H, (x+0.03*ymax, y+0.03*ymax)) 
        win.blit(X, (x+0.13*ymax, y+0.03*ymax)) 
        win.blit(D, (x+0.23*ymax, y+0.03*ymax))
        win.blit(C, (x+0.33*ymax, y+0.03*ymax))
                          
        return()
    gates(0.9*ymax,ymax*0.370)
    gates(0.9*ymax,ymax*0.870)
    
    # Qubit Wire
    for i in range (4):
        pygame.draw.line(win, (0,0,0), (d_x*2+0.0148148*xmax,0.09*ymax+0.08*ymax*i),((1-0.0148148)*xmax,0.09*ymax+0.08*ymax*i), 2)
        pygame.draw.line(win, (0,0,0), (d_x*2+0.0148148*xmax,0.59*ymax+0.08*ymax*i),((1-0.0148148)*xmax,0.59*ymax+0.08*ymax*i), 2)
    
    for i in range(len(x_c)):
        for j in range(len(y_c1)):
            pygame.draw.circle(win, (0,0,0), (x_c[i],y_c1[j]), 3)
            pygame.draw.circle(win, (0,0,0), (x_c[i],y_c2[j]), 3)
    
    return()


# # Important Functions

# In[4]:


### It Records and applies all the circuit part of the intraction wrt the position of defending player ###
def Gate_Intraction_part1(player_active):
    #gate = 0
    global Gate
    global temp_cons1
    global temp_cons2
    global player_mat
    global check_1
    xm_pos,ym_pos=pygame.mouse.get_pos()
    

    if pygame.mouse.get_pressed()[0]:
        
        if abs(xm_pos-x_cancle)<=(0.035*ymax) and abs(ym_pos - y_cancle[int(player_active-1)])<=(0.035*ymax):
            player_mat[player_active-1] = np.zeros((4,4))
            check_1 = True
        
        if Gate==0:
            for i in range(3):
                if abs(xm_pos-x_gate[i])<=(0.035*ymax) and abs(ym_pos - y_gate[int(player_active-1)][i])<=(0.035*ymax):
                    Gate = i+1
                    
        elif Gate ==3:
            for i in range(4):
                    for j in range(4):
                        if abs(xm_pos-x_c[i])<=(0.035*ymax) and abs(ym_pos - y_c[player_active-1][j])<=(0.035*ymax):
                            xm_pos = x_c[i]
                            ym_pos =  y_c[player_active-1][j]
                            temp_cons1 = j
                            temp_cons2 = i
                            for k in range(4):
                                if player_mat[player_active-1][k,i] !=0:
                                    #print(k,i)
                                    pygame.draw.line(win, (100,100,100), (x_c[i],y_c[player_active-1][j]),(x_c[i],y_c[player_active-1][k]), 3)
            win.blit(Gates_image[Gate-1], (xm_pos-0.035*ymax, ym_pos-0.035*ymax))
        else:
            for i in range(4):
                    for j in range(4):
                        if abs(xm_pos-x_c[i])<=(0.035*ymax) and abs(ym_pos - y_c[player_active-1][j])<=(0.035*ymax):
                            xm_pos = x_c[i]
                            ym_pos =  y_c[player_active-1][j]
                            temp_cons1 = j
                            temp_cons2 = i
            win.blit(Gates_image[Gate-1], (xm_pos-0.035*ymax, ym_pos-0.035*ymax))
    else:
        if Gate ==3 and abs(xm_pos-x_c[temp_cons2])<=(0.035*ymax) and abs(ym_pos - y_c[player_active-1][temp_cons1])<=(0.035*ymax):
            temp_const_0 = len(np.where(np.array(player_mat[player_active-1][:,temp_cons2]).flatten()!=0)[0])
            temp_const_1 = len(np.where(np.array(player_mat[player_active-1][:,temp_cons2]).flatten()==1)[0])
            temp_const_2 = len(np.where(np.array(player_mat[player_active-1][:,temp_cons2]).flatten()==2)[0])
            temp_const_3 = len(np.where(np.array(player_mat[player_active-1][:,temp_cons2]).flatten()==3)[0])
            if  temp_const_0 != 0 and temp_const_1+temp_const_2 ==1:
                if temp_const_1 ==1 and temp_const_3<1:
                    player_mat[player_active-1][temp_cons1,temp_cons2] = Gate
                    check_1 = True
                elif temp_const_2 ==1:
                    player_mat[player_active-1][temp_cons1,temp_cons2] = Gate
                    check_1 = True
            
        elif Gate!= 0 and abs(xm_pos-x_c[temp_cons2])<=(0.035*ymax) and abs(ym_pos - y_c[player_active-1][temp_cons1])<=(0.035*ymax) :
            if len(np.where(np.array(player_mat[player_active-1][:,temp_cons2]).flatten()==3)[0]) ==0:
                player_mat[player_active-1][temp_cons1,temp_cons2] = Gate
                check_1 = True
        Gate = 0 
    for i in range (len(x_c)):
        for j in range (len(x_c)):
            if player_mat[player_active-1][i,j]==3:
                for k in range (4):
                    if player_mat[player_active-1][k,j]!=0 and player_mat[player_active-1][k,j]!=3:
                        #print(i,k)
                        pygame.draw.line(win, (100,100,100), (x_c[j],y_c[player_active-1][i]),(x_c[j],y_c[player_active-1][k]), 3)
                win.blit(Gates_image[int(player_mat[player_active-1][i,j])-1], (x_c[j]-0.035*ymax, y_c[player_active-1][i]-0.035*ymax))
    
    
    for i in range (len(x_c)):
        for j in range (len(x_c)):
                  
            if player_mat[player_active-1][i,j]!=0and player_mat[player_active-1][i,j]!=3:
                win.blit(Gates_image[int(player_mat[player_active-1][i,j])-1], (x_c[j]-0.035*ymax, y_c[player_active-1][i]-0.035*ymax))
        
    return()


# In[5]:


### It Records and applies all the circuit part of the intraction wrt the bomb of attacking player ###
def Gate_Intraction_part2(player_active):
    #gate = 0
    global Gate
    global temp_cons1
    global temp_cons2
    global player_mat
    global check_1
    xm_pos,ym_pos=pygame.mouse.get_pos()
    

    if pygame.mouse.get_pressed()[0]:
        
        if abs(xm_pos-x_cancle)<=(0.035*ymax) and abs(ym_pos - y_cancle[int(player_active-1)])<=(0.035*ymax):
            player_mat[player_active-1] = np.zeros((4,4))
            check_1 = True
        
        if Gate==0:
            for i in range(3):
                if abs(xm_pos-x_gate[i])<=(0.035*ymax) and abs(ym_pos - y_gate[int(player_active-1)][i])<=(0.035*ymax):
                    Gate = i+1
        if Gate == 2:
            for i in range(4):
                    for j in range(4):
                        if abs(xm_pos-x_c[i])<=(0.035*ymax) and abs(ym_pos - y_c[player_active-1][j])<=(0.035*ymax):
                            xm_pos = x_c[i]
                            ym_pos =  y_c[player_active-1][j]
                            temp_cons1 = j
                            temp_cons2 = i
            win.blit(Gates_image[Gate-1], (xm_pos-0.035*ymax, ym_pos-0.035*ymax))
    else:            
        if Gate == 2 and abs(xm_pos-x_c[temp_cons2])<=(0.035*ymax) and abs(ym_pos - y_c[player_active-1][temp_cons1])<=(0.035*ymax) :
            if len(np.where(np.array(player_mat[player_active-1][:,temp_cons2]).flatten()==3)[0]) ==0:
                player_mat[player_active-1][temp_cons1,temp_cons2] = Gate
                check_1 = True
        Gate = 0 
    for i in range (len(x_c)):
        for j in range (len(x_c)):
            if player_mat[player_active-1][i,j]==3:
                for k in range (4):
                    if player_mat[player_active-1][k,j]!=0 and player_mat[player_active-1][k,j]!=3:
                        #print(i,k)
                        pygame.draw.line(win, (100,100,100), (x_c[j],y_c[player_active-1][i]),(x_c[j],y_c[player_active-1][k]), 3)
                win.blit(Gates_image[int(player_mat[player_active-1][i,j])-1], (x_c[j]-0.035*ymax, y_c[player_active-1][i]-0.035*ymax))
    
    
    for i in range (len(x_c)):
        for j in range (len(x_c)):
                  
            if player_mat[player_active-1][i,j]!=0and player_mat[player_active-1][i,j]!=3:
                win.blit(Gates_image[int(player_mat[player_active-1][i,j])-1], (x_c[j]-0.035*ymax, y_c[player_active-1][i]-0.035*ymax))
        
    return()


# In[6]:


def Coin_Position(player_active):
    global check_1
    if check_1:
        bool_grid[player_active-1] = val(result(circuit(player_mat[player_active-1]),100))
        check_1 = False
    coord_use = coord_grid[player_active-1][player_active-1]   
    
    for i in range (4):
        for j in range(4):
            if bool_grid[player_active-1][i,j]==1:
                win.blit(coin, (coord_use[0][j]+0.075*ymax, coord_use[1][i]+0.075*ymax)) 
    return()


# In[7]:


def circuit(mat):
    qc = QuantumCircuit(4,4)
    for i in range(4):
        temp_const_1 = list(np.where(np.array(mat[:,i]).flatten()==1)[0])
        temp_const_2 = list(np.where(np.array(mat[:,i]).flatten()==2)[0])
        temp_const_3 = list(np.where(np.array(mat[:,i]).flatten()==3)[0])
        
        
        if len(temp_const_1) != 0:
            if len(temp_const_3) ==0:
                qc.h(temp_const_1)
            else:
                qc.ch(temp_const_3,temp_const_1)
        if len(temp_const_2) != 0:
            if len(temp_const_3) != 0:
                qc.mcx(temp_const_3,temp_const_2)
            else:
                qc.x(temp_const_2)
        
    qc.measure([0,1,2,3],[0,1,2,3])
    return(qc)


# In[8]:


def result(circuit,counts):
    qc = circuit
    
    backend = Aer.get_backend('qasm_simulator')
    job = execute(qc, backend=backend,shots = counts)
    job_result = job.result()
    result = job_result.get_counts(qc)
    return(result)


# In[9]:


def val(result):
    p = np.array([0]*16)
    for i in range(16):
        x = np.binary_repr(i, width=4)
        if x in result:
            p[i] = 1
    p = p.reshape(4, 4)
    return(p)


# In[10]:


def position_check(bool_grid,pos):
    check_2 = False
    for i in range(-1,2):
        for j in range(-1,2):
            if -1<pos[0]-i<4 and -1<pos[1]-j<4:
                if bool_grid[pos[0]-i,pos[1]-j] == 1 and i+j+i*j!=0:
                    check_2 = True
                    break
    return((bool_grid[pos[1],pos[0]] ==1 and len(np.where(bool_grid==1)[0])!=1) or check_2 and len(np.where(bool_grid==1)[0])==1)
    
    


# In[11]:


def Coin_pos_Check(player_active):
    global check_3
    keys=pygame.key.get_pressed()
    if keys[pygame.K_RETURN]!= True and check_3 == 1:
        check_3 = 2

    if keys[pygame.K_RETURN]and check_3==0 and position_check(bool_grid[player_active-1],player_pos[player_active-1]):
        check_3 = 1
    
    elif keys[pygame.K_RETURN] and check_3 == 2:
        check_3 = 3
    


# In[12]:


def player_show_part1(player_active,player_passive):
    coord_use_active = coord_grid[player_active-1][player_active-1]
    win.blit(player_image[player_active-1], (coord_use_active[0][player_pos[player_active-1][0]]+0.025*ymax, coord_use_active[1][player_pos[player_active-1][1]]+0.025*ymax))
    coord_use_passive = coord_grid[player_passive-1][player_active-1]
    win.blit(player_image[player_passive-1], (coord_use_passive[0][player_pos[player_passive-1][0]]+0.025*ymax, coord_use_passive[1][player_pos[player_passive-1][1]]+0.025*ymax))


# In[13]:


def player_show_part2(player_active,player_passive):
    coord_use_active = coord_grid[player_active-1][player_passive-1]
    win.blit(player_image[player_active-1], (coord_use_active[0][player_pos[player_active-1][0]]+0.025*ymax, coord_use_active[1][player_pos[player_active-1][1]]+0.025*ymax))
    coord_use_passive = coord_grid[player_passive-1][player_passive-1]
    win.blit(player_image[player_passive-1], (coord_use_passive[0][player_pos[player_passive-1][0]]+0.025*ymax, coord_use_passive[1][player_pos[player_passive-1][1]]+0.025*ymax))


# In[14]:


def Bomb_Position(player_active,player_passive):
    global check_1
    if check_1:
        bool_grid[player_passive-1] = val(result(circuit(player_mat[player_passive-1]),1))
        check_1 = False
    coord_use = coord_grid[player_active-1][player_passive-1]   
    
    for i in range (4):
        for j in range(4):
            if bool_grid[player_passive-1][i,j]==1:
                win.blit(bomb, (coord_use[0][j]+0.025*ymax, coord_use[1][i]+0.025*ymax)) 
    return()


# In[15]:


def Blast_Position(blast_end,player_active,player_passive):
    coord_use_1 = coord_grid[player_active-1][player_passive-1] 
    coord_use_2 = coord_grid[player_active-1][player_active-1] 
    for i in blast_end:
        win.blit(blast, (coord_use_1[0][i[0]]+0.025*ymax, coord_use_1[1][i[1]]+0.025*ymax))
        win.blit(blast, (coord_use_2[0][i[0]]+0.025*ymax, coord_use_2[1][i[1]]+0.025*ymax))
    return()


# In[16]:


def blast_pos_list(player_passive):
    t = []
      
    for i in range (4):
        for j in range(4):
            if bool_grid[player_passive-1][i,j]==1:
                blast_end = [j,i]
    t.append(blast_end)
    if blast_end[0]-1>=0:
                t.append([blast_end[0]-1,blast_end[1]])
    if blast_end[1]-1>=0:
                t.append([blast_end[0],blast_end[1]-1])
    if blast_end[0]+1<4:
                t.append([blast_end[0]+1,blast_end[1]])
    if blast_end[1]+1<4:
                t.append([blast_end[0],blast_end[1]+1])
    return(t)
    


# In[17]:


def Bomb_Position_end(player_active,player_passive):
    coord_use_1 = coord_grid[player_active-1][player_passive-1] 
    coord_use_2 = coord_grid[player_active-1][player_active-1]   

    
    for i in range (4):
        for j in range(4):
            if bool_grid[player_passive-1][i,j]==1:
                win.blit(bomb, (coord_use_1[0][j]+0.025*ymax, coord_use_1[1][i]+0.025*ymax))
                win.blit(bomb, (coord_use_2[0][j]+0.025*ymax, coord_use_2[1][i]+0.025*ymax))
    return()


# In[18]:


def bomb_exit():
    global check_3
    keys=pygame.key.get_pressed()
    if keys[pygame.K_RETURN]!= True and check_3 == 5:
        check_3 = 6

    if keys[pygame.K_RETURN]and check_3==4 :
        check_3 = 5
    
    elif keys[pygame.K_RETURN] and check_3 == 6:
        check_3 = 7


# In[19]:


def Player_updated_pos(player_active):
    temp_const_3 = int(list(result(circuit(player_mat[player_active-1]),1).keys())[0],2)
    player_pos[player_active-1][1] = temp_const_3//4
    player_pos[player_active-1][0] = temp_const_3%4
    return()

    


# In[20]:


def finish_term(player_active,blast_cord):
    global Turn , check_3,check_4,player_mat,bool_grid ,health
    if player_pos[player_active-1] in blast_cord and health[player_active-1]==1:
        win.blit(p_w[player_active-1], (xmax/2-4*edge,ymax/2-4*edge))  
    else:
        if player_pos[player_active-1] in blast_cord:
            health[player_active-1] -=1
        Turn = (Turn)%2+1
        player_mat= [np.zeros((4,4)),np.zeros((4,4))]
        check_3 += 1
        check_4 = 0
        bool_grid = np.array([0]*16)
        bool_grid = bool_grid.reshape(4, 4)
        bool_grid = [bool_grid,bool_grid]
    return()


# In[21]:


def health_and_text():
    global health
    win.blit(player_one_text, (0,5))
    win.blit(player_one_text, (0,ymax/2+5))
    win.blit(player_two_text, (xmax-0.26*ymax,5))
    win.blit(player_two_text, (xmax-0.26*ymax,ymax/2+5))
    for i in range(len(health)):
        for j in range(health[i]):
                win.blit(heart, (((0.27*ymax+j*0.05*ymax)*abs(i-1))+i*(xmax-0.32*ymax-j*0.05*ymax),7))
                win.blit(heart, (((0.27*ymax+j*0.05*ymax)*abs(i-1))+i*(xmax-0.32*ymax-j*0.05*ymax),ymax/2+7))


    
    


# # Game Run

# In[22]:


player_mat= [np.zeros((4,4)),np.zeros((4,4))]
player_active = 1
bool_grid = np.array([0]*16)
bool_grid = bool_grid.reshape(4, 4)
bool_grid = [bool_grid,bool_grid]
temp_mat = 3*np.ones((4,4))
check_1 = True
check_3 = 0
check_4 = 0
Turn = 1
player1_pos = [0,0]
player2_pos = [0,0]
player_pos=[player1_pos , player2_pos]
health = [3,3]


pygame.init()
win = pygame.display.set_mode((int(xmax),int(ymax)))
pygame.display.set_caption("QGame_1")
time_delay = 10
run = True

while run:
    ##############
    pygame.time.delay(time_delay)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    win.fill((255,255,255))
    Structure()
    ##############
    if check_3 <3:
        if Turn ==1:
            player_defence = 1
            player_attack = 2
        else:
            player_defence = 2
            player_attack = 1
            

        Gate_Intraction_part1(player_defence)
        player_show_part1(player_defence,player_attack)
        Coin_Position(player_defence)
        #Player_updated_pos(player_active)
        Coin_pos_Check(player_defence)
        health_and_text()
        win.blit(blur_half, (0, (player_attack-1)*ymax/2+5))
        check_4=0
    if check_3 ==3:
        win.blit(blur_full, (0, 0))
        if check_4 <70:
            win.blit(countdown_image[0], (xmax/2-edge, ymax/2-edge))
        if 70<=check_4 <140:
            win.blit(countdown_image[1], (xmax/2-edge, ymax/2-edge))
        if 140<=check_4 <210:
            win.blit(countdown_image[2], (xmax/2-edge, ymax/2-edge))
        if check_4 == 210:
            check_3 = 4
        check_4 +=1
        check_1 = True
       
    if 4<=check_3 <7:
        health_and_text()
        win.blit(blur_half, (0, (player_defence-1)*ymax/2+5))
        player_show_part2(player_defence,player_attack)
        Gate_Intraction_part2(player_attack)
        Bomb_Position(player_defence,player_attack)
        bomb_exit()
        check_4 = 0
    if check_3 ==7:
        win.blit(blur_full, (0, 0))
        if check_4 <70:
            win.blit(countdown_image[0], (xmax/2-edge, ymax/2-edge))
        if 70<=check_4 <140:
            win.blit(countdown_image[1], (xmax/2-edge, ymax/2-edge))
        if 140<=check_4 <210:
            win.blit(countdown_image[2], (xmax/2-edge, ymax/2-edge))
        if check_4 == 210:
            check_3 = 8
        check_4 +=1
    if check_3==8:
        Player_updated_pos(player_defence)
        check_3 += 1
        check_4 = 0
    if check_3==9:
        health_and_text()
        player_show_part1(player_defence,player_attack)
        player_show_part2(player_defence,player_attack)
        Bomb_Position_end(player_defence,player_attack)
        check_4+=1
        if check_4 ==50:
            check_3 += 1
    if check_3 == 10:
        blast_cord = blast_pos_list(player_attack)
        check_3+=1
        check_4 = 0
    if check_3 == 11:
        check_4+=1
        if check_4<100:
            health_and_text()
            player_show_part1(player_defence,player_attack)
            player_show_part2(player_defence,player_attack)
            Blast_Position(blast_cord,player_defence,player_attack)
        if 100<=check_4<=200:
            health_and_text()
            player_show_part1(player_defence,player_attack)
            player_show_part2(player_defence,player_attack)
            
        if check_4 >200 and check_4%100<50:
            
            finish_term(player_defence,blast_cord)
    if check_3 ==12:
        win.blit(blur_full, (0, 0))
        if check_4 <70:
            win.blit(countdown_image[0], (xmax/2-edge, ymax/2-edge))
        if 70<=check_4 <140:
            win.blit(countdown_image[1], (xmax/2-edge, ymax/2-edge))
        if 140<=check_4 <210:
            win.blit(countdown_image[2], (xmax/2-edge, ymax/2-edge))
        if check_4 == 210:
            check_3 = 0
        check_4 +=1
        check_1 = True
            
    pygame.display.update()
pygame.quit()


# In[ ]:




