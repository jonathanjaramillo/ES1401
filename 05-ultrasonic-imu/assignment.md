# Lab 5: Ultrasonic Sensing and Obstacle Avoidance

## The Big Idea

An ultrasonic sensor estimates distance by sending out a sound pulse and timing
how long it takes for the echo to return. The number it reports is not always
correct. Objects can be too close, too far away, too small, angled away from the
sensor, or made from a material that produces a weak echo.

In this lab, you will investigate when the XRP's ultrasonic sensor works well,
write a filter that turns raw measurements into a reliable distance estimate,
and use that estimate to make the robot wander without hitting obstacles.

## Learning Objectives

By the end of this lab, you will be able to:

1. Read distance measurements from the XRP ultrasonic sensor.
2. Determine the sensor's useful minimum and maximum distances experimentally.
3. Explain how an object's material affects ultrasonic measurements.
4. Filter invalid, sudden, and noisy readings.
5. Use sensor feedback to create an obstacle-avoidance behavior.

## Materials

- XRP robot with its ultrasonic rangefinder mounted and facing forward
- Laptop with the MicroPython editor
- Tape measure or meterstick
- A large, flat wall
- Test materials such as paper, cardboard, cloth, plastic, metal, and foam
- Open floor space and safe obstacles, such as boxes or backpacks

## XRP Code Reference

This lab uses the code included in `XRP_MicroPython`:

- `XRP_MicroPython/XRPLib/defaults.py` creates the default sensor as
  `rangefinder` and the default drive system as `drivetrain`.
- `XRP_MicroPython/XRPLib/rangefinder.py` defines
  `rangefinder.distance()`. It reports distance in **centimeters**. If no echo
  returns before the timeout, the library returns `rangefinder.MAX_VALUE`,
  which is `65535` in this version.
- `XRP_MicroPython/XRPExamples/sensor_examples.py` contains an
  `ultrasonic_test()` example.
- `XRP_MicroPython/XRPExamples/drive_examples.py` demonstrates
  `drivetrain.set_effort(left, right)` and `drivetrain.stop()`.

## Part 1 — Get the Sensor Running

Connect the robot, create a new MicroPython file, and run this short test:

```python
from XRPLib.defaults import *
import time

while True:
    print(rangefinder.distance())  # centimeters
    time.sleep(0.1)
```

Point the sensor at a wall and slowly move the robot closer and farther away by
hand. Confirm that the number generally decreases as the robot gets closer and
increases as it moves farther away.

Answer:

1. What units does `rangefinder.distance()` return?
2. When the robot is held still, does the value remain perfectly constant?
3. What values appear when the sensor does not seem to detect the wall?

## Part 2 — Find the Useful Measurement Limits

The library comments describe a nominal range of 2 cm to 4 m, but your job is
to measure the useful range of **your** sensor and setup. Do not copy those
numbers.

### 2A. Farthest reliable reading

1. Aim the sensor straight at a large, flat wall.
2. Begin close enough to get stable measurements.
3. Move the robot away from the wall in measured steps.
4. At each distance, watch at least 10 readings and compare them with the tape
   measure.
5. Continue until readings become mostly invalid, unstable, or clearly
   different from the measured distance.

### 2B. Closest reliable reading

1. Begin at a distance that gives stable measurements.
2. Move the robot toward the wall in small measured steps.
3. At each distance, watch at least 10 readings.
4. Continue until values become mostly invalid, unstable, or clearly wrong.

Record representative results:

| Test | Measured distance | Typical sensor reading | Reliable? | What happened? |
|---|---:|---:|:---:|---|
| Far-distance test 1 | | | | |
| Far-distance test 2 | | | | |
| Far-distance test 3 | | | | |
| Near-distance test 1 | | | | |
| Near-distance test 2 | | | | |
| Near-distance test 3 | | | | |

- Closest reliable distance: ______ cm
- Farthest reliable distance: ______ cm
- How did you decide whether a reading was reliable?

## Part 3 — Test Different Materials

Ultrasonic sensing depends on receiving an echo. Different surfaces absorb,
scatter, or reflect sound differently.

Choose at least **five** materials, including both hard and soft surfaces. Hold
each sample at the same measured distance and approximately perpendicular to
the sensor. Collect at least 10 readings for each one. Then repeat one
interesting test with the material tilted at an angle.

