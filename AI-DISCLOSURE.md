# AI development and verification disclosure

## Scope of AI involvement

An automated AI research agent assisted with manuscript preparation, proof checking, symbolic verification, numerical testing, bibliography checking, PDF/source comparison, and editorial revision. No AI system is listed as an author.

The named author field in the manuscript intentionally reads **“An independent contributor.”** It is a neutral attribution chosen because no author name, affiliation, or institutional representation was supplied for this public release.

## Material reviewed

Three incoming artifacts were inspected during preparation:

1. an older five-page PDF containing an incorrect displayed off-diagonal block in the deletion argument and inaccurate bibliography entries;
2. a corrected LaTeX source file;
3. a later five-page PDF whose principal corrected equations and bibliography agreed with the corrected source but whose equality-case prose was not byte-identical to that source.

The incoming artifacts are not included in this repository. They are historical review inputs, not release artifacts.

## What was verified for this release

The release source `paper.tex` was compiled from scratch with Tectonic 0.15.0 and xdvipdfmx. The generated six-page `paper.pdf` was inspected page by page. The following mathematical checks were rerun from `verification/verify.py`:

- the scalar-closure defect factorization was proved symbolically as an identity in `m`, `k`, and `t`;
- the three-by-three base-case principal minors and determinant were verified symbolically;
- the two-sided sign conjugation and coordinate-deletion block decomposition were checked against explicit finite matrices;
- the theorem was tested numerically on random weights for `2 <= m <= 8` and every level, along with exact flat-vector equality and strict fixed non-flat interior examples.

The verification script is included so that these checks can be reproduced. It is evidence supporting the displayed proof, not an alternative proof.

## Important limitation

The earlier frozen hashes cited in project history for the obsolete PDFs did not match the full SHA-256 values of the three incoming files available for review. In particular, the historical inputs alone cannot establish which build generated the defective older PDF. This release does not rely on that provenance claim: `paper.pdf` was regenerated directly from the included `paper.tex`, and the corrected proof steps were checked again.

## Review status

No independent human mathematical referee has reviewed this note. Readers should treat the paper as an openly released, reproducible pre-review manuscript and are encouraged to check the proof independently before relying on it.
