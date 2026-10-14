# Assignment 1: Differential Drive

## Goal

Program your XRP robot to drive in various shapes. You will start with three basic movements: driving forward, following an arc, and spinning in place. Then you will combine movements with a `for` loop and try to make the robot trace a circle and a square.

Along the way, get familiar with the robot's **drivetrain**: the two drive wheels and the commands that control them. For this assignment, control motion using `set_effort()` or `set_speed()`, with `time.sleep()` to choose how long each movement lasts and `stop()` to end it.

## Getting started

Read `XRP_MicroPython/XRPExamples/drive_examples.py`, especially `drive_straight()`, `arc_turn()`, and `point_turn()`. Notice the repeated pattern: command the wheels, wait, and stop.

Create a new MicroPython program with these imports:

```python
from XRPLib.defaults import *
import time
```

The first import creates an object named `drivetrain`, which you will use to control both wheels. In each command, the **first argument controls the left wheel** and the **second controls the right wheel**. Left and right are from the robot's perspective when facing forward.

Run your experiments on a clear, flat floor with room to move. Start with short durations and moderate efforts or speeds so you can observe each movement.

## How `set_effort()` works

```python
drivetrain.set_effort(left_effort, right_effort)
```

Effort tells each motor how strongly to drive. Each value is between **-1.0 and 1.0**:

| Effort | Meaning |
| --- | --- |
| `1.0` | Full effort forward |
| `0.5` | Half effort forward |
| `0.0` | Zero effort |
| `-0.5` | Half effort backward |
| `-1.0` | Full effort backward |

Effort is **not a measured speed**. For example, `0.5` does not mean 0.5 centimeters per second. The resulting speed depends on factors such as battery charge and the floor surface. Equal efforts usually produce roughly straight motion, but the robot may drift because the motors and wheels do not behave identically.

The command starts the motors and returns immediately. It does not choose a duration or stop the robot for you:

```python
drivetrain.set_effort(0.4, 0.4)
time.sleep(1.0)       # Keep moving for 1 second.
drivetrain.stop()    # Stop both motors.
```

## How `set_speed()` works

```python
drivetrain.set_speed(left_speed, right_speed)
```

Speed values are targets in **centimeters per second (cm/s)** for each wheel. Positive values move the wheel forward; negative values move it backward. The library uses wheel encoder measurements to adjust motor effort and try to maintain the requested wheel speeds.

```python
drivetrain.set_speed(10, 10)
time.sleep(1.0)
drivetrain.stop()
```

This asks both wheels to move at 10 cm/s for one second. Ideally, the robot travels about 10 cm, but starting, stopping, and wheel slip can change the actual distance. Speed control does not automatically choose a distance, turn angle, or path for you. The robot also has physical limits, so requesting a very large speed does not guarantee it can reach that speed.

Use `drivetrain.stop()` between separate trials, including when switching from `set_speed()` to `set_effort()`. This stops both wheels and turns off active speed control.

## Part 1: Drive forward for a set time

1. Run the forward-motion example above using `set_effort()`.
2. Change the duration and observe how far the robot travels.
3. Keep the duration fixed and change both efforts together. Observe what changes.
4. Repeat using `set_speed()` instead of `set_effort()`.

For each trial, record the command, its two values, the duration in seconds, and what you observed. Does the robot travel straight? Does repeating the same command produce the same result?

## Part 2: Drive in an arc

Make the robot follow a curved arc by commanding both wheels forward at different efforts or speeds. The robot should curve toward the slower wheel.

Start with either of these commands, followed by a short `time.sleep()` and `drivetrain.stop()`:

```python
drivetrain.set_effort(0.3, 0.5)
```

```python
drivetrain.set_speed(6, 10)
```

Before running the robot, predict which direction it will curve. Then swap the left and right values and try again. Experiment with the wheel values to make a wider arc and a tighter arc. Change one value at a time so you can connect the change to the resulting motion.

## Part 3: Spin in place

Make the robot rotate around its center by commanding the wheels in opposite directions with equal magnitudes. For example:

```python
drivetrain.set_effort(-0.4, 0.4)
```

Or, using speed targets:

```python
drivetrain.set_speed(-8, 8)
```

Add a short wait and a stop. Predict the direction of rotation, then test it. Reverse both signs to spin the other way.

Keep the wheel values fixed and adjust the duration until the robot turns approximately 90 degrees. Record the duration you found; you will use it when attempting a square.

## Part 4: Repeat drive-and-turn movements with a `for` loop

Write a program that drives forward, stops, turns in place, and stops again. Use a `for` loop to repeat that sequence **N times**:

```python
N = 3

for step in range(N):
    # Command both wheels forward.
    # Wait for your chosen forward duration.
    # Stop.

    # Command the wheels to spin in place.
    # Wait for your chosen turn duration.
    # Stop.
    pass  # Replace this line and the comments with your commands.

drivetrain.stop()
```

Use values from your earlier experiments. You may use either effort commands or speed commands. Remember that the indented code runs once for each repetition; `range(N)` repeats it N times.

Try at least two different values of `N`. Predict the path before each run, then compare your prediction with what the robot actually does.

## Part 5: Try to drive a circle

Use what you learned about arcs to make the robot trace one complete circle. Both wheels should move forward, with one moving faster than the other. Choose wheel values and tune the duration so the robot ends near its starting position, facing approximately its starting direction.

A spin in place does not count as a circle: the robot's center should travel around a circular path. Test, record your observations, and adjust your values or duration.

The `circle()` example runs forever with `while True`. For your version, use a finite duration and finish with `drivetrain.stop()`.

## Part 6: Try to drive a square

Adapt your drive-and-turn loop to trace a square:

- Drive forward for one side.
- Spin in place approximately 90 degrees.
- Repeat the sequence four times, turning in the same direction each time.

Use the same forward duration for all four sides and the same turn duration for all four corners. Tune those durations and your wheel commands to improve the shape. Look for approximately equal side lengths, right-angle corners, and an ending position near the starting position.

Use only `set_effort()` or `set_speed()` for movement, plus `time.sleep()` and `stop()`. The reference file's `square()` and `polygon()` functions use `straight()` and `turn()` to request distances and angles directly; build your own timed version for this assignment.

Your circle and square do not need to be perfect. The goal is to connect wheel commands and timing to the resulting path, then improve your result through testing.

## What to turn in

- Your MicroPython code, with clearly labeled sections or functions for forward motion, an arc, a spin, the N-repeat loop, a circle, and a square. Include the final wheel values and durations you used.
- A brief trial log showing the changes you made and what happened, including at least one adjustment for the circle and one for the square.
- Short answers to these questions:
  1. How does `set_effort()` differ from `set_speed()`? Include the meaning and units of their arguments.
  2. What wheel commands produce forward motion, an arc, and a spin in place?
  3. What happened when you changed `N` in your loop?
  4. Which shape was harder to produce? Describe one adjustment that improved it and one source of error that remained.
