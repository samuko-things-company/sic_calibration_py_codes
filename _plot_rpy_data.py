import matplotlib.pyplot as plt
import matplotlib.animation as animation

import time
from sic_mpu9250_serial_comm import SIC # samuko IMU compute



def animate(i):
    global imu, axes, rollDataList, pitchDataList, yawDataList, dataPoints

    roll, pitch, yaw = imu.get('rpy-est') #without heading
    yaw = imu.get('heading') # with heading

    rollDataList.append(roll)
    pitchDataList.append(pitch)
    yawDataList.append(yaw)

    # Fix the list size so that the animation plot 'window' is x number of points
    rollDataList = rollDataList[-dataPoints:]
    pitchDataList = pitchDataList[-dataPoints:]
    yawDataList = yawDataList[-dataPoints:] 
    
    axes.clear()
    axes.plot(rollDataList)
    axes.plot(pitchDataList)
    axes.plot(yawDataList)
    
    axes.grid(which = "major", linewidth = 0.5)
    axes.grid(which = "minor", linewidth = 0.2)
    axes.minorticks_on()

    axes.set_ylim([-4,4]) # Set Y axis limit of plot
    axes.set_title("RPY Data") # Set title of figure
    axes.set_ylabel("angular pos (radians)") # Set title of y axis 
    axes.set_xlabel("number of data points") # Set title of z axis 

    axes.legend(["roll", "pitch", "yaw"], loc ="upper right")






# portName = '/dev/ttyACM0'
portName = '/dev/ttyUSB0'
imu = SIC(portName)

for i in range(15):
  time.sleep(1.0)
  print(i+1, " sec")
# time.sleep(30)

rollDataList = []
pitchDataList = []
yawDataList = []

dataPoints = 50
                                                        
fig = plt.figure()  # Create Matplotlib plots fig is the 'higher level' plot window
axes = fig.add_subplot(111) # Add subplot to main fig window


if __name__ == '__main__':
  ani = animation.FuncAnimation(fig, animate, frames=100, interval=50) 
  plt.show()
