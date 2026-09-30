---
theme: default
highlighter: shiki
css: unocss
colorSchema: dark
title: 'Differential Drive'
info: |
  Week 1, Session 2 — How the XRP moves
transition: fade-out
lineNumbers: false
drawings:
  persist: false
mdc: true
vite:
  server:
    fs:
      strict: false
glowSeed: 202
layout: center
class: text-center
---

# Differential Drive

## How the XRP actually moves

<div v-click class="takeaway max-w-3xl mx-auto mt-10">Two wheels. Two motor commands. Every path the robot can make.</div>

<!--
Welcome students back and connect to the previous session’s assembly. Pose the question: without a steering wheel, how can two fixed wheels produce straight lines, curves, and spins? This lecture builds the mental model before students experiment.
-->

---
layout: two-cols
layoutClass: gap-8
glowSeed: 219
---

# What is differential drive?

<div class="space-y-4 mt-5">
  <div v-click class="course-card teal"><div class="card-label">Independent</div>Left and right wheels each have their own motor.</div>
  <div v-click class="course-card blue"><div class="card-label">No steering linkage</div>The wheels do not pivot like a car’s front wheels.</div>
  <div v-click class="course-card orange"><div class="card-label">Difference creates motion</div>Speed and direction on each side determine the path.</div>
</div>

::right::

<div class="diagram-frame mt-3">
  <ConceptDiagram mode="drive" />
</div>

<!--
Define differential drive in plain language. Compare it to a canoe or tank: changing effort on one side changes the vehicle’s path. Students do not need the kinematics yet; they need to see that the left and right commands are independent.
-->

---
glowSeed: 238
---

# Three motion patterns

<div class="card-grid-3 mt-7">
  <div v-click class="course-card teal">
    <div class="card-label">Straight</div>
    <div class="text-2xl font-bold"><code>vL = vR</code></div>
    <div class="mt-3">Same speed and same direction.</div>
  </div>
  <div v-click class="course-card amber">
    <div class="card-label">Curve</div>
    <div class="text-2xl font-bold"><code>vL ≠ vR</code></div>
    <div class="mt-3">The robot curves toward the slower wheel.</div>
  </div>
  <div v-click class="course-card violet">
    <div class="card-label">Spin in place</div>
    <div class="text-2xl font-bold"><code>vL = −vR</code></div>
    <div class="mt-3">Equal magnitudes, opposite directions.</div>
  </div>
</div>

<div v-click class="takeaway mt-7">A larger speed difference produces a tighter turn.</div>

<!--
Reveal the cases one at a time. For a curve, explain that the faster wheel covers more ground, pushing its side farther around the turn. For a point turn, the center stays nearly fixed while the body rotates.
-->

---
glowSeed: 253
---

# Motion → motor commands

<div class="grid grid-cols-[0.8fr_1.2fr] gap-6 mt-5">
  <div class="space-y-3">
    <div v-click class="course-card teal"><strong>Straight</strong><br><code>(0.5, 0.5)</code></div>
    <div v-click class="course-card amber"><strong>Curve left</strong><br><code>(0.2, 0.5)</code></div>
    <div v-click class="course-card violet"><strong>Spin</strong><br><code>(0.5, -0.5)</code></div>
  </div>
  <div v-click class="course-card">

```python {1|2|4-7|all}
from XRPLib.differential_drive import DifferentialDrive
drive = DifferentialDrive.get_default_differential_drive()

drive.set_effort(0.5, 0.5)
drive.set_effort(0.2, 0.5)
drive.set_effort(0.5, -0.5)
drive.stop()
```

  </div>
</div>

<div class="mt-3 text-sm opacity-70 text-center">Effort: −1.0 full reverse · 0 stopped · +1.0 full forward</div>

<!--
Map each visual case directly to a function call. The first argument controls the left wheel and the second controls the right. Students do not need to memorize values; they should predict the motion from the signs and relative magnitudes.
-->

---
glowSeed: 269
---

# What the two wheel speeds mean

<div v-click class="equation-card text-center max-w-4xl mx-auto mt-5">

$$
\begin{aligned}
v &= \frac{v_R + v_L}{2} &
\omega_{\text{robot}} &= \frac{v_R - v_L}{b}
\end{aligned}
$$

</div>

<div class="grid grid-cols-2 gap-6 mt-5">
  <div v-click class="course-card teal text-center"><div class="card-label">Forward speed</div>The wheel-speed average moves the robot’s center.</div>
  <div v-click class="course-card blue text-center"><div class="card-label">Robot yaw rate</div>The wheel-speed difference rotates it; <strong>b</strong> is wheel spacing.</div>
</div>

<div v-click class="takeaway">Sum controls translation. Difference controls rotation.</div>

<!--
Treat these equations as a preview, not a derivation. If the speeds add to a positive number, the center moves forward. If the speeds differ, the robot rotates. A wider wheel spacing b reduces turning rate for the same speed difference.
-->

---
glowSeed: 284
layout: two-cols
layoutClass: gap-7
---

