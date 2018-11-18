
import RPi.GPIO as gpio
import time
import sys
import tkinter as tk
#from claw import *


def co(dir):
    clawOpen = True
    if clawOpen == True:
        gpio.setmode(gpio.BOARD)
        gpio.setup(3, gpio.OUT)
        p = gpio.PWM(3, 50) # GPIO 17 for PWM with 50Hz
        p.start(2.5) # Initialization
        reverse(1)
        p.ChangeDutyCycle(dir)
        time.sleep(10) # sleep 1 second
        p.stop()
        gpio.cleanup()
        clawOpen = False






def init():
    gpio.setmode(gpio.BOARD)
    gpio.setup(7, gpio.OUT)
    gpio.setup(11, gpio.OUT)
    gpio.setup(13, gpio.OUT)
    gpio.setup(15, gpio.OUT)
    

def forward(tf):
    init()
    gpio.output(7, False)
    gpio.output(11, True)
    gpio.output(13, True)
    gpio.output(15, False)
    time.sleep(tf)
    gpio.cleanup()
    
def reverse(tf):
    init()
    gpio.output(7, True)
    gpio.output(11, False)
    gpio.output(13, False)
    gpio.output(15, True)
    time.sleep(tf)
    gpio.cleanup()
    
def turn_left(tf):
    init()
    gpio.output(7, True)
    gpio.output(11, True)
    gpio.output(13, True)
    gpio.output(15, False)
    time.sleep(tf)
    gpio.cleanup()
    
def turn_right(tf):
    init()
    gpio.output(7, False)
    gpio.output(11, True)
    gpio.output(13, False)
    gpio.output(15, False)
    time.sleep(tf)
    gpio.cleanup()
    
    
def pivot_left(tf):
    init()
    gpio.output(7, True)
    gpio.output(11, False)
    gpio.output(13, True)
    gpio.output(15, False)
    time.sleep(tf)
    gpio.cleanup()
    
def pivot_right(tf):
    init()
    gpio.output(7, False)
    gpio.output(11, True)
    gpio.output(13, False)
    gpio.output(15, True)
    time.sleep(tf)
    gpio.cleanup()
gpio.cleanup()
co(2.5) #For closing
#co(12.5) #For opening   
reverse(1)   
'''  
def key_input(event):
    #init()
    print("Key:", event.char)
    key_press = event.char
    sleep_time = 0.030
    
    if key_press.lower() == "w":
        reverse(sleep_time)
    elif key_press.lower() == "s":
        forward(sleep_time)
    elif key_press.lower() == "a":
        turn_left(sleep_time)
    elif key_press.lower() == "d":
        turn_right(sleep_time)
    elif key_press.lower() == "q":
        pivot_left(sleep_time)
    elif key_press.lower() == "e":
        pivot_right(sleep_time)

    
    
forward(1)
fcommand = tk.Tk()
fcommand.bind("<KeyPress>", key_input)
fcommand.mainloop()
'''
    
