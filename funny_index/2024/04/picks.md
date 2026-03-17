# Skill Tree Unlocks - 2024-04

> patch notes for the AI civilization, April 2024 edition

Total picks: 4

---

## 1. [Phi-3 Technical Report: A Highly Capable Language Model Locally on Your Phone](https://huggingface.co/papers/2404.14219)

**`[BOSS DROP]`** | **ArXiv**: [2404.14219](https://arxiv.org/abs/2404.14219) | **Org**: Microsoft | **Upvotes**: 259 | **Date**: 2024-04-23

**Skill: "Pocket Titan" / 技能名：「口袋泰坦」**

**Category**: `Efficiency` | **Tags**: `small-model, mobile-inference, quality-compression, synthetic-data`

**Source**: [papers/2024/04/2024-04-23.md, Line 9](papers/2024/04/2024-04-23.md#L9)

**EN**: BOSS DROP: Pocket Titan. Phi-3-mini is a 3.8B parameter model that rivals Mixtral 8x7B and GPT-3.5 quality — and it runs on your phone. Trained on high-quality filtered data and synthetic data, it punches 10x above its weight. The boss of "small models that actually work" just dropped. No more cloud dependency for serious inference.

**CN**: BOSS 掉落：口袋泰坦。Phi-3-mini 只有 38 亿参数，却能匹敌 Mixtral 8x7B 和 GPT-3.5 的质量——而且能在你手机上跑。用高质量过滤数据和合成数据训练，以十分之一的体量打出十倍伤害。"小模型也能打"的 Boss 刚刚掉落。严肃推理不再依赖云端。

---

## 2. [Jamba: A Hybrid Transformer-Mamba Language Model](https://huggingface.co/papers/2403.19887)

**`[COMBO]`** | **ArXiv**: [2403.19887](https://arxiv.org/abs/2403.19887) | **Org**: AI21 Labs | **Upvotes**: 112 | **Date**: 2024-04-01

**Skill: "Chimera" / 技能名：「嵌合体」**

**Category**: `Architecture` | **Tags**: `hybrid-architecture, transformer-mamba, MoE, long-context`

**Source**: [papers/2024/04/2024-04-01.md, Line 9](papers/2024/04/2024-04-01.md#L9)

**EN**: COMBO DISCOVERED: Chimera. Jamba fuses Transformer layers, Mamba (SSM) layers, and mixture-of-experts into one model. 256K context window, fits on a single 80GB GPU. The first production-grade hybrid architecture. Instead of choosing Transformer OR Mamba, just use both. The architecture skill tree just unlocked a fusion branch.

**CN**: 发现组合技：嵌合体。Jamba 把 Transformer 层、Mamba（SSM）层和混合专家塞进一个模型。256K 上下文窗口，单卡 80GB 就能跑。第一个生产级混合架构。不用在 Transformer 和 Mamba 之间二选一了，全都要。架构技能树刚刚解锁了融合分支。

---

## 3. [Mixture-of-Depths: Dynamically allocating compute in transformer-based language models](https://huggingface.co/papers/2404.02258)

**`[NEW SKILL]`** | **ArXiv**: [2404.02258](https://arxiv.org/abs/2404.02258) | **Org**: Google DeepMind | **Upvotes**: 107 | **Date**: 2024-04-04

**Skill: "Speed Reader" / 技能名：「一目十行」**

**Category**: `Efficiency` | **Tags**: `dynamic-compute, token-routing, layer-skipping, compute-efficiency`

**Source**: [papers/2024/04/2024-04-04.md, Line 9](papers/2024/04/2024-04-04.md#L9)

**EN**: NEW SKILL UNLOCKED: Speed Reader. Not all tokens need the same amount of thinking. Mixture-of-Depths lets the model dynamically skip layers for easy tokens and use full depth for hard ones — like a reader who skims filler words but slows down for key concepts. Uses 50% less compute with no quality loss. The "allocate compute where it matters" passive just got unlocked.

**CN**: 新技能解锁：一目十行。不是所有 token 都需要同样的思考量。Mixture-of-Depths 让模型对简单 token 动态跳过层、对难 token 用满深度——就像读者扫过废话、在关键概念处放慢。省一半算力，质量不降。"把算力用在刀刃上"的被动技能刚刚解锁。

---

## 4. [Rho-1: Not All Tokens Are What You Need](https://huggingface.co/papers/2404.07965)

**`[NERF ALERT]`** | **ArXiv**: [2404.07965](https://arxiv.org/abs/2404.07965) | **Org**: Microsoft Research | **Upvotes**: 94 | **Date**: 2024-04-12

**Skill: "Token Diet" / 技能名：「挑食训练」**

**Category**: `Training` | **Tags**: `selective-training, excess-loss, token-scoring, data-efficiency`

**Source**: [papers/2024/04/2024-04-12.md, Line 9](papers/2024/04/2024-04-12.md#L9)

**EN**: NERF ALERT: Token Diet. Standard pre-training treats all tokens equally — we've been force-feeding the model junk food. Rho-1 uses a reference model to score tokens by "excess loss" and only trains on the most useful ones. Training on 70% of tokens gives equal or better results. The "train on everything" meta just got nerfed. Selective diet wins.

**CN**: 削弱警告：挑食训练。标准预训练对所有 token 一视同仁——我们一直在给模型硬塞垃圾食品。Rho-1 用参考模型按"超额损失"给 token 打分，只训练最有用的那些。用 70% 的 token 训练就能得到同等或更好的结果。"全吃"流派刚刚被削。挑食才是正道。

---
