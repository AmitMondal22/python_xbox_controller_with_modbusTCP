# Xbox 360 Controller Modbus Integration

This project integrates an Xbox 360 controller with a Modbus TCP server. The controller inputs are read using Pygame, and the data is updated in the Modbus server's registers. This can be useful for various applications that require remote control using a game controller.

## Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Code Overview](#code-overview)
  - [main.py](#mainpy)
  - [Key Components](#key-components)
- [Troubleshooting](#troubleshooting)
- [License](#license)
- [Contributing](#contributing)
- [Contact](#contact)

## Features

- Reads Xbox 360 controller inputs (buttons, axes, and hats).
- Updates Modbus holding registers with controller data.
- Supports multi-threading to handle Modbus server and joystick data concurrently.

## Requirements

- Python 3.x
- Pygame
- pyModbusTCP
- Xbox 360 controller

## Installation

### Clone the Repository

First, clone the repository to your local machine:

```bash
git clone https://github.com/yourusername/xbox-modbus-controller.git
cd xbox-modbus-controller
```


# Xbox 360 Controller Modbus TCP Interface

   This project connects an Xbox 360 controller to a Modbus TCP server, allowing the controller's inputs to update Modbus holding registers.

## Create and Activate a Virtual Environment

   Create a virtual environment to manage dependencies:

```bash
   python -m venv venv
```

   On Windows:

```bash
   venv\Scripts\activate
```
   On macOS and Linux:
```bash
   source venv/bin/activate
```

   Install Required Packages
   Install the necessary Python packages using pip:

```bash
   pip install pygame pyModbusTCP
```
   Configuration
   Update the IP address in the main.py file to match your server's IP address:

   python
   SERVER_HOST = '192.168.29.210'  # Change this to your server's IP address


## Usage
   Ensure Controller is Connected
   Make sure the Xbox 360 controller is properly connected to your system.

   Run the Script
   Execute the script to start reading controller inputs and updating the Modbus server:

```bash
    python main.py
```
   Monitor Console Output
   Press buttons on the Xbox 360 controller and observe the console output. The Modbus server will update its holding registers with the controller data.



## Code Overview


   ### main.py
       This script performs the following tasks:

       Initialization:

       Initializes Pygame and the Xbox 360 controller.
       Configures and starts a Modbus TCP server.
       Data Reading and Updating:

       Reads controller inputs (buttons, axes, and hats).
       Updates Modbus holding registers with the controller data.
       Multi-threading:

       Runs a separate thread to continuously update the Modbus server with joystick data.
       Handles Pygame events in the main loop.


   ### Key Components
       Button Names: Maps Xbox 360 controller buttons to their names for easier identification.
       Joystick Initialization: Sets up the Xbox 360 controller using Pygame.
       Modbus Server: Configures and starts the Modbus TCP server.
       Update Registers Function: A function that continuously updates the Modbus holding registers with joystick data in a separate thread.
       Main Loop: Handles Pygame events (button presses, axis movements, hat motions) and updates the respective values.

       
## Troubleshooting
   Common Issues
   Controller Not Detected:
   Ensure the Xbox 360 controller is properly connected and recognized by your operating system. You may need to install additional drivers.

   Modbus Connection Issues:
   Verify the IP address and port configuration in the main.py file. Ensure your firewall settings allow communication through the specified IP and port.

## License
   This project is licensed under the MIT License. See the LICENSE file for more details.

## Contributing
   Contributions are welcome! Please fork the repository and submit a pull request for review. Make sure to follow the project's coding standards and include appropriate tests.

## Contact
   For any questions or suggestions, please contact your-email@example.com.

   Note: This project requires an Xbox 360 controller and a network setup that supports Modbus TCP communication. Ensure your firewall settings allow communication through the specified IP and port.



Replace `"https://github.com/AmitMondal22/python_xbox_controller_with_modbusTCP.git"` with the actual URL of your GitHub repository and `[info@example.com](mailto:your-email@example.com)` with your actual contact email address. This detailed `README.md` file provides comprehensive instructions and information about the project.