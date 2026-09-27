# Session 8 Lab: Bang-Bang Line Following

## Learning Objectives

By the end of this lab, you will be able to:

1. Explain the difference between open-loop and closed-loop control using your own robot as the example.
2. Identify "error" from a sensor reading (how far off the line the robot is, and in which direction).
3. Implement a simple **bang-bang controller** in MicroPython that reacts to line-sensor error with a full hard turn, and use it to make the XRP follow a taped line.

## Materials Needed

- SparkFun XRP robot kit, fully assembled, battery charged
- XRP web-based MicroPython editor (same one used in prior sessions)
- Masking or electrical tape, laid out on the floor as a closed loop (at least 6 feet around), with gentle curves — avoid sharp 90° corners for this first attempt
- A flat, evenly lit floor area (line sensors are sensitive to glare/shadows)
- Your Session 5–6 notes on how to read the line/reflectance sensor

## Starter Code Skeleton

Copy this into a new file in the XRP editor and fill in the `# TODO` sections.

```python
from XRPLib.defaults import *
import time

# --- Tuning values (adjust to your robot / lighting) ---
DRIVE_SPEED = 0.3      # base forward speed, 0.0 to 1.0
TURN_SPEED  = 0.4      # how hard to turn when off the line

def read_line_state():
    """
    Reads the line sensor and returns one of:
      "on_line"    - centered on the line
      "off_left"   - drifted left of the line (line is to our right)
      "off_right"  - drifted right of the line (line is to our left)

    TODO: Replace this with real reflectance sensor reads.
    Hint: reflectance_sensor.get_left() and .get_right() (or similar,
    check your Session 5-6 notes) return light/dark values per sensor.
    Compare left vs right sensor readings to decide the state.
    """
    left_val = 0   # TODO: read left reflectance sensor
    right_val = 0  # TODO: read right reflectance sensor

    # TODO: pick a threshold and decide the state based on left_val/right_val
    return "on_line"  # placeholder — replace with real logic


def bang_bang_step():
    """
    One iteration of the bang-bang controller:
    reads the error state and commands a hard reaction.
    """
    state = read_line_state()

    if state == "off_left":
        # TODO: command a hard RIGHT turn (e.g. drivetrain.set_effort or similar)
        pass
    elif state == "off_right":
        # TODO: command a hard LEFT turn
        pass
    else:  # "on_line"
        # TODO: drive straight forward
        pass


# --- Main loop: this repetition IS the closed loop ---
try:
    while True:
        bang_bang_step()
        time.sleep(0.02)  # small delay so the loop doesn't spam the sensor/motors
except KeyboardInterrupt:
    # TODO: stop the motors cleanly when you hit stop in the editor
    pass
```

## Step-by-Step Instructions

1. **Lay out your track.** Tape a closed loop on the floor, at least 6 feet in perimeter, with only gentle curves (no sharp corners yet). Make sure the tape contrasts clearly with the floor.
2. **Review your sensor API.** Open your Session 5–6 notes/code and find the exact function names for reading the line/reflectance sensor on your XRP. Test-print raw sensor values first (place the robot on and off the tape by hand, print the numbers) so you know what "on line" vs "off line" looks like numerically.
3. **Fill in `read_line_state()`.** Pick a threshold value that reliably separates "sensor sees tape" from "sensor sees floor." Use the left/right sensor comparison to decide `"on_line"`, `"off_left"`, or `"off_right"`.
4. **Fill in `bang_bang_step()`.** Use your drivetrain motor commands from earlier sessions to:
   - Turn hard right when `off_left`
   - Turn hard left when `off_right`
   - Drive straight when `on_line`
5. **Test on a straight piece of tape first.** Place the robot near the center of a straight section and run your code. It should oscillate side to side but generally stay near the tape. If it immediately spins away and never comes back, your left/right turn directions are probably swapped — fix and retest.
6. **Test on the full loop.** Place the robot on the taped loop and let it run a full lap. Watch where it loses the line (if it does) — usually curves that are too sharp for your turn speed.
7. **Tune your constants.** Adjust `DRIVE_SPEED` and `TURN_SPEED`, and your sensor threshold, until the robot can complete the full loop without losing the line, even if it's zig-zagging the whole way.
8. **Add a clean stop.** Make sure your `except KeyboardInterrupt` block actually stops both motors, so the robot doesn't keep driving after you hit stop in the editor.

## What Success Looks Like

- Your robot completes at least one full lap of a taped loop of 6+ feet **without losing the line**, even though its path visibly zig-zags rather than smoothly tracking the tape.
- If the robot drifts completely off the tape and can't find its way back, that's a bug to fix (usually: turn directions swapped, threshold too loose/tight, or turn speed too weak to catch a curve) — not something to just accept.
- You can point to a specific line in your code and explain, in terms of "error," why the robot turns the direction it does.

## Stretch Goals (Early Finishers)

- **Time it:** Use `time.ticks_ms()` to measure how long a full lap takes. Try to reduce lap time by tuning `DRIVE_SPEED` and `TURN_SPEED` without losing the line.
- **Sharper curves:** Add a section of tighter curve (closer to 90°) to your loop and see if your controller can still handle it. If not, what would you need to change?
- **Count corrections:** Add a counter that increments every time the robot switches between `off_left` and `off_right`, and print it at the end of a lap. How "jittery" is bang-bang, quantitatively?
- **Preview of what's next:** Think about (don't implement yet) how you might make the correction *proportional* to how far off the line the robot is, instead of always turning at full force. Jot down your idea — we'll build exactly this in a future session (PID control).
