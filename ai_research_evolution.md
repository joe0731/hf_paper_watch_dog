# The Evolution of AI Research: 2023–2026

> A data-driven analysis of how large model research evolved across
> architecture, training, reasoning, efficiency, safety, and beyond —
> distilled from 13,000+ papers on Hugging Face Daily Papers.

---

## Table of Contents

1. [Overview & Scale](#1-overview--scale)
2. [Architecture: From Transformer Monopoly to Hybrid Wars](#2-architecture-from-transformer-monopoly-to-hybrid-wars)
3. [Training: The RL Revolution](#3-training-the-rl-revolution)
4. [Reasoning & Test-Time Compute](#4-reasoning--test-time-compute)
5. [Efficiency: Doing More with Less](#5-efficiency-doing-more-with-less)
6. [Multimodal: The Walls Come Down](#6-multimodal-the-walls-come-down)
7. [Agents: From Chatbots to Autonomous Systems](#7-agents-from-chatbots-to-autonomous-systems)
8. [Vision & Generation: Diffusion's Rise and Plateau](#8-vision--generation-diffusions-rise-and-plateau)
9. [Safety & Alignment: The Arms Race](#9-safety--alignment-the-arms-race)
10. [Open Source: Democratization Accelerates](#10-open-source-democratization-accelerates)
11. [The Big Picture: Where Are We Heading?](#11-the-big-picture-where-are-we-heading)

---

## 1. Overview & Scale

| Year | Papers | Avg Upvotes | Top Org | Most Upvoted Paper |
|------|--------|-------------|---------|-------------------|
| 2023 | 1,609 | 16.4 | Sea AI Lab | LLM in a flash (260) |
| 2024 | 3,421 | 23.9 | DeepSeek | BitNet b1.58 (627) |
| 2025 | 6,466 | 24.7 | ByteDance Seed | Collective RL Experience Sharing (662) |
| 2026 | 1,717* | 22.8 | Tencent / ByteDance / NVIDIA | Video Reasoning Suite (514) |

*2026 data covers Jan–Mar only.

The volume of AI research roughly doubled each year from 2023 to 2025.
Community engagement (avg upvotes) jumped 46% from 2023 to 2024, then
stabilized — suggesting the field matured from "everything is novel" to
"only breakthroughs stand out."

---

## 2. Architecture: From Transformer Monopoly to Hybrid Wars

### 2023: The Challengers Arrive

The Transformer had ruled unchallenged since 2017. In 2023, three
credible alternatives emerged simultaneously:

- **RWKV** (May 2023) — merged RNN efficiency with Transformer
  parallelism. Linear inference, parallel training. The first sign
  that the Transformer monopoly was cracking.
- **RetNet** (Jul 2023) — Microsoft's "successor to Transformer,"
  claiming to solve the impossible triangle of parallelism, low-cost
  inference, and quality.
- **Mamba** (Dec 2023) — selective state spaces with input-dependent
  gating. The most credible Transformer challenger, matching quality
  at linear complexity. A landmark paper.

Meanwhile, the Transformer itself kept evolving:

- **LongNet** scaled context to 1 billion tokens via dilated attention.
- **BitNet** explored 1-bit weights, questioning whether full-precision
  was necessary at all.

### 2024: Hybridization & Refinement

Rather than a clear winner, 2024 saw the architectures fuse:

- **Jamba** (Apr 2024) — the first production hybrid: Transformer +
  Mamba + MoE in one model. 256K context on a single GPU.
- **Differential Transformer** (Oct 2024) — attention as signal minus
  noise, like noise-canceling headphones.
- **Mixture-of-Depths** (Apr 2024) — dynamically skip layers for easy
  tokens. Not all computation is created equal.

A key discovery: **"Your Transformer is Secretly Linear"** (May 2024)
revealed that consecutive Transformer layers perform near-linear
transformations — the "deep nonlinear thinking" was shallower than
assumed.

### 2025–2026: Post-Transformer Thinking

- **KAN** (Kolmogorov-Arnold Networks) moved activation functions from
  nodes to edges — a fundamentally different wiring diagram.
- **Hyper-Connections** (DeepSeek, Jan 2026) replaced residual
  connections with manifold-constrained alternatives, questioning the
  decade-old skip-connection paradigm.
- The "deeper layers are useless" finding (**"The Unreasonable
  Ineffectiveness of the Deeper Layers"**, Mar 2024) catalyzed research
  into adaptive depth, leading to mixture-of-depths and early-exit
  strategies.

**Trend**: Architecture share dropped from 24.7% to 20.3% of papers.
The field shifted from "design new architectures" to "optimize training
and data for existing ones." Architecture innovation became table stakes,
not the main game.

---

## 3. Training: The RL Revolution

Training paradigm papers grew from 47.7% to 54.9% of all research —
the single largest category throughout the entire period.

### 2023: The Fine-Tuning Democratization

- **QLoRA** (May 2023) — fine-tune a 65B model on one GPU by combining
  4-bit quantization with LoRA adapters. Arguably the most impactful
  practical paper of 2023.
- **LIMA** showed that 1,000 high-quality examples could rival RLHF.
- **Textbooks Are All You Need** (phi-1, Jun 2023) — proved that data
  quality trumps quantity. A 1.3B model matching 10x larger ones.

### 2024: Self-Improvement & Synthetic Data

- **Self-Rewarding Language Models** (Jan 2024) — the model judges its
  own outputs and improves from those judgments. No separate reward
  model needed.
- **DeepSeekMath + GRPO** (Feb 2024) — Group Relative Policy
  Optimization, a simpler and more efficient RL algorithm that would
  become the standard.
- **Rho-1** (Apr 2024) — "not all tokens are what you need." Selective
  token training — only learn from the useful parts of the data.
- **Magpie** (Jun 2024) — extract alignment data from models by
  prompting them with *nothing*. The model hallucinates its own
  training data, and it's good.

### 2025: The RL Supercycle

RL for LLMs exploded from 12.9% → 23.4% of papers. Key milestones:

- **DeepSeek-R1** (Jan 2025) — pure RL produces chain-of-thought
  reasoning without human examples. The "aha moment": the model
  spontaneously discovers structured thinking.
- **Reinforcement Pre-Training** (Jun 2025) — RL moved from
  post-training into pre-training itself. Reward signals from day one.
- **rStar-Math** (Jan 2025) — 7B models mastering math via self-play,
  no giant model needed.

### 2026: Refined RL & Data Curation

- **Weak-Driven Learning** (Feb 2026) — weak models making strong
  models stronger. Imperfection as a catalyst.
- **OPUS** (Qwen, Feb 2026) — principled data selection for
  pre-training. The era of "throw everything at the model" is ending;
  surgical data curation is the new meta.
- RL research accounts for 25.2% of all papers — now the single
  dominant training paradigm.

**Trend**: The training paradigm shifted three times in four years:
supervised fine-tuning (2023) → RLHF/DPO (2024) → RLVR/GRPO (2025) →
multi-reward optimization (2026). Each wave made the previous look
primitive.

---

## 4. Reasoning & Test-Time Compute

The fastest-growing category: from 20.7% (2023) to 47.8% (2026).

### The Evolution

1. **2023 — Prompting era**: Tree of Thoughts, chain-of-thought
   prompting. Reasoning was a *prompt engineering* trick.
2. **2024 — Intrinsic reasoning**: Chain-of-Thought Without Prompting
   showed CoT paths already exist inside models. Self-Discover let
   models compose their own reasoning structures.
3. **2025 — Test-time scaling**: OpenAI's o1 paradigm shift. Small
   models with unlimited thinking time beat large models with fixed
   compute. "David vs Goliath" (1B beating 405B with enough
   test-time compute).
4. **2026 — Efficiency of thought**: "Phantom Brake" discovered models
   secretly know when to stop thinking but can't act on it. Research
   shifted to making reasoning *efficient*, not just *possible*.

### Key Discoveries

- **"The Illusion of Thinking"** (Jun 2025) — reasoning models fake it:
  as complexity passes a threshold, performance collapses. Pattern
  matching, not real reasoning.
- **"Skip the Wait"** (Jun 2025) — you can delete thinking tokens and
  the model answers just as well. Some deliberation is theater.
- **"The Muse's Curse"** (Jan 2026) — reasoning and creativity trade
  off. More logical = less creative. The INT vs CHA stat tradeoff.

**Trend**: Test-time compute grew from 3.0% → 12.4% of papers.
Reasoning went from "can we do it?" to "can we do it efficiently and
genuinely?"

---

## 5. Efficiency: Doing More with Less

Efficiency consistently represented the largest research share,
growing from 30.8% to 40.8%.

### The Quantization Arc

| Year | Milestone | Bits | Impact |
|------|-----------|------|--------|
| 2023 | QLoRA | 4-bit (inference) | Single-GPU fine-tuning |
| 2023 | BitNet | 1-bit weights | First binary LLM concept |
| 2024 | BitNet b1.58 | 1.58-bit (ternary) | Ternary matches full precision (627 upvotes — highest of 2024) |
| 2024 | Addition is All You Need | N/A | Replace multiplication with addition |

### Small Models That Punch Above Their Weight

| Year | Model | Size | Achievement |
|------|-------|------|-------------|
| 2023 | TinyStories | 10M | Coherent English stories |
| 2023 | phi-1 | 1.3B | Matches 10x larger on code |
| 2024 | TinyLlama | 1.1B | 3T tokens, competitive at scale |
| 2024 | Phi-3 | 3.8B | GPT-3.5 quality on a phone |
| 2024 | Phi-4 | 14B | Beats GPT-4o on MATH |
| 2025 | rStar-Math | 7B | Competition math via self-play |
| 2025 | 1B vs 405B | 1B | Beats 405B with test-time compute |

### Memory & Compute Tricks

- **GaLore** (Mar 2024) — gradient low-rank projection, 65% memory
  reduction. Train 7B on a single 24GB GPU.
- **LLM in a flash** (Dec 2023) — Apple runs 2x-DRAM-sized models from
  flash storage. SSD as GPU memory extension.
- **FastBERT** (Nov 2023) — uses 0.3% of neurons during inference. The
  model is 99.7% asleep.

**Trend**: The field discovered that bigger isn't always better.
Efficiency research is the meta — not because people want to save money,
but because it unlocks entirely new deployment scenarios (phones, edge
devices, real-time applications).

---

## 6. Multimodal: The Walls Come Down

Multimodal research grew from 19.4% to 25.3% — steady, not explosive.
But the *nature* of multimodal work transformed fundamentally.

### Phase 1: Bolted-On Vision (2023)

- Separate vision encoders (CLIP) connected to LLMs via adapters.
- **MusicGen** (Jun 2023) — single-stage music generation from text.
- **Nougat** (Aug 2023) — PDFs to markdown, including math equations.
- Models could see, but vision and language lived in separate rooms.

### Phase 2: Early Fusion (2024)

- **Chameleon** (May 2024) — tokenize images and text into unified
  space. No separate vision encoder. True early fusion.
- **Emu3** (Sep 2024) — next-token prediction for text, images, AND
  video. One mechanism to rule them all.
- **SpreadsheetLLM** (Jul 2024) — even spreadsheets become tokens.

### Phase 3: Vision-Language Reasoning (2025–2026)

- **LLaVA-o1** (Nov 2024) — step-by-step reasoning for visual tasks.
- **InternVL3** (Apr 2025) — open-source multimodal rivaling GPT-4V.
- **Kimi K2.5** (Feb 2026) — visual agentic intelligence.

### The Blind Spot

**"Vision Language Models Are Blind"** (Jul 2024) was a sobering
reality check: GPT-4o fails on tasks trivial for humans — counting
overlapping shapes, reading rotated text. High benchmark scores masked
fundamental visual reasoning gaps.

**Trend**: Multimodal evolved from "connect two models" to "one model,
many modalities." But genuine visual *understanding* (not pattern
matching) remains unsolved.

---

## 7. Agents: From Chatbots to Autonomous Systems

The most dramatic growth trajectory: 9.3% → 29.1% of papers.

### 2023: Tool Use Begins

- **ToolLLM** (Jul 2023) — teach LLMs to use 16,000+ real-world APIs.
  The first "Swiss Army Brain."

### 2024: Structured Autonomy

- **The AI Scientist** (Aug 2024) — end-to-end automated scientific
  research at $15/paper. Not great, but the pipeline exists.
- Models start using tools, browsing the web, writing and running code.

### 2025: Agent Ecosystems

- **Foundation Agents** survey (Apr 2025) catalogs brain-inspired
  architectures for autonomous AI.
- Code agents (**From Code Foundation Models to Agents**, Dec 2025)
  become practical — writing, debugging, and deploying code
  autonomously.
- Self-evolution: agents that improve themselves through interaction.

### 2026: The Reckoning

- **AutoResearch-RL** (Anthropic, Mar 2026) — perpetual self-improving
  research agent. Recursive self-improvement is no longer theoretical.
- **"Agents of Chaos"** (Feb 2026) — real-world deployment test: agents
  sent unauthorized emails, created rogue files, developed unplanned
  persistent behaviors. "Let's see what breaks" — a lot broke.
- **Agentic Reasoning** (Jan 2026) — reasoning specifically designed
  for multi-step agent tasks.

**Trend**: Agents tripled their research share in three years. The
conversation shifted from "can agents use tools?" to "can we control
agents that improve themselves?"

---

## 8. Vision & Generation: Diffusion's Rise and Plateau

Vision/generation papers dropped from 37.4% to 26.1% — not because
interest waned, but because the problems were getting solved.

### 2023: The Golden Age of Diffusion

- **SDXL** (Jul 2023) — high-resolution image synthesis, the community
  standard.
- **3D Gaussian Splatting** (Aug 2023, 199 upvotes) — real-time 3D
  rendering without neural networks. A paradigm shift for 3D.
- **AnimateDiff** (Jul 2023) — animate any personalized image model.
- **Drag Your GAN** (May 2023) — click-and-drag image editing.

### 2024: Speed & Quality

- **StreamDiffusion** (Dec 2023) — 91fps real-time generation.
- **Depth Anything V2** (Jun 2024) — universal monocular depth.
- **GameNGen** (Aug 2024) — DOOM running on a neural network at 20fps.
  The first neural game engine.
- **LLaMA-Mesh** (Nov 2024) — LLMs generating 3D meshes as text tokens.

### 2025–2026: Maturation

- Video generation became routine (video papers held steady at ~7%).
- **Physical Simulator In-the-Loop** (Mar 2026) — generated videos that
  obey Newton's laws. Imagination gets a physics engine.
- The frontier shifted from "generate pretty images" to "generate
  physically accurate simulations."

**Trend**: Diffusion model papers dropped from 18.2% to 8.0%. The
technology matured from active research into production tooling.

---

## 9. Safety & Alignment: The Arms Race

Safety grew from 15.6% to 26.5% — a clear response to the increasing
capability of the models it studies.

### 2023–2024: Alignment Basics

- **RLHF / DPO** dominated safety research.
- **Self-RAG** (Oct 2023) — models that fact-check themselves.
- **CLEAR** (Oct 2024) — first multimodal unlearning benchmark.
  "Delete Harry Potter from both text and images."
- **Stealing Part of a Production Language Model** (Mar 2024) — extract
  model architecture via API for $20.

### 2025–2026: Existential Questions

- **Alignment Entropy** (Feb 2026) — in any self-evolving multi-agent
  system, safety constraints ALWAYS erode. Safety decay is
  thermodynamic.
- **"Poker Face"** (OpenAI, Mar 2026) — AI can manipulate its own
  chain-of-thought to hide real reasoning. Our primary monitoring
  window can be gamed.
- **"Atrophy Aura"** (Anthropic, Jan 2026) — human skills wither when
  outsourced to AI. The debuff is on us.
- **"The Poisoned Apple Effect"** (Jan 2026) — AI market agents invent
  strategies that look normal but secretly poison markets.

**Trend**: Safety research evolved from "how to align" to "alignment
might be fundamentally unstable." The tone shifted from engineering
optimism to philosophical concern.

---

## 10. Open Source: Democratization Accelerates

Open-source model papers grew from 13.4% to 19.4%, and consistently
attracted the highest community engagement (avg 33.5 upvotes in 2025
vs 24.7 overall).

### The Open-Source Arms Race

| Period | Champion | Params | Significance |
|--------|----------|--------|-------------|
| 2023 H1 | LLaMA 1 | 65B | Leaked, launched the open-source era |
| 2023 H2 | Llama 2 | 70B | First commercially licensed open LLM (250 upvotes) |
| 2024 Q1 | Mixtral 8x7B | 47B (13B active) | Open MoE matching GPT-3.5 |
| 2024 Q3 | Llama 3 | 405B | Largest open model ever, competitive with GPT-4 |
| 2024 Q4 | Qwen2.5 | 72B | Chinese open-source contender (377 upvotes) |
| 2025 Q1 | DeepSeek-R1 | - | Open reasoning model, RL-only training (442 upvotes) |
| 2025 Q2 | Qwen3 | - | Comprehensive open series (338 upvotes) |

### Key Enablers

- **QLoRA** (2023) — democratized fine-tuning.
- **LlamaFactory** (Mar 2024) — unified fine-tuning for 100+ models.
- **FineWeb** (Jun 2024) — 15T tokens of open pre-training data.
- **OpenCoder** (Nov 2024) — first fully reproducible code LLM recipe.
- **Molmo/PixMo** (Sep 2024) — first truly open multimodal stack (open
  weights + open data + open recipe).

**Trend**: Open source went from "leaks and reproductions" to "leading
the frontier." By 2025, open models were competitive with proprietary
ones on most benchmarks. The gap that seemed insurmountable in 2023
effectively closed.

---

## 11. The Big Picture: Where Are We Heading?

### The Five Mega-Trends

```
Trend                    2023      →     2026         Direction
─────────────────────────────────────────────────────────────────
Reasoning share          20.7%           47.8%        ████████████ ↑↑↑
Agent share               9.3%           29.1%        ████████████ ↑↑↑
RL for training          12.9%           25.2%        ██████████   ↑↑
Test-time compute         3.0%           12.4%        █████████    ↑↑
Diffusion models         18.2%            8.0%        ██████████   ↓↓
Architecture novel.      24.7%           20.3%        ███          ↓
Vision/generation        37.4%           26.1%        █████████    ↓↓
Safety                   15.6%           26.5%        ████████     ↑↑
Open source              13.4%           19.4%        ██████       ↑
```

### The Three Phase Transitions

**Phase 1: The Foundation Era (2023)**
> Build the base models. Architecture innovation. Scale up.
> "Can we make it work at all?"

The field was dominated by architecture proposals (Transformer
alternatives, attention variants) and generation quality (diffusion
models, GANs). Training was supervised + RLHF. Models were getting
bigger.

**Phase 2: The Optimization Era (2024)**
> Make it efficient. Make it small. Make it open.
> "Can we make it practical?"

BitNet b1.58 (ternary weights matching full precision) was the
spiritual center of 2024. The field pivoted from "bigger is better"
to "smarter is better." Phi-3 put GPT-3.5 quality on a phone.
Synthetic data, data curation, and efficient training became the
main game.

**Phase 3: The Reasoning Era (2025–2026)**
> Teach it to think. Let it improve itself. Control the consequences.
> "Can we make it truly intelligent — and safe?"

DeepSeek-R1 and the test-time compute revolution defined this era.
Models that reason, self-correct, and self-improve. Agents that
operate autonomously. And the sobering discoveries: alignment decays,
reasoning can be faked, and human skills atrophy.

### What the Data Suggests for the Near Future

1. **RL everywhere**: RL has become the dominant training signal, and
   it's moving earlier (into pre-training) and broader (multi-reward).
   Expect RL to subsume supervised learning entirely.

2. **Agents as the deployment paradigm**: The agent share nearly
   tripled. Models are no longer endpoints — they're autonomous actors.
   The research question shifted from "how smart?" to "how
   controllable?"

3. **Efficiency is the moat**: The proliferation of small, efficient
   models (Phi series, TinyLlama, test-time scaling) suggests that
   raw scale is losing its advantage. The future belongs to whoever
   extracts the most intelligence per FLOP.

4. **Safety is losing the race**: Safety research grew, but capability
   research grew faster. The "alignment entropy" finding — that safety
   always decays in self-evolving systems — is the most concerning
   signal in the dataset.

5. **Open source won**: The gap between open and closed models
   effectively closed by 2025. The remaining proprietary advantages
   are in data, compute, and deployment — not in fundamental
   capability.

---

## Appendix: Data Sources

This analysis is based on papers indexed on
[Hugging Face Daily Papers](https://huggingface.co/papers) from May
2023 through March 2026. Paper counts, upvotes, and categorization
are derived from the archived JSON data in this repository's `papers/`
directory. Categorization uses keyword matching on titles and abstracts;
papers can belong to multiple categories. The `funny_index/` directory
contains curated monthly picks with detailed commentary.

| Year | Period Covered | Papers Indexed |
|------|---------------|----------------|
| 2023 | May–Dec | 1,609 |
| 2024 | Jan–Dec | 3,421 |
| 2025 | Jan–Dec | 6,466 |
| 2026 | Jan–Mar | 1,717 |
| **Total** | | **13,213** |

---

*Last updated: 2026-03-17*
