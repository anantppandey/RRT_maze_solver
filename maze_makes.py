# import matplotlib.pyplot as plt
# from matplotlib.patches import Rectangle,Circle
# import random
# import numpy as np

# #Initalizing values

# #border_origin = []
# #border_size = []
# border = []
# start = []
# goal = []
# obstacles = []




# start = [8,8]
    
# goal = [43,43]

# Border = [[5, 5, 1, 40],
#                [5, 45, 40, 1],
#                [6, 5, 40, 1],
#                [45, 6, 1, 40]]
    
# # Obstacles = [[14, 12, 8, 2],
# #                   [12, 32, 8, 3],
# #                   [26, 17, 2, 12],
# #                   [32, 14, 10, 2],
# #                   [33,30,2,8]]

# # Obstacles = [[20,0,10,37],
# #                   [6,15,10,3],
# #                   [12.5,30,10,3],
# #                   [30,30,8,3],
# #                   [37,15,8,3]]

# Obstacles = [[20,8,1,23],
#                   [21,30,13,1],
#                   [33,13,1,18],
#                   [21,18,8,1],
#                   [11.5,6,1,30],
#                   [38,11,1,28],
#                   [18,35,20,1],
#                   [0,5,50,1],
#                   [0,39,50,1]]
    
    

# #define Matplotlib figure and axis
# fig, ax = plt.subplots()

# # #Making the Border
# # for (origx,origy,width,length) in Border:
# #     ax.add_patch(Rectangle((origx, origy), width, length,edgecolor='black',facecolor='black'))

# #Making obstacles
# for (origx,origy,width,length) in Obstacles:
#     ax.add_patch(Rectangle((origx, origy), width, length,edgecolor='black',facecolor='black'))

# # #Making Sart and Goal Points
# # ax.add_patch(Circle(start, 1,edgecolor='blue',facecolor='blue',fill=True))
# # ax.add_patch(Circle(goal, 1,edgecolor='green',facecolor='green',fill=True))

# # # Plotting Tree
# # for i in node_list[1:]:
# #     ax.plot(i[0],i[1],"ro")
# #     xpoi = [node_list[i[2]][0],i[0]]
# #     ypoi = [node_list[i[2]][1],i[1]]
# #     ax.plot(xpoi, ypoi,"red")

# # #Getting Final Path
# # curr_index = (len(node_list) - 1)
# # curr_node = node_list[curr_index]
# # final_path = []
# # final_node = []
# # while True :
# #     final_path.append(curr_index)
# #     curr_node = node_list[curr_index]
# #     final_node.append(curr_node)
# #     curr_index = curr_node[2]
# #     if curr_index == 0:
# #         final_path.append(0)
# #         break

# # for i in final_node:
# #     ax.plot(i[0],i[1],"go")
# #     xpoi = [node_list[i[2]][0],i[0]]
# #     ypoi = [node_list[i[2]][1],i[1]]
# #     ax.plot(xpoi, ypoi,"green")

# #Setting Axis Range
# plt.xlim([0, 50])
# plt.ylim([0, 50])

# plt.show()






import matplotlib.pyplot as plt
import matplotlib.patches as patches

def interactive_maze():
    # Initialize the plot
    fig, ax = plt.subplots()
    ax.set_xlim(0, 50)
    ax.set_ylim(0, 50)
    ax.set_aspect('equal')


    # List to store rectangle parameters
    rectangles = []

    # Function to add a rectangle to the plot
    def add_rectangle(x, y, width, height):
        rect = patches.Rectangle((x, y), width, height, edgecolor='black', facecolor='black', alpha=0.5)
        ax.add_patch(rect)
        plt.draw()

    # Function to add a point to the plot
    def add_point(x, y, color):
        point = plt.Circle((x, y), 0.5, color=color)
        ax.add_patch(point)
        plt.draw()

    # Function to redraw all rectangles and points on the plot
    def redraw_rectangles():
        ax.clear()
        ax.set_xlim(0, 50)
        ax.set_ylim(0, 50)
        ax.set_aspect('equal')
        plt.gca().invert_yaxis()
        ax.axis('off')
        for rect_params in rectangles:
            add_rectangle(*rect_params)
        if 'start_point' in globals():
            add_point(start_point[0], start_point[1], 'blue')
        if 'goal_point' in globals():
            add_point(goal_point[0], goal_point[1], 'green')

    # Function to remove the last drawn rectangle
    def remove_last_rectangle():
        if rectangles:
            rectangles.pop()
            redraw_rectangles()
            print("Last rectangle removed.")
            draw_or_remove_rectangle()
        else:
            print("No rectangles to remove.")
            draw_or_remove_rectangle()

    # Function to ask user for next action after drawing or removing a rectangle
    def draw_or_remove_rectangle():
        next_action = input("Enter 'd' to draw another rectangle, 'r' to remove the last one, or 'f' to finish: ").strip().lower()

        if next_action == 'd':
            draw_rectangle()
        elif next_action == 'r':
            remove_last_rectangle()
        elif next_action == 'f':
            return
        else:
            print("Invalid input. Please enter 'd', 'r', or 'f'.")
            draw_or_remove_rectangle()

    # Function to draw a rectangle
    def draw_rectangle():
        x = float(input("Enter x coordinate of the origin: "))
        y = float(input("Enter y coordinate of the origin: "))
        orientation = input("Enter 'v' for vertical wall or 'h' for horizontal wall: ").strip().lower()
        if orientation == 'v':
            width = 2
            height = float(input("Enter height of the rectangle: "))
        elif orientation == 'h':
            width = float(input("Enter width of the rectangle: "))
            height = 2
        else:
            print("Invalid input. Please enter 'v' or 'h'.")
            draw_rectangle()
            return

        add_rectangle(x, y, width, height)
        rectangles.append([x, y, width, height])
        draw_or_remove_rectangle()

    # Start the interactive loop
    plt.ion()  # Turn on interactive mode
    plt.show()

    # Get user input for start and goal points
    start_x = float(input("Enter x coordinate of the start point: "))
    start_y = float(input("Enter y coordinate of the start point: "))
    goal_x = float(input("Enter x coordinate of the goal point: "))
    goal_y = float(input("Enter y coordinate of the goal point: "))

    # Draw start and goal points
    global start_point, goal_point
    start_point = (start_x, start_y)
    goal_point = (goal_x, goal_y)
    add_point(start_x, start_y, 'blue')
    add_point(goal_x, goal_y, 'green')

    # Initial prompt to draw or remove a rectangle
    draw_or_remove_rectangle()
    plt.close(fig)
    # Return the start point, goal point, and rectangles
    return start_point, goal_point, rectangles

if __name__ == "__main__":
    start, goal, rects = interactive_maze()
