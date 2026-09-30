---
theme: default
highlighter: shiki
css: unocss
colorSchema: dark
title: 'Open vs. Closed Loop Control'
info: |
  Week 2, Session 6 — Feedback, error, and bang-bang control
transition: fade-out
lineNumbers: false
drawings:
  persist: false
mdc: true
vite:
  server:
    fs:
      strict: false
glowSeed: 808
layout: center
class: text-center
---

# Open vs. Closed Loop Control

## Why checking your work matters

<div v-click class="takeaway max-w-3xl mx-auto mt-10">Today, sensing and motion finally become one repeating behavior.</div>

<!--
Connect the course so far: students have commanded motors open-loop and measured sensors. Today they combine those ideas into feedback, define error, build the simplest closed-loop line follower, then test that feedback behavior on a taped line.
-->

---
glowSeed: 825
---

# Open loop: execute a script

<div class="card-grid-3 mt-7">
  <div v-click class="course-card teal"><div class="card-label">1</div>Drive for 2 seconds.</div>
  <div v-click class="course-card blue"><div class="card-label">2</div>Turn for 0.5 seconds.</div>
  <div v-click class="course-card orange"><div class="card-label">3</div>Drive for 1 second.</div>
</div>

<div v-click class="takeaway mt-8"><strong>No sensor checks during execution.</strong> Wheel slip and drift remain uncorrected.</div>

<!--
Recall the timed commands from Session 2 and the square from Session 3. The command sequence only flows forward. If the robot drifts off a taped line, the program does not know and continues the same plan.
-->

---
layout: two-cols
layoutClass: gap-8
glowSeed: 841
---

# Closed loop: sense, compare, react

<div class="space-y-4 mt-5">
  <div v-click class="course-card teal"><div class="card-label">Sense</div>Read a sensor.</div>
  <div v-click class="course-card blue"><div class="card-label">Compare</div>Find the difference from the goal.</div>
  <div v-click class="course-card orange"><div class="card-label">Act</div>Move to reduce that difference.</div>
</div>

::right::

<div class="diagram-frame mt-3">
  <ConceptDiagram mode="feedback" />
</div>

<div v-click class="takeaway">Repeat continuously.</div>

<!--
Use a thermostat analogy: it checks temperature, compares to the setpoint, and reacts. The XRP does the same with line position. The loop’s repetition creates the ability to correct.
-->

---
glowSeed: 857
---

# Side by side

<div class="card-grid-2 mt-7">
  <div v-click class="course-card red">
    <div class="card-label">Open loop</div>
    <div class="text-2xl font-bold">Plan → act</div>
    <ul class="mt-3">
      <li>Simple</li>
      <li>Blind to disturbances</li>
      <li>Error accumulates</li>
    </ul>
  </div>
  <div v-click class="course-card teal">
    <div class="card-label">Closed loop</div>
    <div class="text-2xl font-bold">Sense → compare → act</div>
    <ul class="mt-3">
      <li>More logic</li>
      <li>Responds to disturbances</li>
      <li>Corrects repeatedly</li>
    </ul>
  </div>
</div>

<div v-click class="takeaway">Trade-off: added complexity buys reliability.</div>

<!--
Compare two robots on the same curved line. The open-loop robot continues its script after drifting. The closed-loop robot may wobble, but it keeps measuring and steering back.
-->

---
glowSeed: 873
---

# Error: goal minus measurement

<div class="equation-card text-center max-w-3xl mx-auto mt-7">

$$
e = r - y
$$

<div class="text-sm opacity-75">r is the desired state; y is the measured state.</div>
</div>

<div class="card-grid-3 mt-6">
  <div v-click class="course-card blue text-center"><div class="card-label">Negative error</div>too far, drive forward</div>
  <div v-click class="course-card teal text-center"><div class="card-label">Zero error</div>at target</div>
  <div v-click class="course-card orange text-center"><div class="card-label">Positive error</div>too close, back up</div>
</div>

<div v-click class="takeaway">A controller’s job is to drive e toward zero.</div>

