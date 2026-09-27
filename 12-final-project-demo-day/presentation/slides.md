---
theme: default
highlighter: shiki
css: unocss
colorSchema: dark
title: 'Final Project Demo Day'
info: |
  Week 4, Session 12 — Course finale
transition: fade-out
lineNumbers: false
drawings:
  persist: false
mdc: true
vite:
  server:
    fs:
      strict: false
glowSeed: 1212
layout: center
class: text-center
---

<div class="deck-kicker">Week 4 · Session 12</div>

# Final Project Demo Day

## Welcome, robotics engineers

<div class="diagram-frame max-w-4xl mx-auto mt-5">
  <ConceptDiagram mode="demo" />
</div>

<div v-click class="takeaway max-w-3xl mx-auto">Today is about showing your engineering process—not being perfect.</div>

<!--
Welcome the class and set a celebratory, low-stress tone. There is no new lecture. Teams should power up, load the final code, and use this short briefing to prepare for demos.
-->

---
glowSeed: 1229
---

# Today’s flow

<div class="grid grid-cols-4 gap-3 mt-7">
  <div v-click class="course-card teal text-center"><div class="text-4xl">1</div><div class="card-label mt-2">Setup</div>Power, code, quick check.</div>
  <div v-click class="course-card blue text-center"><div class="text-4xl">2</div><div class="card-label mt-2">Demo</div>Run the course.</div>
  <div v-click class="course-card violet text-center"><div class="text-4xl">3</div><div class="card-label mt-2">Discuss</div>Brief peer Q&A.</div>
  <div v-click class="course-card orange text-center"><div class="text-4xl">4</div><div class="card-label mt-2">Reflect</div>Course wrap-up.</div>
</div>

<div v-click class="takeaway mt-8">No new lecture—100% project and demonstration time.</div>

<!--
Preview the room flow. Teams should finish setup while the order and criteria are reviewed. Audience members are active participants: they watch, take notes, and prepare questions.
-->

---
glowSeed: 1245
---

# Completion criteria

<div class="card-grid-3 mt-7">
  <div v-click class="course-card teal">
    <div class="text-4xl mb-2">〰️</div>
    <div class="card-label">Line following</div>
    Detect and track the taped path.
  </div>
  <div v-click class="course-card red">
    <div class="text-4xl mb-2">🛑</div>
    <div class="card-label">Obstacle handling</div>
    Stop, detour, or reroute as designed.
  </div>
  <div v-click class="course-card blue">
    <div class="text-4xl mb-2">🏁</div>
    <div class="card-label">Course completion</div>
    Reach the end reliably.
  </div>
</div>

<div class="card-grid-2 mt-5">
  <div v-click class="course-card violet"><strong>Two attempts</strong> · best run counts</div>
  <div v-click class="course-card amber"><strong>Completion-focused</strong> · partial progress still shows engineering</div>
</div>

<!--
Review the same rubric teams received in Session 10. Every team that meets the criteria succeeds; this is not a first-place competition. Two attempts reduce the impact of one unlucky run.
-->

---
glowSeed: 1261
---

# Running order & format

<div class="card-grid-3 mt-7">
  <div v-click class="course-card blue"><div class="card-label">Before</div>Be ready one minute before your slot.</div>
  <div v-click class="course-card teal"><div class="card-label">During · ~5 min</div>Place, run, and explain one design decision.</div>
  <div v-click class="course-card violet"><div class="card-label">After</div>Take a brief question, then clear the course.</div>
</div>

<div v-click class="takeaway mt-8">If attempt one fails, reset calmly; attempt two returns later in the rotation.</div>

<!--
Point to the posted random order. Explain the five-minute structure and how second attempts will fit later. Keep transitions quick so every team gets a fair window.
-->

---
glowSeed: 1277
---

# Be a useful audience

<div class="card-grid-3 mt-8">
  <div v-click class="course-card teal"><div class="card-label">Notice</div>Where did sensing change behavior?</div>
  <div v-click class="course-card blue"><div class="card-label">Ask</div>What was the hardest bug to isolate?</div>
  <div v-click class="course-card orange"><div class="card-label">Learn</div>Which design choice would you reuse?</div>
</div>

<div v-click class="takeaway mt-8">Prepare one specific, respectful question for each team.</div>

<!--
Set expectations for peer attention. Good questions focus on evidence and design decisions, not just whether a run finished. Invite students to notice different valid solutions to the same challenge.
-->

---
glowSeed: 1293
---

# Your Sense–Plan–Act journey

<div class="card-grid-3 mt-7">
  <div v-click class="course-card teal">
    <div class="card-label">Sense</div>
    Encoders · ultrasonic · IMU · reflectance
  </div>
  <div v-click class="course-card blue">
    <div class="card-label">Plan</div>
    Thresholds · error · decisions · proportional control
  </div>
  <div v-click class="course-card orange">
    <div class="card-label">Act</div>
    Differential drive · line following · obstacle handling
  </div>
</div>

<div v-click class="takeaway mt-8">Build → test → debug → repeat is the engineering loop behind all three.</div>

<!--
Reflect on the course arc. Students moved from reading one number to integrating multiple sensors and behaviors in an autonomous course. Sense–plan–act is now something they have built, not just a phrase from Session 1.
-->

---
layout: center
class: text-center
glowSeed: 1309
---

# Let’s see those robots run

<div class="text-2xl mt-8">You built a system that senses, decides, acts, and improves through evidence.</div>

<div v-click class="takeaway max-w-3xl mx-auto mt-10">Take a breath. Set the robot down. Press run.</div>

<!--
Celebrate the students’ persistence and transition directly to the first team. Keep the focus on sharing work and learning from every run.
-->
