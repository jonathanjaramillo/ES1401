# Session 3 Lab: Open-Loop Control & First Drive

Week 1, Session 3 — Introduction to Robotics (XRP Robot Kit)

## Learning Objectives

By the end of this lab, you will be able to:

1. Write and run a MicroPython program on the XRP that drives the robot using only **timed motor commands** (no sensors).
2. Explain, from direct observation, why open-loop (timing-based) movement drifts over repeated actions.
3. Tune timing values through iterative testing to make your robot trace a recognizable shape (square or line-and-turn).

## Materials Needed

- Your XRP robot kit, fully charged (check the battery indicator before starting)
- Laptop with the XRP web-based MicroPython editor open and connected to your robot
- A flat, open patch of floor with at least a 3 ft x 3 ft clear area
- Masking tape and a marker (to mark your robot's starting point and orientation)
- A ruler or tape measure (to check how close you land to your start point)

## Starter Code

Below is a starting template using plausible XRP MicroPython motor API conventions. Copy this into a new file in the web editor, then modify the timing values to match your robot.

```python
from XRP import Motor
import time

# Create motor objects for left and right drive motors
left_motor = Motor(port="motor_left")
right_motor = Motor(port="motor_right")

# --- Basic timed movement helpers ---

def drive_forward(seconds, speed=0.5):
    """Drive both motors forward at the same speed for a fixed time."""
    left_motor.set_effort(speed)
    right_motor.set_effort(speed)
    time.sleep(seconds)
    stop()

def turn_right(seconds, speed=0.5):
    """Spin in place: left motor forward, right motor reverse."""
    left_motor.set_effort(speed)
    right_motor.set_effort(-speed)
    time.sleep(seconds)
    stop()

def stop():
    left_motor.set_effort(0)
    right_motor.set_effort(0)

# --- Example: one leg of a square ---
drive_forward(1.0)   # drive forward ~1 second
time.sleep(0.2)       # brief pause to let motors fully stop
turn_right(0.4)       # turn roughly 90 degrees (TUNE THIS NUMBER)
stop()
```

**Note:** The exact `seconds` values that produce a straight line or a 90-degree turn will be different for *your* robot. Finding those numbers through testing is the point of this lab.

## Step-by-Step Instructions

### Part A — Get Straight-Line Driving Working (~10 min)

1. Place your XRP on the floor and mark its starting position and facing direction with tape.
2. Using `drive_forward()`, run the robot forward for **1 second**. Observe: does it drive in a reasonably straight line, or does it curve?
3. If it curves, don't worry — this is expected (remember: motor differences from lecture!). For now, just get a rough forward-driving time that feels reasonable — you'll fine-tune later.
4. Record the `seconds` value you land on for "drive forward about 1 foot" (or whatever consistent distance you choose).

### Part B — Get a 90-Degree Turn Working (~10 min)

5. Mark your robot's starting orientation with a piece of tape as a pointer.
6. Using `turn_right()`, try a starting guess of **0.4 seconds**. Run it and observe how far the robot actually turned.
7. Adjust the `seconds` value up or down and re-test until the robot turns approximately 90 degrees (use the tape pointer and eyeball a right angle, or use a protractor/floor grid if available).
8. Record your tuned turn time.

### Part C — Drive the Full Shape (~15 min)

9. Using your tuned forward and turn values, write a program that repeats **forward → pause → turn** four times to trace a square:

```python
for i in range(4):
    drive_forward(YOUR_FORWARD_TIME)
    time.sleep(0.2)
    turn_right(YOUR_TURN_TIME)
    time.sleep(0.2)
stop()
```

   (If you'd rather do a straight-line-and-turn path instead of a full square, that's fine too — just drive forward, turn once, and drive forward again.)

10. Place the robot back at your taped starting mark and orientation, run the program, and **do not touch the robot** while it runs — this is open-loop control, no interventions allowed!
11. Mark where the robot actually ends up and measure the distance from your starting tape mark.
12. Run it 2-3 more times from the same starting spot. Does it end up in the same place each time, or does it vary? Jot down a quick observation — this is your evidence of open-loop drift in action.

## What Success Looks Like

- Your robot completes all four sides/turns of the shape (or the line-and-turn path) **without you touching it or the keyboard mid-run**.
- On at least one run, the robot ends up **within roughly 1 foot of its starting point** for a square, or clearly completes the intended line-and-turn shape.
- You can point to your taped start/end marks and explain, in your own words, at least one reason your robot didn't land exactly on the start point (battery sag, motor mismatch, or surface friction).
- You have working `seconds` values recorded for both "drive forward one leg" and "turn ~90 degrees" that you could hand to a partner to reproduce roughly the same result.

## Stretch Goal (Early Finishers)

Once your square is working reliably, try one of the following:

- **Triangle:** Drive a 3-sided shape using ~120-degree turns instead of 90-degree turns. You'll need to re-tune your turn timing.
- **Figure-eight:** Chain two loops in opposite turn directions (e.g., four right turns followed by four left turns) to trace a figure-eight pattern.
- **Speed challenge:** Increase your `speed` value and see how it affects both accuracy and drift — does a faster robot drift more or less than a slower one? Be ready to explain why in next session's discussion.
