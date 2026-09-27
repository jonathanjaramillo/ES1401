---
theme: default
highlighter: shiki
css: unocss
colorSchema: dark
title: 'Summary'
info: |
  Course summary — sense, plan, act; motion; sensing; filtering; and feedback
transition: fade-out
lineNumbers: false
drawings:
  persist: false
mdc: true
vite:
  server:
    fs:
      strict: false
glowSeed: 1301
layout: center
class: text-center
---

<div class="deck-kicker">Introduction to Robotics</div>

# Summary

## From sensing the world to correcting motion

<div v-click class="takeaway max-w-3xl mx-auto mt-10">One robot. One repeating loop. Eight ideas that make it work.</div>

<!--
Frame this as a retrieval session, not a rapid replay of every lecture. Students should leave able to explain how the ideas connect and choose the right idea for a new robot problem.
-->

---
glowSeed: 1317
---

# The course in one loop

<div class="loop-grid mt-6">
  <div v-click class="course-card teal text-center">
    <div class="loop-icon">◉</div>
    <div class="card-label">Sense</div>
    Measure the robot and its world.
  </div>
  <div v-click class="loop-arrow">→</div>
  <div v-click class="course-card blue text-center">
    <div class="loop-icon">◇</div>
    <div class="card-label">Plan</div>
    Decide what should happen next.
  </div>
  <div v-click class="loop-arrow">→</div>
  <div v-click class="course-card orange text-center">
    <div class="loop-icon">⚙</div>
    <div class="card-label">Act</div>
    Command motors to change the world.
  </div>
</div>

<div v-click class="feedback-return">↖ <strong>measure the result</strong> and repeat ↙</div>

<div v-click class="takeaway">A robot becomes reliable when information can travel around the whole loop.</div>

<!--
Ask students to name one XRP part in each category. Good answers: ultrasonic/IMU/encoders for Sense, code and processor for Plan, motors and wheels for Act. The bottom arrow previews feedback.
-->

---
glowSeed: 1333
---

# Sense, plan, or act?

<div class="text-sm opacity-70 mb-5">Classify each job before revealing the label.</div>

<div class="card-grid-3">
  <div v-click class="course-card teal">
    <div class="card-label">Read wheel ticks</div>
    <div class="text-3xl font-bold">Sense</div>
    Observe what the wheels did.
  </div>
  <div v-click class="course-card blue">
    <div class="card-label">Choose a left turn</div>
    <div class="text-3xl font-bold">Plan</div>
    Convert a goal into a decision.
  </div>
  <div v-click class="course-card orange">
    <div class="card-label">Set motor effort</div>
    <div class="text-3xl font-bold">Act</div>
    Apply the chosen motion.
  </div>
</div>

<div v-click class="takeaway mt-8">The same component can support more than one stage, but every job has a role in the loop.</div>

<!--
Give students a few seconds for each classification. Emphasize that Sense, Plan, and Act are jobs, not three physical boxes. The processor reads sensors and sends motor commands, so it participates across boundaries.
-->

---
glowSeed: 1349
---

# Differential drive: two speeds, every path

<div class="drive-grid mt-5">
  <div v-click class="course-card teal text-center">
    <div class="wheel-pair"><span>↑</span><span>↑</span></div>
    <div class="card-label">Same speed</div>
    Straight
  </div>
  <div v-click class="course-card blue text-center">
    <div class="wheel-pair"><span>↑</span><span>⇡</span></div>
    <div class="card-label">Different speeds</div>
    Curve toward the slower wheel
  </div>
  <div v-click class="course-card violet text-center">
    <div class="wheel-pair"><span>↑</span><span>↓</span></div>
    <div class="card-label">Equal and opposite</div>
    Spin in place
  </div>
  <div v-click class="course-card red text-center">
    <div class="wheel-pair"><span>—</span><span>—</span></div>
    <div class="card-label">Both stopped</div>
    Hold position
  </div>
</div>

<div v-click class="takeaway">Linear motion comes from the average wheel speed; turning comes from their difference.</div>

<!--
Read each pair as left wheel, right wheel. Ask which direction the curved example turns. With the right wheel faster, the robot curves left. Avoid treating motor effort as guaranteed wheel speed; the later sensing slides explain why.
-->

---
glowSeed: 1365
---

# Encoders turn motion into measurement

