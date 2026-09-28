<script setup lang="ts">
defineProps<{ mode: 'gyro' | 'riemann' | 'axes' | 'tilt' | 'compass' }>()
const heights = [80, 120, 152, 164, 152, 120, 80, 52]
</script>

<template>
  <svg class="imu-diagram" :viewBox="mode === 'tilt' ? '0 0 840 235' : '0 0 440 340'" role="img" :aria-label="({gyro:'Top view of a robot rotating about z',riemann:'Angular velocity curve with left endpoint Riemann rectangles; area is angle change',axes:'Robot body axes and opposite gravity and specific force arrows',tilt:'Level and rolled accelerometer readings resolved into y and z components',compass:'Magnetic north and robot heading in top view'})[mode]">
    <defs>
      <marker :id="`imu-arrow-${mode}`" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto-start-reverse"><path d="M0 0L8 4L0 8Z" fill="context-stroke" /></marker>
    </defs>
    <g v-if="mode === 'gyro'">
      <text x="220" y="28" text-anchor="middle">Top view · level robot</text>
      <g class="gyro-robot-spin">
      <rect x="169" y="115" width="102" height="125" rx="18" class="robot" />
      <rect x="153" y="139" width="16" height="76" rx="5" class="wheel" /><rect x="271" y="139" width="16" height="76" rx="5" class="wheel" />
      <path d="M220 140L208 162H232Z" fill="#eef6ff" />
      <circle cx="220" cy="185" r="10" fill="none" stroke="#eef6ff" stroke-width="2" /><circle cx="220" cy="185" r="3" fill="#eef6ff" />
      </g>
      <path d="M327 231A115 115 0 1 0 107 162" class="arrow purple" :marker-end="`url(#imu-arrow-${mode})`" />
      <text x="220" y="65" text-anchor="middle" class="purple-text">ω<tspan baseline-shift="sub" font-size="12">z</tspan> = +30°/s</text>
      <text x="220" y="285" text-anchor="middle">z points out of the screen</text>
      <text x="220" y="315" text-anchor="middle" class="muted">Positive turn: counterclockwise</text>
    </g>
    <g v-else-if="mode === 'riemann'">
      <text x="25" y="25">Angular velocity ω (°/s)</text>
      <path d="M52 48V255H411" class="axis" />
      <rect v-for="(h,i) in heights" :key="i" :x="60+i*40" :y="255-h" width="40" :height="h" fill="#2dd4bf" fill-opacity=".24" stroke="#2dd4bf" stroke-width="1.5" />
      <path d="M60 175Q80 154 100 135T140 103T180 91T220 103T260 135T300 175T340 203T380 215" fill="none" stroke="#93c5fd" stroke-width="4" />
      <circle v-for="(h,i) in heights" :key="i" :cx="60+i*40" :cy="255-h" r="3.5" fill="#e0f2fe" />
      <text x="32" y="261">0</text><text x="307" y="288">Time t (s)</text>
      <path d="M180 270H220" stroke="#fbbf24" stroke-width="2" /><text x="200" y="290" text-anchor="middle" class="amber-text">Δtᵢ</text>
      <text x="238" y="63" class="blue-text">changing rate</text>
      <path d="M280 69L260 122" stroke="#93c5fd" />
      <text x="219" y="218" text-anchor="middle" class="teal-text">area ≈ Σ ωᵢ Δtᵢ</text>
      <text x="220" y="326" text-anchor="middle" class="muted">(°/s) × s = degrees of rotation</text>
    </g>
    <g v-else-if="mode === 'axes'">
      <path d="M115 165L237 117L331 175L206 230Z" class="robot" />
      <path d="M115 165V191L206 256L331 198V175M206 230V256" fill="none" stroke="#60a5fa" stroke-width="3" />
      <g class="arrow" :marker-end="`url(#imu-arrow-${mode})`">
        <path d="M218 182L350 124" stroke="#93c5fd" /><path d="M218 182L86 99" stroke="#c4b5fd" /><path d="M218 182V49" stroke="#2dd4bf" />
      </g>
      <text x="305" y="105" class="blue-text">x forward</text><text x="29" y="78" class="purple-text">y left</text><text x="230" y="52" class="teal-text">z up</text>
      <path d="M372 168V270" class="arrow" stroke="#fbbf24" :marker-end="`url(#imu-arrow-${mode})`" />
      <text x="347" y="300" class="amber-text">gravity</text>
      <text x="33" y="302" class="teal-text">At rest: a = (0, 0, +g)</text>
      <text x="220" y="330" text-anchor="middle" class="muted">Measured force is opposite gravity.</text>
    </g>
    <g v-else-if="mode === 'tilt'">
      <g v-for="(cx,i) in [195,615]" :key="cx" :transform="`translate(${cx} 145)`">
        <text x="0" y="-122" text-anchor="middle">{{ i === 0 ? 'Level · front view' : '+30° roll · front view' }}</text>
        <g :transform="`rotate(${i === 0 ? 0 : -30})`">
          <rect x="-78" y="-10" width="156" height="25" rx="6" class="robot" />
          <path d="M0 0H115M0 0V-97" fill="none" stroke="#94a3b8" stroke-width="2" />
          <text x="122" y="6">y</text><text x="8" y="-87">z</text>
          <g v-if="i===1" stroke="#c4b5fd" stroke-width="2" stroke-dasharray="5 4" fill="none"><path d="M0 0H47.5V-82.3H0" /></g>
        </g>
        <path d="M0 0V-95" class="arrow" stroke="#2dd4bf" :marker-end="`url(#imu-arrow-${mode})`" />
        <text x="12" y="-66" class="teal-text">1 g</text>
        <path d="M-140 -55V22" class="arrow" stroke="#fbbf24" :marker-end="`url(#imu-arrow-${mode})`" /><text x="-167" y="45" class="amber-text">gravity</text>
        <text x="0" y="78" text-anchor="middle">a<tspan baseline-shift="sub" font-size="12">y</tspan>{{ i===0 ? ' = 0,  a' : ' = 0.50 g,  a' }}<tspan baseline-shift="sub" font-size="12">z</tspan>{{ i===0 ? ' = 1 g' : ' = 0.87 g' }}</text>
      </g>
    </g>
    <g v-else>
      <text x="220" y="26" text-anchor="middle">Top view · compass heading</text>
      <circle cx="220" cy="183" r="112" fill="none" stroke="#475569" stroke-width="2" />
      <path d="M220 183V50" class="arrow" stroke="#2dd4bf" :marker-end="`url(#imu-arrow-${mode})`" />
      <text x="232" y="60" class="teal-text">Magnetic N</text>
      <path d="M220 183L309 94" class="arrow purple" :marker-end="`url(#imu-arrow-${mode})`" />
      <path d="M220 112A71 71 0 0 1 270 133" fill="none" stroke="#fbbf24" stroke-width="3" />
      <text x="242" y="103" class="amber-text">45°</text>
      <g transform="translate(220 183) rotate(45)"><rect x="-27" y="-26" width="54" height="70" rx="9" class="robot" /><path d="M0 -18L-8 -4H8Z" fill="#eef6ff" /></g>
      <text x="333" y="190">E</text><text x="96" y="190">W</text><text x="214" y="318">S</text>
      <text x="220" y="338" text-anchor="middle" class="muted">A reference for heading drift</text>
    </g>
  </svg>
</template>

<style scoped>
.imu-diagram { width: 100%; max-height: 340px; align-self: center; }
.gyro-robot-spin { transform-origin:220px 185px; animation:gyro-turn 12s linear infinite; }
@keyframes gyro-turn { from { transform:rotate(0deg); } to { transform:rotate(-360deg); } }
@media (prefers-reduced-motion:reduce) { .gyro-robot-spin { animation:none; } }
text { fill:#eef6ff; font: 17px 'DM Sans',sans-serif; }
tspan { font-size:12px !important; }
.robot { fill:#0f172a; stroke:#60a5fa; stroke-width:3; }
.wheel { fill:#334155; stroke:#94a3b8; }
.arrow { fill:none; stroke-width:3; }
.axis { fill:none; stroke:#94a3b8; stroke-width:2; }
.purple { stroke:#c4b5fd; }
.purple-text { fill:#c4b5fd; }
.teal-text { fill:#5eead4; }
.blue-text { fill:#93c5fd; }
.amber-text { fill:#fbbf24; }
.muted { fill:#cbd5e1; font-size:15px; }
</style>
