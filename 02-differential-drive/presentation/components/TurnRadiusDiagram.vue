<template>
  <svg class="diagram turn-radius-diagram" viewBox="0 0 620 430" role="img" aria-labelledby="turn-radius-title turn-radius-desc">
    <title id="turn-radius-title">Differential-drive turning geometry</title>
    <desc id="turn-radius-desc">A robot turns left around an instantaneous center of curvature. The left wheel follows a smaller circle and the faster right wheel follows a larger circle.</desc>

    <defs>
      <marker id="radius-arrow" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto">
        <path d="M0,0 L8,4 L0,8 Z" fill="#60a5fa" />
      </marker>
      <marker id="speed-arrow" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto">
        <path d="M0,0 L8,4 L0,8 Z" fill="#2dd4bf" />
      </marker>
    </defs>

    <!-- Concentric paths traced by the two wheels and the robot center. -->
    <path class="wheel-path inner" d="M365 288 A265 265 0 0 0 309 125" />
    <path class="center-path" d="M430 288 A330 330 0 0 0 360 85" />
    <path class="wheel-path outer" d="M495 288 A395 395 0 0 0 411 45" />

    <!-- The shared turn angle, measured at the ICC. -->
    <path class="radius-ray" d="M100 288 H430" />
    <path class="radius-ray faint" d="M100 288 L360 85" />
    <path class="angle" d="M154 288 A54 54 0 0 0 143 255" />
    <text class="angle-label" x="166" y="263">Δθ</text>

    <circle class="icc" cx="100" cy="288" r="9" />
    <text class="label" x="100" y="323">ICC</text>
    <text class="small" x="100" y="344">turn center</text>

    <text class="radius-label" x="252" y="274">R</text>
    <text class="path-label inner-label" x="274" y="115">left path</text>
    <text class="path-label outer-label" x="462" y="39">right path</text>

    <!-- Robot, facing upward and turning left. -->
    <g class="robot-group">
      <rect class="robot" x="385" y="225" width="90" height="126" rx="17" />
      <rect class="wheel" x="354" y="247" width="22" height="82" rx="7" />
      <rect class="wheel" x="484" y="247" width="22" height="82" rx="7" />
      <path class="nose" d="M430 236 L417 258 H443 Z" />

      <path class="speed short" d="M365 240 V178" />
      <path class="speed" d="M495 240 V135" />
      <text class="speed-label" x="365" y="162">vL</text>
      <text class="speed-label" x="495" y="119">vR</text>
    </g>

    <!-- Wheel spacing. -->
    <path class="dimension" d="M365 369 V390 M365 381 H495 M495 369 V390" />
    <text class="dimension-label" x="430" y="413">wheel spacing b</text>

    <text class="formula inner-formula" x="238" y="374">R − b/2</text>
    <text class="formula outer-formula" x="547" y="374">R + b/2</text>
  </svg>
</template>

<style scoped>
.turn-radius-diagram { overflow: visible; }
.wheel-path,
.center-path,
.radius-ray,
.angle,
.speed,
.dimension {
  fill: none;
  stroke-linecap: round;
}
.wheel-path { stroke-width: 4; stroke-dasharray: 10 9; }
.wheel-path.inner { stroke: #fbbf24; }
.wheel-path.outer { stroke: #2dd4bf; }
.center-path { stroke: #60a5fa; stroke-width: 3; stroke-dasharray: 5 8; opacity: .72; }
.radius-ray { stroke: #60a5fa; stroke-width: 3; stroke-dasharray: 8 7; marker-end: url(#radius-arrow); }
.radius-ray.faint { opacity: .38; marker-end: none; }
.angle { stroke: #a78bfa; stroke-width: 5; }
.icc { fill: #a78bfa; stroke: #ede9fe; stroke-width: 3; }
.robot { fill: #0f172a; stroke: #60a5fa; stroke-width: 4; }
.wheel { fill: #1e293b; stroke: #cbd5e1; stroke-width: 3; }
.nose { fill: #eef6ff; }
.speed { stroke: #2dd4bf; stroke-width: 5; marker-end: url(#speed-arrow); }
.speed.short { stroke: #fbbf24; }
.dimension { stroke: #cbd5e1; stroke-width: 2.5; }
text { fill: #eef6ff; font-family: "DM Sans", sans-serif; text-anchor: middle; font-weight: 700; }
.label { font-size: 18px; fill: #c4b5fd; }
.small { font-size: 13px; fill: #94a3b8; font-weight: 500; }
.radius-label { font-size: 24px; fill: #93c5fd; }
.angle-label { font-size: 20px; fill: #c4b5fd; }
.path-label { font-size: 15px; }
.inner-label { fill: #fcd34d; }
.outer-label { fill: #5eead4; }
.speed-label { font-size: 19px; fill: #eef6ff; font-style: italic; }
.dimension-label { font-size: 16px; fill: #cbd5e1; }
.formula { font-size: 16px; }
.inner-formula { fill: #fcd34d; }
.outer-formula { fill: #5eead4; }
</style>