<div class="chain mt-7">
  <div v-click class="chain-step teal"><strong>Ticks</strong><span>count edges</span></div>
  <div v-click class="chain-arrow">→</div>
  <div v-click class="chain-step blue"><strong>Rotations</strong><span>divide by ticks/rev</span></div>
  <div v-click class="chain-arrow">→</div>
  <div v-click class="chain-step orange"><strong>Distance</strong><span>multiply by circumference</span></div>
</div>

<div v-click class="equation-card text-center max-w-3xl mx-auto mt-7">

$$
d = \frac{\text{ticks}}{\text{ticks per revolution}}\,\pi D
$$

</div>

<div v-click class="takeaway">Timing guesses what happened. Encoders measure wheel rotation.</div>

<!--
Have students say the units at each step: ticks, revolutions, then a length unit that matches D. Encoders still measure the wheel rather than the floor, so slip remains a source of error.
-->

---
glowSeed: 1381
---

# Which sensor answers which question?

<div class="card-grid-3 mt-6">
  <div v-click class="course-card teal">
    <div class="card-label">Ultrasonic</div>
    <div class="text-2xl font-bold">How far away?</div>
    Times an echo from an external object.
  </div>
  <div v-click class="course-card blue">
    <div class="card-label">Encoder</div>
    <div class="text-2xl font-bold">How much did a wheel turn?</div>
    Counts rotation at each wheel.
  </div>
  <div v-click class="course-card violet">
    <div class="card-label">IMU</div>
    <div class="text-2xl font-bold">How am I moving or tilted?</div>
    Measures motion and orientation cues on the robot.
  </div>
</div>

<div v-click class="takeaway mt-8">Choose a sensor by the question it can answer, then account for what it cannot observe.</div>

<!--
Contrast sensing the world with sensing the robot itself. Ultrasonic depends on a reflecting surface and beam geometry. Encoders cannot see wheel slip. An IMU does not directly report global position.
-->

---
glowSeed: 1397
---

# IMU: rate is not angle

<div class="grid grid-cols-[0.9fr_1.1fr] gap-6 mt-6">
  <div class="course-card violet text-center">
    <div class="card-label">Gyroscope reports</div>
    <div class="text-5xl font-bold mt-3">ω</div>
    <div class="mt-3">angular velocity, such as °/s</div>
  </div>
  <div class="course-card blue text-center">
    <div class="card-label">We estimate</div>

$$
\Delta\theta \approx \sum_i \omega_i\Delta t_i
$$

<div>add many tiny turns</div>
  </div>
</div>

<div v-click class="card-grid-2 mt-6">
  <div class="course-card amber"><div class="card-label">Accelerometer</div>Acceleration plus the direction of gravity can reveal tilt.</div>
  <div class="course-card teal"><div class="card-label">Complementary senses</div>Different measurements can cover different weaknesses.</div>
</div>

<!--
Ask what the gyro reads after the robot turns 90 degrees and stops: approximately zero, because the turning rate is zero. Integration estimates the change in angle, but bias accumulates into drift.
-->

---
glowSeed: 1413
---

# Noise becomes a behavior problem

<div class="grid grid-cols-[1.1fr_0.9fr] gap-7 mt-5">
  <div class="course-card red">
    <div class="card-label">Raw distance readings</div>
    <div class="reading-row">
      <span>6.1</span><span>6.3</span><span class="bad">5.8</span><span>6.2</span><span>6.0</span>
    </div>
    <div class="text-sm opacity-70 mt-4">The wall did not jump. The measurement did.</div>
  </div>
  <div v-click class="course-card amber">
    <div class="card-label">Decision threshold</div>

$$
\text{stop if } d < 6\text{ in}
$$

<div>One low sample can trigger an early stop.</div>
  </div>
</div>

<div v-click class="takeaway mt-7">Noise matters when it changes the decision or the action.</div>

<!--
The raw values differ only slightly, but the threshold converts a small numerical variation into a visible behavior change. This is why filtering should be selected around the task and decision.
-->

---
glowSeed: 1429
---

# Filters remember different information

<div class="card-grid-3 mt-6">
  <div v-click class="course-card teal">
    <div class="card-label">Moving average</div>
    <div class="text-2xl font-bold">Recent window</div>
    Smooth isolated jitter by averaging the newest N samples.
  </div>
  <div v-click class="course-card blue">
    <div class="card-label">Low-pass</div>
    <div class="text-2xl font-bold">Slow trend</div>
    Follow stable values and soften fast changes.
  </div>
  <div v-click class="course-card violet">
    <div class="card-label">High-pass</div>
    <div class="text-2xl font-bold">Fast change</div>
    Reject the steady level and reveal sudden motion.
  </div>
