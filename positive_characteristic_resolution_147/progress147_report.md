# 任意维正特征奇点消解研究推进 147.0

## 有限 étale 相对完全点簇、Hoskin–Deligne 向量束秩与正维余项族编译器

- **英文标题：** *Finite-Étale Relative Complete Clusters, a Hoskin–Deligne Bundle Rank, and a Compiler for Positive-Dimensional Residual Families*
- **推进日期：** 2026-07-27
- **主提示词：** 任意维正特征奇点消解迭代研究总提示词 v2.0（强化版）
- **算法版本：** `R-v147-AC`（高维相对余项证书类）
- **唯一开放核心：** `FPCRNR = Finite-Presentation Confined Reachability and No-Rebirth`
- **战略基线：** 145.0 六层证书编译器与七个桥接定理。
- **严格输入基线：** 0.0–146.0，尤其是 146.0 的 complete residual point forest 与 surface finite-Rees compiler。

## 最终真实性边界

147.0 **没有**解决任意维正特征奇点消解。它关闭的是下列严格证书类：

> 在完美域上，设 `S` 光滑，`W→S` 为相对维数二的光滑态射，当前有限 Rees owner 经齐次幂压缩、积分闭包和除子提取后，其余项商 `O_W/K` 对 `S` 有限局部自由；再假设该 complete residual family 在一个有限 étale 覆盖后具有一个有限、等变、同时实现的 complete base-point/proximity forest，并且每个暴露根都携带当前 owner 的逐 degree 支付证书。则存在有限个普通光滑中心爆破，使 transformed Rees algebra 的奇异轨迹为空；该过程与 étale 基变换相容，并具有相对 Hoskin–Deligne 严格下降和 no-rebirth。

这个结论允许 `dim S>0`，所以余项支撑在总空间中可以是正维的，环境维数 `dim W=dim S+2` 可以任意大。真正尚未解决的是：从任意高维 Rees 状态**自动构造**上述 simultaneous complete-cluster certificate；处理 cluster type 跳变、非平坦/分歧碰撞、Frobenius-additive coupling、kangaroo、纯不可分下降以及一般高维 active-support strata。

---

# S1 前沿复述

146.0 已把任意有限曲面 Rees owner 压缩为加权活动支撑、Cartier、complete 点树与 monomial 四阶段有限编译器。高维第一缺口是余项支撑正维后，长度不再是局部 Artinian 长度，且 constant Hilbert/flatness 并不自动给光滑中心或稳定的 infinitely-near point forest。

# S2 任务锁定

唯一主任务取 `Q147-1 relative complete-module forest`。目标不是立即处理任意正维余项，而是找到一个非平凡、可全图表、可 étale 下降、具有精确终止秩的最大首批证书类，并同时给出两个最小反例，证明“常 Hilbert 多项式”本身远远不够。

# S3 主体执行

## 3.1 相对 complete residual 状态

固定：

1. `k` 为完美域；
2. `S` 为连通光滑 `k`-scheme；
3. `π:W→S` 为相对维数二的光滑态射；
4. `E` 为相对 SNC 历史边界；
5. `G` 为 `W` 上有限生成 Rees algebra。

对 `G` 做 144–146 的 homogeneous power compression，得到 marked pair `(J,b)`；随后取积分闭包并分解

`\bar J = O_W(-D) K`，

其中 `D` 为相对 Cartier 除子，`K` 在每个几何纤维的余维一处为单位。147.0 只在下列输入门槛通过时进入相对余项层：

- `D_red+E` 在当前 owner-active locus 上已经 relative SNC；
- `F=O_W/K` 对 `S` 有限局部自由；
- 每个几何纤维 `K_s` 是二维正则局部环境中的 finitely supported complete ideal packet；
- 存在下面定义的 finite-étale relative complete-cluster certificate。

## 3.2 定义 D-147-01：FERCC 证书

称 `(W/S,E,K)` 带有 **FERCC**（Finite-Étale Relative Complete-Cluster）证书，如果存在有限 étale 满射 `S'→S`，以及在 `W'=W×_S S'` 上的有限有向 proximity forest `T`，满足：

