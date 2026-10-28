import numpy as np, itertools
def U(m,k,a):
    cols=list(itertools.combinations(range(m),k)); rows=list(itertools.combinations(range(m),k-1))
    ci={T:j for j,T in enumerate(cols)}
    M=np.zeros((len(rows),len(cols)),dtype=np.result_type(a,1.0))
    for i,r in enumerate(rows):
        for x in range(m):
            if x not in r: M[i,ci[tuple(sorted(r+(x,)))]] = a[x]
    return M
rng=np.random.default_rng(11)
print("Complex weights (dtype fixed): worst ratio ||U_k(z)||^2 / [k(m-k+1)/m ||z||^2] over 500 Gaussian draws; flat phase vector must give 1")
for m,k in ((5,2),(5,3),(6,3),(6,4),(7,3)):
    c=k*(m-k+1)/m; worst=0
    for _ in range(500):
        z=rng.normal(size=m)+1j*rng.normal(size=m)
        worst=max(worst, np.linalg.svd(U(m,k,z),compute_uv=False)[0]**2/(c*np.vdot(z,z).real))
    z=np.exp(1j*rng.uniform(0,2*np.pi,m))
    flat=np.linalg.svd(U(m,k,z),compute_uv=False)[0]**2/(c*m)
    print(f"  (m,k)=({m},{k}): worst={worst:.10f}  flat_phase={flat:.10f}")
