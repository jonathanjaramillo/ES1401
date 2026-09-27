---
theme: default
title: Session 5 — Ultrasonic & IMU
info: Intro to Robotics — Week 2, Session 5 of 12
---

# Ultrasonic & IMU
## "How far?" and "Which way?"

- Two new senses for your XRP robot
- Today: distance sensing + heading sensing
- Lab: watch live numbers change as you move the robot

Speaker notes:
Welcome back! Last time we talked about motors and encoders — how the robot moves and how it knows how far its wheels have turned. Today we're adding two more senses: one that tells the robot "how far away is that wall?" and one that tells it "which way am I facing?" By the end of this short lecture you'll go straight into a hands-on lab where you print live numbers to the console while pushing the robot around by hand. Let's go.

---

# Two New Senses

- **Ultrasonic sensor** → "How far is that object?"
- **IMU (gyro)** → "Which direction am I facing?"
- Together: the robot can sense its environment AND its own orientation
- This is the foundation for obstacle avoidance and turning precisely (coming in later sessions)

Description of graphic: Simple two-panel icon graphic — left panel shows a small ultrasonic sensor icon with a dashed arc and a ruler/tape-measure symbol labeled "distance"; right panel shows a compass rose icon with an arrow labeled "heading." A large plus sign between them.

Speaker notes:
Robots need to sense two very different things. First, "what's around me" — is there a wall or a person in front of me, and how far away? That's the ultrasonic sensor's job. Second, "which way am I pointed" — am I facing north, or have I turned 90 degrees? That's the IMU's job. Neither one tells the robot where it IS on a map, just distance-to-object and facing-direction. Keep that distinction in mind, it'll matter later.

---

# Ultrasonic Sensor: The Idea

- Sends out a short burst of sound (too high-pitched for us to hear)
- Sound travels out, hits an object, bounces back like an echo
- Sensor measures how LONG it takes for the echo to return
- Short wait = object is close. Long wait = object is far away
- Same idea as a bat using echolocation, or you shouting in a canyon and timing the echo

Description of animation: Animated SVG — XRP robot icon on the left, a wall/box on the right. A small arc pulses outward from the sensor toward the wall (expanding semicircle), reaches the wall, then an arc animates bouncing back toward the robot. A small stopwatch icon ticks during the round trip. A text readout below updates like "distance: 42 cm" and shrinks as the wall moves closer in a second loop of the animation, with the round-trip arc visibly taking less time.

Speaker notes:
Here's the intuitive version, no math needed: the sensor chirps out a little pulse of sound, way above what your ears can hear. That sound travels through the air, hits whatever's in front of it — a wall, a book, your hand — and bounces back, just like an echo. The sensor has a tiny stopwatch built in. If the echo comes back FAST, the object must be close. If it takes a while, the object is far away. That's it — that's the whole trick. Bats do the same thing to fly around in the dark, and it's the same idea as yelling in a canyon and counting how long until you hear yourself.

---

# Ultrasonic Sensor: In Practice

- XRP has an ultrasonic distance sensor on the front
- Reading updates constantly as the robot moves
- Distance usually reported in centimeters
- Real-world quirks: soft/angled surfaces can absorb or deflect sound → noisy or missing readings

Description of graphic: Static SVG diagram of the XRP robot from a top-down view, with a small cone/beam shape projecting forward from the sensor location, showing the sensor's "field of view" hitting a wall drawn a few grid squares away, with a dashed measurement line and "cm" label.

Speaker notes:
On the XRP, the ultrasonic sensor sits on the front of the robot, so it's really only good at telling you what's directly ahead — it doesn't see sideways or behind. In code, you'll get back a number, typically in centimeters. One thing to expect: the readings aren't perfectly smooth. If you point it at a soft object like a jacket, or a surface at a steep angle, the sound might not bounce straight back, and you'll get weird or missing readings. That's normal — real sensors are noisy, and part of being a robotics engineer is learning to expect that.

---

# IMU / Gyro: The Idea

- IMU = Inertial Measurement Unit — it senses motion and orientation
- Think of it like a combination of a compass and a tilt sensor
- Today we care about ONE number: **heading** — which direction the robot is facing
- Heading is usually in degrees: 0° = straight ahead (starting direction), increasing as you turn

Description of animation: Animated SVG — a compass rose (N/E/S/W ticks) with a robot-top-view icon in the center. As a slider or auto-loop plays, the robot icon rotates smoothly and a heading number readout (e.g., "0°" → "90°" → "180°") updates in sync, with an arrow on the robot always pointing the current heading direction.

Speaker notes:
The IMU is a small chip packed with tiny sensors that can feel motion, tilting, and rotation. It's doing some clever stuff internally, but you don't need to know the details — think of it like a combination compass and tilt sensor. For this course, the one number we care about is called heading: which way is the robot currently facing, measured in degrees. When you turn the robot on, wherever it's pointing usually counts as zero degrees. Turn it a quarter turn, and heading might read ninety. Turn it all the way around, you're back near zero or three-sixty. It updates live as you physically rotate the robot.

---

# Ultrasonic vs. IMU: Quick Comparison

| | Ultrasonic | IMU (heading) |
|---|---|---|
| Answers | "How far is that thing?" | "Which way am I facing?" |
| Uses | Sound + echo timing | Internal motion sensing |
| Output | Distance (cm) | Angle (degrees) |
| Changes when... | robot moves toward/away from objects | robot turns/rotates |

Description of graphic: Simple two-column table rendered directly as a slide table (shown above) — no extra image needed, keep it clean and readable.

Speaker notes:
Quick recap before we go hands-on. Ultrasonic answers "how far," using sound bouncing off things, and gives you a distance in centimeters — it changes when the robot moves closer to or farther from an object. The IMU answers "which way am I facing," using internal motion sensing, and gives you an angle in degrees — it changes when the robot turns. Both numbers update continuously and live, and both are things you're about to see for yourselves.

---

# Today's Lab Preview

- Print live distance readings to the console while moving the robot toward/away from a wall by hand
- Print live heading readings while rotating the robot by hand
- Then combine both: drive it around and watch both numbers update together
- Goal: build intuition — no code logic needed yet, just observe and understand the numbers

Description of graphic: Small static SVG showing a laptop/console window icon with two scrolling lines of text: "distance: 38 cm" and "heading: 112°" with a small up/down arrow next to each suggesting the values are live-updating.

Speaker notes:
Here's what you're about to do in the lab. You'll write a very short loop that prints the distance reading and the heading reading to the console, over and over. Then — this is the fun part — you're not driving with code yet, you're just picking the robot up, or sliding it across the table by hand, and watching the numbers change in real time as you move it toward a wall, pull it away, and spin it around. This is purely about building intuition for what these sensors are telling you before we start writing logic that reacts to them in future sessions. Any questions before we head to the lab? Let's go try it.
