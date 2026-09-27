---
theme: default
highlighter: shiki
css: unocss
colorSchema: dark
title: 'Open-Loop Control & First Drive'
info: |
  Week 1, Session 3 — Introduction to Robotics
transition: fade-out
lineNumbers: false
drawings:
  persist: false
mdc: true
vite:
  server:
    fs:
      strict: false
glowSeed: 303
layout: center
class: text-center
---

<div class="deck-kicker">Week 1 · Session 3</div>

# Open-Loop Control

## Your first autonomous drive

<div v-click class="takeaway max-w-3xl mx-auto mt-10">No remote control. Your program tells the robot what happens next.</div>

<!--
Open with the milestone: today the robot moves under student-written code for the first time. The lecture focuses on one idea—open-loop control—so most of the session can remain hands-on.
-->

---
layout: two-cols
layoutClass: gap-8
glowSeed: 319
---

# What is open-loop control?

<div class="mt-5 space-y-4">
  <div v-click class="course-card teal"><div class="card-label">Command</div>“Drive forward for 2 seconds.”</div>
  <div v-click class="course-card blue"><div class="card-label">Execute</div>The motors run the requested action.</div>
  <div v-click class="course-card red"><div class="card-label">Missing step</div>The robot never checks what actually happened.</div>
</div>

::right::

<div class="diagram-frame mt-3">
  <ConceptDiagram mode="open-loop" />
</div>

<!--
Compare open-loop control to throwing a paper airplane: once released, there is no mid-flight correction. The program sends a timed command and trusts the robot blindly. Closed-loop control will add measurement later.
-->

---
glowSeed: 334
---

# Why timing-based movement drifts

<div class="card-grid-3 mt-7">
  <div v-click class="course-card red"><div class="card-label">Battery</div>Voltage falls, so the same command can produce less motion.</div>
  <div v-click class="course-card amber"><div class="card-label">Hardware</div>Motors, wheels, and friction are never perfectly matched.</div>
  <div v-click class="course-card blue"><div class="card-label">Surface</div>Tile, carpet, dust, and bumps change wheel grip.</div>
</div>

<div v-click class="takeaway mt-8">Small errors accumulate because nothing measures or corrects them.</div>

<!--
Walk through the three common sources of drift. A half-second turn might be near 90 degrees once and noticeably different later. The important limitation is not that errors exist; it is that open-loop control cannot notice them.
-->

---
glowSeed: 349
---

# A square exposes accumulated error

<div class="grid grid-cols-2 gap-7 mt-6">
  <div v-click class="course-card teal">
    <div class="card-label">Intended</div>
    <div class="text-4xl font-bold">4 × 90°</div>
    <div class="mt-4">Four equal sides should return to the start.</div>
  </div>
  <div v-click class="course-card red">
    <div class="card-label">Actual</div>
    <div class="text-4xl font-bold">≈ 90°</div>
    <div class="mt-4">Each imperfect corner shifts every side after it.</div>
  </div>
</div>

<div v-click class="equation-card text-center max-w-3xl mx-auto">

$$
\text{total drift} \approx \sum_{k=1}^{4} \text{error}_k
$$

</div>

<!--
Use the square as a visible experiment. Each turn changes the starting direction for the next side, so angular error compounds into position error. The displayed relationship is conceptual: several small errors add to one noticeable miss.
-->

---
glowSeed: 365
---

# Today’s lab: first drive

<div class="card-grid-3 mt-7">
  <div v-click class="course-card teal"><div class="card-label">1 · Straight</div>Tune one short forward motion first.</div>
  <div v-click class="course-card blue"><div class="card-label">2 · Turn</div>Find a repeatable time for roughly 90°.</div>
  <div v-click class="course-card orange"><div class="card-label">3 · Sequence</div>Combine forward and turn commands into a shape.</div>
</div>

<div v-click class="takeaway mt-8"><strong>No sensors yet.</strong> Use time, observation, and careful adjustment.</div>

<!--
Explain the lab sequence. Students should test straight driving before mixing it with turns. A square is the standard challenge, but a line-and-turn path is acceptable. This is an experiment in timed control, not a precision contest.
-->

---
glowSeed: 381
---

# What success looks like

<div class="grid grid-cols-[1fr_1fr] gap-7 mt-6">
  <div v-click class="course-card red">
    <div class="card-label">First run</div>
    <div class="text-3xl font-bold">Observe</div>
    Where did the robot miss? Position, angle, or both?
  </div>
  <div v-click class="course-card teal">
    <div class="card-label">Improved run</div>
    <div class="text-3xl font-bold">Tune</div>
    Change one timing value, then compare.
  </div>
</div>

<div v-click class="takeaway mt-8">Finishing within roughly one foot is good enough today.</div>

<!--
Set a humane success criterion. Students are not expected to trace a perfect square. The goal is to complete the shape, make evidence-based timing adjustments, and recognize drift as motivation for sensing and feedback.
-->

---
layout: center
class: text-center
glowSeed: 397
---

# Command → observe → adjust

<div class="text-2xl mt-8">Open-loop control is simple, useful—and limited.</div>

<div v-click class="takeaway max-w-3xl mx-auto mt-10">Charge check. Clear floor. Start slow. Then let your code move the robot.</div>

<!--
Transition to the lab. Remind students to verify the battery and motor wiring, test at low effort, and call for help if the robot does not move. End on the excitement of the first autonomous drive.
-->
