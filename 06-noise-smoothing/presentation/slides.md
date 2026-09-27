---
theme: default
highlighter: shiki
css: unocss
colorSchema: dark
title: 'Noise & Smoothing'
info: |
  Week 2, Session 6 — Making sensor decisions more reliable
transition: fade-out
lineNumbers: false
drawings:
  persist: false
mdc: true
vite:
  server:
    fs:
      strict: false
glowSeed: 606
layout: center
class: text-center
---

<div class="deck-kicker">Week 2 · Session 6</div>

# Noise & Smoothing

<div v-click class="takeaway max-w-3xl mx-auto mt-10">A filter turns a stream of measurements into a signal we can use.</div>

<!--
Ask: if a robot is standing still, should its distance reading change? Use the answer to introduce measurement noise, then preview the three filters students will implement today.
-->

---
layout: two-cols
layoutClass: gap-8
glowSeed: 623
---

# Real sensors are jumpy

<div class="space-y-4 mt-5">
  <div v-click class="course-card teal"><div class="card-label">Expected</div>A stationary robot should report one constant distance.</div>
  <div v-click class="course-card red"><div class="card-label">Measured</div>6.0, 6.3, 5.8, 6.1, 6.4 inches…</div>
  <div v-click class="course-card amber"><div class="card-label">Why</div>Echo paths, electronics, vibration, and quantization vary slightly.</div>
</div>

::right::

<div class="diagram-frame mt-3">
  <ConceptDiagram mode="noise" />
</div>

<!--
The underlying distance can be steady while the reported values bounce. This happens in phones, cars, medical devices, and robots.
-->

---
glowSeed: 640
---

# A threshold turns noise into behavior

<div class="equation-card text-center max-w-2xl mx-auto mt-6">

$$
\text{stop if } d < 6\text{ in}
$$

</div>

<div class="card-grid-2 mt-6">
  <div v-click class="course-card amber">
    <div class="card-label">One low glitch</div>
    Robot may stop early even though the wall is still far away.
  </div>
  <div v-click class="course-card red">
    <div class="card-label">One high glitch</div>
    Robot may continue even though the wall is already close.
  </div>
</div>

<div v-click class="takeaway">The filter should match the decision we need to make.</div>

<!--
Connect the raw signal to behavior. A threshold makes one bad sample visible as a mistake. Filtering reduces that sensitivity, but each filter makes a different trade-off.
-->

---
glowSeed: 652
---

# Three filters, three kinds of memory

<div class="card-grid-3 mt-7">
  <div v-click class="course-card teal">
    <div class="card-label">Moving average</div>
    Remembers a fixed window of recent samples.
    <div class="filter-tag mt-4">Good for isolated jitter</div>
  </div>
  <div v-click class="course-card blue">
    <div class="card-label">Low-pass</div>
    Remembers one previous output and follows slow changes.
    <div class="filter-tag mt-4">Good for a stable estimate</div>
  </div>
  <div v-click class="course-card violet">
    <div class="card-label">High-pass</div>
    Remembers the previous input and output to keep changes.
    <div class="filter-tag mt-4">Good for detecting motion</div>
  </div>
</div>

<div v-click class="takeaway mt-8">The code is short. The important question is what information each filter keeps.</div>

<!--
Set up the lesson as three different memories. Students will see that “smoothing” is not one algorithm: the desired signal determines the filter.
-->

---
glowSeed: 668
---

# Moving average: keep a window

<div class="equation-card text-center max-w-3xl mx-auto mt-5">

$$
\bar{x}_k = \frac{1}{N}\sum_{i=0}^{N-1} x_{k-i}
$$

<div class="text-sm opacity-75">Average the newest N readings; start with N = 5.</div>
</div>

<div class="card-grid-3 mt-6">
  <div v-click class="course-card teal"><div class="card-label">1 · Add</div>Append the newest reading.</div>
  <div v-click class="course-card blue"><div class="card-label">2 · Drop</div>Remove the oldest reading.</div>
  <div v-click class="course-card violet"><div class="card-label">3 · Average</div>Use the window’s mean.</div>
</div>

<div v-click class="takeaway mt-7">A single extreme sample is diluted by several nearby measurements.</div>

