import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle,Circle
import random
import numpy as np
import maze_makes

#Initalizing values

#border_origin = []
#border_size = []
border = []
start = []
goal = []
obstacles = []


def option_1():

    start1 = [8,8]
    
    goal1 = [43,43]

    Border1 = [[5, 5, 1, 40],
               [5, 45, 40, 1],
               [6, 5, 40, 1],
               [45, 6, 1, 40]]
    
    Obstacles1 = [[14.0, 12.0, 8.0, 2.0],
                  [12.0, 32.0, 8.0, 3.0],
                  [26.0, 17.0, 2.0, 12.0],
                  [32.0, 14.0, 10.0, 2.0],
                  [33.0,30.0,2.0,8.0]]
    
    return start1,goal1,Border1,Obstacles1


def option_2():

    start2 = [8,8]
    
    goal2 = [43,7.5]

    Border2 = [[5, 5, 1, 40],
               [5, 45, 40, 1],
               [6, 5, 40, 1],
               [45, 6, 1, 40]]

    Obstacles2 = [[20,0,10,37],
                  [6,15,10,3],
                  [12.5,30,10,3],
                  [30,30,8,3],
                  [37,15,8,3]]
    
    return start2,goal2,Border2,Obstacles2 


def option_3():

    start3 = [8,8]
    
    goal3 = [25,25]

    Border3 = [[5, 5, 1, 40],
               [5, 45, 40, 1],
               [6, 5, 40, 1],
               [45, 6, 1, 40]]
    
    Obstacles3 = [[20,8,1,23],
                  [21,30,13,1],
                  [33,13,1,18],
                  [21,18,8,1],
                  [11.5,6,1,30],
                  [38,11,1,28],
                  [18,35,20,1],
                  [0,5,50,1],
                  [0,39,50,1]]
    
    return start3,goal3,Border3,Obstacles3 


def disp_options():

    start1,goal1,Border1,Obstacles1 = option_1()
    start2,goal2,Border2,Obstacles2 = option_2()
    start3,goal3,Border3,Obstacles3 = option_3()

    fig, (ax1, ax2, ax3) = plt.subplots(1, 3)
    fig.suptitle('Choose a Map')
    ax1.set_title("Option 1")
    ax2.set_title("Option 2")
    ax3.set_title("Option 3")

    # #Making the Border
    # for (origx,origy,width,length) in Border1:
    #     ax1.add_patch(Rectangle((origx, origy), width, length,edgecolor='black',facecolor='black'))
    # for (origx,origy,width,length) in Border2:
    #     ax2.add_patch(Rectangle((origx, origy), width, length,edgecolor='black',facecolor='black'))
    # for (origx,origy,width,length) in Border3:
    #     ax3.add_patch(Rectangle((origx, origy), width, length,edgecolor='black',facecolor='black'))
    

    #Making obstacles
    for (origx,origy,width,length) in Obstacles1:
        ax1.add_patch(Rectangle((origx, origy), width, length,edgecolor='black',facecolor='black'))
    for (origx,origy,width,length) in Obstacles2:
        ax2.add_patch(Rectangle((origx, origy), width, length,edgecolor='black',facecolor='black'))
    for (origx,origy,width,length) in Obstacles3:
        ax3.add_patch(Rectangle((origx, origy), width, length,edgecolor='black',facecolor='black'))
    

    #Making Sart and Goal Points
    ax1.add_patch(Circle(start1, 1,edgecolor='blue',facecolor='blue',fill=True))
    ax1.add_patch(Circle(goal1, 1,edgecolor='green',facecolor='green',fill=True))
    ax2.add_patch(Circle(start2, 1,edgecolor='blue',facecolor='blue',fill=True))
    ax2.add_patch(Circle(goal2, 1,edgecolor='green',facecolor='green',fill=True))
    ax3.add_patch(Circle(start3, 1,edgecolor='blue',facecolor='blue',fill=True))
    ax3.add_patch(Circle(goal3, 1,edgecolor='green',facecolor='green',fill=True))


    #Setting Axis Range
    ax1.set_xlim([0, 50])
    ax1.set_ylim([0, 50])
    ax2.set_xlim([0, 50])
    ax2.set_ylim([0, 50])
    ax3.set_xlim([0, 50])
    ax3.set_ylim([0, 50])
 
    plt.show()