<!--
Define the symbols briefly using the wall-parking example: the desired state is a target distance from the wall. Sign tells which direction to correct; magnitude may tell how far. The next slide asks: once we know e, how hard should the robot react?
-->

---
glowSeed: 885
---

# Two ways to approach a wall

<div class="takeaway max-w-3xl mx-auto mt-8">Goal: stop 15 cm from the wall.</div>

<div class="card-grid-2 mt-7">
  <div v-click class="course-card red"><div class="card-label">Open loop</div>Drive for a fixed time, regardless of the wall position.</div>
  <div v-click class="course-card teal"><div class="card-label">Bang-bang feedback</div>Check distance repeatedly: drive while far away, then stop at the target.</div>
</div>

<!--
Connect to the previous lab: a fixed-time drive ignores sensor measurements, while a bang-bang wall approach repeatedly checks distance and stops at the target. The same feedback idea will now steer the line follower.
-->

---
glowSeed: 901
---

# Bang-bang: the simplest reaction

<div class="card-grid-2 mt-7">
  <div v-click class="course-card blue"><div class="card-label">Far from the wall</div><div class="text-2xl font-bold">drive forward, full speed</div></div>
  <div v-click class="course-card teal"><div class="card-label">At the target distance</div><div class="text-2xl font-bold">stop, suddenly</div></div>
</div>

<div v-click class="takeaway mt-8">No middle ground → simple code, but a hard, sudden halt right at the target.</div>

<!--
Explain the name: the output switches between fixed extremes with no gentle middle value — full speed or nothing, exactly like the wall-parking robot from the previous slide. Next we apply this same two-state logic to the line follower, where the two extremes are hard-left and hard-right turns instead of drive and stop.
-->

---
glowSeed: 917
---

# From idea to code

<div class="text-sm opacity-70 -mt-2">The wall only had two states, far or there. A line adds a third: centered.</div>

<div class="grid grid-cols-[1.2fr_0.8fr] gap-6 mt-5">
  <div v-click class="course-card">

```python {1|2|3-4|5-6|7-8|all}
while True:
    state = read_line_state()
    if state == "LEFT":
        turn_right_hard()
    elif state == "RIGHT":
        turn_left_hard()
    else:
        drive_straight()
```

  </div>
  <div class="space-y-4">
    <div v-click class="course-card teal"><div class="card-label">Read</div>Every loop.</div>
    <div v-click class="course-card blue"><div class="card-label">Choose</div>One of three states.</div>
    <div v-click class="course-card orange"><div class="card-label">Act</div>Then immediately read again.</div>
  </div>
</div>

<!--
Trace one loop iteration, then emphasize that while True makes it closed-loop. Exact sensor calls depend on the XRP starter code, but the structure is sense, branch, act, repeat.
-->

---
glowSeed: 933
---

# Lab: bang-bang line following

<div class="card-grid-3 mt-8">
  <div v-click class="course-card teal"><div class="card-label">Calibrate</div>Measure tape and floor; choose a threshold.</div>
  <div v-click class="course-card blue"><div class="card-label">React</div>Command hard corrections from sensor state.</div>
  <div v-click class="course-card violet"><div class="card-label">Complete</div>Follow one taped loop without losing the line.</div>
</div>

<div v-click class="takeaway mt-8">Expect zig-zag. Today, staying on the line matters more than smoothness.</div>

<!--
Set expectations for the lab. Students should tune direction logic first, then effort and speed. A rough oscillating lap is successful because it proves the feedback loop is working. A rough oscillating lap demonstrates feedback in action.
-->

---
layout: center
class: text-center
glowSeed: 949
---

# Sense. Compare. React. Repeat.

<div v-click class="takeaway max-w-3xl mx-auto mt-10">A feedback loop lets the robot notice drift and correct its path.</div>

<!--
Close by connecting the lab to the sense-plan-act model from Session 1. Students first calibrate the line sensor, then repeatedly read, decide, and steer. A full lap demonstrates that the robot can respond to changing measurements.
-->