1. 每个顶点 `v` 对应某一 successive relative blowup model `W_v→S'` 上的有限 étale、闭、两两不交的 smooth multisection `C_v`；
2. 父子关系精确表示第一次邻域中的 infinitely-near successor；
3. 每个顶点带 locally constant 正整数 `r_v`，等于 fibrewise complete transform 在该根的 order；
4. 对每个几何点 `s'→S'`，`T_{s'}` 恰为 `K_{s'}` 的完整 finite base-point/proximity forest，不遗漏任何正 point-basis entry；
5. 对覆盖群胚的每个箭头，顶点、边、orders、birth IDs 与 owner-payment certificates 等变；
6. 当前可执行顶点是尚未归档且所有祖先已经执行的 exposed roots；每个 active exposed orbit batch `C` 都通过
   `\bar J_n ⊂ I_C^b`
   和 relative-SNC 检验；
7. 变换后 child packet 由 complete transform 给出，不允许用 raw weak transform 或单一长度替代；
8. 证书带完整 archive/provenance：新顶点只能由既有父顶点产生，禁止 external birth。

FERCC 是可核验的有限证书，但 147.0 **不证明**任意 relative residual family 自动具有 FERCC。

## 3.3 L-147-01：相对 Hoskin–Deligne 向量束秩公式

设 FERCC 证书成立，记 `d_v=deg(C_v/S')`。则

`H_rel(K/S)=rank_S π_*(O_W/K)`

存在且满足

`H_rel(K/S)=Σ_{v∈T} d_v binom(r_v+1,2)`。

### 证明

`O_W/K` 对 `S` 有限局部自由，故其 rank 等于任一几何纤维长度。有限 étale 拉回保持 rank。对每个几何纤维，146.0 使用的二维 Hoskin–Deligne 点基公式给出

`length(O_{W_s}/K_s)=Σ_{v|s}[κ(v):κ(s)] binom(r_v+1,2)`。

FERCC 的 orders 与 finite-étale degrees 局部常值，右端在连通基上常值，并等于向量束 rank。该等式在有限 étale 覆盖上成立，因而下降到 `S`。证毕。

**关键点：** 这里的 `H_rel` 不是把每个总空间局部环做 Artinian 长度；它是有限局部自由商的基上 rank，并由每个纤维的完整 point forest 计算。

## 3.4 L-147-02：相对根分裂精确下降

设 `C` 是 active exposed roots 的完整有限 étale 轨道 batch，轨道中每个根 order 为 `r_C`，degree 为 `d_C`。沿 `C` 爆破，取 complete transforms，并把所有 children 暴露，则

`H_rel(K'/S)=H_rel(K/S)-d_C binom(r_C+1,2)`。

若 batch 含不同 order 的不交轨道，则下降量为对应和。

### 证明

有限 étale 基变换后，`C` 分裂成不交 sections。爆破与 flat base change 相容；strict/complete transform 与 étale localization 相容。逐几何纤维应用 146.0 的 Hoskin–Deligne root-splitting：父根的贡献被删除，其余正 point-basis entries恰按第一邻域 children 分组。求和并按 finite-étale degree下降。由于至少一个 active root 的 `r_C>0`，下降严格。证毕。

## 3.5 L-147-03：有限 étale 轨道中心的普通光滑下降

FERCC 中任一 exposed orbit batch 在 `S'` 上是有限个不交 sections；section of a smooth morphism 是 regular immersion。群胚等变的完整轨道并下降为 `W` 上有限 étale于 `S` 的 closed smooth center `C`。若 payment 与 relative-SNC certificates 在覆盖上成立，则由忠实平坦下降，它们在 `W` 上成立。沿该中心的 blowup 拉回到 `S'` 后等于 split batch blowup。

因此，147.0 的中心是原空间上的**普通光滑中心**，不是把 cover 上任意一个 branch 当中心，也不是 alteration。

## 3.6 L-147-04：dormant subtree 剪枝与 no-rebirth

在 Cartier normalization 后，若 exposed root `v` 满足

`ord_v(K)+ν_v(D)<b`，

则 `v` 不在当前 `Sing(\bar J,b)`，将其及尚未暴露的全部 descendants 归档。以后：

1. 其他 active root batches 与该已归档根的邻域不交；
2. Cartier quotient 只降低 divisorial weights；
3. complete transforms 的新 roots 只能来自被执行顶点的 registered children；
4. monomial phase 只在 residual-unit locus 执行。

故该 subtree 不能在无父祖先的情况下重新 active。若未来某一注册 descendant 被暴露，它必带同一 ancestor lineage，且在父根已经执行的分支中；不会产生跨树重生。

