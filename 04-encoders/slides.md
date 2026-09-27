---
theme: default
title: Session 4 — Encoders
info: Intro to Robotics — Week 2, Session 4 of 12
---

# Encoders
### Counting Wheel Turns to Measure Distance

Week 2 · Session 4 of 12

<!--
Welcome back! Last time our robot drove "blind" — we just guessed how long to run the motors to cover a distance. Today we fix that. We're adding a sense of "how far have I actually gone." By the end of this 15 minutes, you'll understand what an encoder is, how it counts wheel rotations, and how we turn that count into inches or feet. Then you'll go read live encoder numbers off your own XRP and use them to drive an exact distance.
-->

---

# Last Session's Problem: Driving by Time

- We drove the XRP by saying "run motors for 2 seconds"
- Time-based driving assumes the robot always moves at the same speed
- But battery voltage drops, floors have different friction, wheels aren't perfectly identical
- Result: the "same" 2 seconds gives a DIFFERENT distance each run

**Graphic:** Simple two-panel comparison illustration. Left panel: XRP on carpet, arrow showing it traveled 18 inches in 2 seconds. Right panel: same XRP on smooth tile, arrow showing it traveled 26 inches in the same 2 seconds. Caption underneath: "Same code, same 2 seconds, different distance."

<!--
Quick recap: last week you wrote code like motor.set_speed then time.sleep(2). It worked, sort of — but if you ran that exact same program twice, did you get the exact same distance both times? Probably not. Ask the class to shout out why. Friction, battery charge, carpet vs tile, one motor slightly weaker than the other. Time is a proxy for distance, but it's a bad one because speed isn't perfectly constant. We need something that measures distance directly, not something that assumes speed and multiplies by time.
-->

---

# What Is an Encoder?

- A small sensor attached to each motor's shaft
- Has a wheel with alternating light/dark stripes (or slots) — called a "tick" pattern
- As the wheel spins, the sensor counts each stripe/slot that passes by: one **tick**
- The XRP has one encoder per wheel, so it tracks each side independently

**Graphic:** Animated SVG — a circular disc with ~16 alternating black/white tick marks around its rim, spinning slowly. A small stationary sensor icon (like an eye or LED+detector pair) sits beside the rim. Each time a black-to-white edge passes the sensor, a "tick!" flashes and a counter below increments (0, 1, 2, 3...). Loop the animation for a couple of rotations.

<!--
So what's actually inside there? Attached to the axle of each motor is a little disc with stripes on it — kind of like a barcode wheel. Right next to it sits a tiny sensor that can tell when a stripe passes by. Every time a stripe passes, that's one 'tick,' and the encoder chip keeps a running count of ticks. The XRP has one of these on the left wheel and one on the right wheel, so it can tell if one side is spinning faster than the other, which matters for driving straight — something we'll use in a future session too.
-->

---

# From Ticks to Rotations

- The XRP's encoder produces a fixed number of ticks per one full wheel rotation
- For the XRP, that's roughly **1440 ticks = 1 full wheel turn** (exact spec in your reference sheet)
- So: `rotations = ticks / 1440`
- This ratio is fixed and known — it's a spec of the hardware, not something that drifts

**Graphic:** Simple diagram — a wheel drawn with a dotted line showing one full 360° revolution, with a curved arrow around it labeled "1440 ticks." Below it, a small equation card: "ticks ÷ 1440 = number of rotations."

<!--
Here's the key number: for every single full spin of the wheel, the encoder counts a fixed number of ticks — for the XRP that's about 1440. That number comes from how many stripes are on the disc and some internal gearing, and it doesn't change run to run. So if you read 1440 ticks, you know the wheel spun around exactly once. If you read 2880, that's two full rotations. It's just division: ticks divided by ticks-per-rotation gives you rotations. No calculus, just a ratio.
-->

---

# From Rotations to Distance

- Every full rotation, the wheel rolls forward one **circumference**'s worth of distance
- Circumference = π × wheel diameter (XRP wheels are about 2.4 inches across → ~7.5 inches around)
- So: `distance = rotations × wheel_circumference`
- Putting it together: `distance = (ticks / 1440) × 7.5 inches`

