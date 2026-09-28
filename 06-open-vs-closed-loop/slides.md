---
theme: default
title: Open vs. Closed-Loop Control & Error
---

# Open-Loop vs. Closed-Loop Control
## Session 6 — Week 2

- Today: why "checking your work" matters in robotics
- We'll define **error** and meet our simplest controller: **bang-bang**
- Lab: make the XRP follow a line by reacting to sensor data

Speaker notes: Welcome back. You've driven the XRP with timed motor commands and used sensors to read the world. Today we connect those ideas: what happens when a robot reacts to what it senses, instead of just following a script? By the end of this short lecture you'll understand the difference between open and closed loop control, what "error" means, and the simplest way a robot can respond to error — bang-bang control. Then you'll build it.

---

# Quick Recap: Timed Driving from Session 2

- Robot runs a **pre-planned sequence** — "drive forward 2 sec, turn 90°, drive 1 sec"
- No sensors involved during execution — it's a blind script
- Works great... **until something is off** (wheel slip, low battery, bumpy floor)
- Small errors **accumulate** and never get corrected

Description: Simple diagram — a timeline/flowchart of boxes ("drive 2s" → "turn 90°" → "drive 1s") with no arrows going backward and no sensor icon anywhere, emphasizing one-way flow.

Speaker notes: In Session 2, you programmed the robot with motor effort and a fixed duration. It did what you commanded without checking where it ended up. Friction, battery voltage, and floor material change the result. Open-loop plans cannot adapt. Today we build a robot that can.

---

# Closed-Loop Control: Sense, Compare, React

- **Closed-loop control**: the robot continuously checks a sensor and adjusts its behavior
- The loop: **sense → compare to goal → act → repeat**
- This feedback loop is what lets a robot correct itself in real time
- Almost every real robot (and cruise control, thermostats, video game AI) uses this idea

Description: Animated SVG loop diagram — three circular nodes labeled "SENSE," "COMPARE," "ACT" connected by arrows forming a circle, with the arrows animating (pulsing/flowing) to show the cycle repeating continuously.

Speaker notes: Closed-loop control just means the robot is constantly in a loop: look at a sensor, compare what it sees to what it wants, then act, and immediately do it again. It never stops checking. Think of a thermostat — it doesn't just blast heat for ten minutes and hope; it keeps checking the temperature and reacting. That's the same idea we're bringing to the XRP today.

---

# Open-Loop vs. Closed-Loop, Side by Side

- **Open-loop**: drive blindly along a taped line — ignores drift, eventually drives off the tape
- **Closed-loop**: constantly checks the line sensor, notices drift, and steers back
- Closed-loop costs more code and more sensor reads — but it's far more robust
- Trade-off: complexity vs. reliability

Description: Animated SVG, side-by-side comparison — left side shows a robot icon driving in a straight dashed path that gradually drifts off a taped line and never corrects (open-loop), looping. Right side shows a robot icon whose path wobbles near the line, drifting slightly then snapping back onto the line repeatedly (closed-loop), looping continuously.

Speaker notes: Here's the comparison that matters for today's lab. Picture two identical robots on the same taped line. The open-loop one just drives straight — the instant the tape curves or the wheels don't spin perfectly evenly, it wanders off and never knows it. The closed-loop one is constantly asking 'am I still on the line?' and nudging itself back. It might not be perfectly smooth, but it stays on task. That reliability is worth the extra code.

---

# What Is "Error"?

- **Error = where you want to be − where you actually are**
- For line following: error = how far off the line am I, and in which direction?
- With a simple line sensor, error can be as basic as: **"on the line"** or **"off to the left"** or **"off to the right"**
- Every closed-loop controller's whole job is: **drive the error toward zero**

Description: Simple SVG diagram — a horizontal taped line with a robot icon centered on it (labeled "error = 0"), and a second faded robot icon offset to the left of the line with a dashed arrow pointing back to center labeled "error".

Speaker notes: Let's define error precisely, because you'll hear this word constantly for the rest of the course. Error is simply the gap between your goal and your current state. For our line follower, the goal is 'centered on the line.' If the line sensor tells us we've drifted left, that's our error — and it's telling us which direction to correct. Every single closed-loop controller you will ever write, from a thermostat to a self-driving car, is fundamentally just trying to drive some error down to zero.

---

# Bang-Bang Control: The Simplest Reaction

- **Bang-bang control**: react with full force in one direction or the other — **no in-between**
- Rule: if error says "off to the left" → turn hard right. If "off to the right" → turn hard left.
- No calculating *how much* to correct — just full correction, every time
- Simple to code, but tends to **overcorrect and oscillate** (zig-zag)

Description: Animated SVG — a robot icon zig-zagging sharply back and forth across a straight taped line, overshooting the line each time before snapping the opposite direction, illustrating bang-bang's jittery back-and-forth behavior, looping continuously.

Speaker notes: Now, the simplest possible way to react to error is called bang-bang control — named because the response just 'bangs' from one extreme to the other, full left or full right, with nothing gentle in between. If the sensor says you're off the line to the left, you don't nudge — you turn hard right, immediately. It sounds crude, and it is — it tends to zig-zag rather than smoothly track the line — but it's incredibly simple to implement and it works. It's the perfect first closed-loop controller for us to build today.

---

# From Idea to Code

- Read the line sensor each loop iteration
- If sensor says "off left" → command a hard right turn
- If sensor says "off right" → command a hard left turn
- If sensor says "on line" → drive straight
- Repeat forever — that repetition IS the closed loop

Description: Simple flowchart SVG — a single decision-diamond loop: "Read line sensor" → diamond "off left? / on line? / off right?" → three branches ("hard right", "straight", "hard left") that all merge back to an arrow looping to "Read line sensor" again.

Speaker notes: So structurally, here's all bang-bang line following really is: an infinite loop that reads the sensor, checks which of three states it's in, and picks one of three fixed actions. There's no math, no averaging, no smoothing — just a direct if/elif/else reacting to the sensor. That's exactly what you're going to write in today's lab.

---

# Lab Preview: Bang-Bang Line Following

- You'll write a MicroPython loop that reads the XRP's line sensor every cycle
- Off the line to the left → turn hard right. Off to the right → turn hard left.
- Goal: keep the robot roughly following a taped loop, even if it zig-zags
- Don't worry about smoothness today; focus on sensing and correcting reliably

Speaker notes: In the lab, first print the left and right line sensor readings over tape and floor to choose a threshold. Then fill in the sensing and reacting logic and test it on a taped loop. Expect visible zig-zagging; that is normal for bang-bang control. Your goal is to keep the robot roughly on the line for a full loop without losing it completely. Head to your kits and let's get building.
