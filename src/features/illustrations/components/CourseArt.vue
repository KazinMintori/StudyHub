<script setup>
import { computed } from 'vue'
import { resolveCourseArt, samplePath, bellCurve, bellBars, spiralPath, arrowBetween } from '../services/course-art.mjs'

const props = defineProps({
  course: { type: [Object, String], default: null },
  label: { type: String, default: '' }
})

const art = computed(() => resolveCourseArt(props.course))

const tree = {
  nodes: [
    { id: 'a', x: 80, y: 26, state: 'path' }, { id: 'b', x: 46, y: 58 }, { id: 'c', x: 114, y: 58, state: 'path' },
    { id: 'd', x: 28, y: 94 }, { id: 'e', x: 64, y: 94 }, { id: 'f', x: 96, y: 94, state: 'goal' }, { id: 'g', x: 132, y: 94 }
  ],
  edges: [['a', 'b'], ['a', 'c', 'path'], ['b', 'd'], ['b', 'e'], ['c', 'f', 'path'], ['c', 'g']]
}
const treeNode = id => tree.nodes.find(node => node.id === id)

const bars = bellBars()
const bell = samplePath(bellCurve(79.5, 19, 34, 100), 18, 141)
const pendulumWave = samplePath(x => 100 + 7 * Math.sin((x - 16) / 128 * 4 * Math.PI), 16, 144, 64)
const spiral = spiralPath(80, 46, 2.1, 2.7)

const network = (() => {
  const n = {
    a: { x: 80, y: 60, r: 15 }, b: { x: 34, y: 34, r: 8 }, c: { x: 126, y: 32, r: 10 },
    d: { x: 32, y: 92, r: 7 }, e: { x: 128, y: 92, r: 9 }, f: { x: 82, y: 14, r: 5.5 }
  }
  const links = [['b', 'a'], ['c', 'a'], ['d', 'a'], ['e', 'a'], ['f', 'c'], ['a', 'c'], ['b', 'd'], ['f', 'b']]
  return { nodes: n, arrows: links.map(([from, to]) => arrowBetween(n[from], n[to])) }
})()
</script>

