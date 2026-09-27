# Lab 5b: Finding the Gap in the Wall

## The Big Idea

A rangefinder alone can only tell you "something is X cm away, straight
ahead." An IMU alone can only tell you "I am facing Y degrees." Neither one is
enough by itself to answer a question like *"where is the opening in this
wall?"* — but paired together, and recorded as the robot turns, they are.

In this lab your robot will approach a wall that has a gap in it. It won't
know where the gap is ahead of time. It will **scan** — slowly rotate in
place while repeatedly recording its heading (from the IMU) alongside the
distance reading in that direction (from the rangefinder) — and use that
recorded data to figure out which direction has open space. Then it will turn
to face that direction.

This is the same basic idea behind how a real robot vacuum or a self-driving
car builds a simple picture of "what's around me" using nothing but a moving
sensor and something to keep track of the sensor's orientation while it moves.

## Prerequisite

This lab builds directly on `reliable_distance()` from Lab 5 (Part 4). Bring
your working version with you — you'll call it (or a simplified version of
it) once per heading during the scan.

## Learning Objectives

By the end of this lab, you will be able to:

1. Read the robot's orientation using `imu.get_heading()`.
2. Combine two sensor streams (heading + distance) into a single recorded
   data set as the robot moves.
3. Write a `scan()` function that sweeps the robot and logs paired readings.
4. Analyze the recorded data to find the direction with the most open space.
5. Turn the robot to face a computed target heading rather than a fixed
   amount.

## Materials

- XRP robot with ultrasonic rangefinder and IMU (same setup as Lab 5)
- Laptop with the MicroPython editor
- A wall or barrier built from two sections with a gap between them (boxes,
  books, or binders work well) — wide enough for the robot to drive through
- Open floor space in front of the wall

## XRP Code Reference

- `XRP_MicroPython/XRPLib/imu.py` defines `imu.get_heading()`, which returns
  the robot's current heading in degrees, **bounded to the range [0, 360)**.
  0° is wherever the robot was pointed when it powered on (or last called
  `imu.reset_yaw()`).
- `imu.reset_yaw()` resets the heading to 0. Call this once, before your scan
  begins, so your headings are easy to reason about.
- `rangefinder.distance()` and your own `reliable_distance()` from Lab 5.
- `drivetrain.set_effort(left, right)` sets raw motor power from -1 to 1.
  Equal and opposite efforts (e.g. `set_effort(-0.3, 0.3)`) rotate the robot
  in place.
- `drivetrain.turn(turn_degrees)` turns the robot by a specific number of
  degrees using the IMU internally, then stops automatically.
- `drivetrain.stop()` stops both motors.

## Part 1 — Two Ways to Turn

Before you write `scan()`, decide how you want the robot to rotate while
collecting data. There are two reasonable approaches — try **both** briefly
and pick the one you'll use for your `scan()` function.

**Option A — Continuous slow spin.** Set a small constant turning effort with
`set_effort()` (e.g. `set_effort(-0.2, 0.2)`) and leave the motors running
while you repeatedly read heading and distance in a loop, until you've turned
far enough. This gives you many readings spread unevenly across the sweep,
since your loop isn't perfectly timed.

**Option B — Discrete steps.** Use `drivetrain.turn(step_degrees)` to rotate
a small fixed amount (e.g. 5°), then stop and take one heading + distance
reading, then turn another step, and repeat. This gives you evenly spaced
readings, but each `turn()` call blocks until it's done, so the scan takes
longer overall.

Write a few lines to test each approach — print heading and raw distance in
a loop for a few seconds of each. Then answer:

1. Which approach gave you more readings per second? Which gave more *evenly
   spaced* readings?
2. Did either approach cause the heading or distance values to look noisier
   or less trustworthy? Why might that be?
3. Which one did you pick for Part 2, and why?

## Part 2 — Write `scan()`

Write a function called `scan(sweep_degrees, step_degrees=5)` that rotates
the robot through roughly `sweep_degrees` of rotation (split evenly on
either side of the robot's current heading, or all in one direction — your
choice, just be consistent) and returns a **list of `(heading, distance)`
pairs**, one pair for every reading taken.

Use whichever turning approach you picked in Part 1. Use `reliable_distance()`
(or a faster 1-2 reading version of it, if the full three-reading version
makes your scan too slow) at each sample point rather than a single raw
`rangefinder.distance()` call — a single bad reading in the middle of your
scan could make the robot think the gap is somewhere it isn't.

Use this outline if you need a starting point:

```python
def scan(sweep_degrees, step_degrees=5):
    """
    Slowly rotate the robot and record (heading, distance) pairs.

    :param sweep_degrees: total amount to rotate, in degrees
    :param step_degrees: (Option B only) degrees per discrete turn
    :return: a list of (heading, distance) tuples
    """
    readings = []
    start_heading = imu.get_heading()

    # TODO: rotate the robot using your chosen approach from Part 1.
    # As you rotate, repeatedly:
    #   1. Read the current heading with imu.get_heading()
    #   2. Read a filtered distance with reliable_distance()
    #   3. Append (heading, distance) to readings
    # Stop once you've covered approximately sweep_degrees of rotation.

    drivetrain.stop()
    return readings
```

