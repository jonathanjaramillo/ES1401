---
theme: default
highlighter: shiki
css: unocss
colorSchema: dark
title: 'Sense–Plan–Act & Robot Anatomy'
info: |
  Week 1, Session 1 — Introduction to Robotics with the XRP
transition: fade-out
lineNumbers: false
drawings:
  persist: false
mdc: true
vite:
  server:
    fs:
      strict: false
glowSeed: 101
layout: center
class: text-center
---

<div class="deck-kicker">Week 1 · Session 1</div>

# Welcome to Robotics

## Meet your XRP

<div class="mt-7 text-xl opacity-85">This month, your code becomes a real robot’s behavior.</div>

<div v-click class="takeaway max-w-3xl mx-auto mt-10">
Today’s finish line: <strong>assembled robot + first program running</strong>
</div>

<!--
Welcome students and set the pace: this is a short conceptual launch followed by hands-on assembly. Emphasize that no prior robotics experience is assumed. By the end of class, each team should have an XRP assembled and executing a tiny program.
-->

---
layout: center
class: text-center
glowSeed: 107
---

<div class="deck-kicker">Before We Build Anything</div>

# What *Is* a Robot?

<div class="mt-6 text-xl opacity-85">Not "what parts does it have" — what makes something a robot at all?</div>


<!--
Open cold with the big question and let it sit — don't answer it yourself yet. Give students 30 seconds to talk to a neighbor, then take two or three verbal answers from the room without confirming or rejecting any of them. We're about to stress-test whatever definitions come up against real examples on the next slide.
-->

---
glowSeed: 111
---

# Robot or Not?

<div class="mt-2 text-lg opacity-85">For each one — robot, or not a robot? Be ready to defend your answer.</div>

<div class="grid grid-cols-4 gap-3 mt-6">
  <div v-click class="course-card teal text-center"><div class="text-3xl mb-1">🧹</div>Robot vacuum</div>
  <div v-click class="course-card blue text-center"><div class="text-3xl mb-1">🍽️</div>Dishwasher</div>
  <div v-click class="course-card orange text-center"><div class="text-3xl mb-1">🚗</div>RC car (human driving)</div>
  <div v-click class="course-card violet text-center"><div class="text-3xl mb-1">🌡️</div>Thermostat</div>
  <div v-click class="course-card amber text-center"><div class="text-3xl mb-1">🔑</div>Wind-up toy car</div>
  <div v-click class="course-card red text-center"><div class="text-3xl mb-1">🔊</div>Smart speaker</div>
  <div v-click class="course-card teal text-center"><div class="text-3xl mb-1">🥤</div>Vending machine</div>
  <div v-click class="course-card blue text-center"><div class="text-3xl mb-1">🛰️</div>Mars rover</div>
</div>

<!--
Reveal these one at a time and take a quick show-of-hands vote on each before moving on — don't confirm right or wrong yet. Good friction points: the dishwasher and wind-up car just run a fixed timer/mechanism with no sensing, which feels robot-ish but isn't (this foreshadows open-loop control in Session 3). The RC car has all the sensing and deciding happening in the human's head, not the car. The thermostat is deliberately simple hardware that most people don't call a "robot" despite technically sensing and reacting — a good pressure test for whatever definition the class proposed. Save the actual verdicts for the next slide.
-->

---
layout: center
glowSeed: 115
---

# So, What Makes Something a Robot?

<div v-click class="takeaway max-w-3xl mx-auto mt-6 text-xl">
A robot is a system that <strong>senses</strong> its environment, <strong>decides</strong> what to do, and <strong>acts</strong> — over and over, in a loop.
</div>

<div v-click class="mt-8 text-lg opacity-85 text-center">
No sensing, no loop → not a robot, no matter how clever the mechanism.
</div>

<!--
Land the formal definition: a robot runs a repeating sense-decide-act loop, reacting to its own environment — not to a human operator. Now resolve the "robot or not" list against this definition: the RC car and wind-up car fail it (no autonomous sensing/reacting loop of their own), the dishwasher is the debatable one (fixed timer, not reacting to sensed conditions — a preview of open-loop vs. closed-loop), and the thermostat, vending machine, Roomba, smart speaker, and Mars rover all pass. This one definition covers a thermostat and a Mars rover alike — including the robot sitting in front of each student right now. Transition straight into the formal Sense-Plan-Act loop on the next slide — it's the same idea, just named.
-->

---
layout: iframe
url: https://www.youtube.com/embed/7bsEN8mwUB8
---

<!--
Video slide — play the clip for the class before moving on to the formal Sense-Plan-Act model.
-->

---
layout: two-cols
layoutClass: gap-8
glowSeed: 118
---

# Every robot does three things

<div class="mt-4 space-y-4">
  <div v-click class="course-card teal"><div class="card-label">1 · Sense</div>Gather information about the world.</div>
  <div v-click class="course-card blue"><div class="card-label">2 · Plan</div>Choose what to do with that information.</div>
  <div v-click class="course-card orange"><div class="card-label">3 · Act</div>Do something that changes the world.</div>
</div>

::right::

<div class="diagram-frame mt-2">
  <ConceptDiagram mode="sense-plan-act" />
</div>

<div v-click class="takeaway">Then the loop repeats—many times per second.</div>

<!--
Introduce the one mental model that anchors the course. A Roomba, Mars rover, self-driving car, and XRP all repeat this loop. Point out that acting changes the world, so the next sensor reading is new. Let the animated arrows reinforce repetition.
-->

---
glowSeed: 136
---

# Example: avoiding a wall

