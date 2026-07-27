#!/usr/bin/env python3
"""Apply the final hostile-audit corrections before publication.

The key correction distinguishes the full relative HD bundle rank H_tot from
the active termination energy H_act. Archiving a dormant subtree lowers
H_act but does not pretend that the residual ideal became a unit.
"""
from pathlib import Path

# Markdown report
p=Path(__file__).with_name('progress147_report.md')
s=p.read_text(encoding='utf-8')
s=s.replace(
"7. 变换后 child packet 由 complete transform 给出，不允许用 raw weak transform 或单一长度替代；",
"7. 对任一允许执行前缀，新的余项商仍 finite locally free over `S'`，其剩余 fibre forest 恰由 complete transform 给出；禁止用 raw weak transform 或单一长度替代；")
s=s.replace(
"`H_rel(K/S)=rank_S π_*(O_W/K)`\n\n存在且满足\n\n`H_rel(K/S)=Σ_{v∈T} d_v binom(r_v+1,2)`。",
"定义完整束秩 `H_tot(K/S)=rank_S π_*(O_W/K)`，则\n\n`H_tot(K/S)=Σ_{v∈T} d_v binom(r_v+1,2)`。\n\n终止时另使用 active energy\n\n`H_act=Σ_{v 尚未执行且未归档} d_v binom(r_v+1,2)`。\n\n归档 dormant subtree 只降低 `H_act`，不声称 `K` 已成为单位。")
s=s.replace("**关键点：** 这里的 `H_rel`", "**关键点：** 这里的 `H_tot`")
s=s.replace(
"`H_rel(K'/S)=H_rel(K/S)-d_C binom(r_C+1,2)`。",
"`H_tot(K'/S)=H_tot(K/S)-d_C binom(r_C+1,2)`。若该根未归档，同一步也使 `H_act` 减去相同正整数。")
s=s.replace("8. 用 L-147-02 严格降低 `H_rel`；", "8. 用 L-147-02 严格降低 `H_tot` 与 `H_act`；dormant archive 则仅严格降低 `H_act`；")
s=s.replace("9. `H_rel=0` 后进入真实 relative marked-monomial/SNC terminal", "9. `H_act=0` 后，所有剩余 residual branches 均已 certified dormant；只在其补集进入真实 relative marked-monomial/SNC terminal")
s=s.replace("- 每个 residual blow block 使非负整数 `H_rel` 至少下降一；", "- 每个 residual blow block 或 dormant-archive transition 使非负整数 `H_act` 至少下降一；")
s=s.replace("- `H_rel=0` 等价于 `K=O_W`，因此余项层不会残留正维 hidden support；", "- `H_act=0` 不要求 `K=O_W`；它精确表示剩余 residual support 全部 owner-dormant。后续中心限制在其补集，L-147-04 保证这些邻域不再激活；")
s=s.replace("`Xi_147^rel=(P,Q_Cartier,H_rel,Omega_forest,Omega_mon)`", "`Xi_147^rel=(P,Q_Cartier,H_act,Omega_forest,Omega_mon)`")
s=s.replace("`Omega_forest` 保存 exposed frontier、未归档顶点的 ancestry multiset 和 stable IDs，但终止的主要整数预算是 `H_rel`。", "`Omega_forest` 保存 exposed frontier、未归档顶点的 ancestry multiset 和 stable IDs；终止的主要整数预算是 `H_act`，而 `H_tot` 作为完整束秩与 fibrewise 审计恒等式保留。")
s=s.replace("故\n\n`H_rel=m`。", "故\n\n`H_tot=H_act=m`。")
s=s.replace("degree-weighted HD rank", "degree-weighted HD total/active rank")
p.write_text(s,encoding='utf-8')

