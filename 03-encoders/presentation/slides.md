---
theme: default
highlighter: shiki
css: unocss
colorSchema: dark
title: 'Encoders'
info: |
  Week 1, Session 3 — Counting wheel turns to measure distance
transition: fade-out
lineNumbers: false
drawings:
  persist: false
mdc: true
vite:
  server:
    fs:
      strict: false
glowSeed: 404
layout: center
class: text-center
---

<div class="deck-kicker">Week 1 · Session 3</div>

# Encoders

## Counting wheel turns to measure distance

<div v-click class="takeaway max-w-3xl mx-auto mt-10">Stop guessing how far the robot went. Measure it.</div>

<!--
Connect to the timed-drive lab. The same number of seconds did not always produce the same distance. Today students add a direct measurement of wheel motion and turn it into physical distance.
-->

---
glowSeed: 421
---

# Time is only a proxy for distance

<div class="card-grid-2 mt-7">
  <div v-click class="course-card amber">
    <div class="card-label">Carpet · 2 seconds</div>
    <div class="text-5xl font-bold">18 in</div>
    <div class="mt-3">Higher friction slows the robot.</div>
  </div>
  <div v-click class="course-card blue">
    <div class="card-label">Tile · 2 seconds</div>
    <div class="text-5xl font-bold">26 in</div>
    <div class="mt-3">Lower friction changes the result.</div>
  </div>
</div>

<div v-click class="takeaway mt-8">Same code + same time does not guarantee the same distance.</div>

<!--
Ask why timed movement changed between trials. Battery state, surface friction, and motor mismatch affect speed. Time assumes speed is constant; an encoder measures rotation directly.
-->

---
layout: two-cols
layoutClass: gap-8
glowSeed: 438
---

# What is an encoder?

<div class="space-y-4 mt-5">
  <div v-click class="course-card teal"><div class="card-label">Pattern</div>A striped or slotted disc turns with the motor shaft.</div>
  <div v-click class="course-card blue"><div class="card-label">Sensor</div>Each passing edge produces one count—a <strong>tick</strong>.</div>
  <div v-click class="course-card orange"><div class="card-label">Two sides</div>The XRP tracks left and right wheels independently.</div>
</div>

::right::

<div class="diagram-frame mt-3">
  <ConceptDiagram mode="encoder" />
</div>

<!--
Describe the encoder as a barcode wheel. The sensor detects alternating regions as the motor turns, creating a repeatable tick count. Separate encoders reveal motion on each side of the robot.
-->

---
glowSeed: 454
---

# Ticks → rotations

<div class="equation-card max-w-3xl mx-auto mt-7 text-center">

$$
\text{rotations} = \frac{\text{ticks}}{\text{ticks per rotation}}
$$

</div>

<div class="card-grid-3 mt-6">
  <div v-click class="course-card teal text-center"><div class="card-label">1440 ticks</div><div class="text-3xl font-bold">1 turn</div></div>
  <div v-click class="course-card blue text-center"><div class="card-label">2880 ticks</div><div class="text-3xl font-bold">2 turns</div></div>
  <div v-click class="course-card violet text-center"><div class="card-label">720 ticks</div><div class="text-3xl font-bold">½ turn</div></div>
</div>

<div class="mt-3 text-sm opacity-70 text-center">Use the exact XRP specification from your lab reference.</div>

<!--
Explain that 1440 is the approximate course reference value; students should use the value specified for their kit and library. The ratio is fixed by hardware, so simple division converts counts into rotations.
-->

---
glowSeed: 470
---

# Rotations → distance

<div v-click class="equation-card text-center max-w-4xl mx-auto mt-5">

$$
\begin{aligned}
C &= \pi d \\
x &= \frac{N}{1440}\,C
\end{aligned}
$$

</div>

<div class="grid grid-cols-2 gap-6 mt-5">
  <div v-click class="course-card teal text-center"><div class="card-label">Wheel circumference</div>For d ≈ 2.4 in, C ≈ 7.5 in.</div>
  <div v-click class="course-card blue text-center"><div class="card-label">Distance traveled</div>N is the measured tick count.</div>
</div>

<div v-click class="takeaway">One wheel rotation lays one circumference onto the floor.</div>

<!--
Use the idea of unrolling the tire like a tape measure. Circumference converts rotations into distance. Combine the two ratios: ticks to rotations, then rotations to inches.
-->

---
glowSeed: 486
---

# Why encoders beat timing

<div class="grid grid-cols-2 gap-6 mt-5">
  <div v-click class="course-card red">
    <div class="card-label">Timing-based</div>
    <ul class="comparison-list">
      <li>Assumes a speed</li>
      <li>Changes with battery and floor</li>
      <li>Cannot verify wheel motion</li>
    </ul>
  </div>
  <div v-click class="course-card teal">
    <div class="card-label">Encoder-based</div>
    <ul class="comparison-list">
      <li>Measures actual wheel rotation</li>
      <li>Stops at a target count</li>
      <li>Repeatable across changing speed</li>
    </ul>
  </div>
</div>

<div v-click class="takeaway mt-6">Encoders measure the wheel—not the robot sliding over the floor.</div>

<!--
Clarify the important limitation: encoder ticks are exact for wheel rotation, but wheel slip can still separate wheel motion from robot motion. Encoders are a major improvement over timing, not perfect knowledge of position.
-->

---
glowSeed: 502
---

# Today’s lab: compare three ways to move

<div class="card-grid-3 mt-7">
  <div v-click class="course-card amber text-center"><div class="text-3xl">1</div><div class="card-label mt-2">Effort + timer</div><code>drivetrain.set_effort()</code><div class="mt-3">Run a fixed effort for a fixed time.</div></div>
  <div v-click class="course-card blue text-center"><div class="text-3xl">2</div><div class="card-label mt-2">Speed + timer</div><code>drivetrain.set_speed()</code><div class="mt-3">Use encoder-based speed control for the same timed move.</div></div>
  <div v-click class="course-card teal text-center"><div class="text-3xl">3</div><div class="card-label mt-2">Distance + turns</div><code>drivetrain.straight()</code><br /><code>drivetrain.turn()</code><div class="mt-3">Command the movement goal directly.</div></div>
</div>

<div v-click class="takeaway mt-6">Compare the accuracy and repeatability of each approach.</div>

<!--
Students run the same short path with each approach, measure where the robot finishes, and compare consistency across trials. Set effort is open loop; set speed uses encoder feedback to maintain speed but still relies on a timer; straight and turn command the motion goal directly.
--->

---
layout: center
class: text-center
glowSeed: 518
---

# Count. Convert. Calibrate.

<div class="text-2xl mt-8">Encoder ticks turn hidden wheel motion into a number your program can use.</div>

<div v-click class="takeaway max-w-3xl mx-auto mt-10">Your challenge: stop at 2 feet without using a timer.</div>

<!--
Close with the three-step chain: count ticks, convert ticks to distance, calibrate the relationship on the physical robot. Transition to the encoder reading and tape-measure stations.
-->
