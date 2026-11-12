import pygame
import math
import json
import random
import sys

window = pygame.display.set_mode((1000,700))
clock = pygame.time.Clock()
exit_window = False
width = window.get_width()
height = window.get_height()
# freq = [1,1.1,2,1,2,1]
# freq = [1,0,-1,2,-2]
# inital = [0,0,0,0,0]
# radius = [
#     -12.64 + 20.90j,
#     10.72+16.52j,
#     -135.66 - 45.57j,
#     -44.85 - 23.71j,
#     66.75 - 53.07j]
freq = []
radius = []
inital = []
dt = 1/300
lines = []
append = True
count = 0
colors = []


#array = [data["x"][i] + data["y"][i]*1j for i in range(len(data["x"]))]
# array = []
FILENAME = sys.argv[1]
# FILENAME = 'data.json'
with open(FILENAME) as f:
    data = json.load(f)
    f.close()

contor = [
    -100,-100,
     100,-100,
     100, 100,
    -100, 100,
    -100,-100]
contor = [2*i for i in contor]

array = [i - 300 + 1j*j - 340j for i,j in data]
const = sum(array)/len(array)
#array = [i - const for i in array]
#print(array)

# for i in range(4):
#     start_x , start_y = contor[2*i:2*i+2]
#     end_x,end_y = contor[2*i+2 : 2*i+4]
#     steps = 100
#     dx = (end_x-start_x)/steps
#     dy = (end_y-start_y)/steps
#     print(dx,dy)
#     for i in range(steps):
#         final = (start_x+dx*i) + (start_y + dy*i)*1j
#         array.append(final)





# print(array)
N = len(array)
print(N)
for i in range(-500,500):
    sum = complex(0)
    for k in range(N):
        phi = -2*math.pi*i*k/N
        comp = math.cos(phi) - 1j*math.sin(phi)
        sum += comp*array[k]
    sum /= N
    mag = abs(sum)
    phase = math.atan2(sum.imag,sum.real)

    index = 0
    mini = None
    while(index<len(radius)):
        if mag > radius[index]:
            mini = index
            break
        index += 1

    if mini == None:
        radius.append(mag)
        inital.append(phase)
        freq.append(i)
    else:
        radius.insert(mini,mag)
        inital.insert(mini,phase)
        freq.insert(mini,i)
    colors.append((100,100,100))

# print(colors)
# print(inital)
#radius = [100,100]
#inital = [0,0]
#freq = [1,(math.sqrt(5)+1)/2]
#print(freq)

while not exit_window:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_window = True
    window.fill((0,0,0,255))

    i_x , i_y = window.get_width()//2,window.get_height()//2
    # i_x , i_y = 0,0
    for i in range(len(freq)):
        pygame.draw.circle(window,colors[i],(i_x,i_y),abs(radius[i]),1)
        comp = radius[i]*math.e**(inital[i]*1j)
        new_x,new_y = comp.real + i_x,comp.imag + i_y
        pygame.draw.line(window,(255,255,255,255),(i_x,i_y),(new_x,new_y))
        inital[i] += 2*math.pi*freq[i]*dt
        i_x,i_y = new_x,new_y



    if append:
        lines.append((i_x,i_y))
    if len(lines) > 2:
        pygame.draw.lines(window,(40,163,255),False,lines)
    
    if len(lines) > count+1 and append:
        if int(lines[count][0]) == int(i_x) and int(lines[count][1]) == int(i_y):
            count += 1
        else :
            count = 0
    if count>2 and append:
        append = False
        print("Stopped")
    if len(lines) > 100000:
        lines.pop(0)

    # print(lines)

    pygame.display.update()
    clock.tick(60)
    
