# Session 11 Assignment — Debugging & Iterating (Build/Iterate Lab)

**Week 4, Session 11 of 12**

## Learning Objectives

By the end of today's lab, you should be able to:

1. Apply a systematic debugging process (isolate → print & observe → change one thing → retest) to a real robot behavior, instead of making random changes and hoping.
2. Use `print()` statements to verify sensor readings match your assumptions before changing logic.
3. Test a simplified version of a problem before testing it inside the full challenge course.

This session is **not** about learning new robot skills — you already have everything you need (line-following, obstacle detection, turning, from Sessions 9–10). Today is entirely about making your existing code work *reliably*.

---

## The Debugging Checklist

When something isn't working, work through this checklist in order. Don't skip ahead.

- [ ] **1. Name the exact behavior that's failing.** Not "the robot is broken" — something specific, like "the robot loses the line after the second turn."
- [ ] **2. Isolate it.** Can you reproduce this one behavior on its own, without running the whole course?
- [ ] **3. Print the relevant sensor values.** Add `print()` statements for whatever the robot is "deciding" from — reflectance sensor, distance sensor, gyro heading — and watch the values as the robot runs.
- [ ] **4. Compare expected vs. actual.** Is the sensor reading what you assumed it would? Is your threshold/condition actually matching that reading?
- [ ] **5. Change ONE thing.** One number, one condition, one line. Not several at once.
- [ ] **6. Retest immediately** on the isolated/simplified version.
- [ ] **7. Did it help?** If yes, move on to the next issue. If no, revert that change and try a different single change. If it's unclear, retest again — noise can make one run misleading.
- [ ] **8. Once the piece works reliably (3 times in a row), reintegrate it** into the fuller sequence and retest.

Repeat this loop for each behavior that isn't working yet.

---

## Suggested Approach for Today's Session

1. **Recap (5 min):** As a team, list every behavior your final program needs to handle (e.g., follow line, detect obstacle, go around obstacle, re-find line, handle a curve, stop at finish). Mark each one: Working / Flaky / Not Working.
2. **Test in isolation first (majority of session):** For each "Flaky" or "Not Working" item, build or use a simplified test setup (a short taped line segment, a single obstacle) and debug it on its own using the checklist above. Do **not** test fixes by running the entire course each time — it's slower and harder to interpret.
3. **Reintegrate one piece at a time:** Once a behavior is reliable in isolation, add it back into your combined program and re-run the *relevant section* of the course (not necessarily the whole thing yet) to confirm it still works alongside the other behaviors.
4. **Run the full course:** Once individual pieces are solid, attempt the complete challenge course start to finish.
5. **Iterate on full-course attempts:** After each full run, note exactly where it broke (if it did), and treat that as a new isolated debugging target — back to step 2 for that specific spot.
6. **Log your fixes:** Keep a short running note (comments in your code or a scratch doc) of what you changed and what effect it had. This will help you avoid re-trying things that already failed, and it's useful prep for demo day.

---

## What "Success" Looks Like Today

By the end of the session, aim for this checkpoint:

- Your robot completes the **full challenge course reliably in at least 2 of your last 3 attempts.**
- You can explain, for any remaining rough spot, *what* is going wrong (e.g., "it loses the line if the turn is sharp") — even if you haven't fully fixed it yet. Diagnosed-but-unfixed is real progress.
- Your code doesn't rely on one "lucky" run — you've retested enough times to know the behavior is consistent, not a fluke.

This is a checkpoint, not a final grade — you'll have more iteration time before demo day. The goal today is to leave with a robot that's *meaningfully more reliable* than when you started, and a clear list of what's still left to fix.

---

## If Your Team Is Stuck

It's normal to hit a wall today — don't sit stuck on the same issue for too long.

- **After ~10–15 minutes stuck on the same bug**, flag down the instructor or a TA. Bring your printed sensor values with you — "here's what we're seeing" is much easier to help with than "it's not working."
- **Use office hours** this week if you need more time than lab provides.
- **Simplify your scope if needed.** A robot that reliably follows the line and reliably stops for one obstacle is a strong result. It is completely fine to scale back an overly ambitious feature (e.g., handling two obstacles in a row) in order to make the core behaviors rock-solid. Reliable-and-simple beats ambitious-and-flaky for demo day.
- **Ask teammates on other teams** what worked for similar bugs — comparing notes is encouraged.
