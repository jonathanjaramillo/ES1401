---
theme: default
title: Sense-Plan-Act & Robot Anatomy
info: Week 1, Session 1 — Introduction to Robotics (XRP)
---

# Welcome to Robotics!
## Meet Your Robot: the XRP

- Over these two weeks, you build and program a real robot
- Across six classes, explore how robots sense, decide, and act
- Over two weeks, program the XRP to move and respond to its environment

**Graphic:** Full-bleed photo of an assembled XRP robot sitting on a table, clean and well-lit, no clutter. Just a strong hero image to open the class.

**Speaker notes:** Welcome students and set the scope: over six class meetings, they will learn how a robot senses, decides, and acts, then program the XRP to move and respond to its environment. No prior robotics experience is assumed.

---

# What Is a Robot?

- Before we build anything: what actually makes something a robot?
- Not "what parts does it have" — what's the underlying idea?

**Speaker notes:** (1:00–2:00) Open with the big question and let it sit — don't answer it yourself yet. Ask: "What is a robot? What makes something a robot instead of just... a machine?" Give students 30 seconds to talk to a neighbor, then take two or three verbal answers from the room without confirming or rejecting any of them. We're about to test whatever definitions come up against some real examples.

---

# Robot or Not?

- For each of these: is it a robot, or not? Be ready to defend your answer.
  - Robot vacuum (Roomba)
  - Dishwasher running its wash cycle
  - RC car being driven by a person
  - Thermostat
  - Wind-up toy car
  - Smart speaker (Alexa/Siri)
  - Vending machine
  - Mars rover

**Graphic:** Simple 4x2 grid of icon cards, one per item above, each with a small icon and a "robot or not?" question mark badge — no answers shown yet, this is a live poll slide.

**Speaker notes:** (2:00–4:30) Go through the list one at a time and take a quick show of hands on each — "robot" or "not a robot" — without telling them who's right yet. A few deliberately tricky ones: the dishwasher and the wind-up toy car just run a fixed mechanism/timer with zero sensing, which feels robot-ish but isn't — this foreshadows open-loop control, which we will revisit in Session 6. The RC car has a person doing all the sensing and deciding; the car itself is just obeying, so most students will (correctly) say it's not a robot on its own. The thermostat, vending machine, smart speaker, Roomba, and Mars rover all actually do sense-and-react on their own, even though most people's gut reaction is that a thermostat "isn't a robot" — that tension is exactly what we resolve on the next slide.

---

# So, What Makes Something a Robot?

- A robot is a system that **senses** its environment, **decides** what to do, and **acts** — repeating that loop on its own
- No sensing, no repeating loop → it's just a machine, no matter how clever the mechanism
- By this definition: the thermostat, vending machine, Roomba, and Mars rover ARE robots. The wind-up car and the human-driven RC car are NOT.

**Speaker notes:** (4:30–5:30) Now give the formal definition: a robot senses its environment, decides what to do, and acts — and it does that loop by itself, continuously, not just once and not because a person is doing the sensing/deciding for it. Quickly resolve the "robot or not" list against this definition — the wind-up car and human-driven RC car fail because nothing on the robot itself is sensing and deciding; the dishwasher is the debatable one, since most dishwashers just run a timer rather than reacting to what they sense (a good preview of "open-loop" vs "closed-loop," a concept the whole course builds toward). The thermostat, vending machine, smart speaker, Roomba, and Mars rover all pass, even though they don't look alike physically. This one definition covers everything from a thermostat to a Mars rover — including the robot sitting in front of you.

---

# Every Robot Does the Same 3 Things

- **Sense** — gather information about the world
- **Plan** — decide what to do with that information
- **Act** — do something that changes the world

This is called the **Sense-Plan-Act loop**, and it repeats over and over, very fast.

**Graphic:** Simple animated SVG loop diagram: three circles labeled "SENSE," "PLAN," "ACT" arranged in a triangle, connected by curved arrows forming a continuous cycle. The arrows animate (dashes moving along the path) to show motion/repetition. Each circle has a small icon: an eye for Sense, a gear/brain for Plan, a wheel/arm for Act.

**Speaker notes:** (5:30–7:30) Here's the one idea I want you to walk away with today. Every robot ever built — a Roomba, a Mars rover, a self-driving car, your XRP — does the same three-step loop, forever, in a tight cycle. First it senses: it collects data about the world with sensors. Then it plans: its onboard computer decides, given what it just sensed, what to do next. Then it acts: it moves motors or does something physical that changes the world — which changes what it senses next, and the loop repeats. Sense, plan, act, sense, plan, act, many times per second. That's it. That's robotics in one sentence.