## 3.7 T-147-01：FERCC Relative Residual Compiler

在 3.1 的设置和 FERCC 门槛下，执行：

1. power compression 与 integral closure；
2. 计算 `\bar J=O(-D)K`；
3. 只在 relative-SNC 已准备的 active locus 进入本层；
4. 对高权 smooth relative Cartier components 做有限 controlled extraction，使余数权重在 `[0,b-1]`；
5. 在 finite étale split cover 上计算 exposed roots，但每次只选择完整下降轨道 batch；
6. 归档 owner-dormant roots；
7. 对全部 active exposed batch 执行 ordinary blowup，更新 complete transforms 和 proximity forest；
8. 用 L-147-02 严格降低 `H_rel`；
9. `H_rel=0` 后进入真实 relative marked-monomial/SNC terminal，并调用 132–136 的无标号组合模块。

则算法有限终止，且 transformed Rees algebra 的 singular locus 为空。

### 证明

- 所有中心的闭性、光滑性、owner containment、boundary compatibility 与 descent 由 FERCC 和 L-147-03 给出；
- Cartier microsteps 数量有限；
- 每个 residual blow block 使非负整数 `H_rel` 至少下降一；
- `H_rel=0` 等价于 `K=O_W`，因此余项层不会残留正维 hidden support；
- 此后状态是真实的 relative SNC marked monomial state，已有组合秩有限终止；
- L-147-04 排除 support/Cartier/residual/monomial 之间循环。

证毕。

## 3.8 T-147-02：相对有限可达性与无重生

定义 phase

- `P=2`：Cartier normalization；
- `P=1`：FERCC residual forest；
- `P=0`：relative monomial terminal。

定义序和秩

`Xi_147^rel=(P,Q_Cartier,H_rel,Omega_forest,Omega_mon)`，

其中 `Omega_forest` 保存 exposed frontier、未归档顶点的 ancestry multiset 和 stable IDs，但终止的主要整数预算是 `H_rel`。

每个认证 block 后 `Xi_147^rel` 严格下降；所有 birth 都来自有限 forest 的父边，所有 finite-étale conjugates 以完整轨道 batch 更新，因此 registry finite reachable，且无跨模块重生。

## 3.9 代表算例 A：乘积长链 `K_m=(x,y^m)`

令 `W=S×Spec k[x,y]`，`K_m=(x,y^m)`。则 `O_W/K_m` 对 `S` 自由 rank `m`。FERCC 是一条长度 `m` 的 section chain，每个 point-basis entry 为 `1`，故

`H_rel=m`。

沿 section `x=y=0` 爆破。在 `y`-chart，`x=yX`，complete transform 为 `(X,y^{m-1})`；`x`-chart residual 为单位。因而

`m→m-1→…→1→0`。

这是真正的正维余项例：当 `dim S>0` 时，每个中心都与 `S` 同维，而非闭点。

## 3.10 代表算例 B：有限 étale monodromy

设 `S=Spec k[t,t^{-1}]`，在一个有限 étale cover `S'=Spec k[u,u^{-1}]`, `u^n=t` 上，余项 forest 的 roots 是由群作用置换的 `n` 个不交 sections。单独选择一个 section 不下降；选择完整轨道 batch 得到 `S` 上有限 étale smooth center。相对 HD 下降量乘以轨道 degree `n`。该例说明“无标号”应理解为 orbit-invariant，而非人为排序。

## 3.11 X-147-01：常 Hilbert/finite flat 不保证光滑中心

取

`A=k[t,x,y]`, `K=(x, y(y-t))`。

因为 `y^2=ty`，`A/K` 是 `k[t]`-自由模，基为 `{1,y}`，rank 恒为 `2`。但 support

`Z=V(x,y(y-t))`

是两条 sections `y=0` 与 `y=t` 的并，在 `t=x=y=0` 相交。Jacobian 对 `(x,y,t)` 的行在该点 rank 下降；`Z` 的局部环有两个分支，故 total center 不光滑。

因此：constant Hilbert polynomial、finite flatness 与有限 Fitting 数据本身不产生合法 smooth center。

## 3.12 X-147-02：光滑支撑和常长度仍不决定 point forest

取

`A=k[t,x,y]`, `K=(x^2,xy,y^3-tx)`。

