<script setup>
import { samplePath, bellCurve } from '../services/course-art.mjs'
// The home page scene: a lecture page with its study tools around it.
const curve = samplePath(bellCurve(212, 30, 146, 196), 150, 274, 40)
</script>

<template>
  <svg class="hero-art" viewBox="0 0 420 320" aria-hidden="true" focusable="false">
    <path class="hero-blob" d="M58 172 C40 96 112 34 206 40 C300 46 384 92 378 176 C372 262 290 296 200 290 C110 284 74 248 58 172 Z" />
    <g class="hero-dots">
      <circle v-for="i in 20" :key="i" :cx="318 + ((i - 1) % 5) * 11" :cy="40 + Math.floor((i - 1) / 5) * 11" r="2" />
    </g>

    <!-- Lecture page -->
    <g class="hero-float hero-float-1">
      <rect class="hero-shadow" x="122" y="78" width="184" height="184" rx="16" />
      <rect class="hero-card" x="116" y="70" width="184" height="184" rx="16" />
      <rect class="hero-accent" x="136" y="90" width="64" height="9" rx="4.5" />
      <rect class="hero-line" x="136" y="108" width="140" height="6" rx="3" />
      <rect class="hero-line" x="136" y="120" width="116" height="6" rx="3" />
      <rect class="hero-panel" x="136" y="136" width="144" height="70" rx="10" />
      <path class="hero-curve" :d="curve" />
      <path class="hero-axis" d="M148 196 H276" />
      <rect class="hero-line" x="136" y="218" width="132" height="6" rx="3" />
      <rect class="hero-line" x="136" y="230" width="96" height="6" rx="3" />
    </g>

    <!-- Formula card -->
    <g class="hero-float hero-float-2">
      <rect class="hero-card tone-lam" x="40" y="96" width="92" height="64" rx="12" />
      <text class="hero-formula" x="86" y="137" text-anchor="middle">∇f(x)</text>
    </g>

    <!-- Flashcards -->
    <g class="hero-float hero-float-3">
      <rect class="hero-card-soft tone-hong" x="290" y="176" width="86" height="58" rx="10" transform="rotate(8 333 205)" />
      <rect class="hero-card" x="282" y="182" width="86" height="58" rx="10" />
      <rect class="hero-line" x="296" y="198" width="44" height="6" rx="3" />
      <rect class="hero-line" x="296" y="210" width="30" height="6" rx="3" />
      <circle class="hero-check-bg tone-ngoc" cx="348" cy="222" r="10" />
      <path class="hero-check" d="M343 222 l4 4 l7 -8" />
    </g>

    <!-- Knowledge graph -->
    <g class="hero-float hero-float-2">
      <path class="hero-edge" d="M300 70 L340 92 M300 70 L284 40 M340 92 L366 64" />
      <circle class="hero-node tone-tim" cx="300" cy="70" r="9" />
      <circle class="hero-node-soft" cx="340" cy="92" r="7" />
      <circle class="hero-node-soft" cx="284" cy="40" r="6" />
      <circle class="hero-node-soft" cx="366" cy="64" r="5.5" />
    </g>

    <!-- Focus timer -->
    <g class="hero-float hero-float-3">
      <circle class="hero-card" cx="88" cy="224" r="32" />
      <circle class="hero-timer-track" cx="88" cy="224" r="22" />
      <path class="hero-timer tone-vang" d="M88 202 A22 22 0 1 1 66.6 229" />
      <circle class="hero-timer-dot" cx="88" cy="224" r="3" />
    </g>
  </svg>
</template>