def default_parameters():
    print("Default parameter options:")
    print("CLose the Map window to choose an option")
    disp_options()
    option = input("Choose an option (1-3): ")
    if option == '1':
        start,goal,Border,Obstacles = option_1()
    elif option == '2':
        start,goal,Border,Obstacles = option_2()
    elif option == '3':
        start,goal,Border,Obstacles = option_3()
    else:
        print("Invalid option. Using default parameters for Option 1.")
        start,goal,Border,Obstacles = option_1()
    return start,goal,Border,Obstacles

def self_parameters():
    # Obstacles = []
    # obst = []

    # """border_origin = input("Enter Border Origin Points in space seperated X,Y Co-ordinates : ").split()
    # border_origin = [float(num) for num in border_origin]
    # border_size = input("Enter Border Size in space seperated values of Width and Height  : ").split()
    # border_size = [float(num) for num in border_size]"""

    # print("Borders of workspace are (5,5) and (45,45)")
    # start = input("Enter Starting Points in space seperated X,Y Co-ordinates : ").split()
    # start = [float(num) for num in start]
    # goal = input("Enter Destination Points in space seperated X,Y Co-ordinates : ").split()
    # goal = [float(num) for num in goal]
    # obs_no = input("Enter Number of Obstacles : ")

    # for i in range(int(obs_no)):
    #     print("Obstacle number ", i+1)
    #     obst = input("Enter [X Origin, Y Origin, Width, Height] of the Rectangular Obstacle :").split()
    #     obst = [float(num) for num in obst]
    #     Obstacles.append(obst)

    # """xb,yb = border_origin
    # wb,hb = border_size
    # Border = [[xb,yb,1,hb],
    #           [xb,yb+hb,wb,1],
    #           [xb+1,yb,wb,1],
    #           [xb+wb,yb+1,1,hb]]"""
    
    Border = [[5, 5, 1, 40],
          [5, 45, 40, 1],
          [6, 5, 40, 1],
          [45, 6, 1, 40]]
    
    
    start,goal,Obstacles = maze_makes.interactive_maze()
    plt.ioff()
              
    return start,goal,Border,Obstacles

def set_parameters():
    choice = input("Do you want default parameters? (y/n): ")
    if choice.lower() == 'y':
        start,goal,Border,Obstacles = default_parameters()
    elif choice.lower() == 'n':
        start,goal,Border,Obstacles = self_parameters()
    else:
        print("Invalid choice. Using default parameters.")
        start,goal,Border,Obstacles = default_parameters()
    
    print("Parameters:")
    print("Start:", start)
    print("Goal:", goal)
   # print("Border:", Border)
    print("Obstacles:", Obstacles)
    return start,goal,Border,Obstacles  


# Random Point Generator
def generate_random_point():
    x = random.randrange(0, 50)
    y = random.randrange(0, 50)
    return(x,y)
        
#Collision Checkers
def check_rect_collision(xp,yp, x, y, w, h):
    if xp >= x and xp <= x+w and yp >= y and yp <= y+h:
        return True
    return False

def check_line_collision(x1, y1, x2, y2, rx1, ry1, rx2, ry2):
    if (x1 < rx1 and x2 < rx1) or (x1 > rx2 and x2 > rx2) or \
       (y1 < ry1 and y2 < ry1) or (y1 > ry2 and y2 > ry2):
        return True
    return False

def point_collision(Obstacles):
    while True:
        counter = len(Obstacles)
        xp,yp,node_dist_array,xn,yn,min_dist_index = node_calculator()
        for i in range(len(Obstacles)):
            x,y,w,h = Obstacles[i]
            rx1 = x
            ry1 = y
            rx2 = rx1 + w
            ry2 = ry1 + h
            if check_rect_collision(xp,yp,x,y,w,h) == True or check_line_collision(node_list[min_dist_index][0],node_list[min_dist_index][1],xp,yp,rx1,ry1,rx2,ry2) == False:
                counter = counter-1
        if (counter == len(Obstacles)):
            break
        else:
            continue
    return xp,yp,node_dist_array,xn,yn,min_dist_index