<template>
  <svg
    class="course-art"
    :class="`tone-${art.tone}`"
    viewBox="0 0 160 120"
    :role="label ? 'img' : undefined"
    :aria-label="label || undefined"
    :aria-hidden="label ? undefined : 'true'"
    focusable="false"
  >
    <rect class="art-bg" x="0" y="0" width="160" height="120" rx="14" />
    <g class="art-dots">
      <circle v-for="i in 12" :key="i" :cx="132 + ((i - 1) % 4) * 7" :cy="100 + Math.floor((i - 1) / 4) * 7" r="1.3" />
    </g>

    <g v-if="art.motif === 'tree'">
      <line v-for="[from, to, kind] in tree.edges" :key="from + to" :class="kind ? 'art-path' : 'art-edge'"
        :x1="treeNode(from).x" :y1="treeNode(from).y" :x2="treeNode(to).x" :y2="treeNode(to).y" />
      <circle class="art-ring" cx="96" cy="94" r="14" />
      <circle v-for="node in tree.nodes" :key="node.id" :cx="node.x" :cy="node.y" r="9"
        :class="node.state ? 'art-fill' : 'art-node'" />
      <circle class="art-ink" cx="134" cy="22" r="8.5" />
      <path class="art-ink" d="M140 28 L148 36" />
    </g>

    <g v-else-if="art.motif === 'contour'">
      <g transform="rotate(-18 92 64)">
        <ellipse class="art-node" cx="92" cy="64" rx="60" ry="35" />
        <ellipse class="art-contour" cx="92" cy="64" rx="44" ry="25" />
        <ellipse class="art-contour strong" cx="92" cy="64" rx="28" ry="16" />
        <ellipse class="art-fill soft" cx="92" cy="64" rx="13" ry="7.5" />
      </g>
      <path class="art-ink" d="M22 28 L44 52 L56 38 L68 60 L78 52 L86 64 L92 64" />
      <circle v-for="[x, y] in [[22, 28], [44, 52], [56, 38], [68, 60], [78, 52], [86, 64]]" :key="x" class="art-ink-fill" :cx="x" :cy="y" r="2.6" />
      <circle class="art-fill" cx="92" cy="64" r="5" />
      <circle class="art-ring" cx="92" cy="64" r="9" />
    </g>

    <g v-else-if="art.motif === 'bell'">
      <rect v-for="bar in bars" :key="bar.x" :class="bar.core ? 'art-fill' : 'art-fill soft'" :x="bar.x" :y="bar.y" :width="bar.width" :height="bar.height" rx="2" />
      <path class="art-ink" :d="bell" />
      <path class="art-dash" d="M79.5 30 V100" />
      <path class="art-ink" d="M16 100 H144" />
      <rect class="art-node" x="18" y="14" width="26" height="26" rx="6" />
      <circle v-for="[x, y] in [[25, 21], [37, 21], [31, 27], [25, 33], [37, 33]]" :key="`${x}-${y}`" class="art-ink-fill" :cx="x" :cy="y" r="2.1" />
    </g>

    <g v-else-if="art.motif === 'table-chart'">
      <rect class="art-node" x="16" y="24" width="62" height="68" rx="5" />
      <path class="art-fill" d="M16 29 A5 5 0 0 1 21 24 H73 A5 5 0 0 1 78 29 V38 H16 Z" />
      <path class="art-edge thin" d="M16 51.5 H78 M16 65 H78 M16 78.5 H78 M36.7 38 V92 M57.3 38 V92" />
      <path class="art-path" d="M84 58 H98" />
      <path class="art-fill" d="M102 58 L95 53 L95 63 Z" />
      <path class="art-ink" d="M108 24 V92 H148" />
      <rect class="art-fill soft" x="114" y="70" width="8" height="22" rx="2" />
      <rect class="art-fill soft" x="126" y="56" width="8" height="36" rx="2" />
      <rect class="art-fill" x="138" y="40" width="8" height="52" rx="2" />
      <path class="art-ink" d="M118 62 L130 48 L142 32" />
    </g>

    <g v-else-if="art.motif === 'pendulum'">
      <path class="art-ink" d="M40 18 H100" />
      <path class="art-edge thin" d="M46 18 l-5 -6 M58 18 l-5 -6 M70 18 l-5 -6 M82 18 l-5 -6 M94 18 l-5 -6" />
      <path class="art-dash" d="M44 66 A54 54 0 0 0 96 66" />
      <path class="art-edge" d="M70 18 L46 66" opacity=".45" />
      <circle class="art-fill soft" cx="46" cy="66" r="9" />
      <path class="art-ink" d="M70 18 L94 66" />
      <circle class="art-fill" cx="94" cy="66" r="10" />
      <circle class="art-ink-fill" cx="70" cy="18" r="3" />
      <path class="art-path" :d="pendulumWave" />
    </g>

    <g v-else-if="art.motif === 'field'">
      <path class="art-edge" d="M61 60 H99" />
      <path class="art-edge" d="M58 52 Q80 30 102 52 M55 46 Q80 8 105 46 M58 68 Q80 90 102 68 M55 74 Q80 112 105 74" />
      <path class="art-edge" d="M39 60 H18 M41 52 L22 38 M41 68 L22 82 M121 60 H142 M119 52 L138 38 M119 68 L138 82" />
      <path class="art-fill" d="M80 26 l-5 -3 v6 z M80 94 l-5 -3 v6 z M84 60 l-5 -3 v6 z M30 60 l5 -3 v6 z M132 60 l-5 -3 v6 z" />
      <circle class="art-fill" cx="50" cy="60" r="11" />
      <path class="art-on-fill" d="M44.5 60 H55.5 M50 54.5 V65.5" />
      <circle class="art-ink-fill" cx="110" cy="60" r="11" />
      <path class="art-on-ink" d="M104.5 60 H115.5" />
    </g>

    <g v-else-if="art.motif === 'network'">
      <g v-for="(arrow, index) in network.arrows" :key="index">
        <path class="art-edge" :d="arrow.line" />
        <path class="art-edge-head" :d="arrow.head" />
      </g>
      <circle v-for="(node, key) in network.nodes" :key="key" :cx="node.x" :cy="node.y" :r="node.r"
        :class="key === 'a' ? 'art-fill' : key === 'c' ? 'art-fill soft' : 'art-node'" />
      <circle class="art-ring" cx="80" cy="60" r="20" />
    </g>

    <g v-else-if="art.motif === 'structures'">
      <rect v-for="i in 5" :key="i" :class="i === 3 ? 'art-fill' : 'art-node'" :x="20 + (i - 1) * 24" y="18" width="24" height="22" rx="3" />
      <path class="art-ink-fill" d="M80 50 l-5 6 h10 z" />
      <line class="art-edge" x1="80" y1="66" x2="54" y2="86" />
      <line class="art-edge" x1="80" y1="66" x2="106" y2="86" />
      <line class="art-edge" x1="54" y1="86" x2="40" y2="104" />
      <line class="art-edge" x1="54" y1="86" x2="68" y2="104" />
      <line class="art-edge" x1="106" y1="86" x2="120" y2="104" />
      <circle class="art-fill" cx="80" cy="66" r="7.5" />
      <circle v-for="[x, y] in [[54, 86], [106, 86], [40, 104], [68, 104], [120, 104]]" :key="`${x}-${y}`" class="art-node" :cx="x" :cy="y" r="7" />
    </g>

    <g v-else-if="art.motif === 'venn'">
      <circle class="art-venn" cx="64" cy="50" r="28" />
      <circle class="art-venn" cx="96" cy="50" r="28" />
      <circle class="art-venn" cx="80" cy="76" r="28" />
      <circle class="art-venn-line" cx="64" cy="50" r="28" />
      <circle class="art-venn-line" cx="96" cy="50" r="28" />
      <circle class="art-venn-line" cx="80" cy="76" r="28" />
      <circle class="art-ink-fill" cx="80" cy="59" r="3" />
    </g>

    <g v-else-if="art.motif === 'book-spiral'">
      <path class="art-path" :d="spiral" />
      <path class="art-fill" d="M117 25 l-9 -1 l5 7 z" />
      <path class="art-node" d="M80 104 Q56 94 26 98 V66 Q56 62 80 72 Z" />
      <path class="art-node" d="M80 104 Q104 94 134 98 V66 Q104 62 80 72 Z" />
      <path class="art-edge thin" d="M34 76 Q54 73 72 79 M34 84 Q54 81 72 87 M88 79 Q106 73 126 76 M88 87 Q106 81 126 84" />
    </g>

    <g v-else>
      <rect class="art-fill" x="34" y="74" width="92" height="18" rx="3" />
      <rect class="art-node" x="42" y="56" width="80" height="18" rx="3" />
      <rect class="art-fill soft" x="38" y="38" width="86" height="18" rx="3" />
      <path class="art-edge thin" d="M52 83 H104 M52 65 H100 M50 47 H106" />
    </g>
  </svg>
</template>
