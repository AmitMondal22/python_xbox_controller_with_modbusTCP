import time
import pygame
from pyModbusTCP.server import ModbusServer, DataBank
import threading

# Initialize pygame and joystick
pygame.init()
pygame.joystick.init()
joystick = pygame.joystick.Joystick(0)
joystick.init()

# Modbus server configuration
SERVER_HOST = '192.168.29.210'  # Change this to your server's IP address
SERVER_PORT = 502
server = ModbusServer(host=SERVER_HOST, port=SERVER_PORT, no_block=True)

# Start the Modbus server
server.start()

# Function to update Modbus registers with joystick data
def update_registers():
    # Read joystick data
    axis_values = [int(joystick.get_axis(i) * 100) for i in range(joystick.get_numaxes())]
    button_values = [int(joystick.get_button(i)) for i in range(joystick.get_numbuttons())]
    hat_values = [hat_val for hat_val in joystick.get_hat(0)]  # Assuming there's only one hat on the joystick
    values = axis_values + button_values + hat_values

    # Print the data being sent
    print("Sending data:", values)

    # Update Modbus holding registers using instance method
    server.data_bank.set_holding_registers(0, values)

# Main loop to handle events
try:
    while True:
        for event in pygame.event.get():
            if event.type == pygame.JOYAXISMOTION or event.type == pygame.JOYBUTTONDOWN or event.type == pygame.JOYHATMOTION:
                # Call the function to update Modbus registers when there's a joystick event
                update_registers()
        time.sleep(0.01)  # Add a small delay to avoid consuming too much CPU
except KeyboardInterrupt:
    server.stop()
    pygame.quit()
