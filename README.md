# local-llm-notes
Personal experiments and evaluation notes on running local LLMs (Qwen 2.5) with Ollama.
# Local LLM Exploration & Multilingual Experiments

A hands-on log of my experiments running open-source large language models locally, exploring system prompting, cross-lingual behavior, and creative text generation.

##  Hardware & Environment Setup
- **Device**: MSI Raider GE68 HX (Intel i9, RTX 4070 Ti) / MacBook Pro (M-Series)
- **Runtime**: [Ollama](https://ollama.ai/)
- **Base Model**: Qwen 2.5 (32B parameter version)
- **Interface**: Chatbox / Python scripts

##  What I've Explored So Far
1. **Local Deployment**: Configured and served 32B-scale models locally using quantized GGUF formats via Ollama.
2. **Context & System Prompting**: Tested the impact of detailed system instructions, persona anchoring, and formatting templates on output consistency.
3. **Safety Alignment & Refusal Dynamics**: Experimented with prompt engineering to analyze how default safety alignment behaves across different conversational contexts.

##  Next Steps
- [ ] Evaluate style transfer and response consistency across **English, Chinese, French, and Spanish**.
- [ ] Build a lightweight Python automation script to benchmark cross-lingual responses side by side.
- [ ] Explore parameter-efficient fine-tuning (LoRA) on curated datasets.
