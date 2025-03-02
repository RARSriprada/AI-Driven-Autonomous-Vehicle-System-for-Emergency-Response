# AI-Driven Autonomous Vehicle System for Emergency Response

## Overview
This project simulates an AI-driven autonomous vehicle system designed to clear the path for an emergency vehicle, such as an ambulance. The system detects nearby vehicles and autonomously instructs them to change lanes, ensuring an unobstructed route for the ambulance. The implementation leverages **Python with Pygame**, simulating real-time traffic scenarios where vehicles react dynamically to an approaching ambulance.

## Features
- **Autonomous Traffic Navigation**: Vehicles move independently within designated lanes.
- **AI-Based Detection**: Vehicles detect the ambulance and react accordingly.
- **Dynamic Lane Changing**: When the ambulance approaches, detected vehicles shift lanes to make way.
- **Zoom-In Effect**: The camera zooms in when the ambulance gets close to other vehicles for enhanced visibility.

## Technologies Used
- **Python**
- **Pygame** (for visualization and simulation)
- **Randomized AI Behavior**

## Installation
1. Install Python (if not already installed).
2. Install Pygame using:
   ```sh
   pip install pygame
   ```
3. Clone this repository:
   ```sh
   git clone https://github.com/yourusername/ambulance-ai.git
   cd ambulance-ai
   ```
4. Run the simulation:
   ```sh
   python main.py
   ```

## How It Works
- The system initializes multiple vehicles moving within predefined lanes.
- The ambulance starts moving from the top of the screen.
- When an ambulance is detected near a vehicle, the vehicle shifts lanes to clear the path.
- The zoom effect activates when the ambulance gets close to traffic, enhancing visibility.

## Future Enhancements
- Implement **sensor-based decision-making** using real-world data.
- Introduce **reinforcement learning** for improved vehicle behavior adaptation.
- Extend to **multi-lane complex traffic scenarios** with real-world parameters.



