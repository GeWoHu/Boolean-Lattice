# Final referee report — weighted Boolean incidence note

## Verdict

**READY WITH DISCLOSED HUMAN-REVIEW LIMITATION**

The release manuscript is mathematically coherent under the checks performed, its release PDF was compiled directly from the included source, and the public package is reproducible. This is not a substitute for independent expert peer review. The historical provenance of the older defective PDF cannot be fully reconstructed from the available inputs because its recorded frozen hash was not among them; that issue is disclosed rather than concealed.

## Scope of review

This report evaluates the release files in this repository, especially `paper.tex` and its direct build `paper.pdf`, and records the status of three earlier incoming artifacts. It does not claim an exhaustive literature search or a human referee’s certification of novelty.

## A. Mathematical correctness

### CRITICAL — historical defective PDF, resolved for the release

The older PDF contained a wrong off-diagonal expression in its displayed Gram block. It printed a product involving `U_k(a')U_{k-1}(a')^T`; the correct off-diagonal block is `a_m B^T`, where `B=U_{k-1}(a')`. The printed historical chain would lead to a scalar off-diagonal term of the form `sqrt(t A_0 B_0)`, for which the asserted closure bound is false (explicit small-parameter counterexamples exist). The corrected release derivation is:

- source lines **162–187**, especially equation **(4)**: `a_m B^T` and `a_m B`;
- source lines **229–251**, especially equations **(5)** and **(6)**: the correct scalar term `sqrt(tB_0)`.

This was checked against explicit matrices in `verification/verify.py`. The release source does **not** retain the historical defect.

### MAJOR — sign reduction, resolved for the release

The historical PDF omitted a left diagonal operator in the sign relation. The correct identity is the two-sided orthogonal conjugation

`U_k(σ·a)=D_{σ,k-1} U_k(a) D_{σ,k}`,

stated at source lines **131–145**, equation **(2)**. This was checked explicitly for several dimensions and levels. The norm conclusion is therefore valid.

### MAJOR — equality-case propagation, resolved and clarified

The equality argument must use strict monotonicity of the largest eigenvalue in its diagonal entries only after ensuring the off-diagonal entry is nonzero. The release handles this in source lines **296–324**: equality in the scalar closure gives `t=1/(m-1)>0`; `a_m != 0`; and `β != 0` unless `a'=0`, which was already treated as strict. This supplies the missing condition for strict partial derivatives and makes the lifting argument valid.

### MINOR — Gram-matrix convention, resolved

The proof uses both `G_k=U_k^T U_k` and `H_k=U_kU_k^T`. The older text switched between them without explanation. Source lines **146–160** now explains that they have the same nonzero eigenvalues (the squared singular values), hence the same operator-norm eigenvalue, and identifies which Gram matrix is used where.

### MINOR — endpoint/deletion boundary case, resolved

The case `a'=0` is correctly a scalar multiple of a partial isometry, not merely a vague “bijection matrix.” Source lines **219–228** state its block form and explain why its norm is `a_m` and why the interior inequality is strict.

### Mathematical verification performed

The release passed all checks in `verification/verify.py`:

- symbolic equality of the scalar closure defect in source equation **(7)** (lines **265–277**);
- symbolic base-case diagonal minors, two-by-two principal minors, and determinant for `m=3,k=2` (lines **330–356**);
- exact numerical tests of the sign and block identities;
- randomized tests for `2 <= m <= 8`, every level, plus equality and strictness sanity checks.

These computations corroborate the proof; they do not replace independent human review.

## B. Motivation and conceptual interpretation

### MAJOR — prior manuscript under-motivated, resolved

The earlier manuscript led directly with a theorem and a proof. It did not explain why the sharp constant has the form `||U_k(1)||^2/m` or what is extremized. The new Introduction, source lines **41–101**, now leads with

`||U_k(a)||^2 <= ||U_k(1)||^2 ||a||_2^2/m`

and states the precise interpretation: under a fixed Euclidean weight budget, equal magnitudes maximize the operator norm; at interior levels they are the unique nonzero maximizers.

### SUGGESTION — appropriate scope

