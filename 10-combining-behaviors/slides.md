---
theme: default
title: Session 10 — Combining Behaviors
---

# Combining Behaviors
### Session 10 · Week 4

- From single tricks to a real robot "brain"
- Kickoff: the Final Project!

Speaker notes:
Welcome back! Quick recap: over the last few weeks your XRP has learned to follow a line (Session 9) and to sense obstacles with the ultrasonic sensor (Sessions 5-6). Today we stop treating those as separate party tricks. We're going to combine them into ONE program that makes decisions — and then I'm going to hand you the final project, which you'll build over today and next session. Let's go.

---

# Why Combine Behaviors?

- Real robots juggle MULTIPLE senses at once
- A line-follower that ignores obstacles will crash
- Good robots ask: "What do I sense RIGHT NOW, and what should I do about it?"
- This is the core idea behind all autonomous robots — cars, vacuums, drones

Description: Simple side-by-side icon row — a line-following-only robot icon with a red "X" crashing into a box, next to a "combined behavior" robot icon that stops/turns before the box with a green checkmark.

Speaker notes:
Think about a robot vacuum. It's not JUST following walls, and it's not JUST avoiding obstacles — it's constantly checking several senses and switching behavior. If your XRP only knows how to follow a line, it'll happily drive straight into a box sitting on the line. Today's goal is to make your robot smart enough to notice the box and react. That reaction could be stopping, or steering around it — you'll decide based on your project.

---

# The Core Tool: if / else

- You already know `if` / `else` from Session 5-6 obstacle logic
- Combining behaviors = wrapping your line-follow loop in a decision
- Pattern:
  - **IF** obstacle detected → stop or turn
  - **ELSE** → keep following the line
- This check happens every loop, over and over (that's the "loop" in `while True:`)

Description: Simple SVG flowchart: Start → Read Sensors → "Obstacle Detected?" diamond → (Yes: Stop/Turn arrow) / (No: Keep Following Line arrow) → both arrows loop back up to Read Sensors.

Speaker notes:
The good news: you don't need new syntax today. You already know if/else and you already know while True loops. The trick is nesting: inside your main loop, first check the ultrasonic sensor. If it sees something close, handle that. Otherwise, fall through to your normal line-following code. Every single pass through the loop, the robot re-checks — that's what makes it feel "alive" and responsive instead of running a fixed script.

---

# Example Pattern (Pseudocode)

```
while True:
    distance = get_ultrasonic_distance()
    if distance < 10:  # cm, obstacle close!
        stop_motors()
        # or: turn away, then resume
    else:
        follow_line()  # your Session 9 code
```

- Order matters: check obstacle FIRST, then fall back to line-following
- Keep each behavior as its own function — easier to combine and debug

Speaker notes:
Notice this is barely different from what you wrote weeks ago. get_ultrasonic_distance and follow_line are functions you likely already have — we're just deciding, each loop, which one to trust. A tip that will save you real debugging time: write follow_line() and check_obstacle() as separate functions first, test each alone, THEN combine them. Trying to write it all combined from scratch is where most bugs sneak in.

---

# Sequencing vs. Deciding

- **Sequencing**: do A, then B, then C — a fixed order (Session 2 style)
- **Deciding**: choose WHICH behavior based on what sensors say, live
- Most real solutions mix both: "follow line UNTIL obstacle, THEN do a sequence of turn-avoid-rejoin"
- You'll likely need both this week

Description: Two small horizontal timelines side by side — top one labeled "Sequencing" showing fixed boxes A→B→C with solid arrows; bottom one labeled "Deciding" showing a branching diamond with two paths that reconnect, labeled "if/else."

Speaker notes:
Quick vocabulary check, because you'll use both words with your teammates today. Sequencing is just "do this, then this, then this" — like a recipe. Deciding is "check something, then choose." Going around an obstacle is actually BOTH: you decide to leave the line only when you sense something close, but then the "go around it" part might be a fixed sequence — turn right, drive forward, turn left, look for the line again. That's totally fine and often the simplest working solution.

---

# 🚀 The Final Project

- **Goal**: build a robot behavior for a course combining line-following AND obstacle handling
- **Teams**: 2-3 students
- **Timeline**: today (plan + start combining code) → Session 11 (build/iterate) → Session 12 (Demo Day!)
- Your team picks ONE challenge type — details in the handout

Description: Simple graphic of a course layout — a curvy taped line on the floor with one box/obstacle placed across it partway, and a small robot icon at the start, with a "FINISH" flag at the end.

Speaker notes:
Here's the big news: today kicks off your final project, worth a significant chunk of your grade, due in two sessions at our Demo Day. In teams of 2 or 3, you'll build a robot program that runs an obstacle-and-line course we set up in the room. I'll hand out the official rules sheet now — go ahead and grab it. The short version: your robot needs to follow a taped line, and when it hits an obstacle, it needs to either stop cleanly or navigate around it and get back on the line. You have creative freedom in exactly how, as long as you meet the rubric on the handout.

---

# Today's Lab: Project Kickoff

- Get into your teams, read the challenge rules handout
- Sketch a plan / pseudocode BEFORE touching code — what will your robot do, step by step?
- Start combining your Session 9 line-following code with Session 5-6 obstacle code
- Ask: what should happen at the obstacle? Stop? Turn? Which way?

Speaker notes:
For the rest of today: form your teams, read through the rules handout together, and sketch your plan on paper first — literally draw or write out the steps, including your if/else decision points, before you open the editor. Then start merging your existing line-follow and obstacle-detection code into one file using today's pattern. I'll be walking around to help. Don't worry about getting it perfect today — Session 11 is entirely for building and debugging. Today is about a solid plan and a first combined draft. Let's get moving!
