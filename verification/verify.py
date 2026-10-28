#!/usr/bin/env python3
"""Reproducibility checks for paper.tex.

Checks performed:
1. Symbolic scalar-closure identity (paper eq. (7)).
2. Symbolic m=3,k=2 base-case principal minors and determinant.
3. Exact numerical block decomposition / sign conjugation.
4. Exhaustive small-dimension randomized inequality tests and equality sanity checks.

Requires: Python 3, sympy, numpy.
Run: python3 verification/verify.py
"""
from itertools import combinations
import sys

import numpy as np
import sympy as sp


def U(m, k, a, rows=None, cols=None):
    """Matrix of U_k(a), with optional prescribed subset orderings."""
    if rows is None:
        rows = list(combinations(range(m), k - 1))
    if cols is None:
        cols = list(combinations(range(m), k))
    rindex = {S: i for i, S in enumerate(rows)}
    M = np.zeros((len(rows), len(cols)), dtype=float)
    for j, T in enumerate(cols):
        Tset = set(T)
        for i in T:
            M[rindex[tuple(x for x in T if x != i)], j] += a[i]
    return M, rows, cols


def C(m, k):
    return k * (m - k + 1) / m


def symbolic_checks():
    m, k, t = sp.symbols("m k t", positive=True)
    A0 = k * (m - k) / (m - 1)
    B0 = (k - 1) * (m - k + 1) / (m - 1)
    C0 = k * (m - k + 1) / m
    X = 2 * C0 * (1 + t) - A0 - B0 - t
    defect = sp.expand(X**2 - ((A0 - B0 + t) ** 2 + 4 * B0 * t))
    claimed = sp.expand(
        4 * k * (k - 1) * (m - k) * (m - k + 1)
        / (m**2 * (m - 1) ** 2) * ((m - 1) * t - 1) ** 2
    )
    assert sp.simplify(defect - claimed) == 0

    # m=3,k=2 base case.  G=U^T U in the order {12},{13},{23}.
    x1, x2, x3 = sp.symbols("x1 x2 x3", nonnegative=True)
    s = x1 + x2 + x3
    G = sp.Matrix([
        [x1 + x2, sp.sqrt(x2 * x3), sp.sqrt(x1 * x3)],
        [sp.sqrt(x2 * x3), x1 + x3, sp.sqrt(x1 * x2)],
        [sp.sqrt(x1 * x3), sp.sqrt(x1 * x2), x2 + x3],
    ])
    M = sp.Rational(4, 3) * s * sp.eye(3) - G
    claimed_diag = [
        (x1 + x2 + 4 * x3) / 3,
        (x1 + 4 * x2 + x3) / 3,
        (4 * x1 + x2 + x3) / 3,
    ]
    assert all(sp.simplify(M[i, i] - claimed_diag[i]) == 0 for i in range(3))
    principal2 = [M.extract([0, 1], [0, 1]).det(),
                  M.extract([0, 2], [0, 2]).det(),
                  M.extract([1, 2], [1, 2]).det()]
    claimed2 = [
        s * (x1 + 4 * x2 + 4 * x3) / 9,
        s * (4 * x1 + x2 + 4 * x3) / 9,
        s * (4 * x1 + 4 * x2 + x3) / 9,
    ]
    # The ordering differs, so compare as a multiset by direct permutation.
    assert any(all(sp.simplify(principal2[i] - p[j]) == 0 for i, j in enumerate(perm))
               for perm in __import__("itertools").permutations(range(3))
               for p in [claimed2])
    assert sp.simplify(M.det() - sp.Rational(4, 27) * (s**3 - 27*x1*x2*x3)) == 0


def matrix_checks():
    rng = np.random.default_rng(20261028)
    for m, k in [(5, 2), (5, 3), (6, 3), (6, 4)]:
        a = rng.normal(size=m)
        signs = rng.choice([-1.0, 1.0], size=m)
        Ua, rows, cols = U(m, k, a)
        Usa, _, _ = U(m, k, signs * a)
        Drow = np.diag([np.prod(signs[list(S)]) if S else 1.0 for S in rows])
        Dcol = np.diag([np.prod(signs[list(T)]) for T in cols])
        assert np.allclose(Usa, Drow @ Ua @ Dcol, atol=1e-12)

        ap, am = a[:-1], a[-1]
        row0 = [S for S in rows if m - 1 not in S]
        row1 = [S for S in rows if m - 1 in S]
        col0 = [T for T in cols if m - 1 not in T]
        col1 = [T for T in cols if m - 1 in T]
        Uk, _, _ = U(m, k, a, row0 + row1, col0 + col1)
        A, _, _ = U(m - 1, k, ap)
        B, _, _ = U(m - 1, k - 1, ap)
        expected = np.block([
            [A, am * np.eye(len(row0))],
            [np.zeros((len(row1), len(col0))), B],
        ])
        assert np.allclose(Uk, expected, atol=1e-12)
        H = Uk @ Uk.T
        expected_H = np.block([
            [A @ A.T + am * am * np.eye(len(row0)), am * B.T],
            [am * B, B @ B.T],
        ])
        assert np.allclose(H, expected_H, atol=1e-12)


def numerical_checks():
    rng = np.random.default_rng(47)
    max_ratio = 0.0
    for m in range(2, 9):
        for k in range(1, m + 1):
            for _ in range(500):
                a = rng.normal(size=m) * 10 ** rng.uniform(-2, 2, size=m)
                Mk, _, _ = U(m, k, a)
                ratio = np.linalg.norm(Mk, 2) ** 2 / (C(m, k) * np.dot(a, a))
                max_ratio = max(max_ratio, ratio)
                assert ratio <= 1 + 1e-9, (m, k, ratio)
            flat = np.ones(m)
            Mk, _, _ = U(m, k, flat)
            assert abs(np.linalg.norm(Mk, 2) ** 2 - k * (m - k + 1)) < 1e-9
    # A non-flat interior example must be strict.
    for m in range(3, 8):
        for k in range(2, m):
            a = np.ones(m)
            a[0] = 2
            Mk, _, _ = U(m, k, a)
            ratio = np.linalg.norm(Mk, 2) ** 2 / (C(m, k) * np.dot(a, a))
            assert ratio < 1 - 1e-8
    return max_ratio


def main():
    symbolic_checks()
    matrix_checks()
    max_ratio = numerical_checks()
    print("PASS: scalar-closure identity, base-case minors, block/sign identities.")
    print("PASS: random tests m=2..8, all levels (500 weights each); max ratio %.15f." % max_ratio)
    print("PASS: flat equality and strict non-flat interior examples.")


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:
        print("FAIL:", repr(exc), file=sys.stderr)
        raise
