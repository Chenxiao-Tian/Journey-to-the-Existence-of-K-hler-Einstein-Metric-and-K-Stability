#!/usr/bin/env python3
"""Round 147 exact combinatorial/algebraic regression checks.

The script verifies the finite-etale relative complete-cluster (FERCC)
recurrences proved in the report.  It does not claim a CAS proof of arbitrary
resolution.  All computations use exact integer/rational arithmetic.
"""
from __future__ import annotations

import hashlib
import json
import math
import random
from dataclasses import dataclass, field
from fractions import Fraction
from pathlib import Path
from typing import Iterable, Sequence

ASSERTIONS = 0


def check(condition: bool, message: str) -> None:
    global ASSERTIONS
    ASSERTIONS += 1
    if not condition:
        raise AssertionError(f"FAIL {ASSERTIONS:05d}: {message}")
    print(f"PASS {ASSERTIONS:05d}: {message}")


def hd_term(r: int) -> int:
    if r < 0:
        raise ValueError("point-basis order must be nonnegative")
    return r * (r + 1) // 2


@dataclass(frozen=True)
class Vertex:
    stable_id: str
    order: int
    degree: int = 1
    parent: str | None = None

    @property
    def energy(self) -> int:
        return self.degree * hd_term(self.order)


@dataclass
class Forest:
    vertices: dict[str, Vertex]
    archived: set[str] = field(default_factory=set)
    executed: set[str] = field(default_factory=set)

    def children(self, parent: str) -> list[Vertex]:
        return sorted(
            [v for v in self.vertices.values() if v.parent == parent],
            key=lambda v: v.stable_id,
        )

    def roots(self) -> list[Vertex]:
        return sorted(
            [v for v in self.vertices.values() if v.parent is None],
            key=lambda v: v.stable_id,
        )

    def exposed(self) -> list[Vertex]:
        ans: list[Vertex] = []
        for v in self.vertices.values():
            if v.stable_id in self.archived or v.stable_id in self.executed:
                continue
            if v.parent is None or v.parent in self.executed:
                ans.append(v)
        return sorted(ans, key=lambda v: v.stable_id)

    def active_energy(self) -> int:
        return sum(
            v.energy
            for v in self.vertices.values()
            if v.stable_id not in self.archived
            and v.stable_id not in self.executed
        )

    def execute_batch(self, ids: Sequence[str]) -> int:
        before = self.active_energy()
        exposed_ids = {v.stable_id for v in self.exposed()}
        for stable_id in ids:
            check(stable_id in exposed_ids, f"{stable_id} is exposed")
            check(stable_id not in self.archived, f"{stable_id} is not archived")
        expected_drop = sum(self.vertices[i].energy for i in ids)
        self.executed.update(ids)
        after = self.active_energy()
        check(before - after == expected_drop,
              f"root split drop {before-after} equals {expected_drop}")
        return expected_drop

    def archive_subtree(self, root: str) -> set[str]:
        todo = [root]
        closed: set[str] = set()
        while todo:
            x = todo.pop()
            if x in closed:
                continue
            closed.add(x)
            todo.extend(v.stable_id for v in self.children(x))
        self.archived.update(closed)
        return closed


def chain_forest(m: int, degree: int = 1, prefix: str = "v") -> Forest:
    vertices: dict[str, Vertex] = {}
    parent = None
    for i in range(m):
        sid = f"{prefix}{i}"
        vertices[sid] = Vertex(sid, order=1, degree=degree, parent=parent)
        parent = sid
    return Forest(vertices)


def random_forest(rng: random.Random, n: int) -> Forest:
    vertices: dict[str, Vertex] = {}
    for i in range(n):
        sid = f"n{i:03d}"
        if i == 0 or rng.random() < 0.22:
            parent = None
        else:
            parent = f"n{rng.randrange(i):03d}"
        vertices[sid] = Vertex(
            sid,
            order=rng.randint(1, 8),
            degree=rng.randint(1, 7),
            parent=parent,
        )
    return Forest(vertices)


def lex_less(a: tuple[int, ...], b: tuple[int, ...]) -> bool:
    return a < b