由 relations `x^2=xy=0`, `y^3=tx`，商 `A/K` 对 `k[t]` 自由，基 `{1,x,y,y^2}`，rank 恒为 `4`；radical 为 `(x,y)`，支撑是光滑 section。

- 在 `t=0` 纤维，`K_0=(x^2,xy,y^3)`，complete point basis 为 `(2,1)`，HD 能量 `3+1=4`；
- 在 `t≠0`，令 `u=x-t^{-1}y^3`，则理想化为 `(u,y^4)`，point basis 为 `(1,1,1,1)`，HD 能量仍为 `4`。

所以 support 与 Hilbert rank 均相同，但 infinitely-near forest 类型跳变。任何只存 `{support,rank}` 的规则都无法有限更新下一中心。

## 3.13 X-147-03：有限但分歧的 support 不进入 FERCC

取 `K=(x,y^2-t)`。商对 `k[t]` 自由 rank `2`，但 support 到 `S` 在 `t=0` 分歧，不是有限 étale；它不能在有限 étale cover 后变成不交 sections。这个例子不证明它不可消解，只证明 FERCC 的 orbit-section descent 不适用于 ramified collision，必须另建 discriminant/ramification block。

## 3.14 显著推进门槛结算

147.0 的增量不是把 146.0 与 `S` 做形式乘积后换名。实质新步骤有四个：

1. 把二维 local colength 提升为有限局部自由商的 **relative HD bundle rank**；
2. 证明 finite-étale simultaneous complete forest 下根分裂具有精确 degree-weighted 下降；
3. 把 split sections 的选择编译为原空间上的无标号 orbit center，并证明普通光滑下降；
4. 用两个平坦族反例严格分离“Hilbert flatness”“smooth support”“constant point-cluster type”三层条件。

这关闭了 145.0 桥接定理 6.4 的第一个非平凡正维证书类，但没有关闭一般 relative residual block。

# S4 怀疑者审查

## 4.1 最薄弱处

FERCC 把最困难的 simultaneous base-point effectivity 作为输入证书。若把它误写成由 constant Hilbert polynomial 自动推出，则 147.0 立即被 X-147-01 与 X-147-02 击毁。

## 4.2 真实反驳尝试

尝试删除 FERCC 的 proximity forest，仅保存 `F=O/K` 的 Fitting strata、support 和 rank。X-147-02 给出 smooth support、finite free rank 4，却在 special/generic fibre 分别出现 `(2,1)` 与 `(1,1,1,1)`。下一次 root blow 后 children 数量与 orders 不同，故有限后继无法由缩减状态恢复。反驳成功：完整 forest 或等价信息不可删除。

尝试只要求 finite flat support，不要求 finite étale。X-147-01 的碰撞 union 是 finite flat rank 2 但不光滑；直接爆 support 违反 Z2。反驳成功。

## 4.3 未被解决的攻击

- FERCC 是否可由 normalized blowup、relative Hilbert scheme、complete-ideal factorization和 flattening有限地自动发现？未证。
- cluster type 在边界跳变时，是否可先爆一个 owner-paid smooth discriminant stratum使其常化？未证。
- Frobenius coefficient packet 是否与 relative residual forest共享同一合法中心？未证。
- 不完美域上 regular finite center是否 smooth？未处理。

# S5 裁判结算

## 新定义

- `D-147-01 FERCC`：finite-étale relative complete-cluster certificate。
- `D-147-02 H_rel`：relative Hoskin–Deligne bundle rank。
- `D-147-03 orbit-root batch`：完整有限 étale 共轭暴露根批次。

## 新引理

- `L-147-01` Relative Hoskin–Deligne Bundle Rank Formula。
- `L-147-02` Degree-Weighted Relative Root-Splitting。
- `L-147-03` Finite-Étale Orbit-Center Descent。
- `L-147-04` Dormant-Subtree Pruning and No-Rebirth。

依赖：二维 complete-ideal Hoskin–Deligne 公式、有限局部自由 rank 的 fibre 判定、section of smooth morphism 为 regular immersion、blowup/strict transform 与 flat/étale base change相容、146.0 complete-transform registry。

## 新定理

- `T-147-01` FERCC Relative Residual Compiler。
- `T-147-02` FERCC Finite Reachability and No-Rebirth。

二者均为**证书类定理**，不依赖 C/WH；但输入中明确包含 FERCC certificate。

## 新反例