<div class="card-grid-3 mt-8">
  <div v-click class="course-card teal">
    <div class="card-label">Sense</div>
    <div class="text-3xl font-bold text-teal-300">10 cm</div>
    <div class="mt-2">Ultrasonic sensor measures the wall ahead.</div>
  </div>
  <div v-click class="course-card blue">
    <div class="card-label">Plan</div>
    <div class="text-3xl font-bold text-blue-300">Too close</div>
    <div class="mt-2">The program chooses a turn instead of forward motion.</div>
  </div>
  <div v-click class="course-card orange">
    <div class="card-label">Act</div>
    <div class="text-3xl font-bold text-orange-300">Turn away</div>
    <div class="mt-2">The motors change the robot’s path.</div>
  </div>
</div>

<div v-click class="takeaway mt-7">A fresh distance reading starts the next cycle immediately.</div>

<!--
Make the loop concrete with a behavior students will build later. Stress that the robot does not execute these steps only once. It measures again immediately after turning, and the new measurement may lead to a new decision.
-->

---
glowSeed: 152
---

# Meet the XRP

<div class="card-grid-2 mt-6">
  <div v-click class="course-card blue">
    <div class="card-label">Motion</div>
    Two independently driven wheels steer without a steering linkage.
  </div>
  <div v-click class="course-card teal">
    <div class="card-label">Brain</div>
    A tiny controller runs your MicroPython program.
  </div>
  <div v-click class="course-card orange">
    <div class="card-label">Senses</div>
    Distance, heading, wheel motion, and floor reflectance.
  </div>
  <div v-click class="course-card violet">
    <div class="card-label">Connection</div>
    A browser-based editor sends code and shows live output.
  </div>
</div>

<div v-click class="takeaway">Small rover. Same building blocks as much larger robots.</div>

<!--
Give students a quick physical tour while they look at the robot in front of them. Differential drive means the wheel speeds are controlled independently. The controller is a compact computer, and MicroPython is Python designed for embedded hardware.
-->

---
glowSeed: 171
---

# Five subsystems make the loop possible

<div class="card-grid-3 mt-6">
  <div v-click class="course-card teal"><div class="card-label">Perception</div><strong>Sensors</strong> gather data—the “sense” part.</div>
  <div v-click class="course-card blue"><div class="card-label">Computation</div><strong>Code + processor</strong> decide—the “plan” part.</div>
  <div v-click class="course-card orange"><div class="card-label">Actuation</div><strong>Motors</strong> create motion—the “act” part.</div>
</div>

<div class="card-grid-2 mt-4">
  <div v-click class="course-card violet"><div class="card-label">Communication</div>Moves code, data, and messages between devices.</div>
  <div v-click class="course-card red"><div class="card-label">Power</div>Supplies the energy every other subsystem needs.</div>
</div>

<!--
Connect the first three subsystems directly to sense–plan–act. Then add the two practical necessities: communication and power. Ask students which subsystem would fail first if the battery were removed, then point out that all of them depend on it.
-->

---
glowSeed: 188
---

# Spot the subsystems on the XRP

<div class="grid grid-cols-[1fr_1.25fr] gap-5 mt-5">
  <div class="space-y-3">
    <div v-click class="course-card teal"><strong>Perception</strong><br><span class="text-sm">ultrasonic · IMU · reflectance · encoders</span></div>
    <div v-click class="course-card blue"><strong>Computation</strong><br><span class="text-sm">RP2040 / RP2350 controller</span></div>
    <div v-click class="course-card orange"><strong>Actuation</strong><br><span class="text-sm">two drive motors · servo</span></div>
  </div>
  <div class="space-y-3">
    <div v-click class="course-card violet"><strong>Communication</strong><br><span class="text-sm">built-in wireless connection to the editor</span></div>
    <div v-click class="course-card red"><strong>Power</strong><br><span class="text-sm">onboard battery pack</span></div>
  </div>
</div>

<!--
Use the physical XRP as the real diagram. Call out the front distance sensor, the IMU on the board, the downward-facing reflectance sensor, and the motor encoders. Then locate the controller, motors, wireless connection, and battery pack.
-->

---
glowSeed: 207
---

# Today’s lab: bring it to life

<div class="card-grid-3 mt-8">
  <div v-click class="course-card teal text-center">
    <div class="text-4xl mb-2">📦</div><div class="card-label">Unbox</div>
    Inventory parts and learn their names.
  </div>
  <div v-click class="course-card blue text-center">
    <div class="text-4xl mb-2">🔧</div><div class="card-label">Assemble</div>
    Build the chassis—no soldering required.
  </div>
  <div v-click class="course-card orange text-center">
    <div class="text-4xl mb-2">💻</div><div class="card-label">Code</div>
    Blink the LED and print one live sensor value.
  </div>
</div>

<div v-click class="takeaway mt-8"><strong>Ask early.</strong> Setup problems are part of the lab, not a test of prior knowledge.</div>

<!--
Walk through the three lab phases. The first program should blink the onboard LED, then print one sensor reading to the console. Frame this as a tiny robotics loop: the computer reads or decides, then changes the LED.
-->

---
layout: center
class: text-center
glowSeed: 223
---

# One loop. Five subsystems. Your robot.

<div class="grid grid-cols-2 gap-8 max-w-4xl mx-auto mt-6 text-left">
  <div v-click class="course-card teal"><div class="card-label">Remember</div><strong>Sense → Plan → Act</strong> repeats continuously.</div>
  <div v-click class="course-card blue"><div class="card-label">Find</div>Perception · computation · actuation · communication · power.</div>
</div>

<div v-click class="mt-10 text-2xl">Now let’s build an XRP.</div>

<!--
Close with a fast verbal recap. Ask for the three steps, then ask for any two of the five subsystems. Transition immediately to station setup and assembly.
-->