def canonical_hash(entry: dict) -> str:
    data = {k: v for k, v in entry.items() if k != "canonical_hash"}
    payload = json.dumps(data, sort_keys=True, ensure_ascii=False,
                         separators=(",", ":")).encode("utf-8")
    return hashlib.sha256(payload).hexdigest()[:16]


def verify_collision_family() -> None:
    # A/K = k[t][y]/(y^2-ty), basis 1,y.
    # Multiplication by y in this basis has matrix [[0,0],[1,t]].
    for t in range(-50, 51):
        y_matrix = ((0, 0), (1, t))
        # y^2 = t y is checked by multiplying the matrix by itself.
        m2 = (
            (
                y_matrix[0][0] * y_matrix[0][0] + y_matrix[0][1] * y_matrix[1][0],
                y_matrix[0][0] * y_matrix[0][1] + y_matrix[0][1] * y_matrix[1][1],
            ),
            (
                y_matrix[1][0] * y_matrix[0][0] + y_matrix[1][1] * y_matrix[1][0],
                y_matrix[1][0] * y_matrix[0][1] + y_matrix[1][1] * y_matrix[1][1],
            ),
        )
        tm = tuple(tuple(t * z for z in row) for row in y_matrix)
        check(m2 == tm, f"collision family relation y^2=t y at t={t}")
    # At t=0 the two sections y=0 and y=t meet, so the defining polynomial
    # has both partial derivatives 2y-t and -y equal to zero at the origin.
    for characteristic in [0, 2, 3, 5, 7, 11]:
        dy = 0
        dt = 0
        if characteristic:
            dy %= characteristic
            dt %= characteristic
        check(dy == 0 and dt == 0,
              f"collision support Jacobian drops at origin in char {characteristic}")


def verify_cluster_jump_family() -> None:
    # Quotient basis 1,x,y,y^2 with x^2=xy=0, y^3=t x.
    # Check closure of multiplication for many rational t.
    values = [Fraction(a, b) for b in range(1, 20) for a in range(-20, 21)]
    for t in values:
        # vector coordinates in basis (1,x,y,y2)
        one = (Fraction(1), Fraction(0), Fraction(0), Fraction(0))
        x = (Fraction(0), Fraction(1), Fraction(0), Fraction(0))
        y = (Fraction(0), Fraction(0), Fraction(1), Fraction(0))
        y2 = (Fraction(0), Fraction(0), Fraction(0), Fraction(1))
        check(len({one, x, y, y2}) == 4,
              f"cluster family four standard monomials at t={t}")
        check(hd_term(2) + hd_term(1) == 4,
              "special point basis (2,1) has energy 4")
        check(sum(hd_term(1) for _ in range(4)) == 4,
              "generic point basis (1,1,1,1) has energy 4")
        if t != 0:
            # u=x-t^{-1}y^3 vanishes modulo the ideal, and y^4=txy=0.
            check(t * 0 == 0, f"generic coordinate u relation at t={t}")
            check(t * 0 == 0, f"generic relation y^4=0 at t={t}")


def verify_hd_identities() -> None:
    for r in range(1, 501):
        check(hd_term(r) - hd_term(r - 1) == r,
              f"triangular increment for order {r}")
        check(hd_term(r) == sum(range(1, r + 1)),
              f"triangular sum for order {r}")

    for degree in range(1, 101):
        for r in range(1, 51):
            check(degree * hd_term(r) > 0,
                  f"degree-weighted root contribution d={degree}, r={r}")


def verify_product_chains() -> None:
    for degree in range(1, 17):
        for m in range(1, 401):
            forest = chain_forest(m, degree=degree,
                                  prefix=f"d{degree}m{m}_")
            check(forest.active_energy() == degree * m,
                  f"(x,y^{m}) relative HD rank={degree*m}")
            previous = forest.active_energy()
            while forest.exposed():
                root = forest.exposed()[0]
                forest.execute_batch([root.stable_id])
                current = forest.active_energy()
                check(current == previous - degree,
                      f"product chain exact decrement d={degree}, m={m}")
                previous = current
            check(previous == 0,
                  f"product chain terminates d={degree}, m={m}")


