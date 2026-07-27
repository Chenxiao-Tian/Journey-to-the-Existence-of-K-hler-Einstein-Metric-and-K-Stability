# 研究推进 147.0 基线增量

> 本文件是 `positive_characteristic_resolution_master_memory_0_146.md` 的规范追加段。完整逻辑基线定义为：`0_146 master + 145 strategic baseline + this 147 delta`。147.0 不覆盖或删除此前 G/X/撤销项。

## 推进 147.0：有限 étale 相对完全点簇、Hoskin–Deligne 向量束秩与正维余项族编译器

- **英文标题：** *Finite-Étale Relative Complete Clusters, a Hoskin–Deligne Bundle Rank, and a Compiler for Positive-Dimensional Residual Families*
- **推进日期：** 2026-07-27
- **主提示词：** 任意维正特征奇点消解迭代研究总提示词 v2.0（强化版）
- **唯一开放核心：** `FPCRNR = Finite-Presentation Confined Reachability and No-Rebirth`
- **算法版本：** `R-v147-AC`（高维相对余项证书类）
- **显著推进门槛：** 通过。首次把 146.0 的零维曲面 complete-point forest 提升为任意环境维数中的正维 finite-étale relative forest compiler，并以 degree-weighted relative Hoskin–Deligne bundle rank 严格终止；同时以两个有限平坦族反例证明 constant Hilbert、smooth support 与 constant cluster type 不可混同。
- **真实性边界：** 本轮不自动构造 FERCC，不处理 cluster-type jump boundary、ramified collision、非平坦余项、正相对纤维维数、Frobenius-additive/kangaroo 或不完美域。不是任意维正特征奇点消解证明。

## S1 前沿复述

146.0 完整关闭 smooth surface finite-Rees singular-locus resolution。高维余项支撑正维后，surface colength 不再定义；flatness/Hilbert 数据又不自动给 smooth center 或 stable point forest。

## S2 唯一任务

`Q147-1 relative complete-module forest`：构造首个具有普通光滑中心、étale descent、全图表 complete transform、精确整数 rank 与 no-rebirth 的正维余项证书类。

## S3 新状态接口

### D-147-01 FERCC

在 `π:W→S` 相对光滑、相对维数二，`S` 光滑，`O_W/K` finite locally free 的状态中，FERCC 是有限 étale 覆盖后有限、等变、同时实现的 complete base-point/proximity forest。每个顶点携带 finite-étale multisection、point-basis order、parent ID、owner payment、boundary 与 descent cocycle。所有 births 只来自注册父边。

### D-147-02 relative HD bundle rank

`H_rel(K/S)=rank_S π_*(O_W/K)`；在 FERCC 上

`H_rel=Σ_v deg(C_v/S) binom(r_v+1,2)`。

### D-147-03 orbit-root batch

同一群胚轨道内的 exposed roots 必须完整同时选择；禁止选择 cover 上一个有标号 branch。

## S4 登记册

### 新引理

- `L-147-01 Relative Hoskin–Deligne Bundle Rank Formula`。
- `L-147-02 Degree-Weighted Relative Root-Splitting`。
- `L-147-03 Finite-Étale Orbit-Center Descent`。
- `L-147-04 Dormant-Subtree Pruning and No-Rebirth`。

### 新定理

- `T-147-01 FERCC Relative Residual Compiler`：FERCC certificate class 中有限普通 smooth-center word 使 transformed Rees singular locus 为空。
- `T-147-02 FERCC Finite Reachability and No-Rebirth`：`Xi_147^rel=(P,Q_Cartier,H_rel,Omega_forest,Omega_mon)` 严格下降。

### 新反例

- `X-147-01`：`K=(x,y(y-t))`，商 finite free rank 2，但 support 是碰撞 sections 的奇异并。
- `X-147-02`：`K=(x^2,xy,y^3-tx)`，smooth section support 与 rank 4 恒定，但 point basis 从 `(2,1)` 跳为 `(1,1,1,1)`。
- `X-147-03`：`K=(x,y^2-t)` finite free rank 2，但 ramified support 不进入 finite-étale orbit-section tier。

### 新猜想

`C-147-01 Intrinsic FERCC Stratification`，置信度 32%。最可能死因：ramified/Artin cluster groupoid、奇异 flattening strata、无界 base-point specialization、Frobenius-cluster coupling。

### 新缺口

- `G-147-01` 自动构造 FERCC。
- `G-147-02` cluster-type boundary 的 owner-paid smooth stratification。
- `G-147-03` ramified collision 与 imperfect-field descent。
- `G-147-04` Frobenius-residual shared-center theorem。
- `G-147-05` kangaroo fuel 与 relative forest 联合序和。

## S5 算法 R-v147-AC

1. homogeneous power compression、integral closure、provenance；
2. `bar J=O(-D)K`；
3. 五重合法性硬过滤；
4. relative active support 未 SNC 则退出；
5. 检查 `O/K` finite locally free；
6. 构造/读取 FERCC并审计 complete fibres、proximity、orders、cocycle与 no external birth；
7. 有限 Cartier quotient；
8. dormant subtree archive；
9. 完整 finite-étale orbit batch；
10. ordinary smooth blowup与 complete transforms；
11. `H_rel` 精确下降；
12. `H_rel=0` 后 relative marked-monomial terminal；
13. cluster jump、ramification、nonflatness、positive relative fibre dimension、Frobenius/kangaroo均返回 gap。

## S6 计算与例子库

- 新增例子 `EX-POS-165--171` 与 `EX-PATH-103--105`。
- 例子库采用 compositional version：`v4.4 = v4.3 (274 entries) + example_library_147_patch.jsonl (10 entries)`，共 284 entries；merge/validation 由 `merge_example_library_147.py` 执行。
- `progress147_calc.py` 校验 HD identities、product chains、随机 forests、orbit batches、dormant pruning、phase rank、三个反例代数与 patch hashes。

## S7 下一队列

1. `Q148-1 intrinsic FERCC detection`。
2. `Q148-2 cluster-boundary compiler`。
3. `Q148-3 Frobenius-residual collision`。
4. `Q148-4 ramified/imperfect descent`。
5. `Q148-5 kangaroo-relative ordinal sum`。

## S8 仪表盘

FERCC tier 内 `(Z1,Z2,Z3,Z4,Z5)=(100,100,100,100,100)`。任意维总体完成度不得由 tier 满分推断；一般中心存在仍被 `G-147-01/02/04` 阻断。
