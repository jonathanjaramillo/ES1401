---
theme: default
title: Session 5 — Noise & Smoothing
---

# Noise & Smoothing
### Session 5 · Week 2

- Why sensor readings jump around
- How to calm them down with a "moving average"
- Setting up for today's lab: wall-approach

**Speaker notes:** Welcome back! Quick recap — last session you got the ultrasonic sensor reading distances and maybe printed some numbers to the console. Today we ask: did anyone notice the numbers weren't perfectly steady, even when the robot wasn't moving? That's our topic today, and it's the last thing you need before today's lab, where you'll make the robot drive up to a wall and stop on its own.

---

# Real Sensors Are Jumpy

- Point the ultrasonic sensor at a wall and hold the robot still
- You'd *expect* the same number every time... but you don't
- Readings might bounce: 6.0", 6.3", 5.8", 6.1", 6.4"...
- The IMU/gyro does this too — tiny readings jitter even sitting flat on a table

**Matplotlib plot:** A simple line plot titled "Raw Ultrasonic Readings (Robot Stationary)" — x-axis "Sample #" (0–30), y-axis "Distance (cm)". Plot a jagged, noisy line hovering around 15 cm (true distance), generated as `15 + random noise` — visually chaotic, no clear pattern, just static jitter around a flat true value (shown as a thin dashed horizontal reference line at y=15).

**Speaker notes:** Show this plot. Ask the class: "The robot never moved — so why isn't this a flat line?" Let a couple students guess. The honest answer: sound waves bounce around, electrical noise exists, tiny vibrations happen, and the sensor's own measurement process isn't perfectly precise. This is true of basically every real-world sensor you'll ever use — not just on the XRP, but in phones, cars, medical devices, everything. It's not a bug, it's just how the physical world works when you're trying to measure it electronically.

---

# Why Should We Care?

- If your code says "stop when distance < 15 cm," a jumpy reading can trigger that condition too early or too late
- One bad reading (a "spike" or "glitch") can make the robot stop far from the wall, or nearly bump into it
- We don't need perfect sensors — we need *decisions* that aren't fooled by single bad readings

**Speaker notes:** This is the practical hook for today's lab. Imagine your stopping condition is "if distance is less than 15 cm, stop." If one single noisy reading dips to 12 cm for just one instant, your robot might slam on the brakes way too early, or worse — miss a bad-close reading and keep driving toward the wall. We want our stop decision to be based on something more trustworthy than any single number.

---

# The Fix: Averaging Recent Readings

- Idea: instead of trusting *one* reading, average the last few
- This is called a **moving average**
- Example: keep the last 5 readings, average them, use *that* number
- As new readings come in, drop the oldest, add the newest — the "window" slides forward

**Speaker notes:** Here's the core idea, and it's genuinely simple — no fancy math needed. Instead of asking "what did the sensor just say?", we ask "what have the last few readings said, on average?" A single glitchy value gets diluted out by four or five normal ones around it. We call this a moving average because the group of readings you're averaging — the "window" — slides forward in time as new data arrives.

---

# Moving Average, Visually

- Averaging smooths out the bumps but still tracks real changes
- A bigger window (more readings) = smoother, but slower to react
- A smaller window = faster to react, but jumpier

**Matplotlib plot:** Two overlaid line plots on the same axes, titled "Raw vs. Smoothed Distance Reading Over Time" — x-axis "Time (samples)", y-axis "Distance (cm)". First line: jagged, noisy raw readings (thin, light gray) showing a robot actually approaching a wall — a general downward trend from about 60 cm to 10 cm buried in jitter. Second line: a moving-average (window=5) of the same data (thick, bold color) showing a much smoother downward curve that closely tracks the true trend without the jitter. Include a legend labeling "Raw" and "Smoothed (5-reading average)".

**Speaker notes:** This is the plot that matters most today. Notice the light gray jagged line — that's raw data as the robot drives toward a wall, distance genuinely dropping the whole time. The bold line is the moving average of that same data. See how it follows the real trend but without all the noise? That's the payoff. Also mention the tradeoff: average too many readings and your robot reacts slowly to real changes (like if the wall — or a person — suddenly gets closer); average too few and you still get jitter. Five readings is a reasonable starting point for our lab.

---

# What This Looks Like in Code

- Keep a small list of recent readings (e.g., last 5)
- New reading comes in → add it, drop the oldest if list is too long
- Compute `sum(readings) / len(readings)` → that's your smoothed value
- Use the *smoothed* value in your stop-condition, not the raw value

**Speaker notes:** No frequency math, no filter design — just a list and an average. Add the newest reading, if the list is longer than your window size drop the oldest one, then average what's left. That's the whole trick. In your starter code for lab today, this will be a small function you can drop right into your wall-approach loop.

---

# Today's Lab: Wall-Approach

- Drive the XRP toward a wall using the ultrasonic sensor
- Stop automatically once you're within a set distance (~15 cm)
- Try it with raw readings first — does it ever stop too early/late or jitter near the wall?
- Then try smoothing the readings before your stop check — does it get more reliable?

**Speaker notes:** That's the lecture — let's go build it. In the lab you'll write a loop that drives forward while checking distance, and stops once you're close enough to the wall. First try it with the raw sensor value straight into your if-statement, and watch what happens up close — some of you will probably see it twitch, stop early, or stop late. Then add the moving-average function we just talked about and compare. I want you to actually feel the difference, not just take my word for it. Questions before you head to your robots?
