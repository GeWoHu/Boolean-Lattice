# Revision changelog

## Release package revision

This release replaces earlier review inputs with one newly compiled, verified source/PDF pair. Historical inputs are not distributed in this repository.

### Mathematical repairs

- Corrected the sign reduction to the two-sided identity
  `U_k(σ·a)=D_{σ,k-1}U_k(a)D_{σ,k}`.
- Corrected the coordinate-deletion Gram block to
  `[[AA^T+a_m^2I, a_mB^T], [a_mB, BB^T]]` with
  `B=U_{k-1}(a')`.
- Retained the correct scalar corner term `sqrt(tB_0)`, not the invalid term involving `sqrt(tA_0B_0)`.
- Rechecked the perfect-square closure identity, the `m=3,k=2` base-case certificate, the sign relation, and the block decomposition.
- Strengthened the equality-case explanation by recording the nonzero off-diagonal condition needed for strict monotonicity.

### Conceptual and editorial revision

- Added a new introduction centered on
  \[
  \|U_k(a)\|^2\le \frac{\|U_k(\mathbf 1)\|^2}{m}\|a\|_2^2.
  \]
- Made the extremal interpretation explicit: equal-magnitude weights maximize the norm at fixed `||a||_2`, uniquely for nonzero interior-level weights.
- Explained why the weighted result is not supplied directly by the symmetric equal-weight spectral decomposition.
- Explained why `U^T U` and `UU^T` give the same operator-norm eigenvalue.
- Clarified the `a'=0` partial-isometry case.
- Put the block lemma matrices in display form.
- Unified theorem/lemma numbering.
- Removed the AI system from the author list. The paper uses a neutral contributor attribution and includes a factual disclosure.
- Removed defensive/unrelated background citations and retained only two checked references.
- Used hidden hyperlink styling in the PDF and repaginated the final PDF to six clean pages.

### Release engineering

- Compiled `paper.pdf` from `paper.tex` using Tectonic 0.15.0 and xdvipdfmx.
- Added `verification/verify.py` for symbolic, block-identity, and numerical checks.
- Added `README.md`, `AI-DISCLOSURE.md`, `HERMES_FINAL_REFEREE_REPORT.md`, `LICENSE`, and `SHA256SUMS`.
- Excluded obsolete PDFs, prior task records, scratch images, build logs, and internal transcripts.

## Deliberately not changed

- The theorem, the sharp constant `k(m-k+1)/m`, and the equality characterization are unchanged.
- The coordinate-deletion induction and perfect-square closure remain the proof mechanism.
- No application, novelty, ownership, or journal-acceptance claim was added.

## Historical provenance note

The available incoming v3 LaTeX matched its recorded prefix. The two incoming PDFs did not match the historical PDF prefixes supplied in mission records, and one later PDF had prose not identical to the available v3 source. The historical build path is therefore documented as unresolved. The release itself is not affected: its source/PDF pair was rebuilt and reverified directly.
