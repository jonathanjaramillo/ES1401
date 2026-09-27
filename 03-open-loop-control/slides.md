---
theme: default
title: Session 3 — Open-Loop Control & First Drive
---

# Open-Loop Control
## & Your First Drive

Week 1, Session 3 — Introduction to Robotics

**Today: your robot moves under its own code for the first time.**

::description::
Big, bold title slide. Background graphic: a simple line-art XRP robot icon mid-motion with small "speed lines" behind its wheels, like it's zooming off the slide. Optional confetti/spark accents near the title text to signal a milestone/celebration moment.

::notes::
Welcome back! Quick hype line to open: "Alright everyone — by the end of today's lab, your robot is going to drive on its own, running code YOU wrote. No remote control, no pushing it with your hand — just your program telling it what to do." Pause for a beat, let that land. Today's lecture is short on purpose because I want to save time for you to actually get your hands on the robots. We're covering one big idea: open-loop control. Once you get it, the lab will make total sense.

---

# What Is "Open-Loop Control"?

- Giving the robot a **command** and trusting it blindly — no checking, no feedback
- Example: "Drive forward for 2 seconds" — then just... hope
- The robot never asks "did that actually work?"
- Contrast: **closed-loop** control checks results and corrects (that's coming in later sessions!)

::description::
Simple two-box diagram: Box 1 labeled "YOU (the program)" with an arrow labeled "Command: forward 2s" pointing to Box 2 labeled "ROBOT MOTORS." No arrow going back from robot to program — emphasize the missing feedback loop with a big red "X" or dashed broken-arrow where a return path would be. Caption underneath: "No eyes, no ears, no feedback — just blind trust."

::notes::
So what does "open-loop" actually mean? Think of it like tossing a paper airplane. You fold it, you throw it, and then it's out of your hands — you don't get to steer it mid-flight based on what it's doing. That's open-loop control: you send a command, like 'spin the motors forward for 2 seconds,' and the robot just does it, with zero awareness of whether it actually went where you wanted. Later this month, we'll add sensors so the robot can check itself and correct — that's called closed-loop control. But today, we start simple: no sensors, just timed commands. It's the foundation everything else builds on.

---

# Why Does Timing-Based Movement Drift?

- **Battery voltage sag** — as the battery drains, motors get slightly weaker mid-lab
- **Wheel/motor friction differences** — your two motors are never perfectly identical twins
- **Surface variation** — carpet vs. tile vs. a stray pencil on the floor
- Small errors are invisible on their own... but they **add up** over time

::description::
Animated SVG: a small robot icon attempting to drive a perfect square using dashed guide lines (the "intended" path). Its actual path is drawn as a solid, slightly wobbly line that starts overlapping the dashed square but drifts progressively farther off course with each of the 4 turns, ending noticeably away from the starting corner. Small annotation icons along the path: a battery icon (voltage sag), a friction/gear icon (motor mismatch), and a bumpy-texture icon (surface variation), each pointing to the spot where drift visibly increases.

::notes::
Here's the catch with open-loop control: it drifts. Say you tell your robot 'turn for exactly 0.5 seconds to make a 90-degree turn.' The first turn might be pretty close. But by turn four, you could be way off. Why? Three sneaky culprits. One: your battery is slowly losing voltage as you run the robot, so the same command produces slightly less motion over time. Two: your two motors are not perfectly identical — one might spin just a hair faster than the other, so 'drive straight' quietly curves. Three: the floor itself — carpet grabs wheels differently than tile, and even a piece of dust can throw things off. None of these errors are huge alone, but open-loop control has no way to notice or correct them, so they stack up lap after lap. That's the tradeoff we're making today for simplicity.

---

# Today's Lab: First Drive!

- Program your XRP to trace a **shape** — a square, or a line-and-turn path
- Pure timed commands: `drive forward for X seconds`, `turn for Y seconds`
- **No sensors yet** — just you, timing, and trial and error
- This is it: the moment your code becomes motion

::description::
Bold, energetic slide. Simple diagram of a square path traced with a dotted line and small arrows at each corner labeled "turn ~90°", with a robot icon at the starting corner and a small "GO!" starburst badge overlapping the top corner of the slide.

::notes::
This is the moment we've been building toward. In the lab today, you're going to write a short MicroPython program that drives your XRP in a shape — most of you will do a square: forward, turn, forward, turn, four times, and see if you land back close to where you started. Some of you might do a straight line and a single turn instead — either way, it's the same core skill. You'll be tuning numbers — how many seconds forward, how many seconds to turn — and watching what actually happens. I want you to expect some drift, remember what we just talked about — voltage sag, friction, surface — that's normal and expected, not a bug in your code.

---

# What Success Looks Like

- Robot completes the shape and returns **close** to its starting point
- "Close" = roughly within a foot — this isn't about perfection today
- You'll *tune* your timing values by testing, adjusting, testing again
- Drift you observe = evidence for *why* we'll need sensors soon

::description::
Simple before/after style graphic: left side shows a square path with a large gap between start and end point labeled "too much drift"; right side shows a square path that closes almost into a loop labeled "good enough — success!" Small checkmark icon on the right side.

::notes::
Let's be really clear about the bar here: you are not trying to build a perfect square with laser-precision corners. Success today means your robot drives the shape and comes back within about a foot of where it started — that's it. You'll get there through testing: run it, see where it ends up, tweak your seconds values, run it again. That loop — test, observe, adjust — is basically what engineers do all day. And here's a preview: the drift you're going to see today is exactly the problem that sensors solve. Keep that feeling in your back pocket, because in a couple sessions we start adding eyes and ears to the robot to fix this.

---

# Let's Go Drive Robots

- Grab your XRP, charge check, open the web editor
- Start simple: get straight-line driving solid before attempting turns
- Ask for help early if your robot won't move — usually a wiring/port issue
- **Have fun — this is your robot's first real drive!**

::description::
Full-width celebratory image: a small fleet of simple line-art XRP robots lined up at a "starting line" drawn on the floor, like a race about to start. Optional light motion-blur or speed-line effect behind each robot to convey energy and anticipation.

::notes::
Alright, that's the lecture — short and sweet, just like I promised. Quick tips before you dive in: check your battery is charged, get the web editor open, and start with just driving straight before you add turns, so you know your forward command works first. If your robot doesn't move at all, don't panic — nine times out of ten it's a wiring or USB connection issue, so flag me down and we'll sort it fast. Otherwise — this is the moment. Go write some code, hit run, and watch your robot move for the very first time under its own power. Let's go!
