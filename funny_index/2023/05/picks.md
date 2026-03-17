# Skill Tree Unlocks - 2023-05

> patch notes for the AI civilization, May 2023 edition

Total picks: 4

---

## 1. [QLoRA: Efficient Finetuning of Quantized LLMs](https://huggingface.co/papers/2305.14314)

**`[NEW SKILL]`** | **ArXiv**: [2305.14314](https://arxiv.org/abs/2305.14314) | **Org**: University of Washington | **Upvotes**: 59 | **Date**: 2023-05-23

**Skill: "Budget Forge" / 技能名：「平民锻造」**

**Category**: `Efficiency` | **Tags**: `quantization`, `LoRA`, `memory-efficient`, `finetuning`, `4-bit`, `democratization`

**Source**: [papers/2023/05/2023-05-23.md, Line 9](papers/2023/05/2023-05-23.md#L9)

**EN**: NEW SKILL UNLOCKED: Budget Forge. Finetuning a 65B model used to require a cluster of GPUs. QLoRA freezes the base model in 4-bit (heavily compressed) and only trains tiny adapter weights on top. You get full 16-bit quality on a single 48GB card. The "big model finetuning" branch just became accessible to anyone with a gaming rig. Democratized finetuning for everyone.

**CN**: 新技能解锁：平民锻造。微调 65B 模型以前需要一屋子 GPU。QLoRA 把底座冻成 4-bit 压缩版，只在上面训练小适配器。一张 48GB 显卡就能跑出完整 16-bit 效果。"大模型微调"这条科技树，现在有张游戏卡就能点。平民也能锻造神兵了。

---

## 2. [TinyStories: How Small Can Language Models Be and Still Speak Coherent English](https://huggingface.co/papers/2305.07759)

**`[NERF ALERT]`** | **ArXiv**: [2305.07759](https://arxiv.org/abs/2305.07759) | **Org**: Microsoft Research | **Upvotes**: 45 | **Date**: 2023-05-16

**Skill: "Bedtime Story" / 技能名：「睡前故事」**

**Category**: `Training` | **Tags**: `small-models`, `vocabulary-curation`, `TinyStories`, `10M-params`, `coherent-language`

**Source**: [papers/2023/05/2023-05-16.md, Line 10](papers/2023/05/2023-05-16.md#L10)

**EN**: NERF ALERT: Bedtime Story. Everyone assumed coherent language required billions of parameters. TinyStories trains 10M-parameter models on short stories that only use words a 3–4 year old would know. The result: coherent, diverse stories from a model smaller than some image classifiers. The "scale is everything" meta just took a hit. Maybe we've been over-investing in the wrong stat.

**CN**: 削弱警告：睡前故事。大家都以为连贯语言非得几十亿参数不可。TinyStories 用 3–4 岁小孩能懂的词汇写成的短故事，训练出 1000 万参数模型。结果：能写出连贯、多样的故事，体积比某些图像分类器还小。"规模即一切"的版本答案被削了一刀。也许我们一直在点错天赋树。

---

## 3. [RWKV: Reinventing RNNs for the Transformer Era](https://huggingface.co/papers/2305.13048)

**`[MUTATION]`** | **ArXiv**: [2305.13048](https://arxiv.org/abs/2305.13048) | **Org**: - | **Upvotes**: 21 | **Date**: 2023-05-22

**Skill: "Recurrent Reborn" / 技能名：「轮回重生」**

**Category**: `Architecture` | **Tags**: `RNN`, `transformer-alternative`, `linear-complexity`, `parallel-training`, `efficient-inference`

**Source**: [papers/2023/05/2023-05-22.md, Line 9](papers/2023/05/2023-05-22.md#L9)

**EN**: MUTATION: Recurrent Reborn. Transformers train fast (parallel) but infer slow (quadratic). RNNs infer fast (linear) but train slow (sequential). RWKV is a hybrid: it trains like a transformer and infers like an RNN, scaling to tens of billions of parameters. A forgotten architecture branch just evolved a new form. The transformer monopoly has a challenger.

**CN**: 突变：轮回重生。Transformer 训练快（并行）但推理慢（平方级）。RNN 推理快（线性）但训练慢（串行）。RWKV 两头都占：训练像 Transformer，推理像 RNN，还能堆到几百亿参数。被遗忘的 RNN 分支进化出了新形态。Transformer 一家独大的局面有了挑战者。

---

## 4. [Drag Your GAN: Interactive Point-based Manipulation on the Generative Image Manifold](https://huggingface.co/papers/2305.10973)

**`[NEW SKILL]`** | **ArXiv**: [2305.10973](https://arxiv.org/abs/2305.10973) | **Org**: Max Planck Institute | **Upvotes**: 39 | **Date**: 2023-05-19

**Skill: "Pixel Puppet" / 技能名：「像素提线」**

**Category**: `Vision` | **Tags**: `interactive-editing`, `point-based-manipulation`, `GAN`, `image-editing`, `drag-and-drop`

**Source**: [papers/2023/05/2023-05-19.md, Line 10](papers/2023/05/2023-05-19.md#L10)

**EN**: NEW SKILL UNLOCKED: Pixel Puppet. Click a point on a GAN-generated image, drag it somewhere else, and the whole image deforms realistically. Move a smile, reshape a face, repose a body — no masks, no prompts, just intuitive drag-and-drop. Image editing just got a game-like control scheme. The "generative image" branch learned to obey the cursor.

**CN**: 新技能解锁：像素提线。在 GAN 生成的图上点一个点，拖到别处，整张图跟着真实变形。挪笑容、改脸型、摆姿势——不用蒙版、不用提示词，拖拽就行。图像编辑多了个像玩游戏一样的操作方式。"生成式图像"这条线学会了听鼠标指挥。

---