**Graphic:** Illustration of a wheel rolling along a straight line on the ground, unrolling like a tape measure — showing that one full rotation = one circumference length laid flat on the ground, labeled "7.5 in." A running tally below shows ticks incrementing alongside a distance number in inches climbing in sync.

<!--
Now the last step: every time the wheel makes one full turn, how far did the robot actually move forward? Exactly one circumference — the distance around the wheel. Think of unrolling the tire one time around, like a tape measure laid on the ground. For the XRP's wheels, that circumference is about 7.5 inches. So now we can chain it together: take your tick count, divide by 1440 to get rotations, multiply by 7.5 inches to get distance traveled. That's the whole formula, and it's just arithmetic — no calculus required.
-->

---

# Why Encoders Beat Timing

| | Timing-based | Encoder-based |
|---|---|---|
| Measures | assumed speed × time | actual wheel rotation |
| Affected by battery/friction? | Yes — drifts | No — ticks are exact |
| Repeatable? | Not reliably | Yes, run after run |
| Knows if wheels slip? | No | Can detect (ticks stop increasing) |

**Graphic:** Simple bar chart comparison: five repeated "drive for 2 seconds" trials showing bar heights (distance traveled) varying noticeably (16, 22, 19, 25, 18 inches), versus five "drive until 2880 ticks" trials showing nearly identical bar heights (~24 inches each). Title: "Timing drifts. Encoders don't."

<!--
So why go through all this trouble? Because encoders measure what actually happened, not what we hoped would happen. If the battery is a little low and the motor spins slower, timing-based code still stops at 2 seconds — but it went a shorter distance. Encoder-based code doesn't care about speed at all; it just keeps counting ticks until it hits the target, so it naturally compensates. It's also more honest: if a wheel gets stuck on carpet and slips, encoder ticks will tell you something's wrong, because a wheel that isn't turning isn't producing ticks.
-->

---

# Open Loop vs. Closed Loop

- **Open loop:** send a command, hope for the best. "Run at effort 0.5 for 1.5 seconds." No sensor is watching.
- **Closed loop:** a sensor measures what actually happened and the robot corrects. "Hold 20 cm/s" — the encoder checks every few milliseconds and adjusts.
- `set_effort()` is open loop. `set_speed()` and `straight()` are closed loop — the encoders close the loop.

**Graphic:** Two control-loop diagrams side by side. Left ("open loop"): "Command" → "Motors" → "Wheels" → arrow trailing off into a question mark. Right ("closed loop"): same chain, but an "Encoder" sensor taps the wheel output and feeds back to a "Compare to target" box that loops into "Command." Feedback arrow labeled "actual speed / distance."

<!--
One more idea before the lab, and it's the big one for the whole course. Open loop means you give a command and just trust it worked — like closing your eyes, taking five steps, and hoping you're at the door. Closed loop means something measures the result and fixes the difference — eyes open, adjusting as you walk. set_effort is open loop: nothing checks whether the wheels actually turned the way you wanted. set_speed and straight are closed loop: the encoders constantly measure and the robot corrects itself. Today you'll feel the difference in centimeters of error on the floor.
-->

---

# Today's Lab: Drive a Square, Three Ways

- Same task each time: drive a 2–3 ft square and return to the start
- **Part 1** — `set_effort()` + a timer + `turn(90)`: open loop
- **Part 2** — `set_speed()` (cm/s, encoder-controlled) + `turn(90)`
- **Part 3** — `straight()` (cm, encoder-controlled) + `turn(90)`
- Tape the start, run each version, measure x and y error with a tape measure

**Graphic:** Three small square paths in a row. Path 1: wobbly, doesn't close — big red gap between start and end, labeled "effort + timer." Path 2: closer, small gap, labeled "speed." Path 3: nearly closed, tiny gap, labeled "distance." Caption: "Same turns every time. Only the straights change."

<!--
Here's the plan. You'll drive a square three times. Part one uses raw effort and a stopwatch — expect the square not to close. Part two commands a wheel speed in centimeters per second, which the encoders regulate. Part three uses straight(), where the encoders count out the exact distance. The turns are the same call, turn(90), in all three — so as the error shrinks from part one to part three, you know the straights are what improved. Spend only a few minutes per part, and no more than five minutes tuning effort or speed. Record your x and y error each time. If you finish early, do it again with a bigger box and see whether the error grows. Let's go.
-->
