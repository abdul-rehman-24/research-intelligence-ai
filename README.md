# 🧠 AI Research Intelligence System

> **🏆 Gemini 3 Hackathon Entry** - Multi-Agent Academic Discovery Platform

![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python)
![Gemini](https://img.shields.io/badge/Gemini%202.5-Flash-orange?logo=google)
![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-red?logo=streamlit)
![License](https://img.shields.io/badge/License-MIT-green)

## 🔬 Overview

A cutting-edge **Multi-Agent AI Research System** that leverages **Gemini 2.5 Flash** capabilities to autonomously discover, analyze, and synthesize academic research across 6 major sources.

### ✨ Key Features

| Feature | Description |
|---------|-------------|
| 🤖 **5 Specialized Agents** | Collector, Analyzer, Synthesis, Critic, and Trend agents working in orchestration |
| 📚 **6 Academic Sources** | arXiv, Semantic Scholar, PubMed, OpenAlex, CrossRef, CORE |
| 🧠 **Extended Thinking** | Deep analysis using Gemini 3's native reasoning capabilities |
| 🎨 **Cyberpunk UI** | Modern neon-themed interface built with Streamlit |
| 📊 **Smart Relevance Scoring** | AI-powered paper filtering and ranking |
| 🔄 **Real-time Progress** | Live agent status and search progress tracking |

---

## 🚀 Quick Start

### Prerequisites

- Python 3.10+
- Gemini API Key ([Get one here](https://makersuite.google.com/app/apikey))

### Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/ai-research-intelligence.git
cd ai-research-intelligence

# Create virtual environment
python -m venv .venv

# Activate (Windows)
.venv\Scripts\activate

# Activate (macOS/Linux)
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### Configuration

Create a `.env` file in the project root:

```env
GEMINI_API_KEY=your_api_key_here
```

### Run the Application

```bash
streamlit run app.py
```

Open your browser at `http://localhost:8501`

---

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                    STREAMLIT UI (app.py)                    │
│              Cyberpunk Neon Theme • Real-time UI            │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│              RESEARCH ORCHESTRATOR                          │
│         (gemini3_research_system.py)                        │
├─────────────────────────────────────────────────────────────┤
│  ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐        │
│  │ Collector│ │ Analyzer │ │ Synthesis│ │  Critic  │        │
│  │  Agent   │ │  Agent   │ │  Agent   │ │  Agent   │        │
│  └────┬─────┘ └────┬─────┘ └────┬─────┘ └────┬─────┘        │
│       │            │            │            │               │
│  ┌────┴────────────┴────────────┴────────────┴────┐         │
│  │            GEMINI 2.5 FLASH API                │         │
│  │         Extended Thinking • 1M Context          │         │
│  └─────────────────────────────────────────────────┘         │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│                    DATA SOURCES                             │
│  ┌────────┐ ┌──────────┐ ┌────────┐ ┌─────────┐ ┌────────┐  │
│  │ arXiv  │ │ Semantic │ │ PubMed │ │ OpenAlex│ │CrossRef│  │
│  │        │ │ Scholar  │ │        │ │         │ │        │  │
│  └────────┘ └──────────┘ └────────┘ └─────────┘ └────────┘  │
│                          ┌────────┐                          │
│                          │  CORE  │                          │
│                          └────────┘                          │
└─────────────────────────────────────────────────────────────┘
```

---

## 🎯 Hackathon Alignment

This project demonstrates key Gemini 3 capabilities:

| Hackathon Criteria | Implementation |
|-------------------|----------------|
| **Marathon Agent** | Autonomous multi-hour research sessions with session tracking |
| **Thought Signatures** | Self-correcting analysis across multi-step workflows |
| **Orchestrator Pattern** | 5 specialized agents coordinated by central orchestrator |
| **Beyond RAG** | Native reasoning over 100+ papers using 1M token context |
| **Robust System** | Production-ready with comprehensive error recovery |

---

## 📂 Project Structure

```
project/
├── app.py                      # Streamlit UI (Cyberpunk theme)
├── gemini3_research_system.py  # Multi-agent orchestrator
├── requirements.txt            # Python dependencies
├── .env                        # API keys (create this)
├── START_HERE_GEMINI3.md      # Hackathon quick start
└── GEMINI3_HACKATHON_GUIDE.md # Detailed guide
```

---

## 🤖 Agent Descriptions

### 1. 🔍 Collector Agent
Parallel fetching from 6 academic APIs with intelligent query optimization and relevance scoring.

### 2. 🧠 Analyzer Agent
Deep analysis using Gemini 3's Extended Thinking for methodology evaluation, contribution assessment, and limitation identification.

### 3. 📚 Synthesis Agent
Generates comprehensive literature reviews by synthesizing findings across all collected papers.

### 4. 🔍 Critic Agent
Identifies research gaps, unexplored areas, and potential future research directions.

### 5. 📈 Trend Agent
Predicts emerging research trends and provides forecasts for 2026 and beyond.

---

## 🎨 UI Features

- **Cyberpunk Neon Theme** - Eye-catching dark theme with neon accents
- **Real-time Agent Status** - Live tracking of agent activity
- **Paper Cards** - Beautiful cards with relevance scores and source badges
- **Tab Navigation** - Papers, Analysis, Literature, Gaps, Trends, Agents
- **Export Options** - Download research results in multiple formats

---

## 📊 Data Sources

| Source | Type | Coverage |
|--------|------|----------|
| **arXiv** | Preprints | Physics, Math, CS, Biology |
| **Semantic Scholar** | Academic | 200M+ papers across all fields |
| **PubMed** | Medical | Biomedical and life sciences |
| **OpenAlex** | Open Access | 250M+ works, fully open |
| **CrossRef** | DOIs | 140M+ DOI registrations |
| **CORE** | Open Access | 200M+ open access papers |

---

## 🔧 Configuration Options

In the sidebar, you can configure:

- **Max Papers per Source**: 1-20 papers
- **Enable Deep Analysis**: Toggle AI analysis
- **Enable Literature Review**: Toggle synthesis
- **Enable Gap Analysis**: Toggle research gap identification
- **Enable Trend Prediction**: Toggle future trend analysis

---

## 📝 Example Usage

1. Enter a research topic: *"transformer architectures for medical imaging"*
2. Click **⚡ LAUNCH RESEARCH**
3. Watch as agents collect and analyze papers
4. Explore results across tabs:
   - 📄 **Papers** - Discovered papers with relevance scores
   - 🧠 **Analysis** - Deep AI analysis of each paper
   - 📚 **Literature** - Synthesized literature review
   - 🔍 **Gaps** - Identified research gaps
   - 📈 **Trends** - Predicted future trends

---

## 🛠️ Development

### Running Tests

```bash
python -m pytest tests/
```

### Code Formatting

```bash
black app.py gemini3_research_system.py
```

---

## 📄 License

MIT License - See [LICENSE](LICENSE) for details.

---

## 🙏 Acknowledgments

- **Google Gemini Team** - For the amazing Gemini 3 Pro API
- **Streamlit** - For the rapid UI development framework
- **Academic APIs** - arXiv, Semantic Scholar, PubMed, OpenAlex, CrossRef, CORE

---

<div align="center">

**Built with ❤️ for the Gemini 3 Hackathon**

🏆 *Pushing the boundaries of AI-powered research discovery*

</div>
