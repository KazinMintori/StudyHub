// Mathematical text is authored explicitly with $…$ and $$…$$.
// Keep this adapter for Wiki generation; never infer formulas from prose.
export const formatWikiMath = source => source