# One turn center, three circles

<div class="space-y-4 mt-5">
  <div v-click class="course-card violet"><div class="card-label">Shared center</div>With constant wheel speeds, the robot turns about an <strong>instantaneous center of curvature</strong> (ICC).</div>
  <div v-click class="course-card amber"><div class="card-label">Inner wheel</div>The left wheel traces the smaller circle: <strong>R − b/2</strong>.</div>
  <div v-click class="course-card teal"><div class="card-label">Outer wheel</div>The faster right wheel traces the larger circle: <strong>R + b/2</strong>.</div>
</div>

::right::

<div class="diagram-frame turn-radius-frame">
  <TurnRadiusDiagram />
</div>

<div class="source-note">Geometry adapted from <a href="https://doi.org/10.1016/j.mechatronics.2008.04.001">Han, Choi & Lee (2008)</a>.</div>

<!--
Introduce the instantaneous center of curvature as the point the robot is rotating around right now. For a left turn, the left wheel is closer to that point and the right wheel is farther away. The robot center, left wheel, and right wheel therefore trace three concentric circles.
-->

---
glowSeed: 291
---

# Same angle, different distances

<div class="grid grid-cols-[1.15fr_0.85fr] gap-7 mt-5">
<div>
<div v-click class="equation-card text-center">

$$
\begin{aligned}
\Delta s_L &= \left(R-\frac{b}{2}\right)\Delta\theta \\
\Delta s_R &= \left(R+\frac{b}{2}\right)\Delta\theta
\end{aligned}
$$

</div>
<div v-click class="takeaway">Both wheels sweep the same angle <strong>Δθ</strong> in the same time <strong>Δt</strong>.</div>
</div>
<div class="space-y-4">
<div v-click class="course-card amber text-center">
<div class="card-label">Left wheel</div>

$$v_L = \left(R-\frac{b}{2}\right)\omega_{\text{robot}}$$

</div>
<div v-click class="course-card teal text-center">
<div class="card-label">Right wheel</div>

$$v_R = \left(R+\frac{b}{2}\right)\omega_{\text{robot}}$$

</div>
</div>
</div>

<div v-click class="mt-5 text-center text-lg opacity-80">Here, <strong>ω<sub>robot</sub> = Δθ / Δt</strong> is the robot’s yaw rate—not a wheel’s angular speed.</div>

<!--
Arc length is radius times angle. The two wheels are attached to the same rigid robot, so they sweep through exactly the same angle in exactly the same time. Dividing both arc-length equations by delta t converts distances into wheel speeds.
-->

---
glowSeed: 299
---

# Solve for the turn radius

<div class="grid grid-cols-[1.05fr_0.95fr] gap-7 mt-4">
<div>
<div v-click class="course-card blue text-center">
<div class="card-label">Add the wheel equations</div>

$$v_R+v_L=2R\omega_{\text{robot}}$$

</div>
<div v-click class="course-card violet text-center mt-4">
<div class="card-label">Subtract the wheel equations</div>

$$v_R-v_L=b\omega_{\text{robot}}$$

</div>
</div>
<div v-click class="equation-card radius-result text-center">
<div class="card-label">Divide, then solve for R</div>

$$
\boxed{R=\frac{b\left(v_R+v_L\right)}{2\left(v_R-v_L\right)}}
$$

<div class="text-sm opacity-70 mt-2">Use |R| for the circle’s radius; the sign tells the turn direction.</div>
</div>
</div>

<div class="card-grid-3 mt-5">
  <div v-click class="course-card teal text-center"><div class="card-label">Same speeds</div><strong>vR = vL</strong><br>R → ∞ · straight</div>
  <div v-click class="course-card violet text-center"><div class="card-label">Opposite speeds</div><strong>vR = −vL</strong><br>R = 0 · spin</div>
  <div v-click class="course-card amber text-center"><div class="card-label">Example</div><strong>b = 0.16 m</strong><br>vL = 0.20, vR = 0.40<br><strong>R = 0.24 m</strong></div>
</div>

<!--
Adding cancels the wheel-spacing terms; subtracting cancels R. Dividing the two results also cancels omega. Emphasize the sanity checks: equal speeds make the denominator zero, so the radius is infinite; equal and opposite speeds make the numerator zero, so the robot spins about its center. For the example, 0.08 times 0.60 divided by 0.20 equals 0.24 meters.
-->

---
layout: center
class: text-center
glowSeed: 314
---

# Two numbers control every path

<div class="card-grid-3 max-w-4xl mx-auto mt-8 text-left">
  <div v-click class="course-card teal"><strong>Match</strong><br>go straight</div>
  <div v-click class="course-card amber"><strong>Offset</strong><br>follow a curve</div>
  <div v-click class="course-card violet"><strong>Oppose</strong><br>spin in place</div>
</div>


<!--
Recap the three cases and transition to lab. Ask students to begin at low effort, keep the robot on the floor, and use drive.stop() after each short test. The goal is a reliable mental mapping from values to motion.
-->
