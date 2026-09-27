---
theme: default
highlighter: shiki
css: unocss
colorSchema: dark
title: 'Debugging & Iterating'
info: |
  Week 4, Session 11 — A systematic way to improve robot behavior
transition: fade-out
lineNumbers: false
drawings:
  persist: false
mdc: true
vite:
  server:
    fs:
      strict: false
glowSeed: 1111
layout: center
class: text-center
---

<div class="deck-kicker">Week 4 · Session 11</div>

# Debugging & Iterating

## Why your robot does not work yet—and what to do next

<div v-click class="takeaway max-w-3xl mx-auto mt-10">A failed run is data. Use it to choose the next small test.</div>

<!--
Normalize debugging at the start. Combined robot behaviors rarely work perfectly on the first run, even for professionals. Today’s lecture provides a repeatable method so teams can use the rest of the session effectively.
-->

---
glowSeed: 1128
---

# Why robots rarely work the first time

<div class="card-grid-3 mt-7">
  <div v-click class="course-card teal"><div class="card-label">Sensor noise</div>Readings vary even in the same physical state.</div>
  <div v-click class="course-card blue"><div class="card-label">Mechanical variation</div>Motors, wheels, battery, and friction differ.</div>
  <div v-click class="course-card orange"><div class="card-label">Edge cases</div>Corners, gaps, and obstacle combinations surprise the code.</div>
</div>

<div v-click class="takeaway mt-8">These are properties of real systems—not signs that a team is “bad at robotics.”</div>

<!--
Walk through the three sources of failure. Code that works on another XRP may need different tuning. A course section students did not picture while coding can expose a missing state or assumption.
-->

---
layout: two-cols
layoutClass: gap-8
glowSeed: 1144
---

# The debug loop

<div class="space-y-3 mt-4">
  <div v-click class="course-card teal"><strong>1 · Isolate</strong> one behavior or course section.</div>
  <div v-click class="course-card blue"><strong>2 · Print & observe</strong> what the robot sees.</div>
  <div v-click class="course-card orange"><strong>3 · Change one thing</strong> with a prediction.</div>
  <div v-click class="course-card violet"><strong>4 · Retest</strong> and compare.</div>
</div>

::right::

<div class="diagram-frame mt-3">
  <ConceptDiagram mode="debug" />
</div>

<div v-click class="takeaway">Repeat until the evidence changes.</div>

<!--
Present the four-step cycle as the core tool. It feels slower than random editing, but it preserves cause and effect. Each loop should begin with a specific failing behavior, not “the whole robot.”
-->

---
glowSeed: 1160
---

# Print statements reveal assumptions

<div class="grid grid-cols-[1.15fr_0.85fr] gap-6 mt-5">
  <div v-click class="course-card">

```text
distance: 42 cm
distance: 18 cm
distance: 15 cm
line error: -0.23
behavior: AVOID
```

  </div>
  <div class="space-y-4">
    <div v-click class="course-card teal"><div class="card-label">Expected</div>What value or state did you predict?</div>
    <div v-click class="course-card red"><div class="card-label">Observed</div>What did the console actually show?</div>
    <div v-click class="course-card blue"><div class="card-label">Gap</div>That difference points toward the bug.</div>
  </div>
</div>

<!--
Many code problems are really incorrect assumptions about sensor values. Print distance, line error, and the selected behavior. Once a subsystem is confirmed, remove or reduce prints so the console remains readable.
-->

---
glowSeed: 1176
---

# Test small before testing big

<div class="card-grid-2 mt-7">
  <div v-click class="course-card red">
    <div class="card-label">Full course</div>
    <div class="text-3xl font-bold">slow + ambiguous</div>
    <div class="mt-3">Five behaviors run before the failure appears.</div>
  </div>
  <div v-click class="course-card teal">
    <div class="card-label">Mini test</div>
    <div class="text-3xl font-bold">fast + focused</div>
    <div class="mt-3">One line segment and one obstacle expose the target behavior.</div>
  </div>
</div>

<div v-click class="takeaway mt-8">Prove the small piece, then add it back into the full course.</div>

<!--
Encourage teams to recreate only the troublesome turn or obstacle. Shorter tests produce more iterations in the same lab time and make outcomes easier to interpret.
-->

---
glowSeed: 1192
---

# Change one thing at a time

<div class="card-grid-2 mt-7">
  <div v-click class="course-card teal">
    <div class="card-label">One change</div>
    <div class="text-4xl font-bold">cause → effect</div>
    <div class="mt-3">You can explain why the result improved or worsened.</div>
  </div>
  <div v-click class="course-card red">
    <div class="card-label">Five changes</div>
    <div class="text-4xl font-bold">result → ?</div>
    <div class="mt-3">No clear evidence about which edit mattered.</div>
  </div>
</div>

<div v-click class="takeaway mt-8">Write down the old value, new value, and prediction before rerunning.</div>

<!--
This rule is hardest when teams are frustrated. If several parameters change together, even a successful run teaches very little. A small experiment log turns tuning into evidence.
-->

---
glowSeed: 1208
---

# A useful test record

<div class="grid grid-cols-4 gap-3 mt-7">
  <div v-click class="course-card teal"><div class="card-label">Problem</div>Loses line after obstacle.</div>
  <div v-click class="course-card blue"><div class="card-label">Change</div>Search turn: 0.35 → 0.45 s.</div>
  <div v-click class="course-card amber"><div class="card-label">Prediction</div>Sensor crosses the tape.</div>
  <div v-click class="course-card violet"><div class="card-label">Result</div>Reacquired line 4/5 trials.</div>
</div>

<div v-click class="takeaway mt-8">“Better” becomes measurable when you repeat trials.</div>

<!--
Model a concise engineering log. A single successful run may be luck, so repeat the same mini test several times. Reliability is a frequency, not a feeling.
-->

---
glowSeed: 1224
---

# Today’s build session

<div class="card-grid-3 mt-8">
  <div v-click class="course-card teal"><div class="card-label">Isolate</div>Choose the highest-impact failure.</div>
  <div v-click class="course-card blue"><div class="card-label">Iterate</div>Run short tests and record changes.</div>
  <div v-click class="course-card orange"><div class="card-label">Integrate</div>Return proven pieces to the full course.</div>
</div>

<div v-click class="takeaway mt-8">Stuck on the same issue for 10–15 minutes? Ask for another set of eyes.</div>

<!--
Transition to project work. Every team should identify one priority problem and begin the debug loop. Encourage early help requests after the team has evidence to share: prints, test setup, and what changed.
-->

---
layout: center
class: text-center
glowSeed: 1240
---

# Isolate. Observe. Change one thing. Retest.

<div v-click class="takeaway max-w-3xl mx-auto mt-10">The teams that improve fastest are not bug-free—they run the clearest experiments.</div>

<!--
Close by normalizing persistence and method. Send teams to their mini test setups with one selected failure and a way to record results.
-->
