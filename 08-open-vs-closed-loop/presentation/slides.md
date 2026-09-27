---
theme: default
highlighter: shiki
css: unocss
colorSchema: dark
title: 'Open Loop to Proportional Control'
info: |
  Week 3, Sessions 8–9 — Feedback, error, bang-bang, and proportional control
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

<div class="deck-kicker">Week 3 · Sessions 8–9</div>

# Open Loop to Proportional Control

## Why checking your work matters — and how to react smarter

<div v-click class="takeaway max-w-3xl mx-auto mt-10">Today, sensing and motion finally become one repeating behavior.</div>

<!--
Connect the course so far: students have commanded motors open-loop and measured sensors. Today they combine those ideas into feedback, define error, build the simplest closed-loop line follower, then upgrade its reaction from a hard switch to a proportional response.
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
Recall the Session 3 square. The command sequence only flows forward. If the robot drifts off a taped line, the program does not know and continues the same plan.
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
  <div v-click class="course-card blue text-center"><div class="card-label">Negative error</div>too close, back up</div>
  <div v-click class="course-card teal text-center"><div class="card-label">Zero error</div>at target</div>
  <div v-click class="course-card orange text-center"><div class="card-label">Positive error</div>too far, drive forward</div>
</div>

<div v-click class="takeaway">A controller’s job is to drive e toward zero.</div>

<!--
Define the symbols briefly using the wall-parking example: the desired state is a target distance from the wall. Sign tells which direction to correct; magnitude may tell how far. The next slide asks: once we know e, how hard should the robot react?
-->

---
glowSeed: 885
---

# Two ways to react: parking by a wall

<div class="diagram-frame mt-2">
  <ConceptDiagram mode="wall" />
</div>

<div class="card-grid-2 mt-3">
  <div v-click class="course-card red"><div class="card-label">Bang-bang</div>Drive toward the wall at one constant speed, then stop suddenly the instant error hits zero.</div>
  <div v-click class="course-card teal"><div class="card-label">Proportional</div>Slow down continuously as the wall gets closer — speed shrinks with the error.</div>
</div>

<!--
Ground both reactions in a single-axis example before returning to line following: use the ultrasonic sensor to hold a target distance from a wall. Bang-bang only knows "far" vs "there" — it floors it and slams to a stop. Proportional treats distance error as a dial: big error, big speed; small error, small speed; zero error, zero speed. Same idea drives the rest of today's line follower, just applied to steering instead of forward speed.
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
  <div v-click class="course-card teal"><div class="card-label">Calibrate</div>Use last session’s line threshold.</div>
  <div v-click class="course-card blue"><div class="card-label">React</div>Command hard corrections from sensor state.</div>
  <div v-click class="course-card violet"><div class="card-label">Complete</div>Follow one taped loop without losing the line.</div>
</div>

<div v-click class="takeaway mt-8">Expect zig-zag. Today, staying on the line matters more than smoothness.</div>

<!--
Set expectations for the lab. Students should tune direction logic first, then effort and speed. A rough oscillating lap is successful because it proves the feedback loop is working. Once it works, we upgrade the reaction itself — same loop, smarter Act step.
-->

---
glowSeed: 949
---

# Proportional control: steering smarter, not harder

<div class="takeaway max-w-3xl mx-auto">Small error → small correction. Large error → large correction — just like slowing down as you near the wall.</div>

<div class="card-grid-3 mt-7">
  <div v-click class="course-card red"><div class="card-label">Bang-bang</div>Every nonzero error gets the same hard turn.</div>
  <div v-click class="course-card teal"><div class="card-label">Proportional</div>Turn strength changes continuously with error.</div>
  <div v-click class="course-card blue"><div class="card-label">Result</div>Corrections shrink as the error shrinks — same easing seen at the wall.</div>
</div>

<!--
Bring back the wall-parking picture: bang-bang crossed the line at sharp angles and immediately reversed, same as slamming to a stop at the wall. Proportional control follows a smoother curve and settles toward the center, same as easing up on speed near the wall.
-->

---
glowSeed: 965
---

# The one equation

<div class="equation-card text-center max-w-3xl mx-auto mt-7">

$$
u = K_p e
$$

<div class="text-sm opacity-75">e = error · Kp = sensitivity · u = correction command</div>
</div>

<div class="card-grid-3 mt-6">
  <div v-click class="course-card blue text-center"><div class="card-label">e = +4 ft</div><div class="text-3xl font-bold">drive, fast</div></div>
  <div v-click class="course-card teal text-center"><div class="card-label">e = 0 ft</div><div class="text-3xl font-bold">stop</div></div>
  <div v-click class="course-card orange text-center"><div class="card-label">e = −1 ft</div><div class="text-3xl font-bold">ease back</div></div>
</div>