# TeX report
p=Path(__file__).with_name('progress147_full_derivation.tex')
s=p.read_text(encoding='utf-8')
s=s.replace("\\newcommand{\\Hrel}{\\mathscr H_{\\mathrm{rel}}}", "\\newcommand{\\Hrel}{\\mathscr H_{\\mathrm{rel}}}\n\\newcommand{\\Htot}{\\mathscr H_{\\mathrm{tot}}}\n\\newcommand{\\Hact}{\\mathscr H_{\\mathrm{act}}}")
s=s.replace(
"\\item 变换后保存 complete transform 与完整 proximity 数据，禁止以 raw weak transform 或单一长度替代；",
"\\item 对任一允许执行前缀，新的余项商仍 finite locally free over $S'$，且剩余 fibre forest 恰由 complete transform 给出；禁止以 raw weak transform 或单一长度替代；")
s=s.replace("\\Hrel(K/S):=\\operatorname{rank}_S\\pi_*F.", "\\Htot(K/S):=\\operatorname{rank}_S\\pi_*F.")
s=s.replace("\\Hrel(T):=\\sum_{v\\in T}", "\\Htot(T):=\\sum_{v\\in T}")
s=s.replace("\\operatorname{rank}_S\\pi_*(\\cO_W/K)\n=", "\\Htot(K/S)=\\operatorname{rank}_S\\pi_*(\\cO_W/K)\n=")
s=s.replace("\\Hrel(K'/S)=\\Hrel(K/S)-d\\binom{r+1}{2}.", "\\Htot(K'/S)=\\Htot(K/S)-d\\binom{r+1}{2}.\n\\]\n若该 orbit 未归档，则 active energy\n\\[\n\\Hact(K'/S)=\\Hact(K/S)-d\\binom{r+1}{2}.")
s=s.replace("\\item 由 L-147-02 严格降低非负整数 $\\Hrel$；", "\\item ordinary residual blow 由 L-147-02 同时严格降低 $\\Htot$ 与 $\\Hact$；dormant archive 只降低 $\\Hact$；")
s=s.replace("\\item $\\Hrel=0$ 后，$K=\\cO_W$，状态进入真实 relative marked-monomial/SNC terminal", "\\item $\\Hact=0$ 后，所有剩余 residual branches 均 certified dormant；算法只在其补集进入真实 relative marked-monomial/SNC terminal")
s=s.replace("每个 residual block 使 $\\Hrel$ 严格下降，", "每个 residual blow 或 archive transition 使 $\\Hact$ 严格下降，")
s=s.replace("(P,Q_{\\mathrm{Cartier}},\\Hrel,\\Omega_{\\mathrm{forest}},\\Omega_{\\mathrm{mon}})", "(P,Q_{\\mathrm{Cartier}},\\Hact,\\Omega_{\\mathrm{forest}},\\Omega_{\\mathrm{mon}})")
s=s.replace("residual phase 的 $\\Hrel$ 由 L-147-02 严格下降；", "residual blow 的 $\\Hact$ 由 L-147-02 严格下降，dormant archive 亦删除一个正 subtree contribution；")
s=s.replace("故 $\\Hrel=m$。", "故 $\\Htot=\\Hact=m$。")
s=s.replace("degree-weighted HD rank", "degree-weighted HD total/active rank")
# Insert the active-energy definition after the complete rank definition.
needle="若 $C_v\\to S'$ 的 degree 为 $d_v$，则 FERCC 的点基表达式候选为"
replacement="若 $C_v\\to S'$ 的 degree 为 $d_v$，则完整束秩由全部 remaining vertices 计算。另定义终止能量\\[\n\\Hact:=\\sum_{v\\ \mathrm{unexecuted,unarchived}}d_v\\binom{r_v+1}{2}.\n\\]\n归档只降低 $\\Hact$，不声称 $K$ 成为单位。则 FERCC 的点基表达式为"
s=s.replace(needle,replacement)
p.write_text(s,encoding='utf-8')

# Baseline delta and RSF
p=Path(__file__).with_name('positive_characteristic_resolution_master_memory_147_delta.md')
s=p.read_text(encoding='utf-8')
s=s.replace("`H_rel(K/S)=rank_S π_*(O_W/K)`；在 FERCC 上\n\n`H_rel=Σ_v", "完整束秩 `H_tot(K/S)=rank_S π_*(O_W/K)`；在 FERCC 上\n\n`H_tot=Σ_v")
s=s.replace("`Xi_147^rel=(P,Q_Cartier,H_rel,Omega_forest,Omega_mon)`", "`Xi_147^rel=(P,Q_Cartier,H_act,Omega_forest,Omega_mon)`，其中 `H_act` 只对未执行且未归档顶点求和；`H_tot` 保留作 fibrewise bundle-rank audit")
s=s.replace("11. `H_rel` 精确下降；\n12. `H_rel=0` 后", "11. residual blow 使 `H_tot/H_act` 同量下降，archive 使 `H_act` 下降；\n12. `H_act=0` 后只在 dormant support 补集")
p.write_text(s,encoding='utf-8')

p=Path(__file__).with_name('RSF_v147.md')
s=p.read_text(encoding='utf-8')
s=s.replace("Xi_147^rel=(phase,Q_Cartier,H_rel,Omega_forest,Omega_mon)", "Xi_147^rel=(phase,Q_Cartier,H_act,Omega_forest,Omega_mon)，并保留H_tot=rank_S pi_*(O/K)作完整束秩审计")
p.write_text(s,encoding='utf-8')
print('ROUND147_HOSTILE_AUDIT_CORRECTIONS_APPLIED')
