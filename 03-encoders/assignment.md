# Lab 3: Driving a Square — Effort vs. Speed vs. Distance

**Week 1, Session 3 — Encoders**

## The Big Idea

You are going to make the robot drive a square and come back to where it
started — three different ways. Each version gives the motors *less* to guess
about:

| Part | Forward motion controlled by | What the robot "knows" |
|---|---|---|
| 1 | `drivetrain.set_effort()` + a timer | nothing — just "push this hard for this long" |
| 2 | `drivetrain.set_speed()` | wheel **speed**, measured by the encoders |
| 3 | `drivetrain.straight()` | wheel **distance**, measured by the encoders |

For every part you will measure how far the robot's final position misses its
starting position. The whole point is to see the error shrink as the encoders
take over.

## Learning Objectives

By the end of this lab, you will be able to:

1. Drive a closed path with open-loop effort commands and describe why the path
   does not close.
2. Use `drivetrain.set_speed()` and `drivetrain.straight()`, and explain what
   the encoders are doing in each.
3. Compare open-loop and encoder-based control using your own measured x/y
   error data.

## Materials

- XRP robot, charged, connected to the web-based MicroPython editor
- Tape measure
- Masking or painter's tape
- ~4 ft × 4 ft of clear, flat floor

## API Notes

> Depending on your XRPLib version the drivetrain object is named `drivetrain`
> or `differential_drive`. Use the editor's autocomplete to confirm, and check
> the course reference sheet if a method name doesn't resolve.

- `drivetrain.set_effort(left, right)` — motor effort, `-1.0` to `1.0`. No
  sensor feedback.
- `drivetrain.set_speed(left, right)` — wheel speed in **cm/s**. Uses the
  encoders to hold that speed.
- `drivetrain.straight(distance_cm, max_effort=0.5)` — drives a set distance in
  **centimeters** using the encoders, then stops. Blocks until done.
- `drivetrain.turn(degrees, max_effort=0.5)` — turns in place by an angle in
  **degrees** (uses the IMU). Blocks until done.
- `drivetrain.stop()` — stops both motors.
- `import time` then `time.sleep(seconds)` for timing.

Target edge length: **pick a value between 2 and 3 feet** (about 60–90 cm) and
use the *same* value for all three parts. Convert once: `2 ft = 61 cm`,
`2.5 ft = 76 cm`, `3 ft = 91 cm`.

## Setup: Mark the Start (do this once)

1. Put the robot on the floor. Trace around its footprint with tape, or mark
   the two front corners and note which way it faces. This is your **home
   mark** — the same target for all three parts.
2. Decide on your square's edge length and turn direction (all left turns or
   all right turns).

## Part 1 — Effort + Timer (~10 min)

Write a loop that drives four sides and four corners. Use these calls:

```python
drivetrain.set_effort(effort, effort)   # start the wheels for a straight side
time.sleep(side_time)                    # let it run for a chosen time
drivetrain.stop()
drivetrain.turn(90)                      # a corner
```

- **Spend at most ~5 minutes tuning** your effort and side-time values so one
  side is roughly your target edge length. It will not be exact. That is the
  point.
- Run the full square from the home mark.
- Measure how far the robot's final footprint is from the home mark:
  **x error** = sideways miss, **y error** = forward/back miss. Record both
  (inches or cm — just be consistent).

## Part 2 — Speed + Encoder (~10 min)

Same square structure, but swap the straight-side call so you command a wheel
**speed** in cm/s. The encoders measure the actual wheel speed and the
drivetrain adjusts effort to hold it. You still time the sides yourself.

```python
drivetrain.set_speed(speed, speed)      # cm/s, held using the encoders
time.sleep(side_time)
drivetrain.stop()
drivetrain.turn(90)
```

- **Spend at most ~5 minutes tuning** your speed and side-time so a side is
  about your target edge length. Hint: distance ≈ `speed * side_time`.
- Run the full square from the home mark.
- Measure and record **x error** and **y error**.

## Part 3 — Distance (`straight`) (~5 min)

Now the encoders handle the distance too. No timer.

```python
drivetrain.straight(side_cm)            # encoders count out the distance
drivetrain.turn(90)
```

- No tuning needed — just use your edge length in cm.
- Run the full square from the home mark.
- Measure and record **x error** and **y error**.

## Data to Record

| Part | Method | Edge length | x error | y error |
|---|---|---|---|---|
| 1 | `set_effort` + timer | | | |
| 2 | `set_speed` + timer | | | |
| 3 | `straight` | | | |

Then answer, in 2–3 sentences:

1. Which part had the smallest error? Which had the largest?
2. The turns used `drivetrain.turn(90)` in **all three** parts. If the square
   still doesn't close in Part 3, where is that error coming from?
3. What does an encoder measure, and how did Parts 2 and 3 use it differently?

## If You Have Extra Time

Repeat all three parts with a **bigger square** (say 4–5 ft edges). Add a
second row to your table for each part. Does the error grow with the box size?
Grow faster for some methods than others?

## What Success Looks Like

- A completed data table with x and y error for all three parts.
- Part 3's error is noticeably smaller than Part 1's.
- You can explain to a partner why timing-based driving (Part 1) doesn't
  repeat, and what the encoders changed.
