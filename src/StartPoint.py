import serial
import time


def sserial():
    try:
        ser = serial.Serial('/dev/ttyACM0', 115200)
        time.sleep(2)  
        return ser
    except serial.SerialException as e:
        print(f"Failed to connect: {str(e)}")
        return None
    
    
def initialize(ser):
    if ser:
        ser.write(b'$X\n')
        time.sleep(0.1)
        ser.write(b'$100=790\n')
        ser.write(b'G10 P0 L20 X0 Y0 Z0\n')
        
        
def MoveLeft(ser,distance):
    if ser:
        command = f'$J=G21G91X-{distance}F400\n'.encode()
        ser.write(command)
        time.sleep(2) 
  
 
 
def Light(ser):

 while True:
        
        ser.write(b'H')
        time.sleep(1)
        
        
        ser.write(b'L')
        
        time.sleep(1)    
        


    