"""Transparent exact-arithmetic verification of the perfect-square closure
identity used in the paper (eq. defect):

  X(t)^2 - [(A0-B0+t)^2 + 4*B0*t] = P * ((m-1)t - 1)^2

with A0 = k(m-k)/(m-1), B0 = (k-1)(m-k+1)/(m-1), C = k(m-k+1)/m,
X(t) = 2C(1+t) - A0 - B0 - t,
P  = 4k(k-1)(m-k)(m-k+1) / (m^2 (m-1)^2).

Symbolic: sympy expand (exact rationals, no floats).
Spot checks: exact Fraction arithmetic at t = 1/(m-1) (must vanish) and
t = 1/(m-1) +- 1/j (must be strictly positive).
"""
from fractions import Fraction as F
import sympy as sp

m, k, t = sp.symbols('m k t', positive=True)
A0 = k*(m-k)/(m-1); B0 = (k-1)*(m-k+1)/(m-1); C = k*(m-k+1)/m
X = 2*C*(1+t) - A0 - B0 - t
P = 4*k*(k-1)*(m-k)*(m-k+1)/(m**2*(m-1)**2)
lhs = sp.expand(X**2 - ((A0-B0+t)**2 + 4*B0*t))
rhs = sp.expand(P*((m-1)*t-1)**2)
assert sp.simplify(lhs-rhs) == 0
print("PASS: symbolic perfect-square identity (exact, sympy expand)")

def defect(m_, k_, t_):
    m_, k_ = F(m_), F(k_)
    A0_ = k_*(m_-k_)/(m_-1); B0_ = (k_-1)*(m_-k_+1)/(m_-1); C_ = k_*(m_-k_+1)/m_
    X_ = 2*C_*(1+t_) - A0_ - B0_ - t_
    return X_**2 - ((A0_-B0_+t_)**2 + 4*B0_*t_)

for m_ in range(3, 13):
    for k_ in range(2, m_):
        assert defect(m_, k_, F(1, m_-1)) == 0
        for j in (2, 3, 5, 7, 11):
            for sgn in (1, -1):
                d = defect(m_, k_, F(1, m_-1) + sgn*F(1, j*(m_-1)))
                assert d > 0
print("PASS: exact Fraction spot checks m=3..12, interior k, 10 offsets each")