<!--
Use a physical analogy: write five numbers on sticky notes. Each new note pushes the oldest one out. The moving average has a clear window and a predictable delay.
-->

---
glowSeed: 680
---

# Moving average in Python

<div class="grid grid-cols-[1.2fr_0.8fr] gap-6 mt-5">
  <div class="course-card">

```python
recent = []

def moving_average(new_value, window=5):
    recent.append(new_value)
    if len(recent) > window:
        recent.pop(0)
    return sum(recent) / len(recent)

distance = moving_average(read_distance())
```

  </div>
  <div class="space-y-4">
    <div v-click class="course-card teal"><div class="card-label">Input</div>One raw reading.</div>
    <div v-click class="course-card blue"><div class="card-label">Memory</div>Only the newest five.</div>
    <div v-click class="course-card orange"><div class="card-label">Output</div>One smoothed value.</div>
  </div>
</div>

<!--
Walk through the function in add–drop–average order. During startup the list contains fewer than five samples, so dividing by len(recent) avoids a special empty-window case.
-->

---
glowSeed: 692
---

# Window size is a trade-off

<div class="card-grid-3 mt-7">
  <div v-click class="course-card amber">
    <div class="card-label">Small window</div>
    <div class="text-3xl font-bold">N = 2</div>
    <div class="mt-3">Fast response, still jumpy.</div>
  </div>
  <div v-click class="course-card teal">
    <div class="card-label">Starting point</div>
    <div class="text-3xl font-bold">N = 5</div>
    <div class="mt-3">Useful balance for today’s lab.</div>
  </div>
  <div v-click class="course-card blue">
    <div class="card-label">Large window</div>
    <div class="text-3xl font-bold">N = 20</div>
    <div class="mt-3">Very smooth, slower to react.</div>
  </div>
</div>

<div v-click class="takeaway mt-8">Smoothing removes jitter by accepting a little delay.</div>

<!--
Make the design trade-off explicit. A large window can lag behind a rapidly approaching wall, so N is a design choice rather than a magic number.
-->

---
glowSeed: 704
---

# First-order low-pass: one remembered value

<div class="equation-card text-center max-w-3xl mx-auto mt-5">

$$
y_k = y_{k-1} + \alpha(x_k - y_{k-1})
$$

<div class="text-sm opacity-75">Move the old output a fraction α of the way toward the new input.</div>
</div>

<div class="card-grid-3 mt-6">
  <div v-click class="course-card teal"><div class="card-label">α = 0.1</div>Very calm, slow response.</div>
  <div v-click class="course-card blue"><div class="card-label">α = 0.2</div>A useful starting point.</div>
  <div v-click class="course-card orange"><div class="card-label">α = 0.8</div>Fast response, more noise.</div>
</div>

<div v-click class="takeaway mt-7">This is exponential smoothing: recent samples matter most, and old samples fade away.</div>

<!--
Read the equation as an update rule: error = input minus old output; correction = alpha times error. Alpha is between zero and one. A low alpha behaves like a heavy, slow object; a high alpha follows the input quickly.
-->

---
glowSeed: 716
---

# Low-pass filter in Python

<div class="grid grid-cols-[1.25fr_0.75fr] gap-6 mt-5">
  <div class="course-card">

```python
last_filtered = read_distance()  # initial state
alpha = 0.2

while robot_is_running:
    new_reading = read_distance()
    last_filtered += alpha * (new_reading - last_filtered)
    distance = last_filtered
```

  </div>
  <div class="space-y-4">
    <div v-click class="course-card teal"><div class="card-label">State</div>Store only the previous output.</div>
    <div v-click class="course-card blue"><div class="card-label">Update</div>Correct toward the new reading.</div>
    <div v-click class="course-card orange"><div class="card-label">Startup</div>Use the first sample as the initial estimate.</div>
  </div>
</div>

<!--
Point out the key implementation difference: no list and no sum. The filter remembers one value, then nudges it toward each new sensor reading.
-->

---
glowSeed: 722
---

# Watch a low-pass filter work

