# Skill Tree Unlocks - 2024-05

> patch notes for the AI civilization, May 2024 edition

Total picks: 4

---

## 1. [Your Transformer is Secretly Linear](https://huggingface.co/papers/2405.12250)

**`[BUG REPORT]`** | **ArXiv**: [2405.12250](https://arxiv.org/abs/2405.12250) | **Org**: - | **Upvotes**: 157 | **Date**: 2024-05-22

**Skill: "Flat Earth" / 技能名：「线性真相」**

**Category**: `Interpretability` | **Tags**: `linear-approximation, layer-collapse, interpretability, depth-illusion`

**Source**: [papers/2024/05/2024-05-22.md, Line 9](papers/2024/05/2024-05-22.md#L9)

**EN**: BUG REPORT: Flat Earth. Transformer layers are supposed to learn complex nonlinear transformations. Turns out consecutive layers are almost perfectly linear — the outputs of one layer can be approximated as a simple linear function of the previous. The model's "deep thinking" is shallower than we thought. A fundamental assumption about neural networks just got challenged. Critical discovery in the interpretability patch.

**CN**: BUG 报告：线性真相。Transformer 层本该学习复杂的非线性变换。结果发现连续层几乎完美线性——一层的输出可以近似为前一层的简单线性函数。模型的"深度思考"比我们想的浅。关于神经网络的基本假设刚刚被挑战。可解释性补丁中的关键发现。

---

## 2. [KAN: Kolmogorov-Arnold Networks](https://huggingface.co/papers/2404.19756)

**`[NEW SKILL]`** | **ArXiv**: [2404.19756](https://arxiv.org/abs/2404.19756) | **Org**: MIT | **Upvotes**: 116 | **Date**: 2024-05-01

**Skill: "Edge Activation" / 技能名：「边缘觉醒」**

**Category**: `Architecture` | **Tags**: `KAN, learnable-activation, Kolmogorov-Arnold, scientific-ML`

**Source**: [papers/2024/05/2024-05-01.md, Line 44](papers/2024/05/2024-05-01.md#L44)

**EN**: NEW SKILL UNLOCKED: Edge Activation. MLPs put activation functions on nodes. KANs put learnable activation functions on edges. Inspired by the Kolmogorov-Arnold representation theorem. Smaller, more interpretable, and more accurate on scientific tasks. A completely different wiring diagram for neural networks. The "alternative to MLP" branch just appeared on the skill tree.

**CN**: 新技能解锁：边缘觉醒。MLP 把激活函数放在节点上。KAN 把可学习激活函数放在边上。灵感来自 Kolmogorov-Arnold 表示定理。更小、更可解释、在科学任务上更准。神经网络的接线图完全换了一套。"MLP 替代品"分支刚刚出现在技能树上。

---

## 3. [LoRA Learns Less and Forgets Less](https://huggingface.co/papers/2405.09673)

**`[NERF ALERT]`** | **ArXiv**: [2405.09673](https://arxiv.org/abs/2405.09673) | **Org**: - | **Upvotes**: 91 | **Date**: 2024-05-17

**Skill: "Gentle Touch" / 技能名：「轻拿轻放」**

**Category**: `Training` | **Tags**: `LoRA, parameter-efficient, forgetting, tradeoff`

**Source**: [papers/2024/05/2024-05-17.md, Line 42](papers/2024/05/2024-05-17.md#L42)

**EN**: NERF ALERT: Gentle Touch. LoRA consistently underperforms full finetuning on target domains but retains much more of the base model's original knowledge. It's a tradeoff: learn less, forget less. LoRA isn't a free lunch — it's a diet lunch that keeps you from gaining weight. The "cheap finetuning" meta just got its fine print revealed.

**CN**: 削弱警告：轻拿轻放。LoRA 在目标域上 consistently 不如全量微调，但能保留更多基座模型原有知识。这是个权衡：学得少，忘得少。LoRA 不是免费午餐——是让你不长胖的轻食午餐。"便宜微调"流派的细则刚刚曝光。

---

## 4. [Chameleon: Mixed-Modal Early-Fusion Foundation Models](https://huggingface.co/papers/2405.09818)

**`[NEW SKILL]`** | **ArXiv**: [2405.09818](https://arxiv.org/abs/2405.09818) | **Org**: Meta AI | **Upvotes**: 132 | **Date**: 2024-05-17

**Skill: "True Fusion" / 技能名：「真·融合」**

**Category**: `Multimodal` | **Tags**: `early-fusion, unified-tokenizer, image-text, single-transformer`

**Source**: [papers/2024/05/2024-05-17.md, Line 9](papers/2024/05/2024-05-17.md#L9)

**EN**: NEW SKILL UNLOCKED: True Fusion. Chameleon tokenizes images and text into a unified token space and trains a single transformer end-to-end on interleaved image-text data. No separate vision encoder, no adapter — images and text are the same thing to the model. True early fusion. The wall between vision and language just dissolved. The multimodal skill tree got a major upgrade.

**CN**: 新技能解锁：真·融合。Chameleon 把图像和文本 tokenize 进统一空间，用交错图文数据端到端训练单个 transformer。没有独立视觉编码器，没有 adapter——对模型来说图像和文本是一回事。真正的早期融合。视觉和语言之间的墙刚刚消失。多模态技能树大升级。

---