#Caluclates Nodes based on Sample distance
def node_calculator():
    [xn,yn] = generate_random_point()
    node_dist_list = []
    
    for i in node_list:
        x = i[0]
        y = i[1]
        dist_from_node = (((xn - x)**2 +(yn - y)**2)**0.5)
        node_dist_list.append([round(dist_from_node,2)])
    node_dist_array = np.array(node_dist_list)
    min_dist_index = np.argmin(node_dist_array)  
    t = sample_dist/np.min(node_dist_array)
    node_x = ((1-t)*node_list[min_dist_index][0] + t*xn)
    node_y = ((1-t)*node_list[min_dist_index][1] + t*yn)
    if np.min(node_dist_array) >= 5: 
        return node_x,node_y,node_dist_array,xn,yn,min_dist_index
    else:
        return xn,yn,node_dist_array,xn,yn,min_dist_index

#Final Function

start,goal,Border,Obstacles = set_parameters()
x0,y0 = start
node_list = [[x0,y0,0,0]]
sample_dist = 5

while True:
    node_x,node_y,node_dist_array,xn,yn,min_dist_index = point_collision(Obstacles)
    sample_dist = 5
    if np.min(node_dist_array) >= 5:                                 # if distance less tham sample_dist
        if ((((node_x -goal[0])**2) + (node_y - goal[1])**2) <= (sample_dist/2)**2):
            node_list.append([round(node_x,2),round(node_y,2),min_dist_index,(len(node_list))])
            node_list.append([goal[0],goal[1],(len(node_list)-1),(len(node_list))])
            break
        else:
            node_list.append([round(node_x,2),round(node_y,2),min_dist_index,(len(node_list))])
    else:
            if ((((xn -goal[0])**2) + (yn - goal[1])**2) <= (sample_dist/2)**2):
                node_list.append((xn,yn,min_dist_index,len(node_list)))
                node_list.append([goal[0],goal[1],(len(node_list)-1),(len(node_list))])
                break
            else:
                node_list.append((xn,yn,min_dist_index,len(node_list)))

print(node_list)

#define Matplotlib figure and axis
fig, ax = plt.subplots()

#Making the Border
# for (origx,origy,width,length) in Border:
#     ax.add_patch(Rectangle((origx, origy), width, length,edgecolor='black',facecolor='black'))

#Making obstacles
for (origx,origy,width,length) in Obstacles:
    ax.add_patch(Rectangle((origx, origy), width, length,edgecolor='black',facecolor='black'))

#Making Sart and Goal Points
ax.add_patch(Circle(start, 1,edgecolor='blue',facecolor='blue',fill=True))
ax.add_patch(Circle(goal, 1,edgecolor='green',facecolor='green',fill=True))

# Plotting Tree
for i in node_list[1:]:
    ax.plot(i[0],i[1],"ro")
    xpoi = [node_list[i[2]][0],i[0]]
    ypoi = [node_list[i[2]][1],i[1]]
    ax.plot(xpoi, ypoi,"red")

#Getting Final Path
curr_index = (len(node_list) - 1)
curr_node = node_list[curr_index]
final_path = []
final_node = []
while True :
    final_path.append(curr_index)
    curr_node = node_list[curr_index]
    final_node.append(curr_node)
    curr_index = curr_node[2]
    if curr_index == 0:
        final_path.append(0)
        break

for i in final_node:
    ax.plot(i[0],i[1],"go")
    xpoi = [node_list[i[2]][0],i[0]]
    ypoi = [node_list[i[2]][1],i[1]]
    ax.plot(xpoi, ypoi,"green")

#Setting Axis Range
plt.xlim([0, 50])
plt.ylim([0, 50])
plt.show()