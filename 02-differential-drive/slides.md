---
theme: default
title: Session 2 — Differential Drive
info: |
  Intro to Robotics — Week 1, Session 2
  ~15 minute lecture, XRP robot kit
transition: fade
---

# Differential Drive
### How the XRP Actually Moves

Session 2 · Week 1

<!--
Welcome back! Last time we unboxed the XRP and got the editor running. Today, before we touch code for real, we're going to answer one question: how does a robot with just two wheels turn, drive straight, or spin in place? This is the core idea behind almost every wheeled robot you'll ever build, so it's worth five minutes of your full attention. (~30 sec)
-->

---

# What Is "Differential Drive"?

- The XRP has **two wheels**, each with its **own motor**
- There's no steering wheel — no separate mechanism turns the robot
- Each wheel can spin at its own speed, forward or backward, **independently**
- All motion (straight, curves, spins) comes from *comparing* the two wheel speeds

**Graphic:** Simple top-down flat icon of the XRP chassis (rounded rectangle body) with two wheel rectangles on the left and right sides, front indicated by a small triangle/arrow. Static, labeled diagram: "Left Motor" pointing to left wheel, "Right Motor" pointing to right wheel, "No steering wheel!" callout with an X over a stylized steering wheel icon.

<!--
So what does "differential drive" actually mean? It just means the robot's wheels are driven independently — left wheel, right wheel, two separate motors, no steering linkage like a car. Think about it: a car turns because the front wheels physically pivot. The XRP doesn't have that. Instead, it steers entirely by making one wheel spin faster or slower than the other. That's the whole trick, and it's what we're unpacking today. (~1.5 min)
-->

---

# Same Speed = Straight

- If **left speed = right speed**, and both point the same direction, the robot drives in a **straight line**
- Both wheels cover the same distance in the same time → no turning
- This is the simplest case, and it's your baseline for everything else

**Graphic:** Animated SVG, top-down view of XRP chassis. Two arrows on the wheels, both equal length pointing "up" (forward). Animate the whole chassis sliding straight up the slide in a smooth loop, arrows staying equal-length the whole time.

<!--
The easiest case first: if both wheels spin at exactly the same speed, in the same direction, the robot just goes straight. Imagine you and a friend rowing a canoe — if you both paddle at the same pace, the canoe goes straight ahead. That's literally what's happening here with the two motors. (~1.5 min)
-->

---

# Different Speeds = Turning

- If one wheel spins **faster** than the other, the robot **curves** toward the slower wheel
- Bigger the speed difference → sharper the turn
- Both wheels still moving the *same direction* (both forward, or both backward)

**Graphic:** Animated SVG, same top-down chassis. Left wheel arrow short, right wheel arrow long (both pointing forward/up). Animate the chassis tracing a smooth curved arc to the left as it moves, showing the arc path as a dotted trail behind it. Add a small slider/label showing "Left: slow, Right: fast → curves left."

<!--
Now, what if the wheels don't match? Say the right wheel spins faster than the left. The right side is covering more ground, so the whole robot arcs toward the slower side — toward the left. It's just like rowing again: paddle harder on one side of the canoe, and the canoe curves away from that side. The bigger the mismatch between the two speeds, the tighter the curve. (~2 min)
-->

---

# Opposite Speeds = Spin in Place

- If the wheels spin at the **same speed** but in **opposite directions**, the robot **rotates in place** without moving forward or backward
- This is called a "point turn" or "tank turn"
- Great for making sharp, precise heading changes

**Graphic:** Animated SVG, same chassis. Left wheel arrow points backward (down), right wheel arrow points forward (up), equal lengths. Animate the entire chassis rotating in place around its own center point, looping smoothly, with a small circular rotation arrow icon overlaid at the center.

<!--
Last case, and it's a fun one: if one wheel goes forward and the other goes backward, at the same speed, the robot doesn't go anywhere — it just spins in place around its own center. This is sometimes called a tank turn, because tanks with tracks do exactly this. It's how the XRP can turn 90 or 180 degrees without needing any extra space to swing around in. (~1.5 min)
-->

---

# From Idea to Code: Motor Commands

- In MicroPython on the XRP, you command each motor **separately**
- Typical pattern:
  ```python
  from XRPLib.differential_drive import DifferentialDrive
  drive = DifferentialDrive.get_default_differential_drive()

  drive.set_effort(0.5, 0.5)    # left, right — both forward, straight
  drive.set_effort(0.2, 0.5)    # curve left (right wheel faster)
  drive.set_effort(0.5, -0.5)   # spin in place
  drive.stop()                  # stop both motors
  ```
- `set_effort` values range roughly **-1.0 (full reverse) to 1.0 (full forward)**; 0 = stopped
- This maps *directly* onto the three motion patterns we just saw

**Graphic:** Static side-by-side diagram: on the left, the three chassis diagrams from previous slides (straight / curve / spin) stacked vertically; on the right, their matching one-line `set_effort(left, right)` code snippet next to each, connected by a thin arrow, so students visually map motion → code.

<!--
Here's the payoff: everything we just talked about is one function call. `set_effort` takes two numbers — left wheel effort and right wheel effort — each between -1 and 1, where 1 is full speed forward, -1 is full speed backward, and 0 is stopped. Equal positive numbers: straight. Different numbers: curve. Opposite sign, same size: spin. You don't need to memorize this — you'll have it in your starter code — but I want the mental model to click before you start experimenting in the lab. (~2.5 min)
-->

---

# Quick Recap

- Two independent motors, no steering wheel — that's differential drive
- **Same speed, same direction** → straight
- **Different speeds** → curve toward the slower wheel
- **Same speed, opposite direction** → spin in place
- One command, `set_effort(left, right)`, controls it all

**Graphic:** Small static 3-panel icon strip (straight arrow / curved arrow / rotation icon) as a compact visual summary, no animation needed — just a clean recap row at the top of the slide.

<!--
So to recap before we head to the lab: differential drive just means two independently controlled wheels doing all the work. Match their speed and direction and you go straight. Make them different and you curve. Flip one of them and you spin. And in code, it's all just one function, set_effort, with two numbers. Now it's your turn — head to your XRP, open the starter file, and let's make some wheels spin. Questions before we start? (~1.5 min)
-->