<div class="text-sm opacity-70 mt-4 text-center">Next: apply this same u to steering instead of forward speed.</div>

<!--
Keep the math intuitive and grounded in the wall example: e is how far off target we are (still too far, at target, or overshot). Kp is a dial: multiplying by the error preserves direction and scales magnitude. If error doubles, the correction doubles. At zero error, no correction is needed — the same rule that brought the wall-parking robot smoothly to a stop. Next slide reapplies u as a turn command for the line follower.
-->

---
glowSeed: 981
---

# Mix forward motion with turning

<div class="text-sm opacity-70 -mt-2">Back to the line follower: u now steers instead of setting forward speed.</div>

<div class="equation-card text-center max-w-4xl mx-auto mt-4">

$$
\begin{aligned}
v_L &= v_{\text{base}} - u \\
v_R &= v_{\text{base}} + u
\end{aligned}
$$

</div>

<div class="card-grid-2 mt-6">
  <div v-click class="course-card teal"><div class="card-label">Base speed</div>Moves both wheels forward.</div>
  <div v-click class="course-card blue"><div class="card-label">Turn correction</div>Subtract from one side and add to the other.</div>
</div>

<div v-click class="takeaway">The same turn command slows one wheel while speeding the other.</div>

<!--
Relate the motor mix to differential drive. The sign convention may need to flip depending on how error is defined. Students should test a positive error and confirm that the robot turns toward the line.
-->

---
glowSeed: 997
---

# Tune the sensitivity dial

<div class="card-grid-3 mt-7">
  <div v-click class="course-card blue">
    <div class="card-label">Kp too small</div>
    <div class="text-3xl font-bold">sluggish</div>
    <div class="mt-3">Robot drifts before it reacts enough.</div>
  </div>
  <div v-click class="course-card teal">
    <div class="card-label">Kp useful</div>
    <div class="text-3xl font-bold">smooth</div>
    <div class="mt-3">Robot curves confidently toward center.</div>
  </div>
  <div v-click class="course-card red">
    <div class="card-label">Kp too large</div>
    <div class="text-3xl font-bold">jittery</div>
    <div class="mt-3">Robot overshoots and oscillates.</div>
  </div>
</div>

<div v-click class="takeaway mt-7">Change Kp gradually and keep base speed fixed while tuning.</div>

<!--
Frame tuning as an experiment. A too-small gain cannot correct quickly enough; a too-large gain recreates aggressive oscillation — the wall-parking robot overshooting and bouncing off. Students should change one value at a time and record the result.
-->

---
glowSeed: 1013
---

# From equation to code

<div class="grid grid-cols-[1.25fr_0.75fr] gap-6 mt-5">
  <div v-click class="course-card">

```python {1-2|4|5|6-7|all}
BASE = 0.35
KP = 0.6

error = target - line_value
turn = KP * error
left = BASE - turn
right = BASE + turn
drive.set_effort(left, right)
```

  </div>
  <div class="space-y-4">
    <div v-click class="course-card teal"><div class="card-label">Measure</div>Find error.</div>
    <div v-click class="course-card blue"><div class="card-label">Scale</div>Compute turn.</div>
    <div v-click class="course-card orange"><div class="card-label">Mix</div>Command motors.</div>
  </div>
</div>

<div class="mt-3 text-sm opacity-70 text-center">Clamp motor commands to the library’s allowed range.</div>

<!--
Trace the calculation in order. The target is the calibrated line-center value. If commands exceed the valid range, students should clamp them. Verify steering direction at low speed before running the full loop.
-->

---
glowSeed: 1029
---

# Today’s lab: upgrade to proportional

<div class="card-grid-3 mt-8">
  <div v-click class="course-card teal"><div class="card-label">Upgrade</div>Replace fixed hard turns with a proportional turn.</div>
  <div v-click class="course-card amber"><div class="card-label">Tune</div>Adjust one Kp value at a time.</div>
  <div v-click class="course-card blue"><div class="card-label">Compare</div>Look for less jitter and fewer line losses.</div>
</div>

<div v-click class="takeaway mt-8">Aim for a complete, smooth loop—not the fastest lap.</div>

<!--
Transition to the lab. Students should begin with modest base speed, tune Kp for stability, then only consider increasing speed. Their evidence is the robot’s path, not whether one run happened to succeed.
-->

---
layout: center
class: text-center
glowSeed: 1045
---

# Sense. Compare. Scale the response.

<div v-click class="takeaway max-w-3xl mx-auto mt-10">Feedback turns a blind script into a robot that can correct itself — and one multiplication turns a twitchy corrector into a smooth one.</div>

<!--
Close with both principles: the loop that lets a robot notice it's wrong, and the proportional response that lets it correct gracefully — whether that's parking by a wall or following a taped line. Preview that the next session combines this line-following behavior with obstacle detection.
-->
