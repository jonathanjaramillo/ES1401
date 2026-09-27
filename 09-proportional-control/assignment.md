# Session 9 Lab — Proportional Line Following

## Learning Objectives

By the end of this lab, you will be able to:

1. Measure a continuous "error" value from the XRP's line/reflectance sensor (how far off-line you are), instead of just a left/right on-off reading.
2. Compute a turn amount that scales proportionally to that error (`turn = Kp * error`).
3. Tune a proportional constant (Kp) by trial and error to make the robot's line-following motion visibly smoother than bang-bang control.

## Materials

- Your SparkFun XRP robot kit (rover, line/reflectance sensor, motors)
- The web-based MicroPython editor
- Your **bang-bang line follower code from Session 8** (you'll be modifying it, so keep a backup copy!)
- The same line-follow test loop/track used in Session 8, so you can compare directly

## Starter Code

Below is a skeleton to get you going. It assumes `read_line_error()` returns a single number representing how far off-line the sensor is (negative = drifted left, positive = drifted right, 0 = centered). If your reflectance sensor gives you raw left/right readings instead, you'll compute this error yourself in Step 2.

```python
from XRP import XRP

xrp = XRP.default_XRP()

# --- TUNE THIS! Start small and adjust based on testing ---
Kp = 0.5   # placeholder proportional constant — you WILL change this

BASE_SPEED = 0.3   # forward speed, keep constant for now

def read_line_error():
    """
    Returns a number describing how far off the line we are.
    Negative = line is to our left, Positive = line is to our right, 0 = centered.
    Replace this with real sensor math in Step 2.
    """
    left_val = xrp.reflectance.get_left()
    right_val = xrp.reflectance.get_right()
    error = right_val - left_val   # simple starting point, refine this!
    return error

while True:
    error = read_line_error()
    turn = Kp * error              # <-- the core proportional control idea

    left_speed = BASE_SPEED - turn
    right_speed = BASE_SPEED + turn

    xrp.drivetrain.set_effort(left_speed, right_speed)
```

## Step-by-Step Instructions

**Step 1 — Reload and re-baseline (2 min)**
Open your Session 8 bang-bang line follower. Run it once on the test loop so you (and your lab partner) remember what "jittery" looks like. Keep this file open in a second tab for comparison.

**Step 2 — Measure a real error value (10 min)**
Instead of just checking "is the sensor on the line, yes/no," read the actual sensor values from your reflectance sensor(s) and compute a number that represents *how far* off-line you are, not just which direction.
- If you have two reflectance sensors (left/right), a simple error is `error = right_reading - left_reading`.
- If you have a single sensor or an array, look at how strong/weak the reflectance signal is compared to a "centered" baseline value, and use that difference as your error.
- Print your error value to the console while manually sliding the robot side to side over the line, to confirm it changes smoothly (not just jumping between two values).

**Step 3 — Turn the error into a turn amount (10 min)**
Add the line `turn = Kp * error` to your control loop. Apply `turn` by subtracting it from one wheel's speed and adding it to the other's (see starter code). Start with a small Kp (like 0.3–0.5) so you don't get wild behavior on your first run.

**Step 4 — Run it and observe (10 min)**
Place the robot on the test loop and run your code. Watch closely:
- Does it follow the line at all?
- Is the motion smoother than bang-bang, or still jerky?
- Does it lose the line on curves?

**Step 5 — Tune Kp by trial and error (15–20 min)**
Adjust Kp up or down and re-run:
- If the robot drifts off the line slowly and doesn't correct enough → **increase** Kp.
- If the robot overshoots, oscillates, or zig-zags again → **decrease** Kp.
- Keep a quick log (on paper or in comments) of which Kp values you tried and what happened, so you can find your best value systematically rather than randomly.

**Step 6 — Compare side-by-side (5 min)**
Run your Session 8 bang-bang code and your new proportional code back-to-back on the same loop. Discuss with your lab partner: what's different about the motion? Where does proportional control clearly win, and are there any places bang-bang still seems fine?

## What Success Looks Like

- Your robot completes the same test loop used in Session 8 without losing the line.
- Compared to your bang-bang run, the motion is **visibly smoother** — fewer sharp zig-zags, more gentle curving corrections, especially on the straightaways.
- You can point to a specific Kp value you landed on and explain (in plain language) why a higher or lower value made things worse.
- Your code clearly shows the `turn = Kp * error` calculation, not just left/right if-statements.

## Stretch Goal (Early Finishers)

Pick one:

- **Speed challenge:** Time yourself on a full smooth lap and try to increase `BASE_SPEED` while retuning Kp to keep the robot stable at the higher speed. How fast can you go before it starts losing the line?
- **Sharper curves:** Add a section of tighter curves or a hairpin turn to your test loop. Does your current Kp still work, or do you need a different value for sharp turns vs. straightaways? (No need to solve this perfectly — just observe and note what you'd try next.)