The release deliberately does not invent applications or assert broad novelty. Source lines **91–101** distinguish this single-level `ell^2` estimate from unrelated conclusions. That restraint is appropriate for a public theorem note.

## C. Bibliography

### CRITICAL — fabricated/misattributed historical citations, removed

The older PDF cited arXiv:1104.1481 as an “E. Srinivasan” paper with the wrong title, and cited a non-matching Bannai–Ito journal item with the wrong author initial. Both were unsuitable for release.

The release retains only two checked references:

1. **E. Bannai and T. Ito**, *Algebraic Combinatorics I: Association Schemes*, Benjamin/Cummings, 1984. This matches WorldCat / publisher metadata (authors, title, publisher, year; ISBN 9780805304909).
2. **M. K. Srinivasan**, *Counting spanning trees of the hypercube and its q-analogs by explicit block diagonalization*, arXiv:1104.1481 (2011). The arXiv record confirms author, title, and its explicit Boolean-lattice block-diagonalization content.

They appear at source lines **383–390**. The unrelated reverse-hypercontractivity, polarization, and differential-poset citation list was removed. No citation is used as a novelty claim.

## D. Editorial review

### MAJOR — authorship and disclosure, resolved

An AI system was formerly placed in the author block. The release uses the neutral contributor designation **“An independent contributor”** (source line **12**) and puts the factual AI disclosure in an unnumbered disclosure section (lines **372–381**). The manuscript explicitly states that it has not been independently human-refereed.

### MINOR — theorem / lemma numbering, resolved

Lemmas now share the theorem counter (`\newtheorem{lemma}[theorem]{Lemma}` at line **7**), producing Theorem 1, Lemma 2, Lemma 3, and Remarks 4–5. Display equations are numbered independently and referenced consistently.

### MINOR — cramped matrices and link presentation, resolved

The block lemma uses display matrices (lines **190–211**) rather than an inline cramped construction. The final PDF was compiled with `hyperref[hidelinks]`; no colored link rectangles remain. Six rendered pages were reviewed after the final build. Equations, matrices, author wording, bibliography, and page breaks were visually clean.

## E. Source/PDF provenance

### MAJOR — archived historical-hash discrepancy, disclosed

Available incoming files have these full SHA-256 values:

- older defective PDF: `513f45fd2726a9d8b1fb763c21cd1f76d5bdca49994268b29d2cbea5b34eccb1`;
- corrected incoming LaTeX: `c0fc62fb2983f392c2a5b67805656ac0d9edbd6e20fd331dd16ea6f50eff370b`;
- later incoming PDF: `5ee8a2897db834680f2c583c8157cebae9929ffd1558abda67e59b04bd93e4ea`.

The corrected incoming LaTeX matches the historical v3 prefix `c0fc62fb`. Neither available PDF matches the supplied historical frozen prefixes `cbc9f24732762126` (v2) or `f6f74972` (v3). Therefore the available artifacts do not prove whether the defective PDF was produced by the historical v2 source or was merely an obsolete export. In addition, the later incoming PDF had corrected principal equations and bibliography but non-identical equality-case prose relative to the available v3 source.

The release does not silently substitute an artifact: it creates a new authoritative pair. `paper.pdf` was built directly from the included `paper.tex` using Tectonic 0.15.0 / xdvipdfmx, after the corrected proof was rechecked. Their release hashes appear in `SHA256SUMS`.

## Required corrections completed

- [x] Correct the historical sign-reduction and Gram-block defects in the release source.
- [x] Recheck the scalar identity, base case, and block algebra.
- [x] Replace the author placeholder/AI byline with neutral human contributor wording and disclosure.
- [x] Add a conceptual introduction without inflated claims.
- [x] Keep only verified, relevant citations.
- [x] Clarify the partial-isometry and two-Gram-matrix points.
- [x] Compile and visually inspect the final PDF.
- [x] Include reproducible checks, license, hashes, disclosure, and changelog.

## Optional future work

- An independent specialist can review the proof, exact equality propagation, and prior literature more broadly.
- A named author may replace the neutral contributor wording if they choose to supply attribution and take responsibility for the release.
- A future revision may add applications only if they are independently developed and substantiated.

No optional item is a gate for this public release.
