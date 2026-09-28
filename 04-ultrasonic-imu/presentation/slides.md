---
theme: default
highlighter: shiki
css: unocss
colorSchema: dark
title: 'Ultrasonic & IMU'
info: |
  Week 2, Session 4 — Distance and heading sensing
transition: fade-out
lineNumbers: false
drawings:
  persist: false
mdc: true
vite:
  server:
    fs:
      strict: false
glowSeed: 505
layout: center
class: text-center
---

<div class="deck-kicker">Week 2 · Session 4</div>

# Ultrasonic & IMU

## “How far?” and “Which way?”

<div v-click class="takeaway max-w-3xl mx-auto mt-10">Two new senses: the world ahead and the robot’s orientation.</div>

<!--
Connect to encoders: those measured wheel rotation. Today students add a forward-looking distance measurement and an internal heading measurement. The lab is about watching live values and developing intuition.
-->

---
glowSeed: 522
---

# Sensing yourself vs. sensing the world

<div class="card-grid-2 mt-6">
<div v-click="1" class="course-card violet">
<div class="card-label">Humans · proprioceptive</div>
<div v-click="2" class="text-xl font-bold">What can you sense in a sensory deprivation tank?</div>
<p v-click="3">Sense limb position, joint movement, and muscle tension—even with your eyes closed.</p>
</div>
<div v-click="4" class="course-card teal">
<div class="card-label">Humans · exteroceptive</div>
<div v-click="5">
<div class="text-xl font-bold">What is around me?</div>
<p>Vision, hearing, touch, smell, and taste reveal the outside world.</p>
</div>
</div>
<div v-click="6" class="course-card violet">
<div class="card-label">Robots · proprioceptive</div>
<div v-click="7">
<strong>Encoders:</strong> wheel and joint rotation.<br>
<strong>Gyro + accelerometer:</strong> body motion and tilt, analogous to our inner-ear balance sense.
</div>
</div>
<div v-click="8" class="course-card teal">
<div class="card-label">Robots · exteroceptive</div>
<div v-click="9">
<strong>Range finders:</strong> distance to objects.<br>
<strong>Cameras:</strong> objects and landmarks.<br>
<strong>Contact sensors:</strong> touching a surface.
</div>
</div>
</div>

<!--
Start with only the slide title visible. Click 1: reveal the human proprioceptive box and label; ask what belongs in it. Click 2: reveal the sensory-deprivation-tank prompt, then pause for discussion. Click 3: reveal the proprioceptive examples. Click 4: reveal the human exteroceptive box and label; ask for examples before click 5 reveals the answer. Click 6: reveal the robot proprioceptive box and label; discuss before click 7 reveals its examples. Click 8: reveal the robot exteroceptive box and label; discuss before click 9 reveals its examples. A sensory deprivation tank reduces external stimulation; sensations that remain are not all proprioceptive (for example, hunger is interoceptive). Distinguish proprioception from the vestibular balance sense; both provide information about one's body. Gyros and accelerometers are usually grouped as proprioceptive robot sensors. A magnetometer senses an external field even when packaged with an IMU. Source: https://pubmed.ncbi.nlm.nih.gov/29510103/
-->

---
glowSeed: 522
hideSlideNumber: true
---

<Youtube v-if="$slidev.nav.currentPage === 3" id="pMEROPOK6v8" class="absolute inset-0 w-full h-full" />

---
glowSeed: 522
---

# Two different questions

<div class="card-grid-2 mt-8">
  <div v-click class="course-card teal text-center">
    <div class="text-5xl mb-3">📡</div>
    <div class="card-label">Ultrasonic</div>
    <div class="text-2xl font-bold">How far away?</div>
    <div class="mt-3">Measures distance to an object ahead.</div>
  </div>
  <div v-click class="course-card violet text-center">
    <div class="text-5xl mb-3">🧭</div>
    <div class="card-label">IMU / gyro</div>
    <div class="text-2xl font-bold">Which way am I facing?</div>
    <div class="mt-3">Measures orientation and turning.</div>
  </div>
</div>

<div v-click class="takeaway mt-8">Environment + orientation are not the same as position on a map.</div>

<!--
Keep the distinction crisp. Ultrasonic sensing describes an object relative to the robot. Heading describes the robot’s orientation relative to its starting direction. Neither alone gives global x-y position.
-->

---
layout: two-cols
layoutClass: gap-8
glowSeed: 539
---

# Ultrasonic: time an echo

