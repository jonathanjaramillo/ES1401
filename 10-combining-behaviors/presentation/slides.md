---
theme: default
highlighter: shiki
css: unocss
colorSchema: dark
title: 'Combining Behaviors'
info: |
  Week 4, Session 10 — Final project kickoff
transition: fade-out
lineNumbers: false
drawings:
  persist: false
mdc: true
vite:
  server:
    fs:
      strict: false
glowSeed: 1010
layout: center
class: text-center
---

<div class="deck-kicker">Week 4 · Session 10</div>

# Combining Behaviors

## From single skills to a robot “brain”

<div v-click class="takeaway max-w-3xl mx-auto mt-10">Line following + obstacle handling = your final project begins.</div>

<!--
Connect the two behaviors students already have: proportional line following and ultrasonic obstacle sensing. Today they stop treating those as isolated demos and combine them into one decision-making program.
-->

---
glowSeed: 1027
---

# Why combine behaviors?

<div class="card-grid-2 mt-7">
  <div v-click class="course-card red text-center">
    <div class="text-5xl">💥</div>
    <div class="card-label mt-3">Line follower only</div>
    Follows the tape straight into a box.
  </div>
  <div v-click class="course-card teal text-center">
    <div class="text-5xl">🧠</div>
    <div class="card-label mt-3">Combined behavior</div>
    Detects the box, changes priority, then continues.
  </div>
</div>

<div v-click class="takeaway mt-8">Autonomous robots choose among actions from what they sense right now.</div>

<!--
Use a robot vacuum analogy. It must handle several objectives and switch between them. The XRP needs a rule for which behavior wins when an obstacle sits on the line.
-->

---
layout: two-cols
layoutClass: gap-8
glowSeed: 1043
---

# The core tool: if / else

<div class="space-y-4 mt-5">
  <div v-click class="course-card red"><div class="card-label">If obstacle is close</div>Stop, turn, or begin an avoidance sequence.</div>
  <div v-click class="course-card teal"><div class="card-label">Else</div>Use proportional control to follow the line.</div>
  <div v-click class="course-card blue"><div class="card-label">Every loop</div>Read sensors and choose again.</div>
</div>

::right::

<div class="diagram-frame mt-3">
  <ConceptDiagram mode="combine" />
</div>

<!--
Explain priority: obstacle handling is checked first because collision prevention outranks ordinary line following. Both branches return to the sensor read, so the robot can change behavior on the next loop.
-->

---
glowSeed: 1059
---

# A clean program structure

<div class="grid grid-cols-[1.25fr_0.75fr] gap-6 mt-5">
  <div v-click class="course-card">

```python {1|2|3-4|5-6|all}
while True:
    distance = get_distance_cm()
    if distance < 10:
        handle_obstacle()
    else:
        follow_line()
```

  </div>
  <div class="space-y-4">
    <div v-click class="course-card red"><div class="card-label">Priority</div>Check obstacle first.</div>
    <div v-click class="course-card teal"><div class="card-label">Functions</div>Test each behavior alone.</div>
    <div v-click class="course-card blue"><div class="card-label">Loop</div>Reconsider continuously.</div>
  </div>
</div>

<div v-click class="takeaway mt-5">Combine tested functions; do not rewrite everything inside one giant loop.</div>

<!--
Walk through the pseudocode. The function names hide internal details and make each behavior independently testable. Students may use a smoothed distance from Session 6 and the proportional follower from Session 9.
-->

---
glowSeed: 1075
---

# Sequencing vs. deciding

<div class="card-grid-2 mt-7">
  <div v-click class="course-card blue">
    <div class="card-label">Sequence</div>
    <div class="text-xl font-bold">A → B → C</div>
    <div class="mt-3">Fixed order: turn right, drive, turn left.</div>
  </div>
  <div v-click class="course-card teal">
    <div class="card-label">Decision</div>
    <div class="text-xl font-bold">if / else</div>
    <div class="mt-3">Choose a behavior from live sensor data.</div>
  </div>
</div>

<div v-click class="takeaway mt-8">Real solutions mix both: decide to avoid, then run an avoidance sequence.</div>

<!--
Clarify the vocabulary teams will use while planning. The trigger is a decision. The physical maneuver around an obstacle can be a short open-loop sequence, followed by a search for the line.
-->

---
glowSeed: 1091
---

# Final project challenge

<div class="card-grid-3 mt-7">
  <div v-click class="course-card teal"><div class="card-label">Follow</div>Detect and track the taped line.</div>
  <div v-click class="course-card red"><div class="card-label">Handle</div>Stop, detour, or reroute at an obstacle.</div>
  <div v-click class="course-card blue"><div class="card-label">Finish</div>Reach the end of the course reliably.</div>
</div>

<div class="card-grid-2 mt-5">
  <div v-click class="course-card violet"><strong>Teams:</strong> 2–3 students</div>
  <div v-click class="course-card amber"><strong>Timeline:</strong> start today · iterate Session 11 · demo Session 12</div>
</div>

<!--
Introduce the official handout and rubric. Teams have design freedom in obstacle response as long as their choice meets the challenge criteria. Emphasize that the project spans today, the debugging session, and Demo Day.
-->

---
glowSeed: 1107
---

# Plan before you code

<div class="card-grid-3 mt-8">
  <div v-click class="course-card teal"><div class="card-label">1 · Sketch</div>Draw the course and decision points.</div>
  <div v-click class="course-card blue"><div class="card-label">2 · Pseudocode</div>Write the sensor checks and actions.</div>
  <div v-click class="course-card orange"><div class="card-label">3 · Integrate</div>Merge already-tested behavior functions.</div>
</div>

<div v-click class="takeaway mt-8">Answer now: what exactly happens when distance drops below the threshold?</div>

<!--
Set today’s lab deliverable: a team plan, pseudocode, and first integrated draft. Require a specific obstacle response rather than “avoid it somehow.” Encourage role sharing so every student can explain the decision logic.
-->

---
layout: center
class: text-center
glowSeed: 1123
---

# Sense more. Choose priorities. Compose behaviors.

<div v-click class="takeaway max-w-3xl mx-auto mt-10">Build each behavior alone. Test it alone. Then connect the decisions.</div>

<!--
Close with the safest integration strategy and transition to team formation. Distribute the rules, ask teams to sketch before opening the editor, and circulate to review plans.
-->
