# Funny Index Style Guide

> how to write picks that read like unlocking a skill tree in a sci-fi civilization game

## Philosophy

Imagine the entire AI research landscape as a **massive tech tree** in a
civilization-building game (think Plague Inc., Stellaris, or Factorio research).
Every paper is a node on that tree. Most are incremental upgrades. But some are
**game-changers** — new branches, hidden combos, surprise mutations, or bug
reports in the simulation itself.

The funny_index curates those game-changers and describes them **as if you're
reading patch notes for reality**.

## Audience

- general readers who are curious about AI but may not have a technical
  background
- the description should be understandable by a college freshman
- avoid jargon; when a technical term is necessary, immediately follow it with a
  plain-language explanation in parentheses

## Skill Tags

Every pick gets exactly one tag. Choose the most fitting:

| Tag | Meaning | Game Analogy |
|-----|---------|--------------|
| `[NEW SKILL]` | a genuinely new capability unlocked | unlocked a new branch on the tech tree |
| `[MUTATION]` | an unexpected or counterintuitive finding | a random mutation that changes the rules |
| `[SIDE EFFECT]` | an unintended consequence or risk discovered | your upgrade has a hidden debuff |
| `[COMBO]` | creative cross-domain fusion | two unrelated tech branches combine for a bonus |
| `[BUG REPORT]` | a fundamental limitation or paradox exposed | found a bug in the simulation engine |
| `[NERF ALERT]` | a widely-believed advantage is weaker than thought | devs silently nerfed a popular strategy |
| `[BOSS DROP]` | a major benchmark or milestone achieved | defeated the final boss of a research arc |

## Skill Naming

Every pick must have a **skill name** in both English and Chinese. The name is
the soul of each entry — it should be:

- **short**: 1-3 words in English, 2-6 characters in Chinese
- **evocative**: instantly conjures an image or feeling, like a game skill name
- **accurate**: captures the core essence of the paper, not a generic label
- **memorable**: readers should be able to recall the paper by just hearing the
  skill name

Good examples:

| EN | CN | Why it works |
|----|-----|-------------|
| Phantom Brake | 幽灵刹车 | the AI has a brake pedal it can't press — vivid and paradoxical |
| Alignment Entropy | 对齐熵增 | borrows physics terminology to describe safety decay — precise and ominous |
| Goat.obj | 山羊.obj | a 3D file extension as a name for goat mesh recovery — instantly funny |
| First Sight | 初见 | poetic and minimal, captures pre-verbal baby vision perfectly |
| Fool's Catalyst | 愚者催化剂 | weak models helping strong ones — the "fool" is the secret ingredient |

Bad examples:

| EN | CN | Why it fails |
|----|-----|-------------|
| New Architecture | 新架构 | too generic, could be anything |
| Interesting Paper | 有趣的论文 | says nothing specific |
| AI Safety Issue | AI 安全问题 | descriptive but not evocative |

Rules for the Chinese name:

- do NOT literally translate the English name; find the best Chinese expression
  that carries the same vibe
- classical / literary Chinese flavor is welcome when it fits (e.g. 初见, 内视之眼)
- internet slang or gaming terminology is fine when the tone calls for it
  (e.g. 大剑主义, 山羊.obj)
- the Chinese name should sound natural spoken aloud

Format in the entry:

```
**Skill: "English Name" / 技能名：「中文名」**
```

## Category

Every pick gets exactly one category describing its research domain. Use the
closest match from this fixed list:

| Category | Covers |
|----------|--------|
| `Architecture` | model structure, attention, normalization, connections, tokenization |
| `Training` | pre-training, post-training, RL, optimization, data curation, distillation |
| `Reasoning` | chain-of-thought, logic, math, planning, test-time compute |
| `Safety` | alignment, jailbreak, red-teaming, robustness, deception, guardrails |
| `Agents` | autonomous agents, tool use, multi-agent systems, self-evolution |
| `Vision` | image understanding, video generation, 3D, visual reasoning |
| `Multimodal` | cross-modal learning, audio-visual, unified models, embodied AI |
| `Science` | biology, chemistry, physics, drug discovery, materials, scientific reasoning |
| `Benchmarks` | evaluation, datasets, metrics, leaderboards |
| `Efficiency` | scaling laws, compression, quantization, inference speed, memory |
| `Interpretability` | mechanistic interpretability, probing, feature analysis, explainability |
| `Society` | economics, skill impact, policy, culture, human-AI interaction |
| `Creative` | art, music, games, storytelling, creative generation |

If a paper truly spans two domains equally, pick the one that is more
surprising (e.g. a physics paper from OpenAI → `Science`, not `Architecture`).

Format in the entry:

```
**Category**: `Architecture` | **Tags**: `scaling`, `residual connections`, `depth`
```

## Tags

Every pick gets 3-6 free-form keyword tags. Rules:

- lowercase, comma-separated
- specific to the paper, not generic ("self-play" not "AI research")
- include both WHAT (technique) and WHY (implication) tags
- at least one tag should describe the surprising aspect
- reuse existing tags across entries when the same concept applies, for
  consistency and searchability

Good tag examples:
- `self-play`, `zero-data`, `reasoning`, `small models`
- `safety decay`, `multi-agent`, `emergent behavior`
- `punctuation`, `memory`, `hidden mechanism`

Bad tag examples:
- `paper`, `interesting`, `AI`, `machine learning` (too generic)
- `2501.12948` (that's what ArXiv ID is for)

## Description Format

Each pick has two descriptions (EN + CN). Both must follow these rules:

1. **one-liner hook**: start with `TAG: Skill Name.` — e.g. "NEW SKILL
   UNLOCKED: Neural Superhighway." or "BUG REPORT: Poker Face."
2. **plain explanation**: 1-2 sentences explaining what actually happened, in
   language a non-researcher can understand
3. **why it matters**: 1 sentence on the broader implication — what changes in
   the "game" because of this

Avoid:
- passive voice
- hedging ("this might be interesting because...")
- repeating the paper title verbatim in the description
- dry academic summaries

Embrace:
- direct address ("your model just learned...", "turns out...")
- cause-and-effect framing ("X was supposed to do Y, but instead it does Z")
- game metaphors ("this unlocks a new branch", "the meta just shifted")
- mild humor when natural (don't force it)

## File Structure

```
funny_index/
├── STYLE_GUIDE.md          # this file
└── 2026/
    ├── 01/picks.md
    ├── 02/picks.md
    └── 03/picks.md
```

Each monthly `picks.md` follows the same template. See existing files for
reference.

## Entry Template

```markdown
## N. [Paper Title](hf_url)

**`[TAG]`** | **ArXiv**: [id](arxiv_url) | **Org**: org | **Upvotes**: N | **Date**: YYYY-MM-DD

**Skill: "English Name" / 技能名：「中文名」**

**Category**: `domain` | **Tags**: `tag1`, `tag2`, `tag3`

**Source**: [papers/YYYY/MM/YYYY-MM-DD.md, Line N](relative_path#LN)

**EN**: TAG: Skill Name. <plain explanation + why it matters>

**CN**: 对应标签：技能名。<same content in Chinese, not a literal translation —
rewrite to feel natural in Chinese, keep the game tone>
```
