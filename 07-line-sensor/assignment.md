# Session 7 Lab: Line Sensor

**Week 3, Session 7 of 12 — Intro to Robotics**

## Learning Objectives

By the end of this lab, you will be able to:

1. Read live values from the XRP's line/reflectance sensor in MicroPython.
2. Collect and compare sensor readings over a light floor vs. dark tape (or vice versa).
3. Choose a reliable numeric threshold that separates "on the line" from "off the line" for your specific setup.
4. Write a simple `on_line()` function that returns `True`/`False` based on that threshold.

## Materials Needed

- Your XRP robot kit, USB cable, and laptop with the web-based MicroPython editor open
- A strip of dark tape (electrical tape or black gaffer tape works well) stuck to a light-colored floor or table
  - *If your floor/table is dark, use light-colored tape (masking tape or white tape) instead — just flip your comparisons accordingly.*
  - Tape should be at least 12 inches long and straight, with plain floor visible on both sides
- Starter code (below), saved as `line_test.py` on your XRP

### Starter Code

```python
from XRPLib.defaults import *
import time

# Prints the left reflectance sensor value every 200ms.
# Move the robot by hand: hold it over plain floor, then over the tape,
# then back over floor, and watch how the printed values change.

while True:
    value = reflectance.get_left()
    print(value)
    time.sleep_ms(200)
```

> Note: depending on your XRP library version, reflectance values may be scaled 0–1 (float) or 0–1000 (int). Run the starter code first and look at what range your numbers actually fall in — don't assume.

## Step-by-Step Instructions

**Step 1 — Get baseline floor readings.**
Run the starter code. With the robot powered on but not driving, hold it (or set it) so the sensor is over plain floor, away from the tape. Watch the printed values for about 5 seconds. Record the approximate range you see (e.g., "floor reads about 850–920").

**Step 2 — Get baseline tape readings.**
Without stopping the program, carefully slide the robot so the sensor sits directly over the middle of the tape strip. Watch the printed values for about 5 seconds. Record the approximate range (e.g., "tape reads about 100–180").

**Step 3 — Sweep across the boundary.**
Slowly slide the robot from floor, across the edge of the tape, onto the tape, and back off onto floor again, while readings print continuously. Confirm the transition is fairly sharp (values change quickly, not gradually) and there's a clear gap between your floor numbers and your tape numbers.

**Step 4 — Pick a threshold.**
Choose a single number that sits roughly halfway between your floor average and your tape average. For example, if floor ≈ 900 and tape ≈ 150, a reasonable threshold is 500. Write this number down — you'll use it in your code.

**Step 5 — Write `on_line()`.**
Create a new function that reads the sensor once and returns `True` if the robot is on the line, `False` otherwise, using your threshold. Example shape (fill in your own threshold and comparison direction):

```python
LINE_THRESHOLD = 500  # replace with your measured value

def on_line():
    value = reflectance.get_left()
    return value < LINE_THRESHOLD  # flip to > if your line is lighter than the floor
```

**Step 6 — Test it.**
Write a short loop that calls `on_line()` every 200ms and prints `True`/`False` (instead of the raw number) as you move the robot over floor and tape again. Confirm it correctly reports `True` only when the sensor is actually over the tape.

```python
while True:
    print(on_line())
    time.sleep_ms(200)
```

**Step 7 — Stress-test your threshold.**
Try the edges: hold the sensor half on/half off the tape, and try a spot with a shadow or dirt mark on the floor if one exists. Note any cases where `on_line()` gives a result you didn't expect. You don't need to fix these today — just observe and jot down what you noticed.

## What Success Looks Like

- You can run the starter code and see printed sensor values change as you move the robot over floor vs. tape.
- You have written down approximate numeric ranges for "floor" and "tape" readings from your own setup.
- You have a chosen threshold value and can explain (in one sentence) why you picked that number.
- Your `on_line()` function correctly returns `True` when the sensor is clearly over the tape and `False` when it's clearly over the floor, verified by watching the printed output while moving the robot by hand.
- You can briefly explain, in your own words, why the sensor reading changes between light and dark surfaces (reflected light).

## Stretch Goal (Early Finishers)

Pick one:

1. **Edge detection:** Extend your code to detect when the robot is transitioning onto or off of the line (i.e., when `on_line()` changes from `False` to `True` or back), and print a message like `"Entered line"` or `"Left line"` only at the moment of transition, not on every loop iteration.
2. **Curved line handling:** If your XRP has left and right reflectance sensors, read both, and write a function `line_position()` that reports whether the line is centered, drifting left, or drifting right under the robot, based on comparing the two sensor values. Test it by slowly curving the tape and sliding the robot along it.