| Material | Distance tested | Typical reading | Bad readings out of 10 | Reliable? | Notes |
|---|---:|---:|---:|:---:|---|
| Paper | | | | | |
| Cloth | | | | | |
| Plastic | | | | | |
| | | | | | |
| | | | | | |

Answer:

1. Which materials produced the most reliable readings?
2. Which produced unreliable readings? What did the failures look like?
3. What changed when a material was tilted?
4. Based on your evidence, what objects might be difficult to detect?

## Part 4 — Challenge: Build a Reliable Distance Filter

One raw reading should not automatically control a moving robot. Write a
function that repeatedly calls `rangefinder.distance()` and returns a more
reliable estimate.

Your filter must implement all three rules:

1. **Reject invalid values.** Do not accept `0`,
   `rangefinder.MAX_VALUE`, or readings outside the useful range you measured.
2. **Reject large jumps.** Compare a new value with the last accepted value.
   Reject it if the change is larger than a jump threshold you select. Explain
   how your results helped you choose that threshold.
3. **Average three accepted readings.** Collect three readings that pass Rules
   1 and 2, then return their average. Rejected readings do not count.

Use this outline if you need a starting point:

```python
MIN_DISTANCE = ...       # from Part 2
MAX_DISTANCE = ...       # from Part 2
MAX_JUMP = ...           # your chosen threshold in cm

def reliable_distance():
    accepted = []
    last_accepted = None

    while len(accepted) < 3:
        new_value = rangefinder.distance()

        # Rule 1: Is new_value valid and inside the useful range?

        # Rule 2: Is it close enough to the last accepted value?

        # If it passes both rules, add it to accepted and update
        # last_accepted.

        time.sleep(0.05)

    # Rule 3: Return the average of the three accepted readings.
```

Test the function while the robot is stationary, while moving it slowly, and
with an unreliable material from Part 3. Print raw and filtered values so you
can see what the filter changes.

Show that your filter can:

- ignore `0` and `65535`/`rangefinder.MAX_VALUE`;
- reject a single unrealistic jump;
- return the average of three accepted readings; and
- continue producing useful output under normal test conditions.

> A real robot or obstacle can move quickly, so a real change may look like a
> bad jump. Your threshold is a design choice, not a universal constant.

## Part 5 — Challenge: Roomba-Style Obstacle Avoidance

Use `reliable_distance()` to make the XRP wander through an open area while
avoiding walls and objects. It should not follow a planned path.

Your robot must repeatedly:

1. Obtain a filtered distance reading.
2. Drive forward while the path is clear.
3. Stop before reaching an obstacle.
4. Back up briefly to create space.
5. Turn by a randomly selected amount or for a randomly selected time.
6. Continue driving and repeat.

You may use `drivetrain.set_effort(left, right)` to move or turn,
`drivetrain.stop()` to stop, and MicroPython's `random` module to vary each
turn. See `XRP_MicroPython/XRPExamples/drive_examples.py` for motor examples.

Choose and document these design values:

| Setting | Your value | Why did you choose it? |
|---|---:|---|
| Obstacle distance (cm) | | |
| Forward effort | | |
| Reverse effort and time | | |
| Turn effort | | |
| Turn-time range | | |

### Safety and testing

- Test on the floor, not on a table.
- Begin with low motor effort.
- Keep a hand near the robot and be ready to stop it.
- Use large, solid obstacles first.
- Call `drivetrain.stop()` before switching between forward, reverse, and
  turning behaviors.
- Stop immediately if the robot repeatedly misses an obstacle.

Run three trials. Rearrange the obstacles for each trial and let the robot
encounter at least three obstacles.

| Trial | Obstacles encountered | Successful avoidances | Collisions | What will you change? |
|---|---:|---:|---:|---|
| 1 | | | | |
| 2 | | | | |
| 3 | | | | |

## What to Submit

1. Your completed distance-limit and material-test tables.
2. Your written answers from Parts 1–3.
3. Your filter thresholds and a short explanation of how you chose them.
4. Your complete `reliable_distance()` code.
5. Your complete obstacle-avoidance code.
6. Your three-trial results and a short reflection: What failure occurred most
   often, and what change most improved the robot?

## What Success Looks Like

- You can continuously read distances in centimeters.
- Your near and far limits are supported by measurements.
- You can identify materials or orientations that cause unreliable readings.
- Your filter follows all three required rules and steadies the output.
- Your robot wanders without a fixed path and avoids most large obstacles in
  three differently arranged trials.