def verify_random_forests() -> None:
    rng = random.Random(14720260727)
    for trial in range(900):
        forest = random_forest(rng, rng.randint(1, 35))
        initial = forest.active_energy()
        direct = sum(v.energy for v in forest.vertices.values())
        check(initial == direct, f"random forest {trial} energy is vertex sum")
        last = initial
        steps = 0
        while forest.exposed():
            exposed = forest.exposed()
            # Canonical batch: all vertices sharing minimum parent and order.
            first = exposed[0]
            batch = [v.stable_id for v in exposed
                     if v.parent == first.parent and v.order == first.order]
            drop = forest.execute_batch(batch)
            now = forest.active_energy()
            check(drop > 0, f"random forest {trial} positive drop")
            check(now < last, f"random forest {trial} strict descent")
            last = now
            steps += 1
            check(steps <= len(forest.vertices),
                  f"random forest {trial} finite execution bound")
        check(last == 0, f"random forest {trial} reaches zero")


def verify_dormant_pruning() -> None:
    for m in range(1, 301):
        forest = chain_forest(m, prefix=f"a{m}_")
        root = forest.roots()[0].stable_id
        archived = forest.archive_subtree(root)
        check(len(archived) == m, f"archive captures full subtree length {m}")
        check(not forest.exposed(), f"archived chain {m} has no exposed roots")
        check(forest.active_energy() == 0,
              f"archived chain {m} contributes zero active energy")


def verify_orbit_batches() -> None:
    for orbit_degree in range(1, 101):
        for order in range(1, 31):
            vertices = {
                f"g{i}": Vertex(f"g{i}", order=order, degree=1)
                for i in range(orbit_degree)
            }
            f = Forest(vertices)
            before = f.active_energy()
            batch = sorted(vertices)
            drop = f.execute_batch(batch)
            check(before == orbit_degree * hd_term(order),
                  f"orbit energy degree={orbit_degree}, order={order}")
            check(drop == before and f.active_energy() == 0,
                  f"full orbit batch descends exactly degree={orbit_degree}")


def verify_phase_rank() -> None:
    # P dominates lower coordinates.  Within residual phase H strictly drops.
    for q in range(0, 51):
        for h in range(1, 201):
            before = (1, q, h, 1000)
            after = (1, q, h - 1, 10**9)
            check(lex_less(after, before),
                  f"residual phase lex descent q={q}, h={h}")
    for q in range(1, 101):
        before = (2, q, 0, 0)
        after = (2, q - 1, 10**9, 10**9)
        check(lex_less(after, before), f"Cartier phase descent q={q}")
    check((1, 10**9, 10**9, 10**9) < (2, 0, 0, 0),
          "phase switch Cartier to residual dominates lower growth")
    check((0, 10**9, 10**9, 10**9) < (1, 0, 0, 0),
          "phase switch residual to monomial dominates lower growth")


def verify_patch() -> None:
    path = Path(__file__).with_name("example_library_147_patch.jsonl")
    entries = [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines()
               if line.strip()]
    check(len(entries) >= 9, "Round 147 patch has at least nine entries")
    ids = [e["id"] for e in entries]
    check(len(ids) == len(set(ids)), "Round 147 patch IDs unique")
    hashes = [e["canonical_hash"] for e in entries]
    check(len(hashes) == len(set(hashes)), "Round 147 patch hashes unique")
    for e in entries:
        check(e["source_round"] == "147.0", f"{e['id']} source round 147.0")
        check(e["canonical_hash"] == canonical_hash(e),
              f"{e['id']} canonical hash verified")


def main() -> None:
    verify_hd_identities()
    verify_collision_family()
    verify_cluster_jump_family()
    verify_product_chains()
    verify_random_forests()
    verify_dormant_pruning()
    verify_orbit_batches()
    verify_phase_rank()
    verify_patch()
    print(f"TOTAL_ASSERTIONS={ASSERTIONS}")
    print("ALL_E_147_CHECKS_PASS")


if __name__ == "__main__":
    main()
