from gpiozero import CPUTemperature #Imports CPU Temperature Class
from time import sleep, strftime, time #Imports Time
import matplotlib.pyplot as plt

cpu = CPUTemperature() #Creates CPU Object in CPU Class

plt.ion()
x = []
y = []

def write_temp(temp):
  with open("/home/pi/cpu_temp.csv", "a") as log: #Change Directory if needed
    log.write("{0},{1}\n".format(strftime("%Y-%m-%d %H:%M:%S"),str(temp))) #Variable 'temp' has the CPU Temperature stored within it

def graph(temp):
  #This plots points on a graph
  y.append(temp)
  x.append(time())
  plt.clf()
  plt.scatter(x,y)
  plt.plot(x,y)
  plt.draw()

while True:
  temp = cpu.temperature
  write_temp(temp)
  graph(temp)
  plt.pause(1)