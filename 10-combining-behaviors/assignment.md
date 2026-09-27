# Final Project: The Combined-Behaviors Challenge

**Sessions 10–12 (Weeks 4) · Team-based · Culminating project for Intro to Robotics**

## Overview

Your team will program an XRP robot to autonomously run a course that combines **line-following** with **obstacle detection**. This is the capstone project for the seminar: it pulls together everything you've learned about sensing, decision-making, and motor control into one working robot behavior.

**The course** (set up in the classroom/lab space) consists of:
- A taped line path (straight sections + at least one curve) on the floor
- One or more obstacles (boxes, blocks, or cones) placed directly on or near the line
- A clearly marked START and FINISH

**The goal:** your robot follows the line, detects the obstacle before colliding with it, and either (a) stops cleanly, or (b) navigates around the obstacle and rejoins the line to reach the finish — your team chooses which challenge mode to attempt (see Requirements below).

Teams of **2-3 students**. You'll work on this during Session 10 (today), Session 11, and present it at **Demo Day in Session 12**.

## Learning Objectives

By the end of this project, you will be able to:
- Combine two or more independently-working sensor behaviors into a single coherent MicroPython program
- Use `if`/`else` decision logic to switch behaviors in real time based on sensor input
- Distinguish between fixed sequencing ("do A then B") and reactive decision-making ("do A until sensor says otherwise")
- Debug a multi-sensor program methodically, by testing each behavior in isolation before combining
- Collaborate as a team to plan, build, and present a working robotics demo

## Choose Your Challenge Mode

Pick ONE (check with your instructor if unsure which fits your team):

- **Mode A — Stop & Report (baseline, required minimum):** Robot follows the line and, upon detecting the obstacle within a set distance, stops completely and (optionally) signals detection (e.g., LED, print statement, or servo movement).
- **Mode B — Go Around (stretch of baseline):** Robot detects the obstacle, leaves the line, drives around the obstacle using a fixed turn sequence, and re-finds/rejoins the line to reach the finish.
- **Mode C — Your Own Twist:** Propose your own variation (e.g., obstacle triggers a different route, or the robot backs up and reroutes) — must be approved by the instructor during Session 10.

All teams must implement at least Mode A; Mode B or C earns higher rubric marks.

## Requirements / Rubric

| Criteria | What it looks like |
|---|---|
| **Line-following works** | Robot reliably follows the taped line for the straight and curved sections without instructor intervention |
| **Obstacle detection works** | Robot reliably detects the obstacle using the ultrasonic sensor before making contact with it |
| **Behavior combination (core)** | Program correctly uses if/else so obstacle-handling only triggers when needed, and line-following resumes/continues appropriately |
| **Chosen mode completed** | Robot performs the full chosen mode (stop cleanly, OR go around and rejoin line and reach finish) |
| **Code quality** | Behaviors are organized into separate, named functions (e.g., `follow_line()`, `check_obstacle()`); code is reasonably commented |
| **Team plan/pseudocode** | Team has a written plan/pseudocode sketch from Session 10, visibly followed or revised |
| **Demo Day presentation** | Team can run their robot live and briefly explain (1-2 min) how their decision logic works |

Grading will weigh reliability (does it work consistently, not just once) as much as ambition.

## Milestones

- **Session 10 (today) — Plan & Combine:**
  - Form your team, read this handout together
  - Sketch your plan/pseudocode on paper: what does the robot sense, and what decisions does it make?
  - Choose your challenge mode
  - Pull together your existing Session 9 line-following code and Session 5-6 obstacle-detection code into one file
  - Get a first combined version running, even if rough

- **Session 11 — Build, Iterate, Debug:**
  - Test on the actual course; tune your obstacle-detection distance threshold
  - Debug behavior transitions (the trickiest part is usually "how does the robot find the line again?")
  - Refine turn sequences, timing, and sensor thresholds
  - Do full run-throughs and fix failure points
  - Prepare your 1-2 minute explanation for Demo Day

- **Session 12 — Demo Day:**
  - Each team runs their robot on the live course in front of the class
  - Brief explanation of your logic and any interesting bugs/fixes
  - Instructor scores against the rubric above

## Materials & Starter Code Needed

- Your XRP robot kit (motors, encoders, ultrasonic sensor, IMU, line/reflectance sensor, servo)
- Web-based MicroPython editor (same as previous sessions)
- Your own Session 9 line-following code (bring it forward)
- Your own Session 5-6 obstacle-detection code (bring it forward)
- Course rules handout (provided in class)
- Recommended starting skeleton:

```python
from XRP import *

def follow_line():
    # paste/adapt your Session 9 line-following logic here
    pass

def obstacle_detected():
    # returns True if ultrasonic sensor reads closer than your threshold
    return get_distance() < 10  # tune this value in cm

def handle_obstacle():
    # Mode A: stop. Mode B: turn sequence to go around.
    stop_motors()

while True:
    if obstacle_detected():
        handle_obstacle()
    else:
        follow_line()
```

## What "Success" Looks Like at Demo Day

- The robot starts at the marked START, follows the taped line without needing to be picked up or nudged
- When it reaches the obstacle, it clearly and reliably detects it (not by luck) and performs your chosen behavior (clean stop or go-around)
- If attempting Mode B/C, the robot successfully finds its way back to the line and reaches FINISH
- Your team can explain, in plain language, where the if/else decision points are in your code
- The run doesn't need to be flawless every single time — but it should work reliably, not just "once, if you're lucky"

## Stretch Goal / Bonus Challenge

**Victory Flag:** Add a servo-based "flag" that raises when your robot successfully completes the course (reaches FINISH, or successfully completes its obstacle maneuver). This means adding a third behavior/decision point: detecting "am I done?" (e.g., via a timer, a second line marker, or distance traveled) and triggering a servo movement in response.

Other bonus ideas (pick at most one, talk to your instructor):
- Handle **two obstacles** instead of one, each requiring correct detection and response
- Use the **IMU/gyro** to make your go-around turns more precise (e.g., turn exactly 90 degrees) instead of timed turns
- Add a **sound or LED signal** that's different for "obstacle stopped" vs. "obstacle avoided" vs. "finished"

Bonus work will not replace missing core requirements — it's extra credit on top of a working baseline robot.
