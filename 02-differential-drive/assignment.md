# Lab 2: Exploring Differential Drive

In this lab, you will control the XRP's left and right wheels independently. First, you will command raw motor effort. Then, you will command wheel speeds in centimeters per second and predict the radius of the robot's path.

## Learning objectives

By the end of this lab, you will be able to:

1. Make a differential-drive robot move straight, follow an arc, and turn in place.
2. Explain how the left and right wheel commands determine the robot's motion.
3. Calculate the radius of a circular path from the two wheel speeds and the robot's wheelbase.
4. Use both `drivetrain.set_effort()` and `drivetrain.set_speed()`.

## Setup and safety

Work in a clear area on the floor. Be ready to pick up the robot or stop the program if it moves unexpectedly. Motor effort values must be between `-1.0` and `1.0`.

Create a new MicroPython file and begin with:

```python
from XRPLib.defaults import *
import time
```

In each drivetrain command, the left-wheel value comes first:

```python
drivetrain.set_effort(left_effort, right_effort)
drivetrain.set_speed(left_speed, right_speed)
```

Use `drivetrain.stop()` after every motion.

## Part 1 — Motion with `set_effort()`

`set_effort()` sends a raw effort to each motor. Positive values drive forward, negative values drive backward, and zero applies no effort. Effort does **not** specify a speed in cm/s, so the robot's actual speed may change with battery charge, friction, and differences between motors.

### 1. Drive straight

When the two wheels receive equal efforts in the same direction, the robot should drive approximately straight. Run this short example:

```python
drivetrain.set_effort(0.5, 0.5)
time.sleep(1)
drivetrain.stop()
```

Observe the motion. Did the robot travel perfectly straight? Record any drift that you see.

### 2. Drive in an arc

Make both wheels turn forward, but give one wheel a smaller effort than the other. The robot should curve toward the slower wheel.

Write three lines of code that:

1. Set two different positive wheel efforts.
2. Continue for two seconds.
3. Stop the drivetrain.

Before running your code, predict whether the robot will curve left or right. Then test your prediction. Swap the two effort values and run the test again.

### 3. Turn in place

A point turn occurs when the wheels move with equal magnitudes in opposite directions.

Write three lines of code that make the robot turn in place for one second and then stop. Reverse the signs to turn in the other direction. Use an effort magnitude of `0.5` or less for your first test.

### Part 1 check-in

Show all three motions to an instructor or classmate. For each motion, explain how the relationship between the left and right commands produces the observed path.

## Part 2 — Predict a circle with `set_speed()`

Unlike raw effort, `drivetrain.set_speed()` uses the wheel encoders to command the linear speed of each wheel. Both arguments are in **centimeters per second (cm/s)**.

The standard XRP's wheel track is

$$
b = 15.5\ \text{cm}.
$$

Here, $b$ is the center-to-center distance between the left and right wheels. The XRP MicroPython library stores this value as `wheel_track`. Do not confuse it with the wheel diameter, which is 6.0 cm on the standard XRP.

### Differential-drive equations

Recall the equations from the differential-drive presentation. Let $v_L$ and $v_R$ be the left and right wheel speeds. The speed of the center of the robot is

$$
v = \frac{v_R + v_L}{2},
$$

and the angular velocity of the robot is

$$
\omega = \frac{v_R - v_L}{b}.
$$

Because $v = R\omega$, the signed turning radius measured from the center of the robot is

$$
R = \frac{v}{\omega}
  = \frac{b\left(v_R + v_L\right)}{2\left(v_R - v_L\right)}.
$$

Use $|R|$ for the physical radius of the circle. The sign of $R$ indicates the turn direction. Notice the two limiting cases:

- If $v_L = v_R$, the denominator is zero and the robot drives straight; its turn radius is infinite.
- If $v_L = -v_R$, the numerator is zero and the robot turns in place; its turn radius is zero.

### Calculate, predict, and test

Use these commanded wheel speeds:

$$
v_L = 10\ \text{cm/s}, \qquad v_R = 20\ \text{cm/s}.
$$

Before running the robot:

1. Calculate the center speed $v$ in cm/s.
2. Calculate the angular velocity $\omega$ in rad/s.
3. Calculate the circle radius $R$ in cm.
4. Predict whether the robot will curve left or right.

Then test your prediction with:

```python
left_speed = 10    # cm/s
right_speed = 20  # cm/s

drivetrain.set_speed(left_speed, right_speed)
time.sleep(4)
drivetrain.stop()
```

Mark or estimate the center of the circle traced by the robot. Measure the radius from that point to the midpoint between the two wheels. Compare the measured radius with your calculated value.

Finally, swap the left and right speed values. Predict what will stay the same and what will change, and then run the test.

## What to submit

Submit your MicroPython file and a short response containing:

1. The effort pairs you used for the arc and point turn.
2. Your calculated values of $v$, $\omega$, and $R$, including units.
3. Your predicted and observed turn direction.
4. Your measured radius and one reason it may differ from the calculated radius.

## Success criteria

- Your robot drives straight, follows arcs in both directions, and performs point turns in both directions using `set_effort()`.
- Your Part 2 program uses `set_speed()`, not `set_effort()`.
- Your radius calculation uses $b=15.5$ cm and shows units.
- You stop the drivetrain after every test.