<div class="space-y-3 mt-3">
  <div v-click class="course-card teal"><div class="card-label">1 · Send</div>A short sound pulse leaves the sensor.</div>
  <div v-click class="course-card blue"><div class="card-label">2 · Bounce</div>The pulse reflects from an object.</div>
  <div v-click class="course-card orange"><div class="card-label">3 · Receive</div>The return time reveals distance.</div>
</div>

<div v-click class="equation-card text-center" style="margin:.5rem auto;padding:.55rem 1rem">

$$
d = \frac{c\,\Delta t}{2}
$$

<div class="text-sm opacity-75">Divide by 2 because the sound travels out and back.</div>
</div>

::right::

<div v-click class="diagram-frame mt-2">
  <ConceptDiagram mode="ultrasonic" />
</div>

<!--
Use the bat or canyon-echo analogy. The sensor times a round trip, so the one-way distance is half of speed times time. Students do not need to compute this manually; the library reports distance.
-->

---
glowSeed: 555
---

# Ultrasonic in the real world

<div class="card-grid-3 mt-7">
  <div v-click class="course-card teal"><div class="card-label">Best case</div>Flat, hard object directly in front.</div>
  <div v-click class="course-card amber"><div class="card-label">Angled surface</div>The echo reflects away from the sensor.</div>
  <div v-click class="course-card red"><div class="card-label">Soft surface</div>Fabric absorbs sound and weakens the return.</div>
</div>

<div v-click class="takeaway mt-8">Noisy or missing readings are physical behavior—not automatically bad code.</div>

<!--
Point out the forward cone of sensing. A jacket, narrow chair leg, or angled book may yield unreliable values. Prepare students to expect variation when they move targets around in the lab.
-->

---
glowSeed: 571
---

# Ultrasonic: failure modes → filters

<div class="card-grid-2 mt-5 ultrasonic-filters">
<div v-click class="course-card teal">
<div class="card-label">1 · Random noise</div>
<div>Small jitter around the true distance; often modeled as Gaussian noise.</div>
<p><strong>Filter:</strong> average a few valid readings or smooth over time. More smoothing adds delay.</p>
</div>
<div v-click class="course-card amber">
<div class="card-label">2 · No returning echo</div>
<div>XRP’s XRPLib returns <strong>65535</strong> on timeout: an invalid-reading code, not a distance.</div>
<p><strong>Filter:</strong> reject 65535 and values outside 2–400 cm before averaging. Mark missing data “unknown.”</p>
</div>
<div v-click class="course-card violet">
<div class="card-label">3 · Multiple reflections</div>
<div>Extra bounces lengthen the echo path and can produce a sudden, overly large distance.</div>
<p><strong>Filter:</strong> flag jumps too large for speed × time; recheck. A short median filter rejects isolated spikes.</p>
</div>
<div v-click class="course-card blue">
<div class="card-label">4 · An object enters the beam</div>
<div>A hand or passing object can abruptly replace the wall as the measured target.</div>
<p><strong>Filter:</strong> for wall tracking, flag and recheck jumps. For obstacle avoidance, treat a new close object as real.</p>
</div>
</div>
<div v-click class="takeaway ultrasonic-filter-rule">Same stationary target + nearly fixed beam: flag |Δd| &gt; v<sub>max</sub> Δt + noise margin.<br>Turning or switching targets can cause real jumps—even when the robot moves slowly.</div>

<!--
Reveal one failure/filter pair per click, then reveal the jump rule. Gaussian noise is a useful model for small fluctuations, not a guarantee that every sensor error is normally distributed. A moving average reduces independent, zero-mean noise but cannot repair bias, multipath, or invalid measurements; reject invalid values before smoothing.

Verified against the course checkout ../../XRP_MicroPython/XRPLib/rangefinder.py and https://open-stem.github.io/XRP_MicroPython/api.html#XRPLib.rangefinder.Rangefinder : distance() returns centimeters; MAX_VALUE is 65535, returned for nonpositive echo pulse times or ETIMEDOUT. The documented HC-SR04 operating range is 2–400 cm. This sentinel is library-specific, not a universal ultrasonic-sensor behavior. Do not interpret repeated timeouts as proof that the path is clear or keep a stale estimate indefinitely.

“Double reflections” are multipath: a longer sound route can yield an excessive apparent distance, not necessarily exactly twice the correct value. Compare a new valid measurement to the last accepted value using actual elapsed time and consistent units. Example: at a maximum approach speed of 50 cm/s and a 0.10 s interval, allow 5 cm plus a measured noise margin for a near-normal, fixed wall view. Rotation, oblique surfaces, edges, and changing targets invalidate a simple translational-speed bound. Recheck flagged readings and reacquire a target if a new level persists rather than rejecting real changes forever. A median of three valid readings can remove a single isolated spike but also delays genuine changes.