<div class="filter-demo-layout">
  <div class="plot-frame">
    <img class="filter-plot" src="/range_low_pass_demo.png" alt="Noisy simulated range sensor data and a low-pass filtered estimate" />
  </div>
  <div class="space-y-4">
    <div v-click class="course-card"><div class="card-label">Raw sensor</div>Jumps around the true range and occasionally glitches.</div>
    <div v-click class="course-card teal"><div class="card-label">Low-pass output</div>Follows the approach while ignoring most fast wiggles.</div>
    <div v-click class="course-card amber"><div class="card-label">Trade-off</div>The estimate is calmer, but it lags behind a changing wall.</div>
  </div>
</div>

<!--
Point to the gray raw trace, dashed true range, and teal filtered trace. Connect the plot directly to the previous code: every new reading nudges last_filtered a little closer to the sensor value.
-->

---
glowSeed: 728
---

# Choosing α from the sample time

<div class="sample-time-grid">
  <div class="equation-card text-center">

$$
\alpha = \frac{\Delta t}{\tau + \Delta t}
$$

<span class="text-sm opacity-75">τ is the response time you want.</span>
  </div>
  <div class="course-card">
    <div class="card-label">Example</div>
    <div class="text-xl font-bold">Read every 0.1 s, choose τ = 0.4 s</div>
    <div class="text-3xl font-bold text-teal-300 mt-3">α = 0.2</div>
    <div class="mt-3 opacity-80">If the loop timing changes, recompute α from the actual Δt.</div>
  </div>
</div>

<div v-click class="takeaway mt-7">Use α to tune by feel; use τ when you want the tuning to match real time.</div>

<!--
This gives students a practical way to choose alpha without turning the lesson into a continuous-time controls lecture. The approximation is the standard simple discrete first-order filter.
-->

---
glowSeed: 740
---

# First-order high-pass: keep the change

<div class="equation-card text-center max-w-3xl mx-auto mt-5">

$$
y_k = \beta\left(y_{k-1} + x_k - x_{k-1}\right)
$$

<div class="text-sm opacity-75">The new input minus the old input is the change to keep.</div>
<div class="text-sm opacity-75 mt-2">For the same response time, choose β = τ / (τ + Δt).</div>
</div>

<div class="card-grid-3 mt-6">
  <div v-click class="course-card violet"><div class="card-label">Steady input</div>xₖ − xₖ₋₁ ≈ 0, so output fades toward zero.</div>
  <div v-click class="course-card blue"><div class="card-label">Rising input</div>Positive output: something changed upward.</div>
  <div v-click class="course-card red"><div class="card-label">Falling input</div>Negative output: something changed downward.</div>
</div>

<div v-click class="takeaway mt-7">A high-pass filter is useful for detecting motion, edges, bumps, or sudden changes.</div>

<!--
Contrast the low-pass goal with the high-pass goal. The high-pass output is not a better distance estimate; it is a change signal. A steady wall should eventually produce nearly zero.
-->

---
glowSeed: 752
---

# High-pass filter in Python

<div class="grid grid-cols-[1.25fr_0.75fr] gap-6 mt-5">
  <div class="course-card">

```python
last_reading = read_distance()  # previous input
last_change = 0.0               # previous output
beta = 0.8

while robot_is_running:
    new_reading = read_distance()
    last_change = beta * (last_change + new_reading - last_reading)
    last_reading = new_reading
    change = last_change
```

  </div>
  <div class="space-y-4">
    <div v-click class="course-card violet"><div class="card-label">Remember</div>Previous input and previous output.</div>
    <div v-click class="course-card blue"><div class="card-label">Subtract</div>Current input − previous input.</div>
    <div v-click class="course-card orange"><div class="card-label">Use</div>Trigger an event when change is large.</div>
  </div>
</div>

<!--
Trace one update by hand: if x goes from 6.0 to 6.5, x - x_prev is positive. If x stays at 6.5, that difference becomes zero and the stored output decays.
-->

---
glowSeed: 758
---

# Use high-pass output to detect collisions