</div>

<div v-click class="tradeoff-line mt-8"><span>more smoothing</span><span class="line"></span><span>more delay</span></div>

<div v-click class="takeaway">There is no universal “best” filter. Keep the information your decision needs.</div>

<!--
Ask students to choose: stable wall distance → moving average or low-pass; collision-like jolt → high-pass. Larger windows and smaller low-pass alpha values smooth more but respond more slowly.
-->

---
glowSeed: 1445
---

# Open loop vs. closed loop

<div class="card-grid-2 mt-6">
  <div v-click class="course-card red">
    <div class="card-label">Open loop</div>
    <div class="text-2xl font-bold mb-4">plan → act</div>
    <div class="mini-flow"><span>Drive 2 s</span><b>→</b><span>Turn 0.5 s</span></div>
    <p class="mt-4">Simple, but disturbances and drift go unchecked.</p>
  </div>
  <div v-click class="course-card teal">
    <div class="card-label">Closed loop</div>
    <div class="text-2xl font-bold mb-4">sense → compare → act → repeat</div>
    <div class="mini-flow"><span>Measure</span><b>→</b><span>Correct</span><b>↻</b></div>
    <p class="mt-4">More logic, but the robot can correct while moving.</p>
  </div>
</div>

<div v-click class="takeaway mt-7">Feedback uses the result of an action to choose the next action.</div>

<!--
Use the timed square as the open-loop example: each small motion error carries into the next side. In closed loop, the robot repeatedly observes its result and can respond to disturbances.
-->

---
glowSeed: 1461
---

# Put the pieces together: stop 6 inches from a wall

<div class="scenario-grid mt-5">
  <div v-click class="course-card teal"><div class="card-label">1 · Sense</div>Read ultrasonic distance.</div>
  <div v-click class="course-card blue"><div class="card-label">2 · Clean</div>Reduce jitter with a suitable filter.</div>
  <div v-click class="course-card violet"><div class="card-label">3 · Compare</div>Is the robot farther than 6 inches?</div>
  <div v-click class="course-card orange"><div class="card-label">4 · Act</div>Drive or stop the differential wheels.</div>
  <div v-click class="course-card amber"><div class="card-label">5 · Verify</div>Measure again immediately.</div>
</div>

<div v-click class="takeaway mt-7">Reliability comes from the connections: measurement → decision → motion → new measurement.</div>

<!--
Trace one pass through the loop, then a second pass. Ask where encoders might help: they could monitor wheel motion, but the ultrasonic sensor directly measures the wall distance that defines success.
-->

---
glowSeed: 1477
---

# Choose the idea that solves the problem

<div class="quiz-list mt-5">
  <div v-click class="quiz-row"><span>Robot curves when both motors receive the same command.</span><strong>Encoders + calibration</strong></div>
  <div v-click class="quiz-row"><span>Distance reading flickers around a stop threshold.</span><strong>Noise smoothing</strong></div>
  <div v-click class="quiz-row"><span>A timed turn changes as battery voltage drops.</span><strong>Measure the result</strong></div>
  <div v-click class="quiz-row"><span>Robot must spin without translating.</span><strong>Equal, opposite wheel speeds</strong></div>
</div>

<div v-click class="takeaway mt-6">Start by naming the failure. Then choose the measurement or control idea that addresses it.</div>

<!--
Pause before each reveal. For the first prompt, encoders expose unequal wheel rotation and calibration adjusts the commands. For the timed turn, an encoder or gyro can close the loop around the measured result.
-->

---
glowSeed: 1493
layout: center
class: text-center
---

<div class="deck-kicker">The complete mental model</div>

# Sense. Decide. Act. Check.

<div class="final-loop mt-8">
  <span class="teal-text">measure</span>
  <b>→</b>
  <span class="blue-text">interpret</span>
  <b>→</b>
  <span class="orange-text">move</span>
  <b>→</b>
  <span class="violet-text">learn from the result</span>
</div>

<div v-click class="takeaway max-w-3xl mx-auto mt-10">Every topic in this summary improves one link in that loop.</div>

<!--
Close by asking students to explain one project behavior using all four verbs. The goal is a connected mental model rather than memorized definitions.
-->