An object entering the beam is a real scene change. It is an outlier only relative to the task of estimating distance to the original wall; it can be the most important observation for collision avoidance. Use conservative stop/slow behavior for a new close obstacle while verifying it, rather than filtering it away on the assumption that the robot itself moved slowly.
-->

---
glowSeed: 571
---

# Gyroscope: how fast am I turning?

<div class="imu-columns">
<div>
<div v-click class="course-card violet"><div class="card-label">Angular velocity · <span style="text-transform:none">ω</span></div>A gyroscope measures rotational velocity, usually in <strong>°/s</strong> or <strong>rad/s</strong>.</div>
<p>A 3-axis gyro reports rotation rates about the robot’s x, y, and z axes.</p>
</div>
<ImuDiagram mode="gyro" />
</div>

<!--
Rotate the robot quickly, slowly, then stop while keeping it turned. The gyro reports rate, not an absolute angle. For the next examples the robot stays level and turns only about z; integrating a body-axis gyro independently is not a general 3D attitude solution.
-->

---
glowSeed: 574
---

# Rate × time = change in position

<div class="card-grid-2 mt-7">
<div v-click class="course-card blue">
<div class="card-label">Straight-line motion</div>

$$\Delta x = v\,\Delta t$$
$$2\;\mathrm{m/s}\times3\;\mathrm{s}=6\;\mathrm{m}$$

Constant velocity × elapsed time gives displacement.
</div>
<div v-click class="course-card violet">
<div class="card-label">Rotation about one axis</div>

$$\Delta\theta=\omega\,\Delta t$$
$$30^\circ/\mathrm{s}\times3\;\mathrm{s}=90^\circ$$

Constant angular velocity × elapsed time gives angle change.
</div>
</div>
<div v-click class="takeaway mt-7">Add the change to the starting angle: θ = θ₀ + Δθ. Direction gives the sign.</div>

---
glowSeed: 577
---

# Changing rate? Add tiny turns.

<div class="imu-columns chart-columns">
<ImuDiagram mode="riemann" />
<div>
<div v-click class="course-card teal"><div class="card-label">A Riemann sum</div>Sample rapidly. Treat the rate as constant over each short time interval.</div>
<p>Each rectangle has area <strong>ωᵢ Δtᵢ</strong>: one tiny angle change.</p>
<p>Add the rectangles to approximate the area under the curve.</p>
<div v-click class="takeaway">Signed area = angular displacement Δθ.</div>
</div>
</div>

<!--
The blue curve is the changing rate; teal rectangles use the left endpoint of each interval. Shorter intervals better capture changes in rate, but do not eliminate sensor bias. This example has only positive rotation; area below zero would subtract from the angle. Angular position is the starting angle plus the accumulated signed area.
-->

---
glowSeed: 580
---

# The sum becomes a loop

<div class="card-grid-2 mt-6">
<div v-click class="course-card teal">
<div class="card-label">Math · one-axis rotation</div>

$$\theta_N\approx\theta_0+\sum_{i=0}^{N-1}\omega_i\,\Delta t_i$$
$$\Delta t_i=t_{i+1}-t_i$$

Each update adds one rectangle:

$$\theta\leftarrow\theta+\omega_i\,\Delta t_i$$

</div>
<div v-click class="course-card violet">
<div class="card-label">Python · recorded samples</div>

```python
# t: timestamps in seconds
# omega: z-axis rates in deg/s
theta = 0.0  # starting angle, deg
for i in range(len(t) - 1):
    dt = t[i + 1] - t[i]
    theta += omega[i] * dt
```

Use measured elapsed time, even if the sampling interval varies.
</div>
</div>
<div v-click class="takeaway">A 0.5°/s bias adds 30° of error in 60 s. Integrated gyro angles drift.</div>

---
glowSeed: 583
---

# Accelerometer: three axes of acceleration

<div class="imu-columns">
<div>
<div v-click class="course-card blue"><div class="card-label">Readings · <span style="text-transform:none">a<sub>x</sub>, a<sub>y</sub>, a<sub>z</sub></span></div>A tiny suspended mass deflects as the sensor is pushed. Electronics measure the deflection along three axes.</div>
<p>It measures <strong>specific force</strong>, in m/s² or g. At rest, its readings reveal the direction of gravity.</p>
<div v-click class="takeaway">1 g ≈ 9.81 m/s². A resting sensor reads about 1 g in total, not zero.</div>
</div>
<ImuDiagram mode="axes" />
</div>