<div class="filter-demo-layout">
  <div class="plot-frame">
    <img class="filter-plot" src="/accelerometer_high_pass_demo.png" alt="Simulated accelerometer collision and high-pass output" />
  </div>
  <div class="space-y-4">
    <div v-click class="course-card"><div class="card-label">Raw accelerometer</div>Slow drift can cross the raw threshold before the collision.</div>
    <div v-click class="course-card violet"><div class="card-label">High-pass output</div>Slow drift fades near zero; the collision spike stands out.</div>
    <div v-click class="course-card amber"><div class="card-label">Decision</div>Trigger when <code>abs(change) &gt; threshold</code>.</div>
  </div>
</div>

<!--
Point out that the raw threshold crosses during slow drift, before the collision. The high-pass output suppresses that low-frequency motion, so the threshold responds to the brief impulse instead.
-->

---
layout: two-cols
layoutClass: gap-8
glowSeed: 764
---

# What survives each filter?

<div class="diagram-frame mt-3">
  <FilterComparison />
</div>

::right::

<div class="space-y-3 mt-2">
  <div v-click class="course-card"><div class="card-label">Raw</div>Noise and the real signal are mixed together.</div>
  <div v-click class="course-card teal"><div class="card-label">Moving average</div>Fixed window; corners and delay are easy to see.</div>
  <div v-click class="course-card blue"><div class="card-label">Low-pass</div>Slow shape survives; fast wiggles are reduced.</div>
  <div v-click class="course-card violet"><div class="card-label">High-pass</div>Steady level disappears; changes become visible.</div>
</div>

<!--
Use the same imagined input in every row. The moving average and low-pass both smooth, but their shapes differ. The high-pass row is intentionally not a smoothed distance: it is a signal about change.
-->

---
glowSeed: 776
---

# Which filter fits the question?

<div class="filter-table mt-6">
  <div class="filter-table-row filter-table-head"><div>Question</div><div>Filter</div><div>Why</div></div>
  <div v-click class="filter-table-row"><div>“What is the current distance?”</div><div class="text-teal-300 font-bold">Low-pass</div><div>Stable estimate with one small state.</div></div>
  <div v-click class="filter-table-row"><div>“What was the recent average?”</div><div class="text-cyan-300 font-bold">Moving average</div><div>Simple, visible window of samples.</div></div>
  <div v-click class="filter-table-row"><div>“Did something change?”</div><div class="text-violet-300 font-bold">High-pass</div><div>Steady background fades away.</div></div>
</div>

<div v-click class="takeaway mt-7">Choose the output you need first. Then choose the filter that preserves it.</div>

<!--
Ask students to name the output before naming the algorithm. This keeps filter choice connected to a robot behavior rather than treating equations as isolated recipes.
-->

---
glowSeed: 788
---

# Lab: run all three on the same readings

<div class="grid grid-cols-[1fr_1fr] gap-6 mt-6">
  <div class="course-card red">
    <div class="card-label">Raw trial</div>
    <div class="text-xl font-bold">Stop on the raw distance.</div>
    <div class="mt-3">Repeat several times. Record where the robot stops.</div>
  </div>
  <div class="course-card teal">
    <div class="card-label">Filtered trial</div>
    <div class="text-xl font-bold">Stop on the low-pass distance.</div>
    <div class="mt-3">Try α = 0.2, then adjust it and explain the result.</div>
  </div>
</div>

<div class="card-grid-3 mt-6">
  <div v-click class="course-card blue"><div class="card-label">Moving average</div>Compare N = 2 and N = 5.</div>
  <div v-click class="course-card violet"><div class="card-label">High-pass</div>Print the change signal while the robot moves.</div>
  <div v-click class="course-card orange"><div class="card-label">Evidence</div>Plot raw, filtered, and stopping points.</div>
</div>

<div v-click class="equation-card text-center max-w-2xl mx-auto mt-6">

$$
\text{drive while } \text{filtered distance} \ge 6\text{ in}
$$

</div>

<!--
Students should first experience raw behavior, then change only the signal used in the condition. The high-pass output is for observation and event detection, not for replacing the distance estimate.
-->

---
layout: center
class: text-center
glowSeed: 800
---

# Filter the signal for the decision

<div class="takeaway max-w-3xl mx-auto mt-10">
  Moving average keeps a window.<br>
  Low-pass keeps the slow trend.<br>
  High-pass keeps the change.
</div>

<!--
Close by asking students to explain each filter without looking at the equations. The implementation is short because the design choice came first.
-->