- `X-147-01` finite-flat collision support 非光滑。
- `X-147-02` smooth support + constant rank 不决定 point forest。
- `X-147-03` ramified finite support 不进入 finite-étale section tier。

## 新猜想

`C-147-01 Intrinsic FERCC Stratification`，置信度 `32%`：对 integral-complete relative codimension-two residual module，存在由 normalized blowup、relative Fitting/Hilbert 数据、proximity incidence 与 normal flatness定义的有限 stratification；在每个 stratum 上取得 FERCC，边界进入严格较低基维或更高 leading/Frobenius 缺陷。

最可能死因：cluster stack 可能需要非有限 étale而是 ramified/Artin groupoid；flattening strata可能奇异；complete ideal factorization在家族中可能出现无界 base-point specialization；正特征 Frobenius jumps可与 cluster boundary耦合。

## 新缺口

- `G-147-01` 自动构造 FERCC。
- `G-147-02` cluster-type boundary 的 owner-paid smooth stratification。
- `G-147-03` ramified collision 与不完美域 descent。
- `G-147-04` Frobenius-residual shared-center theorem。
- `G-147-05` kangaroo fuel 与相对 forest 的联合序和。

# S6 算法版本 R-v147-AC

输入当前状态 `Σ`：

1. 执行 homogeneous power compression、integral closure 与 Rees provenance冻结；
2. 分解 `\bar J=O(-D)K`；
3. 所有中心先过 closed、smooth、current-owner-contained、relative-SNC、descent 五重硬过滤；
4. 若 active divisorial support 未 relative SNC，退出本 tier并返回 `G-147-02`；
5. 检查 `O/K` 是否 finite locally free over a smooth base `S`；失败则返回 `G-147-01/02`；
6. 构造或读取 FERCC；检查 fibre completeness、proximity、orders、finite-étale cocycle和无 external birth；
7. 执行有限 Cartier quotient；
8. 归档 owner-dormant exposed roots；
9. 对 remaining active exposed roots 取完整有限 étale orbit batch；
10. 沿下降后的普通 smooth center 爆破，计算 complete transforms；
11. 验证 `H_rel` 按 L-147-02 精确下降，否则立即输出 gap；
12. `H_rel=0` 后仅在 residual-unit locus进入 relative marked-monomial scheduler；
13. cluster jump、ramification、nonflatness、positive relative fibre dimension、Frobenius-additive/kangaroo state不得伪装成 FERCC。

相对于 `R-v146-AB`，新版本保留所有 surface phases；新增 finite-étale relative cluster state、degree-weighted HD rank、orbit descent和三个明确退出门槛。

# S7 队列刷新

1. `Q148-1 intrinsic FERCC detection`：从 normalized blowup 与 relative complete-ideal factorization构造 certificate，而不是外加 forest。
2. `Q148-2 cluster-boundary compiler`：对 X-147-01/02 的碰撞与类型跳变构造 owner-paid discriminant/normal-flat smooth strata。
3. `Q148-3 Frobenius-residual collision`：研究 `z^{p^e}+F` 的 coefficient packet与 FERCC root batch是否共享中心。
4. `Q148-4 ramified/imperfect descent`：区分 smooth、regular、radicial multisections并寻找原底域替代 block。
5. `Q148-5 kangaroo-relative ordinal sum`：把 finite fuel与 `H_rel`、proximity ancestry合成无重置秩。

# S8 新版 RSF 摘要

- **轮次：** 147.0
- **算法：** `R-v147-AC`
- **主轨道：** A，Rees/idealistic-filtration 证书编译。
- **已关闭新层：** smooth base 上 relative surface family 的 FERCC positive-dimensional residual tier。
- **最强结论：** `T-147-01/02`。
- **失败博物馆新增：** X-147-01–03。
- **当前最深前沿：** 从任意 integral-complete relative residual module 内禀产生 FERCC，并清理 cluster-type boundary。
- **真实性声明：** 任意维正特征奇点消解仍开放；147.0 是任意环境维数中的一个严格正维余项证书类，而非一般高维定理。

## 仪表盘

在 FERCC tier 内：`(Z1,Z2,Z3,Z4,Z5)=(100,100,100,100,100)`。

对任意维主问题，本轮的真实增量集中在 Z3–Z5 的一个新正维证书类；一般状态的 Z1/Z2 仍被 `G-147-01/02/04` 阻断，不能用 tier 内满分替代全局完成度。
