import numpy as np, itertools, math
from math import comb

def U(m,k,a):
    # rows: (k-1)-sets S, cols: k-sets T; entry a_i if T=S+{i}
    cols=list(itertools.combinations(range(m),k)); rows=list(itertools.combinations(range(m),k-1))
    ci={T:j for j,T in enumerate(cols)}
    M=np.zeros((len(rows),len(cols)))
    for i,r in enumerate(rows):
        for x in range(m):
            if x not in r: M[i,ci[tuple(sorted(r+(x,)))]] = a[x]
    return M

def R(m,k,a):
    c=k*(m-k+1)/m
    return np.linalg.svd(U(m,k,a),compute_uv=False)[0]**2/(c*np.dot(a,a))

print("R(a) = ||U_k(a)||^2 / [k(m-k+1)/m ||a||^2]   (flat, sparse, nearly-flat, random)")
print(f"{'(m,k)':>6} {'flat':>8} {'e_1':>8} {'2-sparse':>9} {'near-flat':>10} {'random(mean)':>12} {'random(max of 200)':>19}")
rng=np.random.default_rng(7)
for m in (4,5,6,7):
    for k in range(1,m+1):
        flat=R(m,k,np.ones(m)); e1=R(m,k,np.eye(m)[0])
        a2=np.zeros(m); a2[0]=a2[1]=1.0; two=R(m,k,a2)
        nf=np.ones(m); nf[0]=1.01; nf[1]=0.99; near=R(m,k,nf)
        rs=[R(m,k,rng.normal(size=m)) for _ in range(200)]
        print(f"{(m,k)!s:>6} {flat:8.6f} {e1:8.4f} {two:9.4f} {near:10.6f} {np.mean(rs):12.4f} {max(rs):19.4f}")

print()
print("Complex weights: max sigma^2 vs bound (flat complex attains equality)")
for m,k in ((5,2),(5,3),(6,3)):
    worst=0
    for _ in range(300):
        z=rng.normal(size=m)+1j*rng.normal(size=m)
        c=k*(m-k+1)/m
        val=np.linalg.svd(U(m,k,z),compute_uv=False)[0]**2
        worst=max(worst, val/np.vdot(z,z).real/c)
    z=np.ones(m,dtype=complex)*np.exp(1j*0.7)
    flatv=np.linalg.svd(U(m,k,z),compute_uv=False)[0]**2/(comb(m,k-1)*k*k*1.0)  # = k(m-k+1)
    print(f"  (m,k)=({m},{k}): worst ratio over 300 complex draws = {worst:.10f} (<=1); flat phase vector ratio = {flatv/(k*(m-k+1)/m):.10f}")