---

# Example: A Robot Avoiding a Wall

1. **Sense:** ultrasonic sensor measures "wall is 10 cm away"
2. **Plan:** program decides "that's too close — turn"
3. **Act:** motors spin to turn the robot away

Then the loop repeats immediately with a fresh sensor reading.

**Graphic:** Simple top-down SVG scene: a small robot icon approaching a wall, with a dashed distance line and "10 cm" label between the robot and wall, a thought-bubble icon above the robot showing a decision (checkmark/arrow turning), and a curved arrow showing the robot's new turned path away from the wall. Could be a 3-frame mini storyboard (before / decide / after) rather than animated.

**Speaker notes:** (7:30–9:30) Let's make that concrete with an example you'll actually build later in the course. Say the robot is driving forward and there's a wall ahead. Sense: the ultrasonic sensor pings the wall and measures the distance — say, 10 centimeters. Plan: the code checks that number and decides that's too close, time to turn. Act: the motors turn the robot away from the wall. And then — critically — it doesn't stop there. It immediately senses again, gets a new distance reading, and the whole loop repeats. That constant repeating is what makes it "smart" instead of just running a single scripted move.

---

# Meet the XRP: Your Robot for the Course

- Small differential-drive rover — two independently controlled wheels
- Built around a tiny computer chip (like the one inside many gadgets)
- Loaded with sensors and a motor for steering
- You'll program it in MicroPython, a beginner-friendly language

**Graphic:** Clean labeled photo/diagram of the XRP chassis from a 3/4 angle, with 5-6 numbered callout leader lines pointing to: the two drive wheels/motors, the ultrasonic sensor (front), the line/reflectance sensor (bottom), the servo, the main board, and the battery. Numbers correspond to a small legend list beside the image.

**Speaker notes:** This is the XRP — your robot for the course. It is a differential-drive rover: two wheels, each with its own motor, steer by spinning at different speeds. The robot has sensors, a small onboard computer, and runs MicroPython. Over the next two weeks, connect the sense-plan-act idea to these physical parts and use code to control them.

---

# The 5 Subsystems Every Robot Needs

- **Perception** — sensors that gather data (the "sense" part)
- **Computation** — the brain that decides (the "plan" part)
- **Actuation** — motors/motion that do things (the "act" part)
- **Communication** — how it talks to you or other devices
- **Power** — the energy source that runs everything

**Graphic:** SVG or diagram: five colored boxes arranged around a central robot icon, each box connected by a line to the robot, labeled with the subsystem name and a one-icon summary (eye=perception, chip=computation, wheel=actuation, wifi symbol=communication, battery=power). Color-code perception/computation/actuation to match the sense/plan/act colors from slide 2 for visual continuity.

**Speaker notes:** (11:00–13:00) Sense-plan-act is the loop, but robots also need supporting systems to make that loop possible. Perception is anything that senses — your sensors. Computation is the brain that plans — your onboard processor. Actuation is anything that acts — usually motors. Those three map directly onto sense-plan-act. But there are two more you need in real life: communication, so the robot can talk to you, or to other computers, often over WiFi; and power, because none of this works without a battery or energy source. Five subsystems: perception, computation, actuation, communication, power. Let's find every single one on the XRP.

---

# Course Overview

A new title slide introduces the structure of the course.

**Speaker notes:** This course combines technical content, hands-on robot programming, short quizzes, and class discussions.

---

# Content

- Robot anatomy and the sense-plan-act loop
- Differential drive
- Wheel encoders and motion measurement
- Ultrasonic sensing and the IMU
- Sensor noise and smoothing
- Open- and closed-loop control

**Speaker notes:** Present the technical topics as a subject overview without dividing them by week or session.

---

# Coding Activities

Most class meetings will be spent writing code and implementing algorithms on the robot.

**Speaker notes:** Explain that students will regularly turn lecture ideas into code and run them on the XRP.

---

# Quizzes

- One 3-question quiz each week
- Usually Friday unless otherwise specified
- In person, handwritten, short answer
- Based on lecture material

**Speaker notes:** Set expectations for the regular weekly quiz format and timing.

---

# Discussion Activities

Each class includes a discussion of recent events and interesting topics in robotics and AI.

1. AI Agents, Responsibility, and Society
2. Robots and Privacy
3. Autonomous Cars, Safety, and Responsibility
4. Specialized Robots and General-Purpose Humanoids

**Speaker notes:** Introduce the four discussion topics students will encounter during the course.