Test it by printing the returned list. Confirm that:

- The list is non-empty and covers roughly the sweep you asked for.
- The distance values change in a way that makes sense as you manually
  verify by watching the robot turn (larger where there's open space or the
  gap, smaller where it's facing a wall section).

## Part 3 — Find the Gap

Write a function called `find_gap_heading(readings)` that takes the list
returned by `scan()` and returns the single heading that best points at the
gap.

Think carefully about *how* to decide. A few reasonable strategies:

- Return the heading with the single largest distance reading.
- Since a real gap is usually several readings wide, average the headings of
  every reading above some "this must be open space" distance threshold,
  rather than trusting one single maximum reading.
- Look for the *widest run* of consecutive headings that all report a large
  distance, and return the heading in the middle of that run.

Pick one strategy, implement it, and be ready to explain your choice.

```python
def find_gap_heading(readings):
    """
    Given a list of (heading, distance) pairs from scan(), return the
    heading that best points toward the gap in the wall.

    :param readings: list of (heading, distance) tuples
    :return: the target heading, in degrees
    """
    # TODO: implement your chosen strategy.
```

Answer:

1. What strategy did you choose, and why? What could go wrong with just
   taking the single largest reading?
2. What distance threshold (if any) did you use to decide a reading counts
   as "open space," and how did you pick it?
3. Print your `readings` list for one scan and, by hand, work out what
   heading your strategy *should* return. Does your function's actual output
   match?

## Part 4 — Turn to Face the Gap

Write a function called `face_gap(target_heading)` that turns the robot so
its current heading matches `target_heading` as closely as possible.

```python
def face_gap(target_heading):
    """
    Turn the robot in place until it is facing target_heading.

    :param target_heading: the heading to turn to, in degrees
    """
    # TODO: turn the robot toward target_heading.
    # Think about which direction to turn (left or right) based on
    # whether target_heading is greater or less than the current heading.
```

You may implement this with a simple loop that checks
`imu.get_heading()` against `target_heading` and applies turning effort
until the difference is small enough, or you may compute the turn amount
and call `drivetrain.turn(...)` once. Either is acceptable, but explain your
choice.

> **Watch out for wraparound.** `get_heading()` is bounded to `[0, 360)`, so
> a heading of 355° and a heading of 5° are only 10° apart in reality, even
> though a naive subtraction gives you 350°. If your scan sweeps near 0°/360°,
> your turning logic needs to account for this. (If your test wall setup
> keeps the whole sweep comfortably away from 0°/360°, you can skip this for
> now — just note it as a known limitation.)

## Part 5 — Put It Together

Write a short script that:

1. Places the robot facing generally toward the wall (by hand).
2. Calls `imu.reset_yaw()`.
3. Calls `scan(sweep_degrees)` with a sweep wide enough to see both wall
   sections and the gap.
4. Calls `find_gap_heading()` on the result.
5. Calls `face_gap()` with that heading.
6. Prints the readings list, the computed gap heading, and the final heading
   the robot actually stopped at.

Run this at least three times, rearranging the gap's position between runs
(move the wall sections, or rotate the whole setup relative to the robot).

| Trial | Approx. true gap heading (measured by hand) | Computed gap heading | Final robot heading | Faced the gap correctly? |
|---|---:|---:|---:|:---:|
| 1 | | | | |
| 2 | | | | |
| 3 | | | | |

### Safety and testing

- Test on the floor, not a table.
- Keep turning efforts low while debugging — a fast spin makes it hard to
  read printed output and easy to knock the wall sections over.
- Keep a hand near the robot.

## What to Submit

1. Your Part 1 comparison notes and which turning approach you chose.
2. Your complete `scan()` code.
3. Your complete `find_gap_heading()` code, plus your written answers from
   Part 3.
4. Your complete `face_gap()` code, plus your note on how you handled (or
   deliberately didn't handle) heading wraparound.
5. Your three-trial results table and a short reflection: how close did the
   robot's final heading come to the true gap direction, and what's the
   biggest source of error you noticed (sensor noise, scan speed, turning
   overshoot, something else)?

## What Success Looks Like

- `scan()` returns a list of paired heading/distance readings that visibly
  changes as the robot turns across the gap.
- `find_gap_heading()` returns a heading that, when you check it by hand
  against the readings list, plausibly points at the open space.
- `face_gap()` reliably turns the robot to within a few degrees of that
  target heading.
- Across three differently-arranged trials, the robot consistently ends up
  facing the gap rather than a wall section.

## Optional Extension

Once `face_gap()` works reliably, try driving the robot straight forward
after facing the gap (`drivetrain.straight(...)` or a short `set_effort()`
burst) to actually pass through it. Use `reliable_distance()` while driving
forward as a safety check — if the distance ahead suddenly drops well below
what you expected for the gap, stop before hitting a wall section.
