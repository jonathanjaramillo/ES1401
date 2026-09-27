# Introduction to Robotics — 1-Month Freshman Seminar (Course Outline)

Redesigned from the original 1-credit upper-level "Introduction to Robotics" course into a 1-month, freshman-level seminar for incoming engineering students with no prior coursework. Programmed in MicroPython on the SparkFun XRP (Experiential Robotics Platform).

**Format:** 3 sessions/week for 4 weeks (12 sessions total). Each session is a short (~15 minute) lecture followed by hands-on lab/programming time.

**Design goal:** Get students driving a real robot as early as possible, then layer in sensing and simple feedback control — all taught conceptually/intuitively, with the calculus- and linear-algebra-heavy material from the original course (DH parameters, Jacobians, PID math, Bode plots, Kalman filtering) deliberately cut and mentioned only as "there's math for this in later courses."

## Week 1 — Get It Moving

1. **Sense-Plan-Act & Robot Anatomy** — Sense-Plan-Act loop, tour of robot subsystems using the XRP as the example (motors, encoders, ultrasonic, IMU, line sensor, servo). Lab: unbox/assemble, MicroPython web editor setup, first program (blink an LED, print one sensor reading).
2. **Differential Drive** — how the XRP drives, differential drive intuition (two motors, different speeds = turning), what motor commands look like in MicroPython. Lab: write and run basic motor commands — spin each wheel, drive forward, turn in place.
3. **Open-Loop Control & First Drive** — timed commands vs. "smart" driving, why timing-based movement drifts. Lab: program the XRP to drive a simple shape (square or straight line + turn). **Milestone: students are driving their robots by the end of this session.**

## Week 2 — Sensing the World

4. **Encoders** — how the XRP counts wheel rotations to measure distance. Lab: read encoder counts live; drive a specific measured distance instead of a timed guess.
5. **Ultrasonic & IMU** — "how far" and "which way." Lab: print live distance/heading readings while driving; observe how the numbers change.
6. **Noise & Smoothing** — noisy sensors and simple smoothing (just the intuition — averaging a few readings). Lab: wall-approach behavior — drive toward a wall and stop at a set distance using the ultrasonic sensor.

## Week 3 — Reacting & Following

7. **Line Sensor** — what the line/reflectance sensor sees, how to read it. Lab: read the line sensor live; detect "on the line" vs. "off the line."
8. **Open vs. Closed-Loop / Error** — open-loop vs. closed-loop, the "error" idea (how far off am I?). Lab: simple bang-bang line following (turn hard left/right based on sensor reading).
9. **Proportional Control** — a taste of proportional control ("steer harder the more off-line you are"), instead of hard on/off turns. Lab: smooth out the line-following behavior using a simple proportional turn.

## Week 4 — Bring It Together

10. **Combining Behaviors** — sequencing and simple decision-making (if/else) to chain sensing + driving into one program. Lab: final project kickoff (line-following course or wall-following challenge — team choice).
11. **Debugging & Iterating** — why robots don't work the first time, how to isolate the problem. Lab: final project build/iterate time.
12. **Final Project Demo Day** — teams run their XRPs through the course, peer showcase. No new lecture content.

## What's Cut From the Original Course (and Why)

The original 11-lecture, 1-credit upper-level course covered forward/inverse kinematics via Denavit-Hartenberg parameters, Jacobian-based velocity kinematics and inverse kinematics, rotation matrices and homogeneous transforms, configuration space, full PID control theory (rise time/overshoot/settling time derivations), frequency-domain filter design (Bode plots), and Bayesian/Kalman filtering. All of this requires calculus and linear algebra that incoming freshmen won't yet have, so it's cut from this version entirely and only referenced in passing as material students will encounter in later robotics/controls courses.
