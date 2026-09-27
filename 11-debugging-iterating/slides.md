---
theme: default
title: Session 11 — Debugging & Iterating
---

# Debugging & Iterating

Why your robot doesn't work yet (and what to do about it)

Session 11 · Week 4 · Intro to Robotics

::speaker::
Welcome back, everyone. Today's lecture is short on purpose — most of your time today is build time. You're combining line-following and obstacle-handling into one program that has to run the whole course, and honestly, it probably won't work perfectly the first time you run it. That's not a sign something's wrong with you or your code — it's just what robotics is. This 15 minutes is about giving you a simple, repeatable way to find and fix problems instead of just poking at your code randomly and hoping. Let's go.

---

# Why Robots Rarely Work the First Time

- **Sensor noise** — the ultrasonic sensor and reflectance sensor don't give the exact same reading twice, even in the same spot
- **Mechanical variation** — your two motors are never perfectly identical; wheels, battery charge, and friction differ robot to robot
- **Edge cases you didn't think of** — what happens at a corner, a gap in the line, or two obstacles close together?
- This is true for professional robots too — it's not just a "beginner" problem

Description: Simple SVG graphic — three labeled icon "cards" in a row: a wavy noisy-signal icon labeled "Sensor Noise," a slightly mismatched pair of wheel icons labeled "Mechanical Variation," and a fork-in-road icon labeled "Unexpected Edge Cases." A small caption underneath reads "Every robot deals with all three."

::speaker::
So let's start with why this happens, because understanding *why* your robot is being weird makes it way less frustrating to debug. First, sensor noise — your distance sensor might read 15 centimeters, then 14, then 16, all while sitting perfectly still. Your code has to expect that, not assume one perfect number. Second, mechanical variation — even robots built from identical kits drift differently, because no two motors spin at exactly the same speed and no two wheels have exactly the same grip. That's why code that works on your teammate's robot might not work identically on yours. Third — and this is the big one — edge cases. You write code thinking about the normal case, but the course has corners, gaps, maybe two obstacles near each other. Your code needs to handle situations you didn't originally picture. None of this means you did something wrong. It means debugging is just part of the job.

---

# A Systematic Approach: The Debug Loop

- **Isolate** — test ONE behavior at a time, not the whole course
- **Print & Observe** — print sensor values to check what the robot actually "sees," don't just guess
- **Change ONE thing** — adjust a single variable, threshold, or line of logic
- **Retest** — run it again immediately and compare to before
- Repeat the loop — debugging is a cycle, not a one-shot fix

Description: Circular arrow flowchart SVG with four nodes arranged clockwise: "Isolate" (magnifying glass icon) → "Print & Observe" (terminal/text icon) → "Change ONE Thing" (single gear/knob icon) → "Retest" (play button icon) → curving arrow back to "Isolate," forming a continuous loop.

::speaker::
Here's the core idea for today, and honestly for the rest of your time building robots: the debug loop. Four steps. Step one — isolate. Don't try to fix "the whole course isn't working." Pick one behavior — just the turn at obstacle two, say — and test that alone. Step two — print and observe. Add a print statement for your sensor value or your motor speed and actually look at the numbers instead of guessing what the robot is "thinking." Step three — change one thing. Not five things at once. One threshold, one number, one line. Step four — retest immediately, and see if that one change helped, hurt, or did nothing. Then you go around the loop again. This feels slow, but it's actually the fastest way to fix things, because when you change one thing at a time, you always know what caused the improvement — or the new problem.

---

# Print Statements Are Your Best Friend

- Before assuming the code is "wrong," check: is the sensor giving the value you think it is?
- Add `print()` for distance, reflectance, or gyro readings and watch them scroll as the robot moves
- Compare what you *expected* to see vs. what actually printed — the gap is usually where your bug lives
- Remove or comment out prints once that part is confirmed working

Description: Small mock terminal/console window SVG showing a few lines of scrolling text output, e.g. "distance: 42cm", "distance: 15cm", "line: LEFT", "distance: 14cm" — styled like a real REPL output stream to make it feel concrete.

::speaker::
A huge number of "my code is broken" problems are actually "my assumption about a sensor value was wrong" problems. So before you dive into rewriting logic, just print the number. If your obstacle code should trigger under 15 centimeters, print the distance reading as the robot approaches and watch what it actually says. You'll often find it's bouncing around, or it never quite gets below your threshold, or it's reading correctly but your if-statement has a typo. Printing turns "the robot is being weird" into "oh, the number is 18 when I expected 12" — which is something you can actually act on. Once a piece is confirmed working, you can quiet down those prints so your output isn't overwhelming.

---

# Test Small Before Testing Big

- Don't debug a turn by running the entire course — build a mini version of just that section
- Example: tape down a short straight line plus one obstacle, instead of the full course
- Simplified tests are faster to run and easier to reason about
- Once the small piece works reliably, add it back into the full course

Description: Side-by-side comparison SVG — left panel shows a long, complex full course layout (multiple curves, two obstacles, line gaps) labeled "Full Course (slow to test)"; right panel shows a short simplified test strip with just one line segment and one obstacle labeled "Mini Test (fast to test)." An arrow points from right to left labeled "add back in once it works."

::speaker::
One mistake people make under time pressure is testing every change by running the *entire* course, start to finish. That takes forever, and if something goes wrong, you don't know which of the five behaviors along the way caused it. Instead, build a stripped-down version of just the tricky part — a short strip of line plus one obstacle, taped to your table or the floor. Test your fix against that small setup first. It's faster, it's clearer, and once that piece works reliably, you plug it back into the full course. Think of it like rehearsing one scene before running the whole play.

---

# Change One Thing At a Time

- It's tempting to change several things when you're frustrated — resist that
- If you change multiple things and it works, you won't know *why*
- If you change multiple things and it breaks worse, you won't know *what* broke it
- Small, single changes are slower per-step but faster overall

Description: Simple two-path SVG comparison — top path shows a single gear turning with a clean checkmark result labeled "1 change → clear result"; bottom path shows five gears turning at once with a tangled question-mark result labeled "5 changes → no idea what worked."

::speaker::
This one is hard to follow when you're frustrated, but it matters the most. When something isn't working, the instinct is to change the threshold, and the speed, and the turn angle, all at once, and rerun. If it works — great, but now you don't know which change actually fixed it, so you can't repeat that success on the next problem. If it works worse, you're now debugging three new changes instead of one. Slow down. Change one number. Rerun. See what happened. It feels slower in the moment, but it saves you time overall because you're never confused about what caused what.

---

# Debugging Is Normal — Keep Going

- Every team here will hit bugs today — that includes strong teams, that's expected
- A robot that "mostly" works and gets refined is further along than it looks
- Use the debug loop, isolate the problem, and chip away at it piece by piece
- Ask for help early if you're stuck — that's what today's lab time is for

Description: Simple two-panel "before/after" animated SVG — left panel shows a small robot icon approaching a turn and drifting off the line with a red X; right panel shows the same robot, after one small code tweak (a highlighted single changed line of pseudocode), taking the turn cleanly with a green checkmark. Caption underneath: "Same robot. One small fix."

::speaker::
Last thing before you get to building — I want to be really direct about this: everyone in this room is going to hit frustrating bugs today, and that is completely normal, not a sign you're behind. The teams that do well aren't the ones who never hit problems, they're the ones who use a method like the debug loop to work through problems calmly instead of getting stuck in "just try random stuff" mode. A robot that mostly works and just needs a couple more fixes is in great shape. If you're stuck for more than about ten or fifteen minutes on the same issue, flag me down — that's exactly what I'm here for during lab time. Alright, let's go build.
