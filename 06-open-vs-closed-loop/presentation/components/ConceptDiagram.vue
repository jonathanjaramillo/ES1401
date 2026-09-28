<script setup lang="ts">
defineProps<{
  mode:
    | 'sense-plan-act'
    | 'drive'
    | 'open-loop'
    | 'encoder'
    | 'ultrasonic'
    | 'noise'
    | 'reflectance'
    | 'feedback'
    | 'combine'
    | 'debug'
    | 'demo'
}>()
</script>

<template>
  <svg class="diagram concept-diagram" viewBox="0 0 760 330" role="img" :aria-label="`${mode} concept diagram`">
    <defs>
      <marker id="arrow-teal" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto">
        <path d="M0,0 L8,4 L0,8 Z" fill="#2dd4bf" />
      </marker>
      <marker id="arrow-blue" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto">
        <path d="M0,0 L8,4 L0,8 Z" fill="#60a5fa" />
      </marker>
      <linearGradient id="beam" x1="0" x2="1">
        <stop offset="0" stop-color="#22d3ee" stop-opacity=".55" />
        <stop offset="1" stop-color="#22d3ee" stop-opacity="0" />
      </linearGradient>
    </defs>

    <g v-if="mode === 'sense-plan-act'">
      <path class="flow" d="M228 83 C335 16 430 16 532 83" />
      <path class="flow delay-1" d="M570 122 C626 218 561 282 448 274" />
      <path class="flow delay-2" d="M313 274 C191 282 132 210 190 122" />
      <g class="node"><circle cx="190" cy="103" r="63" /><text x="190" y="97">SENSE</text><text class="small" x="190" y="122">read the world</text></g>
      <g class="node blue"><circle cx="570" cy="103" r="63" /><text x="570" y="97">PLAN</text><text class="small" x="570" y="122">choose an action</text></g>
      <g class="node orange"><circle cx="380" cy="263" r="63" /><text x="380" y="257">ACT</text><text class="small" x="380" y="282">change the world</text></g>
    </g>

    <g v-else-if="mode === 'drive'">
      <g v-for="(x, i) in [130, 380, 630]" :key="x" :transform="`translate(${x} 160)`">
        <rect class="robot" x="-55" y="-62" width="110" height="124" rx="18" />
        <rect class="wheel" x="-72" y="-43" width="18" height="86" rx="7" />
        <rect class="wheel" x="54" y="-43" width="18" height="86" rx="7" />
        <path d="M0 -46 L-11 -27 H11 Z" fill="#eef6ff" />
        <g v-if="i === 0" class="move-straight">
          <path class="motion" d="M-63 75 V-105" /><path class="motion" d="M63 75 V-105" />
        </g>
        <g v-else-if="i === 1">
          <path class="motion short" d="M-63 65 V-50" /><path class="motion" d="M63 75 V-105" />
          <path class="guide" d="M-20 113 C-95 40 -93 -55 -23 -112" />
        </g>
        <g v-else class="spin">
          <path class="motion" d="M-63 -72 V72" /><path class="motion" d="M63 72 V-72" />
          <path class="guide" d="M-5 -104 A104 104 0 1 1 -8 104" />
        </g>
      </g>
      <text class="label" x="130" y="310">equal → straight</text>
      <text class="label" x="380" y="310">different → curve</text>
      <text class="label" x="630" y="310">opposite → spin</text>
    </g>

    <g v-else-if="mode === 'open-loop'">
      <g class="card-svg"><rect x="45" y="62" width="210" height="92" rx="16" /><text x="150" y="101">PROGRAM</text><text class="small" x="150" y="126">“forward for 2 s”</text></g>
      <path class="flow" d="M266 108 H474" />
      <g class="card-svg blue"><rect x="487" y="62" width="228" height="92" rx="16" /><text x="601" y="101">MOTORS</text><text class="small" x="601" y="126">execute blindly</text></g>
      <path class="broken" d="M600 172 C560 275 223 275 160 172" />
      <g class="cross"><path d="M365 240 l30 30 M395 240 l-30 30" /></g>
      <text class="label red-text" x="380" y="310">no measurement returns to the program</text>
    </g>

    <g v-else-if="mode === 'encoder'">
      <g transform="translate(246 164)">
        <g class="encoder-wheel">
          <circle class="wheel-disc" r="105" />
          <g>
            <path v-for="n in 16" :key="n" d="M0 -99 V-76" :transform="`rotate(${n * 22.5})`" />
          </g>
          <circle r="24" fill="#0f172a" stroke="#60a5fa" stroke-width="6" />
        </g>
      </g>
      <rect class="sensor" x="342" y="143" width="52" height="42" rx="8" />
      <path class="pulse" d="M395 164 H444" />
      <g class="card-svg"><rect x="466" y="83" width="238" height="164" rx="18" /><text x="585" y="126">COUNT TICKS</text><text class="big-number" x="585" y="181">1440</text><text class="small" x="585" y="216">ticks ≈ 1 rotation</text></g>
    </g>

    <g v-else-if="mode === 'ultrasonic'">
      <g transform="translate(105 165)"><rect class="robot" x="-42" y="-62" width="84" height="124" rx="14" /><rect class="wheel" x="-57" y="-42" width="15" height="84" rx="6" /><rect class="wheel" x="42" y="-42" width="15" height="84" rx="6" /><circle cx="42" cy="-17" r="7" fill="#22d3ee" /><circle cx="42" cy="17" r="7" fill="#22d3ee" /></g>
      <path d="M150 113 L615 54 V276 L150 217 Z" fill="url(#beam)" />
      <g class="ping"><path d="M175 108 Q250 165 175 222" /><path d="M226 91 Q325 165 226 239" /><path d="M288 73 Q414 165 288 257" /></g>
      <rect x="635" y="42" width="44" height="246" rx="8" fill="#334155" stroke="#94a3b8" stroke-width="3" />
      <path class="measure" d="M160 287 H630" />
      <text class="label" x="395" y="318">distance = speed × round-trip time ÷ 2</text>
    </g>

    <g v-else-if="mode === 'noise'">
      <line x1="62" y1="271" x2="713" y2="271" class="axis" />
      <line x1="62" y1="45" x2="62" y2="271" class="axis" />
      <path class="raw-trace" d="M62 80 L90 112 L118 72 L146 127 L174 102 L202 151 L230 122 L258 168 L286 137 L314 189 L342 171 L370 210 L398 182 L426 228 L454 201 L482 247 L510 217 L538 252 L566 231 L594 267 L622 245 L650 276 L682 252 L712 272" />
      <path class="smooth-trace" d="M62 91 C135 99 185 123 240 142 S344 185 405 205 S522 234 585 249 S663 263 712 268" />
      <g class="legend"><line x1="472" y1="64" x2="520" y2="64" class="raw-trace" /><text x="532" y="70">raw</text><line x1="472" y1="94" x2="520" y2="94" class="smooth-trace" /><text x="532" y="100">moving average</text></g>
    </g>

    <g v-else-if="mode === 'reflectance'">
      <rect x="70" y="246" width="260" height="36" rx="5" fill="#e2e8f0" />
      <rect x="430" y="246" width="260" height="36" rx="5" fill="#111827" stroke="#64748b" />
      <g v-for="x in [150, 510]" :key="x">
        <rect class="sensor" :x="x" y="52" width="100" height="52" rx="10" />
        <circle :cx="x + 25" cy="78" r="10" fill="#fbbf24" />
        <circle :cx="x + 75" cy="78" r="10" fill="#22d3ee" />
        <path class="light-ray" :d="`M${x + 25} 90 L${x + 12} 234 M${x + 25} 90 L${x + 74} 234`" />
      </g>
      <g class="bounce"><path d="M162 234 L225 112" /><path d="M212 234 L248 120" /><path class="faint" d="M522 234 L578 150" /></g>
      <text class="label" x="200" y="316">light floor → high return</text>
      <text class="label" x="560" y="316">dark tape → low return</text>
    </g>

    <g v-else-if="mode === 'feedback'">
      <path class="flow" d="M235 87 C335 24 430 24 525 87" />
      <path class="flow delay-1" d="M564 126 C611 224 548 282 445 270" />
      <path class="flow delay-2" d="M316 270 C206 282 148 217 194 126" />
      <g class="node"><circle cx="194" cy="105" r="59" /><text x="194" y="100">SENSE</text><text class="small" x="194" y="124">measurement</text></g>
      <g class="node blue"><circle cx="566" cy="105" r="59" /><text x="566" y="100">COMPARE</text><text class="small" x="566" y="124">find error</text></g>
      <g class="node orange"><circle cx="380" cy="260" r="59" /><text x="380" y="255">ACT</text><text class="small" x="380" y="279">correct</text></g>
    </g>

    <g v-else-if="mode === 'combine'">
      <g class="card-svg"><rect x="40" y="111" width="160" height="84" rx="14" /><text x="120" y="145">READ</text><text class="small" x="120" y="170">both sensors</text></g>
      <path class="flow" d="M211 153 H290" />
      <g class="decision"><path d="M380 72 L474 153 L380 234 L286 153 Z" /><text x="380" y="145">OBSTACLE</text><text class="small" x="380" y="170">close?</text></g>
      <path class="flow blue-line" d="M474 123 C530 75 575 68 615 84" />
      <path class="flow" d="M474 184 C530 231 575 240 615 223" />
      <g class="card-svg blue"><rect x="604" y="42" width="126" height="74" rx="14" /><text x="667" y="74">YES</text><text class="small" x="667" y="97">avoid</text></g>
      <g class="card-svg"><rect x="604" y="206" width="126" height="74" rx="14" /><text x="667" y="238">NO</text><text class="small" x="667" y="261">follow line</text></g>
      <path class="return-flow" d="M667 291 C665 323 120 328 120 207" />
    </g>

    <g v-else-if="mode === 'debug'">
      <path class="flow" d="M236 72 C326 22 432 22 522 72" />
      <path class="flow delay-1" d="M587 127 C618 211 566 268 494 286" />
      <path class="flow delay-2" d="M421 304 C324 322 218 295 171 228" />
      <path class="flow delay-3" d="M153 157 C149 106 183 80 211 68" />
      <g class="mini-node"><circle cx="200" cy="93" r="48" /><text x="200" y="99">ISOLATE</text></g>
      <g class="mini-node blue"><circle cx="560" cy="93" r="48" /><text x="560" y="91">PRINT</text><text class="tiny" x="560" y="110">& OBSERVE</text></g>
      <g class="mini-node orange"><circle cx="527" cy="258" r="48" /><text x="527" y="250">CHANGE</text><text class="tiny" x="527" y="270">ONE THING</text></g>
      <g class="mini-node violet"><circle cx="220" cy="258" r="48" /><text x="220" y="264">RETEST</text></g>
    </g>

    <g v-else>
      <g class="demo-robot">
        <rect class="robot" x="80" y="180" width="130" height="80" rx="18" />
        <circle class="wheel-disc" cx="110" cy="266" r="22" /><circle class="wheel-disc" cx="185" cy="266" r="22" />
        <circle cx="194" cy="203" r="8" fill="#22d3ee" />
      </g>
      <g class="finish"><rect x="562" y="58" width="11" height="237" fill="#e2e8f0" /><path d="M573 58 H696 V152 H573 Z" fill="#f8fafc" /><path d="M573 58 H614 V89 H573 Z M655 58 H696 V89 H655 Z M614 89 H655 V121 H614 Z M573 121 H614 V152 H573 Z M655 121 H696 V152 H655 Z" fill="#111827" /></g>
      <path class="road" d="M45 294 H716" />
      <g class="confetti"><path d="M255 56 l12 16 M322 34 l-5 20 M388 68 l18 -8 M454 32 l9 19 M512 72 l18 5" /></g>
      <text class="label teal-text" x="377" y="320">build → test → debug → demonstrate</text>
    </g>
  </svg>
