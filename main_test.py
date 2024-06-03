import pygame
import time
from pymodbus.client.sync import ModbusTcpClient


# Initialize pygame and the joystick
pygame.init()
pygame.joystick.init()

# Configure Modbus TCP/IP
MODBUS_SERVER_IP = '192.168.1.100'  # Change this to the IP address of your Modbus server
MODBUS_PORT = 502

client = ModbusTcpClient(MODBUS_SERVER_IP, port=MODBUS_PORT)

# Check for joysticks
joystick_count = pygame.joystick.get_count()
if joystick_count == 0:
    print("No joystick detected.")
else:
    # Initialize the first joystick
    joystick = pygame.joystick.Joystick(0)
    joystick.init()
    
    print(f"Detected joystick: {joystick.get_name()}")

    try:
        while True:
            # Event processing
            pygame.event.pump()
            
            # Get the number of axes and buttons
            num_axes = joystick.get_numaxes()
            num_buttons = joystick.get_numbuttons()
            
            axis_values = []
            button_values = []

            # Collect axis values
            for i in range(num_axes):
                axis = joystick.get_axis(i)
                axis_values.append(int((axis + 1) * 32767 / 2))  # Normalize to 0-32767 range
                print(f"Axis {i}: {axis:.3f}")
            
            # Collect button values
            for i in range(num_buttons):
                button = joystick.get_button(i)
                button_values.append(button)
                print(f"Button {i}: {'Pressed' if button else 'Released'}")

            # Combine values into a single list
            values = axis_values + button_values

            # Send values over Modbus
            client.write_registers(0, values)
            
            # Wait for a short period to avoid flooding the output
            time.sleep(0.1)
            print("\n" + "="*20 + "\n")
    
    except KeyboardInterrupt:
        print("Program terminated.")
    
    finally:
        # Close the Modbus client
        client.close()
        # Quit pygame
        pygame.quit()
