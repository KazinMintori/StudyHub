# Chapter41 theoryA: Parent source and implementation review

Status: Parent-reviewed draft. This accepts neither the Antigravity job as succeeded nor the full chapter for release.

## Worker result and boundary record

The initial A job and its first corrective job became unknown after bridge restarts. Their complete preserved snapshots are under qa/physics/chapter41/worker-a-call1-snapshot and worker-a-call2-snapshot. Four unowned source-text scratch files from the initial run were preserved outside the worktree in worker-a-call1-out-of-scope-quarantine. The failed initial boundary audit is recorded in worker-a-call1-boundary-violation.json. The original worker report's statement that no unowned files were created was inaccurate. No fourth call or ownership expansion was used. The parent imported 20 owned files from the frozen call2 snapshot, then reviewed and repaired them independently in the main draft.

## Source coverage

| Source unit | Destination | Parent review |
| --- | --- | --- |
|41.1, PDF1380–1382|01-schrodinger-ba-chieu.md|Three kinetic contributions, time-dependent equation, probability volume, normalization, stationary-state derivation, equations1–6 and original selfcheck1. Physical-law statement restricted to the nonrelativistic model.|
|41.2, PDF1382–1387|02-hop-ba-chieu.md|Full box boundaries, separation proof, three one-dimensional equations, normalization and partial-volume integrals, positive quantum numbers, energy/degeneracy, unequal-edge box, original comparison and selfcheck2. Distinguish a separable eigenbasis from all possible degenerate superpositions. Nodes do not mean discontinuities.|
|41.3, PDF1387–1395|03-nguyen-tu-hydro.md|Bohr limitations, reduced mass, spherical coordinate separation and all three equations, boundary conditions, Coulomb energies, orbital momentum, state/shell notation and table41.1, Examples2–4, angular-integrated radial distributions, 1s normalization, positronium/muonic and one-electron ions, original selfcheck3.|
|41.4, PDF1395–1398|04-hieu-ung-zeeman.md|Current-loop derivation, electron sign, orbital moment and Bohr magneton, level shifts/degeneracy, Example5, selection rules and nine transitions/three photon energies, original open-ended selfcheck4. SourceFigures13–15 are placed here by parent despite B owning their PNG files.|

Equations41.1–41.35 are present, with43tags including lettered11/13/14/20 variants. Named complete terms preserve each derivative/factor while allowing mobile layout.

## Teaching examples and questions

-41.1: Full(a)normalizationC and(b)quarter-volume probabilities for actual(1,2,1),(2,1,1),(3,1,1). Positive realC is a phase convention stated explicitly. Three results are approximately.0908,.250,.303.
-41.2: n3, nine spatial states, energy−1.51eV without spin.
-41.3: n4, lmax3, Lmaxsqrt12ħ,Lzmax3ħ, minimum30degrees. l0 has no vector direction; l1/2 have larger minimum angles.
-41.4: Source1s wavefunction, normalization over all space and P(r<a)=1−5exp(−2)≈.323, full antiderivative/bounds, distinguish volume density/radial density/probability.
-41.5: Source600.000nm, l1→0,B2.00T, shifts±1.16e−4eV and resulting599.966/600.000/600.034nm. Numeric chains retained as complete relation rows after actual320px overflow was found.
-Four source selfchecks are placed directly after their sections with answers closed and absent from summaries. Parent removed invented yes/no options in selfcheck4.

## Corrections and source limitations

The source's universal r=n²a peak statement is false. The actual selfcheck3 ranking is retained and proved using actual1s/2p radial functions. The rule is limited to circular states l=n−1;2s outer maximum(3+sqrt5)a is a checked counterexample. General radial probability uses the angular integral, not local3Ddensity. Spherical symmetry explains m-degeneracy, while equality across l is an additional Coulomb property. A uniform magnetic field preserves rotations around its axis. Unequal box lengths split the particular three first-excited states but do not prohibit every higher accidental degeneracy. Zeeman photon shift uses a clearly defined initial-minus-final m difference.

The source sunspot caption itself gives.4T as1000timesEarthfield. Parent keeps the.4T physical data and qualitative comparison in the public caption because that numerical ratio does not match the usual Earthfield scale. No illustration pixels were changed. The classical satellite caption now names the semimajoraxis rather than ambiguous meanradius.

## Images

All12A-owned sourcePNG files were regenerated from explicit source rectangles, with fresh exactRGB comparisons in the owned verifier. Figure41.2 top was expanded from308to300points to retain the complete(a) state label; Figure41.3 bottom was trimmed from360to350 to remove an unrelated separator. All3panels of41.2 were visually inspected after recrop. Figures13–15 were copied from the preserved Bsnapshot, exactRGB-checked previously and visually reviewed, then placed after the appropriate level/selection discussion. Vietnamese captions and per-image one-time English glossaries are retained. Full image integration audit remains part of the complete chapter review.

## Actual verification

-raw_materials/physics/verify_chapter41_theory_a.py: Passed actual numeric, freshPNGpixels, annotation syntax, Markdown and wholeMathJax checks. Logqa/physics/chapter41/theory-a-verifier.log.
-Parent independent calculations: verify_chapter41_parent.py and verify_chapter41_end_independent.py, actual computed source inputs and state/probability enumeration. Their scope is numerical, not certification of every prose argument.
-qa/physics/chapter41/parent-math-review.json: Opening/summary plus four integrated A fragments have no measured wholeformula width/render findings.
-Browser initially ran72cases at320/360/375/1440:71passed, oneZeeman320case exposed two279.48px inline chains in260px. Both chains were rewritten without dropping arithmetic, then the failed case reran and passed. Seea-browser-review-record.json and a-browser/results.json. All20Wiki pages separately passed40cases and39Cheatsheet+12Slides separately passed52cases. Those tests do not accept B/C/D.
-Language review reduced14suggestions to mathematical/panel-label falsepositives and two later-removed evaluative phrases. Parent read the flagged paragraphs and corrected long sentences, physical quantifiers and excessive claims.
-Repository53tests passed; mandatoryskill39tests passed; check_lectureall110lessons/177topics has0errors/0warnings. These structural checks do not certify unfinished chapter41.

## Initial remaining work and final resolution

The initial pending B theory and C/D exercises have since been integrated and independently reviewed. Final coverage and acceptance are recorded in ch41-final-source-review.md and chapter-41-review.json. The final theory browser pass contains88cases, the eight exercise fragments32cases, and20Wiki pages40cases. All40sourcePNG match fresh source RGB. The content is ready for a GitHub build, with publication checked separately. Earlier counts in this staged A report describe that earlier check, not the final release.
