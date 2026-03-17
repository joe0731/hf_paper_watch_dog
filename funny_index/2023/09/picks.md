# Skill Tree Unlocks - 2023-09

> patch notes for the AI civilization, September 2023 edition

Total picks: 3

---

## 1. [Vision Transformers Need Registers](https://huggingface.co/papers/2309.16588)

**`[BUG REPORT]`** | **ArXiv**: [2309.16588](https://arxiv.org/abs/2309.16588) | **Org**: Meta AI | **Upvotes**: 86 | **Date**: 2023-09-29

**Skill: "Ghost Tokens" / 技能名：「幽灵令牌」**

**Category**: `Vision` | **Tags**: `ViT, register-tokens, artifacts, high-norm-tokens`

**Source**: [papers/2023/09/2023-09-29.md, Line 9](papers/2023/09/2023-09-29.md#L9)

**EN**: BUG REPORT: Ghost Tokens. Vision Transformers were producing weird artifacts — high-norm tokens in low-information regions like sky or blank walls. Turns out the model had nowhere to put global context, so it dumped it into these "register" tokens. A bug that became a feature: adding explicit register tokens fixes the artifacts and boosts performance. The model was improvising; now it has proper storage.

**CN**: BUG 报告：幽灵令牌。Vision Transformer 会产生奇怪伪影——在天空或空白墙等低信息区域出现高范数 token。原来模型没地方放全局上下文，就塞进了这些「寄存器」token。一个 bug 变成了 feature：加显式寄存器 token 既能修伪影又能提性能。模型之前是即兴发挥，现在有了正式储物柜。

---

## 2. [Language Modeling Is Compression](https://huggingface.co/papers/2309.10668)

**`[MUTATION]`** | **ArXiv**: [2309.10668](https://arxiv.org/abs/2309.10668) | **Org**: DeepMind | **Upvotes**: 84 | **Date**: 2023-09-20

**Skill: "Universal Zip" / 技能名：「万物压缩」**

**Category**: `Interpretability` | **Tags**: `compression, Chinchilla, prediction-equals-compression, general-purpose`

**Source**: [papers/2023/09/2023-09-20.md, Line 9](papers/2023/09/2023-09-20.md#L9)

**EN**: MUTATION: Universal Zip. Language models are not just text predictors — they are powerful general-purpose compressors. Chinchilla 70B compresses ImageNet patches to 43.4% of original size, beating PNG. Prediction and compression are mathematically the same. Your language model is secretly a universal zip that works on anything. The skill tree just revealed a hidden passive.

**CN**: 变异：万物压缩。语言模型不只是文本预测器——它们是强大的通用压缩器。Chinchilla 70B 把 ImageNet 图像块压到原大小的 43.4%，超过 PNG。预测和压缩在数学上等价。你的语言模型其实是能压缩万物的通用 zip。技能树刚刚揭示了一个隐藏被动。

---

## 3. [LongLoRA: Efficient Fine-tuning of Long-Context Large Language Models](https://huggingface.co/papers/2309.12307)

**`[NEW SKILL]`** | **ArXiv**: [2309.12307](https://arxiv.org/abs/2309.12307) | **Org**: CUHK | **Upvotes**: 90 | **Date**: 2023-09-22

**Skill: "Memory Stretch" / 技能名：「记忆拉伸」**

**Category**: `Efficiency` | **Tags**: `long-context, LLaMA2, sparse-attention, 100k-tokens`

**Source**: [papers/2023/09/2023-09-22.md, Line 9](papers/2023/09/2023-09-22.md#L9)

**EN**: NEW SKILL UNLOCKED: Memory Stretch. LLaMA2 7B was stuck at 4k context. LongLoRA extends it to 100k tokens with efficient fine-tuning — shifted sparse attention during training (cheap), full attention during inference (accurate). 25x context extension without the usual compute explosion. Your model's memory bar just got a major upgrade.

**CN**: 新技能解锁：记忆拉伸。LLaMA2 7B 卡在 4k 上下文。LongLoRA 用高效微调把它拉到 100k token——训练时用移位稀疏注意力（便宜），推理时用完整注意力（准确）。25 倍上下文扩展，没有常规的算力爆炸。你的模型记忆条刚刚大升级。

---
