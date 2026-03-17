# Skill Tree Unlocks - 2023-12

> patch notes for the AI civilization, December 2023 edition

Total picks: 3

---

## 1. [Mamba: Linear-Time Sequence Modeling with Selective State Spaces](https://huggingface.co/papers/2312.00752)

**`[BOSS DROP]`** | **ArXiv**: [2312.00752](https://arxiv.org/abs/2312.00752) | **Org**: Carnegie Mellon / Princeton | **Upvotes**: 150 | **Date**: 2023-12-04

**Skill: "Mamba Strike" / 技能名：「黑曼巴」**

**Category**: `Architecture` | **Tags**: `SSM, selective-state-spaces, linear-time, transformer-alternative`

**Source**: [papers/2023/12/2023-12-04.md, Line 9](papers/2023/12/2023-12-04.md#L9)

**EN**: BOSS DROP: Mamba Strike. Transformers have ruled sequence modeling for years, but their quadratic attention cost is a bottleneck. Mamba introduces selective state spaces — an SSM that can selectively remember or forget based on input. Linear time complexity, no attention mechanism, yet matches or exceeds Transformer quality. The first real contender to dethrone the Transformer. The architecture meta just got a new boss drop.

**CN**: BOSS 掉落：黑曼巴。Transformer 统治序列建模多年，但二次方注意力成本是瓶颈。Mamba 引入选择性状态空间——一种能根据输入选择性记忆或遗忘的 SSM。线性时间复杂度，无注意力机制，却达到或超越 Transformer 质量。第一个真正有实力推翻 Transformer 的挑战者。架构流派刚刚掉落了新 Boss 装备。

---

## 2. [LLM in a flash: Efficient Large Language Model Inference with Limited Memory](https://huggingface.co/papers/2312.11514)

**`[NEW SKILL]`** | **ArXiv**: [2312.11514](https://arxiv.org/abs/2312.11514) | **Org**: Apple | **Upvotes**: 260 | **Date**: 2023-12-20

**Skill: "Flash Load" / 技能名：「闪存召唤」**

**Category**: `Efficiency` | **Tags**: `offloading, flash-storage, edge-inference, memory-extension`

**Source**: [papers/2023/12/2023-12-20.md, Line 9](papers/2023/12/2023-12-20.md#L9)

**EN**: NEW SKILL UNLOCKED: Flash Load. Apple figured out how to run LLMs that are 2x larger than available DRAM by intelligently loading model weights from flash storage. Windowing and row-column bundling make it work. Your phone's SSD just became a GPU memory extension. LLMs on edge devices are suddenly possible. The "run big models on small hardware" skill tree just unlocked.

**CN**: 新技能解锁：闪存召唤。苹果找到了如何运行比可用 DRAM 大 2 倍的 LLM——通过智能从闪存加载模型权重。窗口化和行列捆绑让它可行。你手机的 SSD 刚刚变成了 GPU 内存扩展。边缘设备上的 LLM 突然成为可能。"小硬件跑大模型"技能树刚刚解锁。

---

## 3. [StreamDiffusion: A Pipeline-level Solution for Real-time Interactive Generation](https://huggingface.co/papers/2312.12491)

**`[NEW SKILL]`** | **ArXiv**: [2312.12491](https://arxiv.org/abs/2312.12491) | **Org**: - | **Upvotes**: 75 | **Date**: 2023-12-21

**Skill: "Live Canvas" / 技能名：「实时画布」**

**Category**: `Vision` | **Tags**: `diffusion, real-time, pipelining, interactive-generation`

**Source**: [papers/2023/12/2023-12-21.md, Line 9](papers/2023/12/2023-12-21.md#L9)

**EN**: NEW SKILL UNLOCKED: Live Canvas. Diffusion image generation used to mean waiting for all denoising steps to finish. StreamDiffusion pipelines the process — it streams intermediate results and processes new inputs simultaneously. Achieves up to 91.07fps. Image generation at 91fps — diffusion just went from slideshow to live stream. The "real-time creation" branch just got a major upgrade.

**CN**: 新技能解锁：实时画布。扩散图像生成曾经意味着等所有去噪步骤完成。StreamDiffusion 将流程流水线化——流式输出中间结果，同时处理新输入。最高达 91.07fps。91 帧的图像生成——扩散从幻灯片变成了直播。"实时创作"分支刚刚获得重大升级。

---
