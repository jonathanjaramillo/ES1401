# Session 5 Lab: Wall-Approach with Noise & Smoothing

## Learning Objectives

By the end of this lab, you will be able to:

1. Explain, in your own words, why real sensor readings (like the ultrasonic sensor) are noisy rather than perfectly consistent.
2. Implement a simple moving-average smoothing function in MicroPython.
3. Program the XRP robot to drive toward a wall and stop automatically at a target distance, using the ultrasonic sensor as feedback.
4. Compare the reliability of a stop decision based on raw sensor readings vs. smoothed sensor readings.

## Materials Needed

- SparkFun XRP robot kit, fully charged, with ultrasonic sensor mounted facing forward
- Laptop with the web-based MicroPython editor connected to your XRP
- A flat, open test area with a wall or large flat object (a stack of books, a whiteboard, a cardboard box works too) at least 4 feet away
- A tape measure or ruler for verifying stop distance
- Starter code (below), saved as `wall_approach.py` or added to `main.py`

## Starter Code

### Part A: Simple moving-average smoothing function

```python
# A small "window" of the most recent readings
reading_window = []
WINDOW_SIZE = 5

def smooth_reading(new_value):
    """Add new_value to the window, drop the oldest if too full,
    and return the average of what's left."""
    reading_window.append(new_value)
    if len(reading_window) > WINDOW_SIZE:
        reading_window.pop(0)  # remove oldest reading
    return sum(reading_window) / len(reading_window)
```

### Part B: Basic wall-approach loop (raw version — starting point)

```python
from XRPLib.defaults import *
import time

STOP_DISTANCE_CM = 15.0  # target stopping distance in centimeters
DRIVE_SPEED = 0.3        # slow, controlled speed (adjust as needed)

while True:
    distance = rangefinder.distance()  # raw reading, in centimeters

    if distance <= 0 or distance >= rangefinder.MAX_VALUE:
        drivetrain.stop()
        print("No valid echo; check the sensor before retrying")
        break

    if distance <= STOP_DISTANCE_CM:
        drivetrain.stop()
        print("Stopped! Distance:", distance)
        break
    else:
        drivetrain.set_effort(DRIVE_SPEED, DRIVE_SPEED)
        print("Driving... distance:", distance)

    time.sleep(0.05)
```

## Step-by-Step Instructions

1. **Set up your test area.** Place your XRP about 3–4 feet from a wall or flat surface, aimed straight at it. Clear the path of obstacles.

2. **Test the raw version first.** Type in (or open) the Part B code above exactly as written — using the raw `distance` value directly in the stop check. Run it 2–3 times and observe:
   - Does the robot always stop at roughly the same distance?
   - Does it ever stop way too early, or get closer than expected before stopping?
   - Take a quick note of what you observed (a sentence is fine).

3. **Add the smoothing function.** Add the `smooth_reading()` function from Part A above your main loop.

4. **Modify your loop to use the smoothed value.** Inside the `while True:` loop, change it so you compute the smoothed distance and use *that* in your stop check instead of the raw value:

   ```python
   raw_distance = rangefinder.distance()
   if raw_distance <= 0 or raw_distance >= rangefinder.MAX_VALUE:
       drivetrain.stop()
       print("No valid echo; check the sensor before retrying")
       break
   distance = smooth_reading(raw_distance)

   if distance <= STOP_DISTANCE_CM:
       drivetrain.stop()
       print("Stopped! Smoothed distance:", distance)
       break
   else:
       drivetrain.set_effort(DRIVE_SPEED, DRIVE_SPEED)
   ```

5. **Re-test with smoothing.** Run the updated program 3 times from roughly the same starting distance. Measure the actual stopping distance each time with your tape measure/ruler and record all 3 results.

6. **Compare.** Write 2–3 sentences comparing what you observed with raw vs. smoothed readings. Which version felt more consistent? Did smoothing change how quickly the robot reacted near the wall?

7. **Tune it (optional but encouraged).** Try changing `WINDOW_SIZE` to 2 and then to 10. What changes about how the robot behaves as it approaches the wall?

## What Success Looks Like

- Your robot reliably drives forward and stops **without physically touching the wall**.
- Across **3 repeated trials** with the smoothed version, the robot stops within a **10–20 cm window** of the wall each time (target is 15 cm, some variation is expected and fine).
- The robot does **not** stop dramatically early (e.g., 38+ cm away) or overshoot into the wall in any of the 3 trials.
- You can explain, in a sentence or two, why the smoothed version behaved differently than the raw version.
- You've recorded your 3 measured stopping distances and your short written comparison.

## Stretch Goal (Early Finishers)

Choose one:

- **Multi-stop challenge:** Program the XRP to approach the wall and stop at 30 cm, pause for 1 second, then continue approaching and stop again at 15 cm. This requires tracking which "stage" of approach you're in.
- **Reliability comparison:** Run 5 trials each with raw-only and smoothed stopping logic, recording the actual stop distance every time. Calculate roughly how much the stopping distance varies (e.g., biggest minus smallest) for each method, and report which method was more consistent and by how much.
