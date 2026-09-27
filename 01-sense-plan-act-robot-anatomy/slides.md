---
theme: default
title: Sense-Plan-Act & Robot Anatomy
info: Week 1, Session 1 — Introduction to Robotics (XRP)
---

# Welcome to Robotics!
## Meet Your Robot: the XRP

- This month, you build and program a real robot
- Today: the big idea behind ALL robots, then meet your XRP
- By the end of class: XRP assembled, first program running

**Graphic:** Full-bleed photo of an assembled XRP robot sitting on a table, clean and well-lit, no clutter. Just a strong hero image to open the class.

**Speaker notes:** (0:00–1:00) Welcome everyone, quick intro to the course — one month, hands-on, you'll be programming this little rover sitting in front of you by the end of today's lab. No prior robotics experience assumed. Today's lecture is short on purpose: 15 minutes of "why" and "what," then straight into hands-on building. Let's get into it.

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

**Speaker notes:** (2:00–4:30) Go through the list one at a time and take a quick show of hands on each — "robot" or "not a robot" — without telling them who's right yet. A few deliberately tricky ones: the dishwasher and the wind-up toy car just run a fixed mechanism/timer with zero sensing, which feels robot-ish but isn't — this foreshadows "open-loop control," which we'll hit in Session 3. The RC car has a person doing all the sensing and deciding; the car itself is just obeying, so most students will (correctly) say it's not a robot on its own. The thermostat, vending machine, smart speaker, Roomba, and Mars rover all actually do sense-and-react on their own, even though most people's gut reaction is that a thermostat "isn't a robot" — that tension is exactly what we resolve on the next slide.

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

**Speaker notes:** (7:30–9:30) Let's make that concrete with an example you'll actually build later this month. Say the robot is driving forward and there's a wall ahead. Sense: the ultrasonic sensor pings the wall and measures the distance — say, 10 centimeters. Plan: the code checks that number and decides that's too close, time to turn. Act: the motors turn the robot away from the wall. And then — critically — it doesn't stop there. It immediately senses again, gets a new distance reading, and the whole loop repeats. That constant repeating is what makes it "smart" instead of just running a single scripted move.

---

# Meet the XRP: Your Robot for the Month

- Small differential-drive rover — two independently controlled wheels
- Built around a tiny computer chip (like the one inside many gadgets)
- Loaded with sensors and a motor for steering
- You'll program it in MicroPython, a beginner-friendly language

**Graphic:** Clean labeled photo/diagram of the XRP chassis from a 3/4 angle, with 5-6 numbered callout leader lines pointing to: the two drive wheels/motors, the ultrasonic sensor (front), the line/reflectance sensor (bottom), the servo, the main board, and the battery. Numbers correspond to a small legend list beside the image.

**Speaker notes:** (9:30–11:00) This is the XRP — your robot for the rest of the month. It's a differential-drive rover, which just means it has two wheels, each with its own motor, and it steers by spinning them at different speeds, kind of like a tank. It has a handful of sensors, a small onboard computer, and we'll program it all in MicroPython — Python, but designed to run on tiny low-power chips like this one. Over the next few weeks you'll use every part you see labeled here. Today, let's connect what we just learned about sense-plan-act to these actual physical parts.

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

# Spot the Subsystems on the XRP

| Subsystem | On the XRP |
|---|---|
| Perception | Ultrasonic sensor, IMU/gyro, line sensor |
| Computation | RP2040/RP2350 controller board |
| Actuation | Two drive motors + one servo |
| Communication | Built-in WiFi |
| Power | Onboard battery pack |

**Graphic:** Same labeled XRP photo/diagram from the earlier slide, but now each numbered callout is recolored/grouped to match one of the five subsystem colors from the previous slide, with a small color-coded legend (Perception=blue, Computation=green, Actuation=orange, Communication=purple, Power=red) so students can visually map parts to categories at a glance.

**Speaker notes:** (13:00–15:00) Here's the full picture. Perception: the ultrasonic sensor out front measures distance, the IMU — that's the gyro — senses tilting and turning, and the line sensor on the bottom detects light and dark surfaces, like a line on the floor. Computation: all of that data goes to the RP2040 or RP2350 chip on the main board — that's the brain, running your MicroPython code. Actuation: the two drive motors move the robot, plus one servo you can attach things to, like a little arm or a sensor mount. Communication: it has WiFi built in, which is how the web editor on your laptop talks to the robot. And power: a battery pack keeps all of it running without a cord. Every single piece maps onto one of our five categories.

---

# Today's Lab: Bring It to Life

- Unbox and assemble your XRP kit
- Set up the MicroPython web editor and connect to your robot
- Write your first program:
  - Blink the onboard LED
  - Print one live sensor reading to the console

**Graphic:** Simple 3-icon horizontal flow: a cardboard box icon → a wrench/screwdriver icon → a blinking LED + terminal window icon, with arrows between them, representing "unbox → assemble → code." Keeps it light and encouraging rather than technical.

**Speaker notes:** (15:00–17:00) Now it's your turn. In the lab today you'll unbox your XRP kit and put it together — don't worry, no soldering, it's mostly snap-together plus a few screws, and we'll walk you through it. Then you'll set up the MicroPython web editor in your browser and get your laptop talking to the robot over WiFi — that's the communication subsystem in action already. Finally, you'll write your very first program: just a few lines that blink the onboard LED and print one live reading from a sensor, like the distance sensor, to the console. That's a real sense-plan-act moment — even blinking a light is your code making a decision and acting on it.

---

# Quick Recap Before We Start

- Every robot runs a **Sense → Plan → Act** loop, repeating constantly
- Robots are built from 5 subsystems: **perception, computation, actuation, communication, power**
- The XRP has all five — you can point to each one
- Today's goal: assemble your XRP and get code running on it

**Graphic:** Small combined recap graphic: the sense-plan-act triangle from slide 2 (small, static, no animation needed here) sitting next to a mini version of the labeled XRP image, connected by an equals-style arrow, visually saying "this loop = this robot."

**Speaker notes:** (17:00–18:30) Quick recap before you head to your stations: every robot, no exceptions, runs sense-plan-act on repeat. Every robot is built from the same five subsystems, and you now know exactly where to find each one on your XRP. Your job for the rest of today is hands-on — get the robot assembled, get the editor talking to it, and get your first tiny program running. If anything's unclear as you go, flag down an instructor — that's what we're here for. Let's build some robots.
