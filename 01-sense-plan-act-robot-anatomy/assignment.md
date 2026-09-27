# Session 1 Lab: Unboxing, Setup & First Program

**Course:** Introduction to Robotics (Freshman Seminar) — Week 1, Session 1
**Duration:** ~60–75 minutes (lab portion, following the 15-minute lecture)
**Robot:** SparkFun XRP (RP2040/RP2350, MicroPython)

## Learning Objectives

By the end of this lab, you should be able to:

1. Identify the physical subsystems of the XRP (perception, computation, actuation, communication, power) on your own robot.
2. Physically assemble the XRP kit from its unboxed parts.
3. Connect your laptop to the XRP and open the MicroPython web editor.
4. Write, save, and run a simple MicroPython program on the XRP that blinks the onboard LED and prints one live sensor reading to the console.
5. Explain, in your own words, how this first program is a tiny example of the sense-plan-act loop.

## Materials / Starter Code Needed

- 1x SparkFun XRP kit (chassis, two motor/wheel assemblies, battery pack, ultrasonic sensor, IMU (built-in), line/reflectance sensor, servo, screws/standoffs, USB cable)
- 1x laptop with a modern web browser (Chrome or Edge recommended) and WiFi
- Access to the XRP MicroPython web editor (instructor will provide the URL/link)
- Starter file `blink_and_sense.py` (provided by instructor, or written from scratch following the steps below)
- Phillips screwdriver (provided at your station)

## Step-by-Step Instructions

### Part A — Unbox and Assemble (~20 min)

1. Open your kit box and lay out all parts on your table. Check them against the parts checklist taped to your station.
2. Attach the two motor/wheel assemblies to the chassis using the provided screws. Make sure wheels spin freely once mounted.
3. Mount the main board (RP2040/RP2350 controller) onto the chassis standoffs.
4. Connect the ultrasonic sensor to its port on the board, facing forward on the chassis.
5. Connect the line/reflectance sensor underneath the chassis, facing down.
6. Attach the servo to its mounting point (no attachment arm needed yet — just the servo body).
7. Install the battery pack and connect it to the board's power input, but leave the robot powered OFF for now.
8. Raise your hand for an instructor check before powering on — we'll do a quick visual inspection of every connection.

### Part B — Set Up the MicroPython Web Editor (~15 min)

1. Power on your XRP using its power switch.
2. On your laptop, connect to the XRP's WiFi network (network name/password is on your station card) — this is the robot's built-in **communication** subsystem at work.
3. Open a browser and navigate to the MicroPython web editor URL provided by your instructor.
4. Confirm the editor shows a connected status to your XRP (green "connected" indicator or equivalent).
5. Open the built-in file browser in the editor and confirm you can see the robot's existing files (e.g., `main.py`).

### Part C — Write Your First Program (~15–20 min)

1. Create a new file in the editor named `blink_and_sense.py`.
2. Write a program that does the following in a loop:
   - Turns the onboard LED on, waits half a second, turns it off, waits half a second (a blink).
   - Reads one live value from a sensor (recommend the ultrasonic distance sensor, or the IMU if your station is assigned that instead).
   - Prints that sensor reading to the console using `print()`.
3. A minimal example structure (fill in the actual sensor/LED calls using the XRP library reference sheet at your station):

```python
from machine import Pin
import time
# import the XRP board/sensor library as shown on your reference sheet

led = Pin("LED", Pin.OUT)   # adjust pin name per XRP docs

while True:
    led.value(1)
    time.sleep(0.5)
    led.value(0)
    time.sleep(0.5)

    distance = 0  # replace with real ultrasonic sensor read call
    print("Distance reading:", distance)
```

4. Save the file and run it on the XRP using the editor's Run button.
5. Watch the console output and the onboard LED simultaneously.
6. Stop the program, and in a one-sentence comment at the top of your file, explain which part of your code is "sense," which is "plan," and which is "act." (Hint: even a fixed blink timing counts as a simple "plan.")

## What Success Looks Like

- Your XRP is fully assembled: wheels spin freely, all sensors and the servo are connected, battery installed.
- The web editor shows a live connection to your robot over WiFi.
- Running `blink_and_sense.py` makes the onboard LED blink visibly and continuously.
- The console prints a new sensor reading (e.g., a distance in cm) at least once per blink cycle, and the value changes when you move your hand or the robot.
- Your file includes the one-sentence sense/plan/act comment at the top.
- You can point to your XRP and correctly name which physical part is doing perception, computation, actuation, communication, and power when asked by an instructor.

## Stretch Goal (for early finishers)

Modify `blink_and_sense.py` so the LED blink *speed* changes based on the sensor reading — for example, the closer an object is to the ultrasonic sensor, the faster the LED blinks. This is a real (if tiny) sense-plan-act loop: sense the distance, plan a blink delay based on that distance, act by blinking at that speed. Try to get the blink rate to visibly speed up as you move your hand closer to the sensor.
