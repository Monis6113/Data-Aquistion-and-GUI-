# Data-Aquistion-and-GUI-
This is a GUI for DAQ for our Formula Student car. I am attaching all my test GUI
Data-Acquisition-System-Telemetry
This project involves telemetry i.e transmission and reception of data from various sensors such as Battery Management System, Motor Control, Mass Flow Rate Sensor,Hall Effect Sensor etc to a remote computer using HC-12 module on UART serial communication protocol.

HARDWARE AND COMPONENTS

1.) Arduino UNO and Arduino MEGA 2560

![image](https://github.com/user-attachments/assets/c1b57924-bf67-44a5-82f0-f053c377c9af)
![image](https://github.com/user-attachments/assets/03bdeb3c-69f7-4870-8388-f332f84a511c)



2.) Arduino IDE Software
![image](https://github.com/user-attachments/assets/4f19198d-2294-451d-8975-dcade1f77f21) 


3.) Male to Female Jumper Wires
![image](https://github.com/user-attachments/assets/0c7f0865-f5d7-4ee9-8aa9-2ac6bf9da059)


4.)2 HC-12 Communication Modules
![image](https://github.com/user-attachments/assets/f5b063ac-85e1-4835-b5b6-d6ab02b46b21)

5.) Arduino USB Cable
![image](https://github.com/user-attachments/assets/27abe7d2-d16b-4d56-bca2-bc34b3f659f0)

CONNECTIONS

1)Connect the VCC pin of HC-12 module to 5V or 3.3 V of the Arduino board.
2)Connect the GND pin of HC-12 module to any of the GND port of the Arduino board to ensure common grounding.
3)Connect the RX pin to the digital pin 11 and the TX pin to the digital pin 10. 
![image](https://github.com/user-attachments/assets/a3bf95ca-ec49-4961-8fe2-0015e52a2061)
4)Power the Arduino Mega using LV(Low voltage) power supply from the power outlet whereas power the Arduino Uno using Arduino USB cable Type A to Type B. 
5) Open Arduino IDE software and choose appropriate Arduino Board and COM port to ensure correct serial values and uploading.

MY ROLE 
I undertook this aspect of the Data Acquisition system and UI Dashboard Creation where I published the Sender Code consisting of BMS,MFR,Motor Controller and Hall Effect Sensor data which is encapuslated and then sent in the form of a byte array.Also, I published the reciever code which decapsulates the data recieved on the HC-12 and then showcases it on the Serial Monitor.For this an important library needs to be installed :-https://downloads.arduino.cc/libraries/github.com/coryjfowler/mcp_can-1.5.0.zip  
