# Skill Tree Unlocks - 2024-03

> patch notes for the AI civilization, March 2024 edition

Total picks: 4

---

## 1. [GaLore: Memory-Efficient LLM Training by Gradient Low-Rank Projection](https://huggingface.co/papers/2403.03507)

**`[NEW SKILL]`** | **ArXiv**: [2403.03507](https://arxiv.org/abs/2403.03507) | **Org**: - | **Upvotes**: 189 | **Date**: 2024-03-07

**Skill: "Memory Diet" / 技能名：「显存瘦身」**

**Category**: `Efficiency` | **Tags**: `low-rank, gradient-projection, memory-optimization, single-GPU-training`

**Source**: [papers/2024/03/2024-03-07.md, Line 9](papers/2024/03/2024-03-07.md#L9)

**EN**: NEW SKILL UNLOCKED: Memory Diet. GaLore projects gradients into a low-rank subspace during training, reducing optimizer memory by up to 65.5%. Train a 7B model on a single 24GB GPU without checkpointing tricks. Full-rank training quality at a fraction of the memory cost. The "out of memory" boss just got a lot easier to beat.

**CN**: 新技能解锁：显存瘦身。GaLore 在训练时将梯度投影到低秩子空间，优化器显存减少高达 65.5%。单卡 24GB GPU 即可训练 7B 模型，无需 checkpoint 技巧。全秩训练质量，几分之一的显存成本。「显存不足」Boss 突然好打多了。

---

## 2. [The Unreasonable Ineffectiveness of the Deeper Layers](https://huggingface.co/papers/2403.17887)

**`[BUG REPORT]`** | **ArXiv**: [2403.17887](https://arxiv.org/abs/2403.17887) | **Org**: - | **Upvotes**: 82 | **Date**: 2024-03-27

**Skill: "Dead Weight" / 技能名：「冗余之层」**

**Category**: `Architecture` | **Tags**: `layer-pruning, redundancy, Llama, Mistral`

**Source**: [papers/2024/03/2024-03-27.md, Line 9](papers/2024/03/2024-03-27.md#L9)

**EN**: BUG REPORT: Dead Weight. You can remove up to half the layers of popular LLMs (Llama, Mistral, Phi) with minimal impact on quality. The deeper layers are surprisingly redundant — they're doing almost nothing. We've been paying rent on half an apartment we don't use. Critical discovery: the architecture skill tree has been over-investing in depth.

**CN**: BUG 报告：冗余之层。你可以删掉流行 LLM（Llama、Mistral、Phi）最多一半的层，对质量影响微乎其微。深层出乎意料地冗余——它们几乎什么都没做。我们一直在为没用到的半间房付租金。关键发现：架构技能树在深度上过度投资了。

---

## 3. [MM1: Methods, Analysis & Insights from Multimodal LLM Pre-training](https://huggingface.co/papers/2403.09611)

**`[NEW SKILL]`** | **ArXiv**: [2403.09611](https://arxiv.org/abs/2403.09611) | **Org**: Apple | **Upvotes**: 129 | **Date**: 2024-03-15

**Skill: "Apple's Cookbook" / 技能名：「苹果秘方」**

**Category**: `Multimodal` | **Tags**: `vision-language, ablation-study, image-encoder, training-recipe`

**Source**: [papers/2024/03/2024-03-15.md, Line 9](papers/2024/03/2024-03-15.md#L9)

**EN**: NEW SKILL UNLOCKED: Apple's Cookbook. Apple's first major multimodal LLM paper. Systematically ablates every design choice: image encoder, data mix, training recipe. The takeaway? Image resolution and data diversity matter most; fancy architectures matter least. A cookbook for multimodal training. The "multimodal" skill tree just got a proper recipe book.

**CN**: 新技能解锁：苹果秘方。苹果第一篇重磅多模态 LLM 论文。系统消融了每个设计选择：图像编码器、数据配比、训练配方。结论？图像分辨率和数据多样性最重要；花哨架构最不重要。多模态训练的菜谱。「多模态」技能树刚刚有了正经配方书。

---

## 4. [Stealing Part of a Production Language Model](https://huggingface.co/papers/2403.06634)

**`[SIDE EFFECT]`** | **ArXiv**: [2403.06634](https://arxiv.org/abs/2403.06634) | **Org**: Google DeepMind | **Upvotes**: 91 | **Date**: 2024-03-12

**Skill: "API Pickpocket" / 技能名：「接口扒手」**

**Category**: `Safety` | **Tags**: `model-extraction, API-attack, architecture-leak, security`

**Source**: [papers/2024/03/2024-03-12.md, Line 9](papers/2024/03/2024-03-12.md#L9)

**EN**: SIDE EFFECT: API Pickpocket. By querying a production LLM API with less than $20, researchers extracted the exact hidden dimension and final projection matrix of OpenAI's models. You can steal part of a closed-source model's architecture through its API. A $20 attack that reveals proprietary model secrets. The "closed model" shield has an unexpected vulnerability.

**CN**: 副作用：接口扒手。通过不到 20 美元的 API 查询，研究人员提取了 OpenAI 模型的精确隐藏维度和最终投影矩阵。你可以通过 API 窃取闭源模型的部分架构。20 美元的攻击就能泄露专有模型秘密。「闭源模型」护盾有一个意想不到的漏洞。

---