<!--
Our right-handed body axes are x forward, y left, z up. The raw specific-force vector points opposite gravity when supported at rest: a level sensor reads (0,0,+g). Free fall gives approximately zero. Some libraries flip axes or output gravity-removed acceleration, so check the sensor convention. Reference: https://www.vectornav.com/resources/inertial-navigation-primer/theory-of-operation/theory-inertial
-->

---
glowSeed: 586
---

# Tilt redistributes the gravity signal

<ImuDiagram mode="tilt" class="wide-imu" />

<div class="card-grid-2 mt-3">
<div v-click class="course-card teal">Level: nearly all the stationary reading lies on z.</div>
<div v-click class="course-card violet">Rolled 30°: the same 1 g signal has both y and z components.</div>
</div>
<div v-click class="takeaway">The robot’s axes rotate; gravity stays vertical. The components tell us the tilt.</div>

<!--
Front view, looking backward along x. Positive roll rotates y toward z by the right-hand rule. For a pure +30-degree roll, ay=g sin(30)=0.50g and az=g cos(30)=0.87g, with ax=0. The upward teal arrow is the measured specific force, opposite the actual downward gravity arrow.
-->

---
glowSeed: 589
---

# From acceleration to roll and pitch

<div class="card-grid-2 mt-5">
<div v-click class="course-card teal">
<div class="card-label">Roll · φ · rotation about x</div>

$$\phi=\operatorname{atan2}(a_y,a_z)$$

For (0, 0.50g, 0.87g): <strong>roll ≈ 30°</strong>.
</div>
<div v-click class="course-card violet">
<div class="card-label">Pitch · θ · rotation about y</div>

$$\theta=\operatorname{atan2}\!\left(-a_x,\sqrt{a_y^2+a_z^2}\right)$$

For (−0.50g, 0, 0.87g): <strong>pitch ≈ 30°</strong>.
</div>
</div>
<p class="imu-caption">Convention: x forward, y left, z up; level a<sub>z</sub> = +g. Right-hand rotations; atan2 returns radians.</p>
<div v-click class="takeaway">Works when gravity dominates: hold still or move gently. Driving acceleration and vibration distort tilt estimates.</div>
<p class="imu-caption">Gravity alone cannot reveal yaw: turning on a level table leaves (a<sub>x</sub>, a<sub>y</sub>, a<sub>z</sub>) ≈ (0, 0, g).</p>

<!--
These are standard roll/pitch extraction equations for this stated specific-force convention and yaw-pitch-roll ordering. Pitch is limited to ±90 degrees; roll becomes ambiguous near vertical pitch. Convert radians to degrees with math.degrees. In a right-handed x-forward/y-left/z-up frame, positive pitch is nose down. Adapt signs to the actual board mounting. Derivation reference: https://www.nxp.com/docs/en/application-note/AN3461.pdf
-->

---
glowSeed: 592
---

# Magnetometer: a digital compass

<div class="imu-columns">
<div>
<div v-click class="course-card violet"><div class="card-label">Magnetic field · <span style="text-transform:none">m<sub>x</sub>, m<sub>y</sub>, m<sub>z</sub></span></div>Measures Earth’s magnetic field along three axes. Its horizontal direction provides a reference for <strong>yaw</strong>.</div>
<p>Yaw is rotation about the vertical axis: which way the robot faces.</p>
<p>Use roll and pitch to compensate for tilt when the robot is not level.</p>
<div v-click class="takeaway">Calibrate the compass. Motors, magnets, and nearby steel can distort heading.</div>
</div>
<ImuDiagram mode="compass" />
</div>

<!--
The field sensor is the magnetometer; software converts its vector into compass heading. Magnetic north differs from true north. The sketch shows heading magnitude; compass bearings conventionally increase clockwise, whereas right-handed yaw with z up increases counterclockwise. Do not silently mix the signs. Reference: https://www.vectornav.com/resources/inertial-navigation-primer/theory-of-operation/theory-gpsins
-->

---
glowSeed: 595
---

# An IMU combines complementary senses

