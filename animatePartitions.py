import turtle
import imageio
import os
import math

def draw_partition(partition, filename):
    window = turtle.Screen()
    window.setup(800, 800)
    window.clearscreen()  # Clear the screen
    window.bgcolor(0,0,0)

    
    t = turtle.Turtle()
    t.speed(0)
    t.hideturtle()
    t.goto((-405,-405))
    t.fillcolor("black")
    t.begin_fill()
    t.goto((-405,405))
    t.goto((405,405))
    t.goto((405,-405))
    t.end_fill()

    num_points = len(partition)
    angle_step = 360 / num_points

    colors = [
        (0.9, 0.7, 0.8),  # Pastel pink
        (0.7, 0.9, 0.7),  # Pastel green
        (0.7, 0.7, 0.9),  # Pastel blue
        (0.9, 0.9, 0.7),  # Pastel yellow
        (0.9, 0.7, 0.9),  # Pastel magenta
        (0.7, 0.9, 0.9),  # Pastel cyan
        (0.8, 0.7, 0.7),  # Pastel red
        (0.7, 0.8, 0.7),  # Pastel green
        (0.7, 0.7, 0.8),  # Pastel blue
        (0.8, 0.8, 0.7),  # Pastel yellow
        (0.8, 0.7, 0.8),  # Pastel magenta
        (0.7, 0.8, 0.8),  # Pastel cyan
    ]
    #inverted_colors = list(map(lambda x: (1-x[0], 1-x[1], 1-x[2]), colors))
    
    k = max(partition)+1

    blocks = []
    for i in range(k):
        blocks.append([])
    allpoints = []
    
    for i, block in enumerate(partition):
        angle = i * angle_step
        x = 200 * math.sin(math.radians(angle))
        y = 200 * math.cos(math.radians(angle))
        blocks[block].append((x,y))
        allpoints.append((x,y))
    
    t.pencolor("white")
    t.penup()
    centerx=[]
    centery=[]
    for i in range(k):
        t.fillcolor(*colors[i % len(colors)])  # Use contrasting colors
        t.goto(blocks[i][0])
        t.begin_fill()
        t.pensize(20)
        centerx.append(0)
        centery.append(0)
        for point in blocks[i]:
            t.goto(point)
            centerx[i] = centerx[i] + point[0]/float(len(blocks[i]))
            centery[i] = centery[i] + point[1]/float(len(blocks[i]))
        t.goto(blocks[i][0])
        t.end_fill()
    
    t.goto(allpoints[0])
    t.pensize(1)
    t.pencolor("white")
    t.pendown()
    for point in allpoints:
        t.goto(point)
    t.goto(allpoints[0])

    t.penup()
    for i, block in enumerate(partition):
        x = allpoints[i][0]
        y = allpoints[i][1]
        t.fillcolor(*colors[block % len(colors)])
        t.goto((x-5,y-5))
        t.tiltangle(180)
        t.begin_fill()
        t.pencolor("white")
        t.pendown()
        t.circle(10)
        t.end_fill()
        t.pencolor("black")
        t.write(i+1, align="center", font=("Arial",12,"normal"))
        t.penup()

    for i in range(k):
        t.goto((centerx[i]+10,centery[i]+10))
        t.pencolor("white")
        t.write(i+1,align="center", font=("Arial", 16, "bold"))

    window.getcanvas().postscript(file=filename + ".ps")
    window.getcanvas().postscript(file=filename + ".eps")
    img = imageio.imread(filename + ".eps")
    return img

def animate_partitions(partitions):
    images = []
    for i, partition in enumerate(partitions):
        img = draw_partition(partition, f"image_{i}")
        images.append(img)
    return images

def save_animation(partitions, filename):
    images = animate_partitions(partitions)
    imageio.mimsave(filename, images, duration=0.04, loop=0)
    # Clean up image files
    for i in range(len(partitions)):
        file = f"image_{i}.png"
        if os.path.exists(file):
            os.remove(file)
        file = f"image_{i}.eps"
        if os.path.exists(file):
            os.remove(file)
        file = f"image_{i}.ps"
        if os.path.exists(file):
            os.remove(file)


if __name__ == '__main__':
    partitions = [
        [[2,1,1,0,1,2,2,3],[3,1,1,0,1,2,2,3],[3,1,1,0,1,3,2,3],[3,1,0,0,1,3,2,3],[1,1,0,0,1,3,2,3],[1,1,1,0,1,3,2,3],[1,1,1,0,1,2,2,3]],
        [[0,0,1,2,2,3,3,4],[0,0,1,3,2,3,3,4],[0,0,1,3,2,2,3,4],[0,0,1,2,2,2,3,4]],
        [[3,0,0,1,3,2,2,3],[3,1,0,1,3,2,2,3],[3,3,0,1,3,2,2,3],[3,3,0,1,3,3,2,3],[3,1,0,1,3,3,2,3],[3,0,0,1,3,3,2,3]],
        [[1,0,1,1,2,2,3],[2,0,1,1,2,2,3],[2,0,0,1,2,2,3],[3,0,0,1,2,2,3],[3,0,0,1,3,2,3],[3,0,1,1,3,2,3],[1,0,1,1,3,2,3]],
        [[2,0,0,1,1,2],[2,1,0,1,1,2],[2,2,0,1,1,2],[2,2,0,2,1,2],[2,0,0,2,1,2]],
        [[2,0,1,1,2],[2,0,2,1,2],[0,0,2,1,2],[0,0,1,1,2],[1,0,1,1,2]]
    ]
    for i,partition in enumerate(partitions):
        save_animation(partition, f"animation_{i}.gif")