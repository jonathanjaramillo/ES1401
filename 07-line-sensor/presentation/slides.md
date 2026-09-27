---
theme: default
highlighter: shiki
css: unocss
colorSchema: dark
title: 'The Line Sensor'
info: |
  Week 3, Session 7 — Teaching the XRP to see the floor
transition: fade-out
lineNumbers: false
drawings:
  persist: false
mdc: true
vite:
  server:
    fs:
      strict: false
glowSeed: 707
layout: center
class: text-center
---

<div class="deck-kicker">Week 3 · Session 7</div>

# The Line Sensor

## Teaching your robot to see the floor

<div v-click class="takeaway max-w-3xl mx-auto mt-10">No camera required—just shine light down and measure what returns.</div>

<!--
Connect to previous distance sensing. Today’s sensor looks down, not forward, and it measures brightness rather than distance. This measurement becomes the foundation for line following.
-->

---
layout: two-cols
layoutClass: gap-8
glowSeed: 724
---

# What does reflectance mean?

<div class="space-y-4 mt-5">
  <div v-click class="course-card amber"><div class="card-label">Illuminate</div>A tiny LED shines light onto the floor.</div>
  <div v-click class="course-card blue"><div class="card-label">Detect</div>A nearby sensor measures returned light.</div>
  <div v-click class="course-card teal"><div class="card-label">Compare</div>Light surfaces return more; dark surfaces absorb more.</div>
</div>

::right::

<div class="diagram-frame mt-3">
  <ConceptDiagram mode="reflectance" />
</div>

<!--
Emphasize that the sensor does not form an image. It asks only how much emitted light came back. Point to the animated return rays: strong over a light floor, weak over dark tape.
-->

---
glowSeed: 740
---

# From light to a number

<div class="grid grid-cols-[1fr_1.4fr_1fr] gap-4 mt-8">
  <div v-click class="course-card red text-center"><div class="card-label">Dark tape</div><div class="text-5xl font-bold">120</div><div class="mt-2">low return</div></div>
  <div v-click class="course-card amber text-center"><div class="card-label">Gray zone</div><div class="text-5xl font-bold">?</div><div class="mt-2">depends on your setup</div></div>
  <div v-click class="course-card teal text-center"><div class="card-label">Light floor</div><div class="text-5xl font-bold">950</div><div class="mt-2">high return</div></div>
</div>

<div v-click class="takeaway mt-8">Room lighting, floor, tape, and sensor height all shift the values.</div>

<!--
Explain that some libraries scale readings from 0 to 1 and others from 0 to 1000. The direction—low for dark and high for light—is the mental model. Students must measure their own setup.
-->

---
glowSeed: 756
---

# Watch the signal live

<div class="grid grid-cols-[1.2fr_0.8fr] gap-6 mt-5">
  <div v-click class="course-card">

```python {1|3-5|all}
from XRPLib.defaults import *

while True:
    value = reflectance.get_left()
    print(value)
    time.sleep_ms(200)
```

  </div>
  <div class="space-y-4">
    <div v-click class="course-card teal"><div class="card-label">Floor</div>Reading rises.</div>
    <div v-click class="course-card red"><div class="card-label">Tape</div>Reading falls.</div>
    <div v-click class="course-card blue"><div class="card-label">Repeat</div>Look for two clusters.</div>
  </div>
</div>

<div class="mt-3 text-sm opacity-70 text-center">The short delay keeps the console readable.</div>

<!--
Walk through the loop. Students should slide the robot by hand over floor, tape, and floor again. They are looking for repeatable high and low clusters, not one exact number.
-->

---
glowSeed: 772
---

# Choose a threshold

<div class="equation-card text-center max-w-3xl mx-auto mt-6">

$$
T \approx \frac{R_{\text{dark}} + R_{\text{light}}}{2}
$$

</div>

<div class="card-grid-2 mt-6">
  <div v-click class="course-card red text-center"><div class="card-label">Below T</div><div class="text-2xl font-bold">ON dark line</div></div>
  <div v-click class="course-card teal text-center"><div class="card-label">Above T</div><div class="text-2xl font-bold">OFF dark line</div></div>
</div>

<div v-click class="takeaway">Flip the comparison for a light line on a dark floor.</div>

<!--
Use the midpoint as a practical starting threshold. If floor is near 900 and tape near 150, 500 separates them comfortably. Stress that their measured values, not the example numbers, determine the final threshold.
-->

---
glowSeed: 788
---

# Turn the threshold into a helper

<div class="grid grid-cols-2 gap-6 mt-6">
  <div v-click class="course-card">

```python
THRESHOLD = 500

def on_line():
    value = reflectance.get_left()
    return value < THRESHOLD
```

  </div>
  <div v-click class="course-card blue">
    <div class="card-label">Why a function?</div>
    <ul>
      <li>Gives the decision a clear name</li>
      <li>Keeps the threshold in one place</li>
      <li>Prepares for line-following logic</li>
    </ul>
  </div>
</div>

<div v-click class="takeaway mt-6">A continuous measurement becomes a simple True / False decision.</div>

<!--
Explain how abstraction helps: later code can ask on_line() without repeating sensor details. Students should still print the raw value while calibrating, then use the helper in behavior code.
-->

---
glowSeed: 804
---

# Today’s lab

<div class="card-grid-3 mt-8">
  <div v-click class="course-card teal"><div class="card-label">Measure</div>Record floor and tape ranges.</div>
  <div v-click class="course-card amber"><div class="card-label">Choose</div>Pick and test a threshold.</div>
  <div v-click class="course-card blue"><div class="card-label">Package</div>Write a reliable <code>on_line()</code>.</div>
</div>

<div v-click class="takeaway mt-8">Test in several spots—one reading is not calibration.</div>

<!--
Transition to lab. Students should sample multiple locations and lighting conditions, record ranges, choose a midpoint threshold, and verify the helper over repeated floor-to-tape transitions.
-->

---
layout: center
class: text-center
glowSeed: 820
---

# Read brightness. Decide line or floor.

<div v-click class="takeaway max-w-3xl mx-auto mt-10">Today’s one reliable measurement powers every line-following behavior that comes next.</div>

<!--
Close by previewing the next session: the robot will use this decision inside a feedback loop to steer itself. Move students to calibration strips and live consoles.
-->