<div class="card-grid-3 mt-6">
<div v-click class="course-card violet"><div class="card-label">Gyroscope</div><strong>Fast rotation changes</strong><p>Integrate rates to track orientation. Small errors accumulate.</p></div>
<div v-click class="course-card teal"><div class="card-label">Accelerometer</div><strong>Gravity reference</strong><p>Correct roll and pitch drift when gravity dominates.</p></div>
<div v-click class="course-card blue"><div class="card-label">Magnetometer</div><strong>Heading reference</strong><p>Correct yaw drift when the magnetic field is reliable.</p></div>
</div>
<div v-click class="takeaway">Sensor fusion combines these measurements into a better orientation estimate.</div>
<p class="imu-caption"><strong>6-axis IMU:</strong> gyro + accelerometer. <strong>9-axis package:</strong> adds a magnetometer for heading.</p>
<p class="imu-caption">Two sensor types track motion and tilt; the third anchors yaw. An IMU alone does not give drift-free position on a map.</p>

<!--
IMU means Inertial Measurement Unit. A typical IMU has a 3-axis gyro and a 3-axis accelerometer; a magnetometer is optional and often called a 9-axis IMU package. The fusion system may be called an AHRS. With only gyro and accelerometer, yaw remains relative and drifts. Full 3D fusion handles coupled rotations, often using quaternions; our earlier scalar sum taught the one-axis idea. Reference: https://www.vectornav.com/resources/detail/what-is-an-inertial-measurement-unit
-->

---
glowSeed: 587
---

# Ultrasonic vs. IMU

<div class="card-grid-2 mt-7">
  <div v-click class="course-card teal">
    <div class="card-label">Ultrasonic</div>
    <div class="text-xl font-bold">Distance in cm</div>
    <ul class="sensor-comparison-list">
      <li>Uses sound + echo timing</li>
      <li>Changes near objects</li>
      <li>Looks primarily forward</li>
    </ul>
  </div>
  <div v-click class="course-card violet">
    <div class="card-label">IMU heading</div>
    <div class="text-xl font-bold">Angle in degrees</div>
    <ul class="sensor-comparison-list">
      <li>Uses internal motion sensing</li>
      <li>Changes when the robot turns</li>
      <li>Moves with the robot</li>
    </ul>
  </div>
</div>

<!--
Use this as a quick verbal check. Ask which value should change when the robot slides straight toward a wall, and which should change when it rotates in place. Both readings update continuously.
-->

---
glowSeed: 603
---

# Estimating position: what do we know?

<div class="card-grid-3 mt-6 position-comparison">
<div v-click class="course-card orange">
<div class="card-label">1 · Wheel voltage + time</div>
<div class="text-xl font-bold">Predict motion</div>
<p>Use a model to turn voltage into expected wheel speed, then speed × time into travel.</p>
<p><strong>Weakness:</strong> load, battery, or a stalled wheel can make actual motion differ.</p>
</div>
<div v-click class="course-card violet">
<div class="card-label">2 · Wheel encoders</div>
<div class="text-xl font-bold">Measure wheel travel</div>
<p>Convert measured wheel rotation into distance. Combine both wheels to estimate the path.</p>
<p><strong>Weakness:</strong> wheel slip and wheel-size errors accumulate in the position estimate.</p>
</div>
<div v-click class="course-card teal">
<div class="card-label">3 · Range finder + IMU</div>
<div class="text-xl font-bold">Relate motion to the world</div>
<p>Measure distance to a wall or landmark and estimate which way the robot faces.</p>
<p><strong>Weakness:</strong> one range + heading does not uniquely locate the robot in 2D.</p>
</div>
</div>
<div v-click class="takeaway">Toward a known wall: range constrains distance to the wall; IMU supplies orientation. Add landmarks or odometry to track the full path.</div>

<!--
Compare the same task: estimate how far the robot moved toward a wall. Voltage is a command rather than a position measurement. Encoders observe actual wheel motion, but not wheel slip. A range finder observes the environment, and IMU orientation helps interpret the measurement direction. For a beam perpendicular to a known wall, range directly gives distance to that wall, but position along the wall remains unknown. General localization requires known geometry or a map and enough independent observations. These sources are complementary and can be combined. Source: https://www.roboticsbook.org/S52_diffdrive_actions.html
-->

---
layout: center
class: text-center
glowSeed: 619
---

# Sense the world. Sense yourself.

<div v-click class="takeaway max-w-3xl mx-auto mt-10">Distance supports obstacle avoidance. Heading supports precise turns. Today, build intuition for both.</div>

<!--
Close by linking each sensor to future behaviors. Transition to the lab consoles and remind students to move the robot gently by hand before driving it under power.
-->
