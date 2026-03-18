
## General

Real Time World Model are specific for **Generative Interactive World Models** (User-Model interaction)

**Real Time** here means $\geq 10$ fps and low latency ($< 100$ ms)

There are three searching directions: (Grouped by predictive mechanism)

### Autoregressive world model

4-24 FPS

- MineWorld: a Real-Time and Open-Source Interactive World Model on Minecraft [![arXiv](https://img.shields.io/badge/arXiv-2504.08388-b31b1b.svg)](https://arxiv.org/pdf/2504.08388)  
  - Method: `Autoregressive`  
  - Core idea: visual-action autoregressive Transformer with tokenized frames and actions  
  - Speed: `4-7 FPS` reported by the official repo

- Genie: Generative Interactive Environments [![arXiv](https://img.shields.io/badge/arXiv-2402.15391-b31b1b.svg)](https://arxiv.org/pdf/2402.15391)  
  - Method: `Autoregressive`  
  - Core idea: video tokenizer + autoregressive dynamics model + latent action model  
  - Speed: `interactive`, but the original paper is not usually cited with a clear public realtime FPS number

- Transformers are Sample-Efficient World Models [![arXiv](https://img.shields.io/badge/arXiv-2209.00588-b31b1b.svg)](https://arxiv.org/pdf/2209.00588)  
  - Method: `Autoregressive`  
  - Core idea: Transformer world model for causal future prediction in RL  
  - Speed: no standard rendered `FPS` reported; mainly evaluated by sample efficiency and return

### Diffusion world model

20-25 FPS (few-step / streaming diffusion)

- Diffusion for World Modeling: Visual Details Matter in Atari [![arXiv](https://img.shields.io/badge/arXiv-2405.12399-b31b1b.svg)](https://arxiv.org/pdf/2405.12399)  
  - Method: `Diffusion`  
  - Core idea: diffusion world model for environment dreaming; low-res dynamics + upsampler  
  - Speed: `~10 FPS` on `RTX 3090` reported on the official project page  

- Diffusion Models Are Real-Time Game Engines [![arXiv](https://img.shields.io/badge/arXiv-2408.14837-b31b1b.svg)](https://arxiv.org/pdf/2408.14837)  
  - Method: `Diffusion`  
  - Core idea: neural game engine for DOOM using diffusion-based next-frame simulation  
  - Speed: `>20 FPS` on a single `TPU` reported on the official project page  

- Matrix-Game 2.0: An Open-Source, Real-Time, and Streaming Interactive World Model [![arXiv](https://img.shields.io/badge/arXiv-2508.13009-b31b1b.svg)](https://arxiv.org/pdf/2508.13009)  
  - Method: `Diffusion`  
  - Core idea: few-step autoregressive diffusion with causal/streaming design  
  - Speed: `25 FPS` reported on the official project page  

### Latent world model

(Always not real time)

- World Models [![arXiv](https://img.shields.io/badge/arXiv-1803.10122-b31b1b.svg)](https://arxiv.org/pdf/1803.10122)  
  - Method: `Latent`  
  - Core idea: `world -> latent -> latent transition -> decode`  
  - Speed: no standard rendered `FPS` reported; latent rollout is fast, decoder quality is the bottleneck

- PlaNet: Learning Latent Dynamics for Planning from Pixels [![arXiv](https://img.shields.io/badge/arXiv-1811.04551-b31b1b.svg)](https://arxiv.org/pdf/1811.04551)  
  - Method: `Latent`  
  - Core idea: latent dynamics model + online planning in latent space  
  - Speed: not usually reported as video `FPS`; designed for fast latent-space planning

- Dream to Control: Learning Behaviors by Latent Imagination [![arXiv](https://img.shields.io/badge/arXiv-1912.01603-b31b1b.svg)](https://arxiv.org/pdf/1912.01603)  
  - Method: `Latent`  
  - Core idea: imagine trajectories in compact latent space and learn policy/value there  
  - Speed: not usually reported as video `FPS`; latent imagination is much faster than pixel generation

- Mastering Atari with Discrete World Models [![arXiv](https://img.shields.io/badge/arXiv-2010.02193-b31b1b.svg)](https://arxiv.org/pdf/2010.02193)  
  - Method: `Latent`  
  - Core idea: discrete latent world model for Atari control  
  - Speed: no standard rendered `FPS` reported; evaluated by Atari score and data efficiency

- Mastering Diverse Domains through World Models [![arXiv](https://img.shields.io/badge/arXiv-2301.04104-b31b1b.svg)](https://arxiv.org/pdf/2301.04104)  
  - Method: `Latent`  
  - Core idea: scalable latent world model across Atari, DMC, Procgen, Minecraft  
  - Speed: no standard rendered `FPS` reported; evaluated by cross-domain control performance


The challenges real time world model encounters are: **Causal generation**, **Long term consistency**, **Physically plausibility** and **inference speed**. (In most researches, consistency is more important.)

## Genie: Generative Interactive Environments [![arXiv](https://img.shields.io/badge/arXiv-2402.15391-b31b1b.svg)](https://arxiv.org/pdf/2402.15391)

Use only video data to train a world model (No RL data/action notation needed now)

Pipeline in training:

!!! pure ""

    Video frames --> Latent action inference --> world model training --> interactive generation

## LingBoT

A language-conditioned embodied world model 




memory 机制 / 自回归 **DMD (distill) -> Diffusion Forcing → CausVid → Self-Forcing** 

Self-Forcing

VideoJAM

    https://primecai.github.io/moc/

    https://context-as-memory.github.io/

    https://context-as-memory.github.io/

加速技术 LiveAvatar: TTP (其它、非常规)


