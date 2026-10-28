# Verification results

Release verification was run with:

```sh
python3 verification/verify.py
```

Output:

```text
PASS: scalar-closure identity, base-case minors, block/sign identities.
PASS: random tests m=2..8, all levels (500 weights each); max ratio 1.000000000000001.
PASS: flat equality and strict non-flat interior examples.
```

The displayed maximum is floating-point output; the proof’s exact equality statement comes from the symbolic and analytic parts of the manuscript, not from that rounded numerical value.

The release PDF was then compiled from `paper.tex` with:

```sh
tectonic -X compile paper.tex --keep-logs
```

Build facts: Tectonic 0.15.0; `xdvipdfmx (0.1)`; six pages; no undefined references, multiply-defined labels, or TeX errors detected. All six rendered pages were visually reviewed after the final build.
