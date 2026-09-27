---
theme: default
title: Session 7 — Line Sensor
info: Intro to Robotics — Week 3, Session 7 of 12
---

# The Line Sensor
### Teaching your robot to see the floor

- Today: how the XRP "sees" a dark line on a light floor (or vice versa)
- Why it matters: this is the sensor behind everything we'll do with line following for the rest of the course

Speaker notes:
Welcome back. Quick session today — about 15 minutes — because I want you to spend most of your time in lab actually watching numbers change on screen. Last time we worked with the ultrasonic sensor for distance. Today we add a new sense: the line sensor, which lets the robot tell the difference between light and dark surfaces right under it. This is a big one — basically every line-following lab for the rest of this course builds on what you learn today.

---

# What Does "Reflectance" Mean?

- The line sensor is a tiny LED + light detector pair
- The LED shines light down at the floor
- The detector measures how much of that light bounces back
- Light floors reflect a LOT of light back → high reading
- Dark tape absorbs light instead of reflecting it → low reading

SVG: Cross-section side view of the line sensor module close to the floor. Two side-by-side scenarios. Left scenario: LED (small triangle/bulb icon) shining a light cone down onto a white floor surface; arrows show most of the light bouncing back up into a photodetector icon; label "White floor → reading ≈ 950 (out of 1000)". Right scenario: identical LED/detector setup but shining onto a strip of black tape; arrows show the light being absorbed (fewer/faded arrows bouncing back, drawn as short dashed arrows fading into the tape); label "Black tape → reading ≈ 120 (out of 1000)". Both scenarios drawn at the same scale so students can visually compare "lots of light back" vs "almost no light back."

Speaker notes:
Here's the core idea, and it's simple: the sensor doesn't "see" a line the way your eye does. It just measures brightness. There's a tiny LED that shines light straight down at the floor, and right next to it, a light detector that measures how much of that light comes bouncing back. White or light-colored floors are great reflectors — most of the light bounces right back up into the detector, so you get a high number. Black tape absorbs light instead of reflecting it, so much less light comes back, and you get a low number. That's it. No cameras, no image processing — just "how much light bounced back."

---

# From Light to Number

- The sensor reports its reading as a number, not a picture
- On the XRP, values typically range roughly from 0 to 1 (or 0–1000 depending on library) — check your reference sheet
- Low number = dark surface underneath (absorbing light)
- High number = light surface underneath (reflecting light)
- The exact numbers depend on your floor, tape, and lighting in the room

Matplotlib plot: Simple horizontal bar or gauge-style illustration showing a number line from 0 to 1000. Two labeled markers on the line: one near the left (e.g., 120) labeled "dark tape" with a small black square icon, one near the right (e.g., 950) labeled "light floor" with a small white/light gray square icon. A shaded gray band in between labeled "the gray zone — depends on your setup" to foreshadow the threshold discussion.

Speaker notes:
So the sensor hands you a single number. Depending on the exact library call we use, that number might be scaled from 0 to 1, or 0 to 1000 — I'll show you exactly which one when we get to code in a second. The important mental model is just: low number, dark surface; high number, light surface. But — and this is important — the actual numbers you get will depend on your specific floor and tape and even the room lighting. That's why you can't just trust a number I tell you here; you have to go measure it yourselves in lab today.

---

# Reading It in MicroPython

- The XRP library gives you a simple function call to get the current reading
- You'll typically read one sensor value; some XRP kits have more than one line sensor (left/right) for later labs
- Pattern: read the value, then print it, in a loop, so you can watch it live

```python
from XRPLib.defaults import *

while True:
    value = reflectance.get_left()
    print(value)
    time.sleep_ms(200)
```

- `time.sleep_ms(200)` just slows down the printing so it's readable

Speaker notes:
In code, this looks a lot like the ultrasonic sensor from a couple sessions ago — call a function, get a number back. Here we're calling something like reflectance.get_left(), which returns the current reading from the sensor. We wrap it in a loop with a print statement and a short sleep so the numbers scroll by at a readable pace instead of flooding your screen. In lab, you're going to run something almost exactly like this and watch the number change as you move the robot by hand over the floor and over a piece of tape.

---

# Watching the Signal Live

- Move the sensor by hand over floor → tape → floor
- The printed numbers should rise and fall accordingly
- This "live watching" is exactly how you'll pick a threshold in lab

Matplotlib plot: Line trace with time (or sample number) on the x-axis and sensor reading (0–1000) on the y-axis. The trace starts high (~900, over floor), dips sharply down to a low plateau (~150, over tape) for a stretch, then rises back to a high plateau (~900, over floor again) — like a wide "U" upside down, or a notch. Annotate the low plateau region with a bracket labeled "on tape" and the two high regions labeled "on floor." Add a horizontal dashed reference line around y=500 labeled "possible threshold?" to preview the next slide.

Speaker notes:
This is what you should expect to see: hold the robot steady over plain floor, and the numbers stay high and roughly steady. Slide the sensor over a strip of tape, and the numbers drop — often quite sharply, not gradually. Slide it back onto floor, and the numbers pop back up. That sharp jump between "high" and "low" is really useful, because it means we can pick a single cutoff number — a threshold — to decide, in code, whether the robot is on the line or not.

---

# The Idea of a Threshold

- A threshold is just a cutoff number you choose
- If reading < threshold → probably on dark line
- If reading > threshold → probably on light floor
- (Flip the comparison if your line is light-on-dark instead of dark-on-light!)
- Pick a threshold roughly in the middle of your "floor" and "tape" readings

SVG: The same number line from 0–1000 as before, but now with a single vertical dashed line drawn at a chosen threshold value (e.g., 500), splitting the line into two colored regions — left region shaded dark labeled "ON LINE (below threshold)", right region shaded light labeled "OFF LINE (above threshold)". Small callout arrow pointing at the threshold line: "You choose this number from YOUR measurements."

Speaker notes:
Once you have a sense of your two clusters of numbers — one cluster when you're over floor, one cluster when you're over tape — picking a threshold is easy: just pick something in between. If floor reads around 900 and tape reads around 150, a threshold of 500 comfortably separates the two. In code, this becomes a simple comparison: if the reading is below your threshold, you say "on the line"; otherwise, "off the line." One catch — depending on whether your tape is darker or lighter than your floor, you might need to flip that greater-than or less-than. You'll sort that out hands-on in a minute.

---

# Why This Matters Going Forward

- Everything from here forward — line following, intersections, turns — builds on this one measurement
- Today's job: get comfortable reading the value and picking a good threshold
- Next sessions: use on_line() logic to make the robot steer itself along a path

- Today's lab goal: read live values, choose a threshold, write a small on_line() helper function

Speaker notes:
I want to be really clear about why we're spending a whole session on what seems like "just reading a number." This single sensor reading, and the threshold you pick today, is the foundation for every line-following robot behavior for the rest of this course — following a line, detecting intersections, stopping at markers, all of it starts here. So today in lab, your only jobs are: watch the live values, figure out a threshold that reliably separates line from floor for your setup, and wrap that decision into a simple function called on_line() that returns True or False. Get that solid today, and next session's line-following work will feel much easier. Let's head to lab.