</template>

<style scoped>
.concept-diagram { overflow: visible; }
text { fill: #eef6ff; font-family: "DM Sans", sans-serif; text-anchor: middle; font-weight: 700; font-size: 21px; }
text.small { font-size: 15px; font-weight: 500; fill: #cbd5e1; }
text.tiny { font-size: 13px; font-weight: 600; fill: #cbd5e1; }
text.label { font-size: 17px; font-weight: 650; }
text.big-number { font-size: 52px; fill: #2dd4bf; }
.red-text { fill: #fb7185; }
.teal-text { fill: #2dd4bf; }
.node circle, .mini-node circle { fill: rgba(13,148,136,.18); stroke: #2dd4bf; stroke-width: 3; }
.node.blue circle, .mini-node.blue circle, .card-svg.blue rect { fill: rgba(30,64,175,.22); stroke: #60a5fa; }
.node.orange circle, .mini-node.orange circle { fill: rgba(194,65,12,.20); stroke: #fb923c; }
.mini-node.violet circle { fill: rgba(109,40,217,.22); stroke: #a78bfa; }
.mini-node text { font-size: 14px; }
.flow, .return-flow { fill: none; stroke: #2dd4bf; stroke-width: 4; stroke-linecap: round; marker-end: url(#arrow-teal); stroke-dasharray: 10 10; animation: dash 1.7s linear infinite; }
.blue-line { stroke: #60a5fa; marker-end: url(#arrow-blue); }
.delay-1 { animation-delay: -.5s; }.delay-2 { animation-delay: -1s; }.delay-3 { animation-delay: -1.4s; }
.card-svg rect { fill: rgba(13,148,136,.14); stroke: #2dd4bf; stroke-width: 3; }
.robot { fill: #0f172a; stroke: #60a5fa; stroke-width: 4; }
.wheel { fill: #1e293b; stroke: #94a3b8; stroke-width: 3; }
.motion { fill: none; stroke: #2dd4bf; stroke-width: 5; marker-end: url(#arrow-teal); animation: pulse 1.4s ease-in-out infinite; }
.motion.short { stroke: #fbbf24; }
.guide { fill: none; stroke: #64748b; stroke-width: 3; stroke-dasharray: 8 7; marker-end: url(#arrow-blue); }
.spin { transform-origin: 0 0; animation: spin 4s linear infinite; }
.broken { fill: none; stroke: #fb7185; stroke-width: 4; stroke-dasharray: 12 10; }
.cross path { stroke: #fb7185; stroke-width: 8; stroke-linecap: round; }
.encoder-wheel { transform-origin: 0 0; animation: spin 5s linear infinite; }
.encoder-wheel path { stroke: #e2e8f0; stroke-width: 8; stroke-linecap: round; }
.wheel-disc { fill: #1e293b; stroke: #60a5fa; stroke-width: 4; }
.sensor { fill: #0f172a; stroke: #22d3ee; stroke-width: 3; }
.pulse { fill: none; stroke: #fbbf24; stroke-width: 6; stroke-dasharray: 9 9; animation: dash .8s linear infinite; }
.ping path { fill: none; stroke: #22d3ee; stroke-width: 4; opacity: .7; animation: echo 2.2s ease-in-out infinite; transform-origin: 150px 165px; }
.ping path:nth-child(2) { animation-delay: .25s; }.ping path:nth-child(3) { animation-delay: .5s; }
.measure { stroke: #e2e8f0; stroke-width: 2; stroke-dasharray: 7 7; }
.axis { stroke: #64748b; stroke-width: 2; }
.raw-trace { fill: none; stroke: #94a3b8; stroke-width: 3; opacity: .72; }
.smooth-trace { fill: none; stroke: #2dd4bf; stroke-width: 7; stroke-linecap: round; stroke-dasharray: 900; stroke-dashoffset: 900; animation: draw 3s ease-out forwards; }
.legend text { text-anchor: start; font-size: 15px; font-weight: 500; }
.light-ray { stroke: #fbbf24; stroke-width: 5; fill: none; opacity: .8; }
.bounce path { stroke: #22d3ee; stroke-width: 5; fill: none; marker-end: url(#arrow-blue); animation: pulse 1.5s ease-in-out infinite; }
.bounce .faint { opacity: .22; }
.bang-path { fill: none; stroke: #fb7185; stroke-width: 5; }
.proportional-path { fill: none; stroke: #2dd4bf; stroke-width: 6; }
.traveler.bang { fill: #fb7185; }.traveler.smooth { fill: #2dd4bf; }
.decision path { fill: rgba(245,158,11,.16); stroke: #fbbf24; stroke-width: 3; }
.return-flow { stroke: #a78bfa; marker-end: url(#arrow-blue); }
.demo-robot { animation: drive-across 4s ease-in-out infinite; }
.road { stroke: #64748b; stroke-width: 8; stroke-linecap: round; stroke-dasharray: 18 12; }
.confetti path { stroke: #fbbf24; stroke-width: 7; stroke-linecap: round; animation: pulse 1.2s ease-in-out infinite alternate; }
.wall { fill: #334155; stroke: #94a3b8; stroke-width: 3; }
.lane-floor { stroke: #94a3b8; stroke-width: 4; stroke-linecap: round; opacity: .4; }
.target-line { stroke: #fbbf24; stroke-width: 3; stroke-dasharray: 6 6; }
.wall-robot .robot { fill: #0f172a; stroke: #60a5fa; stroke-width: 4; }
.wall-robot .wheel { fill: #1e293b; stroke: #94a3b8; stroke-width: 3; }
.wall-robot.bang { animation: approach-bang 3.4s linear infinite; }
.wall-robot.prop { animation: approach-prop 3.4s cubic-bezier(.22, .68, .2, 1) infinite; }
.speed-graph { fill: none; stroke-width: 4; stroke-linecap: round; }
.speed-graph.bang { stroke: #fb7185; }
.speed-graph.prop { stroke: #2dd4bf; }
@keyframes approach-bang {
  0% { transform: translate(56px, 0); }
  78% { transform: translate(600px, 0); }
  82% { transform: translate(600px, 0) scale(1.12, .82); }
  100% { transform: translate(600px, 0); }
}
@keyframes approach-prop {
  0% { transform: translate(56px, 0); }
  100% { transform: translate(600px, 0); }
}
@keyframes dash { to { stroke-dashoffset: -40; } }
@keyframes pulse { 50% { opacity: .35; } }
@keyframes spin { to { transform: rotate(360deg); } }
@keyframes echo { 0%,100% { opacity: .1; transform: scale(.72); } 50% { opacity: .9; transform: scale(1.04); } }
@keyframes draw { to { stroke-dashoffset: 0; } }
@keyframes drive-across { 0% { transform: translateX(0); } 55%,100% { transform: translateX(320px); } }
@media (prefers-reduced-motion: reduce) {
  * { animation-duration: .001ms !important; animation-iteration-count: 1 !important; }
}
</style>
