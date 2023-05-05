import tkinter as tk
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import logging
import serial
import datetime
import math
# Configure logging
logging.basicConfig(filename='data.log', level=logging.INFO, format='%(asctime)s %(message)s')
def start_button_clicked(event):
    print("Start button clicked!")
    root.withdraw()
    ui_window()
# ----------------------------------------------Create the intro window----------------------------------------------
root = tk.Tk()
root.title("TDR - SDC")
# Define the label widget
value_label = tk.Label(root, text="")
value_label.pack()


#----------------------------------------------bg----------------------------------------------
# Get the screen width and height
screen_width, screen_height = 800, 450
root.geometry("%dx%d" % (screen_width, screen_height))
#make bg dimentions equal to window
bg_image_pg1 = Image.open("dash pg1.png")
if bg_image_pg1.size != (screen_width, screen_height):
    bg_image_pg1 = bg_image_pg1.resize((screen_width, screen_height), Image.LANCZOS)
bg_image_pg1 = ImageTk.PhotoImage(bg_image_pg1)
#Adding background image in form of a label
bg_label_pg1 = ttk.Label(root, image = bg_image_pg1)
bg_label_pg1.place(x=0, y=0, relwidth=1, relheight=1)
bg_label_pg1.image = bg_image_pg1
#----------------------------------------------window align on screen----------------------------------------------
# Set the window size and position
# window_width = 300
# window_height = 200
# window_x = (screen_width - window_width) // 2
# window_y = (screen_height - window_height) // 2
# root.geometry(f"{window_width}x{window_height}+{window_x}+{window_y}")
#----------------------------------------------start button----------------------------------------------
# import the Start button image
start_button_image = Image.open("start button red bg.png")
start_button_image = start_button_image.resize((110, 60), Image.LANCZOS)
start_button_image = ImageTk.PhotoImage(start_button_image)
# Create a canvas to hold the start button image
start_button_canvas = tk.Canvas(root, width=start_button_image.width(), height=start_button_image.height(), bg='white', highlightthickness=0)
start_button_canvas.pack()
# Add the image to the canvas
start_button_canvas.create_image(0, 0, anchor='nw', image=start_button_image)
start_button_canvas.place(relx=0.5, rely=0.60, anchor="center")
# Bind the button click event to the function
start_button_canvas.bind("<Button-1>", start_button_clicked)
# create the Start button with image
# start_button = tk.Button(root, image=start_button_image, bg = 'white',relief=tk.FLAT, command=start_button_clicked)
# start_button.pack()
# start_button.place(relx=0.5, rely=0.60, anchor="center")
#----------------------------------------------intro window ends----------------------------------------------
def ui_window(): 
#----------------------------------------------create central window----------------------------------------------
    central_window = tk.Toplevel()  # Create a new top-level window
    central_window.title("TDR - SDC")  # Set the title of the new window
    central_window.geometry("800x450")
#----------------------------------------------central window bg----------------------------------------------
    #make bg dimentions equal to window
    bg_image_pg2 = Image.open("dash pg2.png")
    if bg_image_pg2.size != (800, 450):
         bg_image_pg2 = bg_image_pg2.resize((800, 450), Image.LANCZOS)
    bg_image_pg2 = ImageTk.PhotoImage(bg_image_pg2)
    #Adding background image in form of a label
    bg_label_pg2 = tk.Label(central_window, image = bg_image_pg2)
    bg_label_pg2.place(x=0, y=0, relwidth=1, relheight=1)
    bg_label_pg2.image = bg_image_pg2
