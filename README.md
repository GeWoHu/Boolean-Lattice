# Weighted Boolean Incidence Operators

This repository contains a short, self-contained mathematical note about a weighted inclusion operator on the Boolean lattice. It is intended as an openly inspectable result, not as a claim of journal certification or broad application.

## The result

For a vector of real coordinate weights `a = (a_1,...,a_m)` and `1 <= k <= m`, define

\[
(U_k(a)f)(S)=\sum_{i\notin S}a_i f(S\cup\{i\}),\qquad |S|=k-1,
\]

where `S` and `S ∪ {i}` are subsets of `[m] = {1,...,m}`. Thus `U_k(a)` is the weighted `(k,k-1)` inclusion matrix between two adjacent levels of the Boolean lattice.

The theorem proved in `paper.tex` is

\[
\boxed{\quad
\|U_k(a)\|^2\le
\frac{\|U_k(\mathbf 1)\|^2}{m}\,\|a\|_2^2
=\frac{k(m-k+1)}{m}\sum_{i=1}^m a_i^2.
\quad}
\]

The constant is sharp. At interior levels `1 < k < m`, and for nonzero `a`, equality holds exactly when every coordinate has the same magnitude:

\[
|a_1|=\cdots=|a_m|.
\]

So, among all coordinate-weight vectors with a fixed Euclidean norm, spreading weight equally in magnitude maximizes the operator norm. The endpoint levels `k=1,m` are different: equality then holds for every weight vector.

## Why the statement is nontrivial

For equal weights, the Boolean lattice has symmetric-group / Johnson-scheme structure, and classical block diagonalization gives the spectrum of the ordinary inclusion operator. Generic coordinate weights destroy that symmetry. The proof here does not diagonalize the weighted matrix. Instead, it deletes one coordinate, obtains a two-by-two block estimate, and closes an induction through an exact perfect-square identity.

No application or novelty claim beyond the stated theorem is made here.

## Contents

- `paper.tex` — authoritative source.
- `paper.pdf` — PDF compiled from that source with Tectonic 0.15.0 / xdvipdfmx.
- `verification/verify.py` — symbolic, exact block-identity, and numerical checks.
- `verification/perfect_square_exact.py` — standalone transparent exact-arithmetic
  verification (SymPy expansion plus exact `Fraction` spot checks) of the
  perfect-square closure identity.
- `verification/numerical_table.py` — regenerates the normalized-ratio table of the
  paper's numerical-ratios section.
- `verification/complex_weights.py` — randomized checks of the complex-weight extension.
- `verification/RESULTS.md` — recorded release verification output and build facts.
- `AI-DISCLOSURE.md` — factual development and verification disclosure.
- `HERMES_FINAL_REFEREE_REPORT.md` — independent editorial and mathematical review.
- `HERMES_REVISION_CHANGELOG.md` — changes made to produce this release.
- `LICENSE` — CC0 1.0 Universal dedication.
- `SHA256SUMS` — artifact hashes.

## Reproduce

### Build the paper

A Tectonic installation is sufficient:

```sh
tectonic -X compile paper.tex --keep-logs
```

The resulting `paper.pdf` should be reviewed as a generated artifact. PDF bytes can vary by TeX engine version and build metadata; the supplied `SHA256SUMS` identifies this release build.

### Run the verification suite

```sh
python3 verification/verify.py
```

Requirements are Python 3, NumPy, and SymPy. The script checks:

1. the scalar perfect-square identity used in the induction;
2. the `m=3, k=2` base-case principal minors and determinant;
3. the sign-conjugation identity and coordinate-deletion block decomposition;
4. randomized small-dimensional instances, exact flat-weight equality, and strictness for fixed non-flat interior examples.

The auxiliary scripts run the same way:

```sh
python3 verification/perfect_square_exact.py
python3 verification/numerical_table.py
python3 verification/complex_weights.py
```

These checks support the proof; they do not substitute for independent human peer review.

## Review status

The release PDF was regenerated directly from the included source. The source, proof identities, final PDF rendering, and the two retained references were checked during preparation. **Independent human mathematical peer review has not occurred.** Revision v1.1 adds a
convention statement, a notation pass, a comparison proposition against
general-purpose norm bounds, a complex-weight remark, and a numerical appendix, in
response to an external referee-style checklist. See `HERMES_FINAL_REFEREE_REPORT.md` and `AI-DISCLOSURE.md` for scope and limitations.

## License

This release is dedicated to the public domain under CC0 1.0 Universal. See `LICENSE`.
