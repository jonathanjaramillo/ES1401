# Introduction to Robotics — Freshman Seminar (Course Outline)

Redesigned from the original 1-credit upper-level course for incoming engineering students with no prior coursework. Students program a SparkFun XRP robot in MicroPython.

**Format:** 3 sessions per week for 2 weeks (6 sessions total). Each session begins with a short lecture and continues with hands-on lab and programming time.

**Design goal:** Get students driving a real robot early, then add sensing and simple feedback control. Calculus and linear algebra topics from the upper-level course are left for later courses.

## Week 1 — Motion and Measurement

1. **Sense-Plan-Act & Robot Anatomy** — Tour the XRP's motors, encoders, ultrasonic sensor, IMU, line sensor, and controller. Lab: assemble the robot, connect the MicroPython editor, and run a first program.
2. **Differential Drive** — See how two independently driven wheels make the XRP move straight, turn, and spin. Lab: command each wheel and make the robot drive. **Milestone: students drive their robots by the end of this session.**
3. **Encoders** — Count wheel turns to measure motion and compare timed movement with measured movement. Lab: drive a square using motor effort, regulated speed, and measured distance.

## Week 2 — Sensing and Feedback

4. **Ultrasonic & IMU** — Measure distance to objects and changes in orientation. Lab: observe live sensor readings and investigate when ultrasonic measurements are reliable.
5. **Noise & Smoothing** — Interpret noisy readings and use a short moving average. Lab: approach a wall and stop at a target distance, comparing raw and smoothed readings.
6. **Open vs. Closed-Loop Control & Error** — Compare a fixed motor script with repeated sensing and correction. Lab: calibrate the line sensor, then build and tune a simple bang-bang line follower.

## What's Cut From the Original Course

The upper-level course covered kinematics, coordinate transforms, Jacobians, full PID control theory, frequency-domain filter design, and Bayesian/Kalman filtering. Those topics require mathematics incoming freshmen have not yet studied, so they are outside this seminar.