#----------------------------------------------get arduino data---------------------------------------------- 
    """
    # Serial communication settings
    ser = serial.Serial('/dev/ttyACM0', 9600)  # Update with the correct port and baud rate for your Arduino   
    # Create label to display data 1
    label_data1 = tk.Label(central_window, text="1st value: ")
    label_data1.pack()
    #label_data1.place(relx=0.5, rely=0.60, anchor="center")
    # Create label to display data 2
    label_data2 = tk.Label(central_window, text="2nd value: ")
    label_data2.pack()
    #label_data2.place(relx=0.6, rely=0.70, anchor="center")
    # Function to update data from Arduino
    def update_data():
        if ser.in_waiting:
            data = ser.readline().decode().strip().split(",")  # Read and decode the data from Arduino
            print(data)

            if len(data) == 2:
               label_data1.config(text = data[0])  # Update label with pin 2 value
               label_data2.config(text = data[1])  # Update label with pin 3 value
            update_data()
    

    # Start data update
    update_data()"""
    
    #----------------------------------------------data retrieval bypass----------------------------------------------
    # Create label to display BATTERY VOLTAGE
    label_data_battery_voltage = tk.Label(central_window, text="BV", bg="black", fg="red")
    label_data_battery_voltage.place(relx=0.13, rely=0.18, anchor="center")
    # Create label to display ACCUMULATOR TEMPERATURE
    label_data_accumulator_temperature = tk.Label(central_window, text="AT")
    label_data_accumulator_temperature.place(relx=0.4, rely=0.18, anchor="center")
    # Create label to display BATTERY CURRENT
    label_data_battery_current = tk.Label(central_window, text="BC")
    label_data_battery_current.place(relx=0.66, rely=0.18, anchor="center")
    # Create label to display RPM
    label_data_rpm = tk.Label(central_window, text="RPM", font=("Arial", 30))
    label_data_rpm.place(relx=0.62, rely=0.72, anchor="center")
    # Create label to display speed
    label_data_speed = tk.Label(central_window, text="SPD", font=("Arial", 45))
    label_data_speed.place(relx=0.83, rely=0.66, anchor="center")
    # Create label to display brake pressure
    label_data_brake_pressure = tk.Label(central_window, text="BP")
    label_data_brake_pressure.place(relx=0.46, rely=0.794, anchor="center")
    # Create label to display fluid speed
    label_data_fluid_speed = tk.Label(central_window, text="FS")
    label_data_fluid_speed.place(relx=0.385, rely=0.89, anchor="center")
    # Create label to display MOTOR TEMP
    label_data_motor_temperature = tk.Label(central_window, text="MT")
    label_data_motor_temperature.place(relx=0.24, rely=0.46, anchor="center")
    # Create label to display MOTOR controller TEMP
    label_data_motor_controller_temperature = tk.Label(central_window, text="MCT")
    label_data_motor_controller_temperature.place(relx=0.54, rely=0.46, anchor="center")
    # Create label to display lv battery status
    label_data_LV_battery_status = tk.Label(central_window, text="LVBS")
    label_data_LV_battery_status.place(relx=0.48, rely=0.71, anchor="center")
    # Create label to display THERMISTOR MAX TEMP
    label_data_thermistor_max_temperature = tk.Label(central_window, text="TMT")
    label_data_thermistor_max_temperature.place(relx=0.55, rely=0.975, anchor="center")  

    # Open serial connection to Arduino
    ser = serial.Serial('COM6', 9600)

    # Function to read data from serial port and update label
    def update_label():
    #value = ser.readline().decode().strip()
    #value_label.config(text="Sensor Value: {}".format(value))
    #logging.info(value) # Log the data to a file
    #main.after(100, update_label)
        value1 = ser.readline().decode().strip()
        value2 = ser.readline().decode().strip()
        value3 = ser.readline().decode().strip()
        value4 = ser.readline().decode().strip()
        value5 = ser.readline().decode().strip()
        value6 = ser.readline().decode().strip()
        value7 = ser.readline().decode().strip()
        value8 = ser.readline().decode().strip()
        value9 = ser.readline().decode().strip()
        value10 = ser.readline().decode().strip()
        value11 = ser.readline().decode().strip()
        values = f"battery_voltage: {value1}, accumulator_temperature: {value2},battery_current: {value3},rpm: {value4},speed: {value5},brake_pressure: {value6},fluid_speed: {value7},motor_temperature: {value8}, motor_controller: {value9}, LV_battery_status: {value10}, thermistor_max_temperature: {value11} "
        value_label.config(text=values)
        logging.info(values) # Log the data to a file
            #----------------------------------------------data updation----------------------------------------------
         # Function to update data from Arduino
        def update_data():
                data = [value1,value2,value3,value4,value5,value6,value7,value8,value9,value10,value11]
                
                print(data)
                label_data_battery_voltage.config(text = data[0])  # Update label with pin 2 value
                label_data_accumulator_temperature.config(text = data[1])  # Update label with pin 3 value
                label_data_battery_current.config(text = data[2])  # Update label with pin 3 value
                label_data_rpm.config(text = data[3])
                label_data_speed.config(text = data[4])
                label_data_brake_pressure.config(text = data[5])
                label_data_fluid_speed.config(text = data[6])
                label_data_motor_temperature.config(text = data[7])
                label_data_motor_controller_temperature.config(text = data[8])
                label_data_LV_battery_status.config(text = data[9])
                label_data_thermistor_max_temperature.config(text = data[10])

        update_data()
        root.after(110, update_label)

    update_label()
        


# Start the Tkinter event loop
root.mainloop()
