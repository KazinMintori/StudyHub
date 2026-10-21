<script setup>
// Small scene illustrations for page headers and empty states.
defineProps({
  name: { type: String, required: true },
  tone: { type: String, default: 'tim' }
})
</script>

<template>
  <svg class="spot-art" :class="[`spot-${name}`, `tone-${tone}`]" viewBox="0 0 120 96" aria-hidden="true" focusable="false">
    <ellipse class="art-bg" cx="60" cy="52" rx="56" ry="40" />

    <g v-if="name === 'wiki'">
      <path class="art-node" d="M60 80 Q42 72 18 75 V33 Q42 30 60 39 Z" />
      <path class="art-node" d="M60 80 Q78 72 102 75 V33 Q78 30 60 39 Z" />
      <path class="art-edge thin" d="M25 44 Q40 41 53 47 M25 53 Q40 50 53 56 M25 62 Q40 59 53 65" />
      <path class="art-edge" d="M74 47 L88 41 M74 47 L86 60" />
      <circle class="art-fill" cx="74" cy="47" r="4.5" />
      <circle class="art-fill soft" cx="89" cy="40" r="3.5" />
      <circle class="art-fill soft" cx="87" cy="61" r="3.5" />
      <circle class="art-paper-ring" cx="94" cy="24" r="10" />
      <path class="art-ink" d="M101 31 L110 40" />
    </g>

    <g v-else-if="name === 'tools'">
      <rect class="art-fill soft" x="16" y="30" width="50" height="34" rx="6" transform="rotate(-10 41 47)" />
      <rect class="art-node" x="22" y="36" width="50" height="34" rx="6" />
      <path class="art-edge thin" d="M30 48 H60 M30 56 H52" />
      <path class="art-path" d="M56 61 l4 4 l8 -9" />
      <circle class="art-node" cx="88" cy="50" r="18" />
      <path class="art-fill" d="M88 50 V32 A18 18 0 0 1 104.3 57.6 Z" />
      <path class="art-ink" d="M88 50 V38 M88 50 L96 54 M84 27 H92" />
    </g>

    <g v-else-if="name === 'guide'">
      <path class="art-node" d="M18 28 L44 20 L72 28 L100 20 V70 L72 78 L44 70 L18 78 Z" />
      <path class="art-edge thin" d="M44 20 V70 M72 28 V78" />
      <path class="art-dash" d="M26 66 C36 52 50 64 58 50 S78 40 84 36" />
      <path class="art-fill" d="M86 18 a9 9 0 0 1 9 9 c0 7 -9 15 -9 15 s-9 -8 -9 -15 a9 9 0 0 1 9 -9 z" />
      <circle class="art-paper-dot" cx="86" cy="27" r="3.2" />
      <circle class="art-ink-fill" cx="26" cy="66" r="3" />
    </g>

    <g v-else-if="name === 'empty'">
      <rect class="art-dash-box" x="18" y="22" width="62" height="54" rx="8" />
      <path class="art-edge thin" d="M28 38 H62 M28 48 H54 M28 58 H58" opacity=".55" />
      <circle class="art-paper-ring" cx="78" cy="54" r="16" />
      <path class="art-ink thick" d="M90 66 L104 80" />
      <path class="art-path" d="M72 49 l12 10 M84 49 l-12 10" />
    </g>

    <g v-else-if="name === 'notfound'">
      <path class="art-dash" d="M10 86 C30 70 22 56 44 54 S66 66 70 46" />
      <path class="art-ink" d="M78 84 V30" />
      <path class="art-fill" d="M78 30 H106 L112 38 L106 46 H78 Z" />
      <path class="art-node" d="M78 50 H52 L46 58 L52 66 H78 Z" />
      <text class="art-on-fill-text" x="92" y="42" text-anchor="middle">?</text>
      <text class="art-ink-text" x="63" y="62" text-anchor="middle">?</text>
      <ellipse class="art-shadow" cx="78" cy="86" rx="12" ry="3" />
    </g>
  </svg>
</template>
