import tkinter as tk
import serial
import logging


# Configure logging
logging.basicConfig(filename='data.log', level=logging.INFO, format='%(asctime)s %(message)s')

# Create root window
root = tk.Tk()
root.withdraw() # Hide the root window

# Welcome window
def welcome_window():
    welcome = tk.Toplevel()
    welcome.geometry("600x400")
    welcome.configure(bg="white")
    welcome.title("Welcome to TDR-SDC!")

    
    # Create welcome message
    welcome_label = tk.Label(welcome, text="Welcome to TDR-SDC", font=("Helvetica", 36, "bold"), bg="white")
    welcome_label.pack(pady=(80, 20))



    # Create start button
    def start():
        welcome.destroy()
        main_window()

    start_button = tk.Button(welcome, text="Start", font=("Helvetica", 24), bg="#0077cc", fg="white", command=start)
    start_button.pack(pady=(0, 100))


    
# Main window
def main_window():
    main = tk.Toplevel()
    main.geometry("800x600")
    main.title("TDR-SDC Data Collection")

    # Set background image
    #background_image = tk.PhotoImage(file="index.jpeg")
    #background_label = tk.Label(main, image=background_image)
    #background_label.place(x=0, y=0, relwidth=1, relheight=1)

    # Create label for displaying the data
    value_label = tk.Label(main, text="SENSOR DATA", font=("Helvetica", 28, "bold"), bg="#0077cc", fg="white")
    value_label.pack(pady=(80, 40))



    # Open serial connection to Arduino
    ser = serial.Serial('COM3', 9600)

    # Function to read data from serial port and update label
    def update_label():
        #value = ser.readline().decode().strip()
        #value_label.config(text="Sensor Value: {}".format(value))
        #logging.info(value) # Log the data to a file
        #main.after(100, update_label)
        value1 = ser.readline().decode('ISO-8859-1').strip()
        value2 = ser.readline().decode('ISO-8859-1').strip()
        value3 = ser.readline().decode('ISO-8859-1').strip()
        value4 = ser.readline().decode('ISO-8859-1').strip()
        value5 = ser.readline().decode('ISO-8859-1').strip()
        value6 = ser.readline().decode('ISO-8859-1').strip()
        m=f"{value1} \n,{value2}\n,{value3}\n,{value4}\n,{value5}\n,{value6}"
        values = f"{value1},{value2},{value3}{value4}{value5}{value6}"
        value_label.config(text=m)
        logging.info(values) # Log the data to a file
        main.after(100, update_label)

    update_label()

welcome_window()

root.mainloop()
