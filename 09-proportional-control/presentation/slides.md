---
theme: default
highlighter: shiki
css: unocss
colorSchema: dark
title: 'Proportional Control'
info: |
  Week 3, Session 9 — Steering smarter, not harder
transition: fade-out
lineNumbers: false
drawings:
  persist: false
mdc: true
vite:
  server:
    fs:
      strict: false
glowSeed: 909
layout: center
class: text-center
---

<div class="deck-kicker">Week 3 · Session 9</div>

# Proportional Control

## Steering smarter, not harder

<div v-click class="takeaway max-w-3xl mx-auto mt-10">Small error → small correction. Large error → large correction.</div>

<!--
Connect to the bang-bang line follower. It stayed near the line, but hard left and hard right corrections produced a visible zig-zag. Today students keep feedback and make the response scale with error.
-->

---
layout: two-cols
layoutClass: gap-8
glowSeed: 926
---

# Bang-bang vs. proportional

<div class="space-y-4 mt-5">
  <div v-click class="course-card red"><div class="card-label">Bang-bang</div>Every nonzero error gets the same hard turn.</div>
  <div v-click class="course-card teal"><div class="card-label">Proportional</div>Turn strength changes continuously with error.</div>
  <div v-click class="course-card blue"><div class="card-label">Result</div>Corrections shrink as the robot approaches the line.</div>
</div>

::right::

<div class="diagram-frame mt-3">
  <ConceptDiagram mode="proportional" />
</div>

<!--
Use the animated dots to compare paths. Bang-bang crosses the line at sharp angles and immediately reverses. Proportional control follows a smoother curve and settles toward the center.
-->

---
glowSeed: 942
---

# The one equation

<div class="equation-card text-center max-w-3xl mx-auto mt-7">

$$
u = K_p e
$$

<div class="text-sm opacity-75">e = line-position error · Kp = sensitivity · u = turn command</div>
</div>

<div class="card-grid-3 mt-6">
  <div v-click class="course-card blue text-center"><div class="card-label">e = −4</div><div class="text-3xl font-bold">strong left</div></div>
  <div v-click class="course-card teal text-center"><div class="card-label">e = 0</div><div class="text-3xl font-bold">straight</div></div>
  <div v-click class="course-card orange text-center"><div class="card-label">e = +1</div><div class="text-3xl font-bold">gentle right</div></div>
</div>

<!--
Keep the math intuitive. Kp is a dial: multiplying by the error preserves direction and scales magnitude. If error doubles, the correction doubles. At zero error, no turn correction is needed.
-->

---
glowSeed: 958
---

# Mix forward motion with turning

<div class="equation-card text-center max-w-4xl mx-auto mt-6">

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
glowSeed: 974
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
Frame tuning as an experiment. A too-small gain cannot correct quickly enough; a too-large gain recreates aggressive oscillation. Students should change one value at a time and record the result.
-->

---
glowSeed: 990
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
glowSeed: 1006
---

# Today’s lab

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
glowSeed: 1022
---

# Measure error. Scale the response.

<div v-click class="takeaway max-w-3xl mx-auto mt-10">One multiplication turns a twitchy controller into a smoother line follower.</div>

<!--
Close with the proportional principle and transition to the taped loop. Preview that the next session will combine this line-following behavior with obstacle detection.
-->
