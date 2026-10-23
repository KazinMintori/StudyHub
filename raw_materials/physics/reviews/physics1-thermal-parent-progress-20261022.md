# Parent review: Thermal theory changes, chapters18 and19

This is a historical private progress record. Current status is recorded in physics1-priority-status-20261023.md. Chapter18 has since completed its review, while Chapter19 remains a draft. The remaining paragraphs describe the earlier checkpoint.

Chapter18: Restored actual source examples18.3–18.4, including the initially nonempty diving cylinder and the Everest evaluation. Removed an invented van der Waals constant table that conflicted with the realTable18.1. Recomputed the CO2 comparison using the same rounded volume in both models: difference531.8168Pa, about0.5percent. Distinguished composing the speed-density function with energy from transforming the probability density with its Jacobian. Verified all ten MaxwellTable18.2 entries by numerical integration. Preserved the actualH2 self-check25Kto500K, all phase paths, all nine triple-point rows, and the Mars pressure comparison.

Original36 theory crops passed fresh RGB comparison. Corrected incomplete figure18.1,18.5,18.9,18.18 and tightened the excessive blank crop18.23. Vietnamese captions occur once. All eight teaching examples were recalculated by the two parent verifiers.

Chapter19: Restored actual example19.3 questions and example19.6 input2500mol,35to26°C. Restored the25percent model in19.2. Distinguished the rounded work values in19.7 from an exactly consistentCp/Cv ratio. RestoredTable19.1's nine rows, including correctAr/O2 entries and removal of an inventedCl2 row. Corrected formula numbering19.11–19.24. Added the essential near-equilibrium/constantCv restrictions and the variableCv integral. Removed a substituted keyboard-aerosol example and the unsupported Joule–Thomson historical digression. Rewrote the free-expansion explanation to distinguish monatomic translation from internal rotation/vibration.

Question19.2 is ambiguous without the comparison state. The source answer uses the horizontal line at final pressurep2 and selects isothermal work as larger. With a common initial state and isobaric pressurep1, the order reverses. Both comparisons are now derived explicitly. Figure19.7d is a direct curved path, not the separately discussed closed cycle.

Original29 theory crops passed fresh RGB comparison. Corrected missing text/axes in19.3,19.4,19.7,19.9,19.19 and summaryfigures1–3. A tiny extraneous continuation mark remains at the lower-right of19.12 because a rectangle that removes it would cut its upper label or lower axis; resolve this artwork boundary before publication.

Browser results: qa/physics1-priority/theory-browser/ch18-ch19/results.json,64 preliminary cases. Further text changes were made afterward, so final browser acceptance must be rerun when chapter content is locked.

The authored formula helper initially hid125 display formulas from static extraction. They are now explicit d(String.raw...) calls, with a regression check covering every cheatsheet formula in all seven chapters. Browser review of every slide and cheatsheet across all seven chapters passed272cases, including an explicit unrendered-TeX check. Testedviewports320,360,375,1440.

Repository tests passed140cases before the additional reading-passage boundary test. The updated exercise-group suite then passed5cases, including a chapter18 passage starting belowquestion92 and multiple reading passages. Skill tests passed39cases. No local full build was run.
