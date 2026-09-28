<template>
  <svg class="filter-comparison" viewBox="0 0 760 420" role="img" aria-label="Comparison of raw, moving average, low-pass, and high-pass signals">
    <defs>
      <linearGradient id="comparison-grid" x1="0" x2="1">
        <stop offset="0" stop-color="#334155" stop-opacity=".35" />
        <stop offset="1" stop-color="#475569" stop-opacity=".12" />
      </linearGradient>
    </defs>

    <g v-for="row in rows" :key="row.label" :transform="`translate(0 ${row.y})`">
      <rect x="152" y="0" width="574" height="76" rx="9" fill="url(#comparison-grid)" stroke="#334155" stroke-width="1" />
      <line x1="170" y1="38" x2="712" y2="38" stroke="#64748b" stroke-width="1" stroke-dasharray="5 7" opacity=".7" />
      <text class="row-label" x="136" y="44">{{ row.label }}</text>
      <path :d="row.path" fill="none" :stroke="row.color" stroke-width="5" stroke-linecap="round" stroke-linejoin="round" />
    </g>

    <text class="axis-label" x="435" y="414">time →</text>
    <text class="axis-note" x="170" y="410">quiet</text>
    <text class="axis-note" x="680" y="410">step + noise</text>
  </svg>
</template>

<script setup lang="ts">
const rows = [
  {
    label: 'raw input',
    y: 8,
    color: '#94a3b8',
    path: 'M170 39 L194 31 L218 45 L242 34 L266 49 L290 36 L314 47 L338 32 L362 44 L386 36 L410 48 L430 31 L442 49 L454 28 L466 45 L478 23 L490 48 L502 30 L514 43 L526 25 L538 40 L550 29 L562 45 L574 34 L586 48 L598 31 L610 43 L622 25 L634 40 L646 29 L658 45 L670 34 L682 40 L694 36 L712 38',
  },
  {
    label: 'moving avg',
    y: 101,
    color: '#2dd4bf',
    path: 'M170 39 C220 39 270 40 320 40 S400 40 420 39 C438 38 445 35 454 33 C470 29 482 25 496 22 C522 18 552 18 580 21 C612 24 650 30 680 35 C694 37 704 38 712 38',
  },
  {
    label: 'low-pass',
    y: 194,
    color: '#60a5fa',
    path: 'M170 39 C250 39 320 39 390 39 C414 39 428 38 440 36 C458 33 468 28 482 23 C502 17 526 16 550 18 C580 20 610 26 638 31 C666 35 692 38 712 39',
  },
  {
    label: 'high-pass',
    y: 287,
    color: '#a78bfa',
    path: 'M170 38 C250 38 330 38 400 38 C420 38 430 36 438 31 L448 48 L458 22 L468 51 L478 25 L488 47 C500 39 514 38 530 38 C570 38 610 38 650 38 C674 38 692 38 712 38',
  },
]
</script>

<style scoped>
.filter-comparison { width: 100%; max-height: 26rem; overflow: visible; }
text { fill: #eef6ff; font-family: "DM Sans", sans-serif; text-anchor: middle; }
.row-label { font-size: 16px; font-weight: 700; text-anchor: end; }
.axis-label { font-size: 17px; font-weight: 700; }
.axis-note { font-size: 13px; fill: #94a3b8; text-anchor: start; }
</style>
