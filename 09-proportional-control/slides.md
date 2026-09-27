---
theme: default
title: Session 9 — Proportional Control
---

# Proportional Control
### Steering smarter, not harder

Session 9 · Week 3 · Intro to Robotics

Speaker notes:
Welcome back! Last time you got bang-bang control working on the XRP — the line follower that swerves hard left or hard right the instant it sees the line. It works, but it's twitchy and jerky. Today we're going to smooth that out with one simple idea. This whole lecture is about fifteen minutes, so let's dive right in.

---

# Quick Recap: Bang-Bang Control

- Sensor reads "on line" or "off line" — only two states
- Robot response: full turn left OR full turn right, nothing in between
- Works, but causes constant zig-zagging ("jitter")
- Feels like a car swerving lane to lane instead of driving smoothly

Graphic: Animated SVG showing the robot on a straight line, sensor reading flips between two states, robot path is a sharp jagged zig-zag with abrupt full-angle turn arrows at each correction.

Speaker notes:
Quick reminder of where we left off. Bang-bang control is simple: the sensor basically tells you "yes I'm on the line" or "no I'm not," and the robot reacts with a full, maximum turn every single time. That's easy to code, but think about what it looks like — the robot is always overcorrecting, so it wiggles back and forth constantly. Today's question is: can we do better?

---

# The Big Idea: Steer Proportionally

- What if the robot could tell HOW FAR off the line it is, not just left or right?
- Barely off the line? → steer gently
- Way off the line? → steer hard
- This is called **proportional control** — "proportional" just means the turn scales with the error

Graphic: Animated SVG split-screen — left side repeats last slide's jagged bang-bang zig-zag; right side shows the same robot smoothly curving back onto the line with a turn arrow that visibly shrinks as the robot gets closer to center. Label under each: "Bang-Bang" vs "Proportional."

Speaker notes:
Here's the shift in thinking. Instead of a yes/no sensor reading, imagine your sensor gives you a number — how far off the line you are. If you're just barely drifting, you only need a small nudge. If you've drifted way off, you need a bigger correction. That's the entire idea behind proportional control. No fancy math yet — just "the further off you are, the harder you steer."

---

# From Error to Turn Amount

- "Error" = how far off-line you currently are (can be negative or positive, left or right)
- Turn amount = a constant number × the error
- Bigger error → bigger turn. Smaller error → smaller turn. Zero error → no turn.
- We call that constant "Kp" for now — just think of it as a "sensitivity dial"

Plot: Simple matplotlib line/bar chart, x-axis "Error (distance from line, e.g. -5 to +5)", y-axis "Turn Strength," showing a straight line through the origin — a handful of example error values (-4, -2, 0, 2, 4) plotted as bars or points scaling linearly, labeled "turn = Kp × error."

Speaker notes:
So how do we turn "how far off I am" into an actual motor command? We multiply. Turn amount equals some constant times the error. If the error doubles, the turn doubles. If there's no error at all, there's no turn — the robot just drives straight. That constant is often called "Kp," which you can just think of as a dial that controls how aggressively the robot reacts. We're not deriving formulas today — just get comfortable with this one relationship.

---

# Why This Feels Smoother

- Bang-bang: robot always "fights" the line, constant hard corrections
- Proportional: robot eases back in, corrections shrink as it approaches center
- Result: fewer jitters, less zig-zag, more like gliding back onto the line
- Same sensor, same motors — just a smarter way of using the reading

Graphic: Side-by-side animated SVG comparison (reuse from slide 3 if helpful): sharp sawtooth path vs. smooth S-curve path converging onto a straight line.

Speaker notes:
Why does this actually help? Because with bang-bang control, the robot always overreacts — even a tiny drift gets a maximum turn, so it overshoots and has to correct again. With proportional control, small drifts get small corrections, so the robot naturally settles onto the line instead of overshooting past it. Same hardware, same sensor — we're just being smarter about how we respond to what it tells us.

---

# Tuning the "Sensitivity Dial" (Kp)

- Too small Kp → robot barely reacts, drifts off the line slowly
- Too large Kp → robot overreacts again, back to jittery zig-zag
- "Just right" Kp → smooth, confident curves back to center
- You'll find a good Kp today by trial and error — no formula required

Graphic: Simple SVG or diagram of a dial/slider labeled "Kp" with three robot path sketches underneath at low/medium/high settings — sluggish drift, smooth curve, and jittery overshoot.

Speaker notes:
One practical heads-up before you head to lab: that constant, Kp, matters a lot. If it's too small, the robot barely responds and drifts off slowly. If it's too big, you're basically back to bang-bang, overcorrecting every time. There's a sweet spot in between, and today your job is to find it experimentally — turn the dial, watch what happens, adjust. That's exactly what real robotics engineers do too.

---

# Today's Lab

- Take your bang-bang line follower code from last session
- Measure error: how far off-line is the sensor reading, not just which side
- Compute turn = Kp × error, and apply it to the motors
- Tune Kp until the robot follows the loop smoothly, with minimal jitter

Graphic: none — simple text/checklist slide to transition into the hands-on lab.

Speaker notes:
So that's the whole idea in a nutshell: measure how far off you are, multiply by a constant, and steer by that amount. In lab today you'll take your bang-bang follower from last time and upgrade it to proportional control. You'll compute an error value from the line sensor, scale your turn by a constant you pick, and then tune that constant until the robot glides around the loop smoothly instead of zig-zagging. Head to your XRP kits and let's get it running smoother than ever.
