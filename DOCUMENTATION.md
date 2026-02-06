# 📖 AI Research Intelligence System - Complete Documentation

> Comprehensive technical documentation for the Multi-Agent Research System

---

## 📋 Table of Contents

1. [Project Overview](#project-overview)
2. [Architecture](#architecture)
3. [File Structure](#file-structure)
4. [Core Classes](#core-classes)
5. [Agent System](#agent-system)
6. [Data Sources](#data-sources)
7. [API Reference](#api-reference)
8. [UI Components](#ui-components)
9. [Configuration](#configuration)
10. [Workflow](#workflow)

---

## 🎯 Project Overview

### Purpose
This system automates academic research discovery by:
- Fetching papers from 6 academic sources simultaneously
- Using AI (Gemini 2.5 Flash) for deep analysis
- Synthesizing literature reviews automatically
- Identifying research gaps and future trends

### Technology Stack

| Component | Technology |
|-----------|------------|
| **AI Model** | Gemini 2.5 Flash |
| **Backend** | Python 3.10+ |
| **Frontend** | Streamlit |
| **API Client** | google-genai SDK |
| **Data Sources** | arXiv, Semantic Scholar, PubMed, OpenAlex, CrossRef, CORE |

---

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                         USER INTERFACE                          │
│                         (app.py)                                │
│   ┌─────────────┐  ┌─────────────┐  ┌─────────────────────────┐ │
│   │ Search Bar  │  │  Controls   │  │      Results Tabs       │ │
│   └─────────────┘  └─────────────┘  └─────────────────────────┘ │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                    RESEARCH ORCHESTRATOR                        │
│               (gemini3_research_system.py)                      │
│                                                                 │
│   ┌─────────────────────────────────────────────────────────┐   │
│   │                   ResearchSession                       │   │
│   │     (Tracks progress, insights, corrections)            │   │
│   └─────────────────────────────────────────────────────────┘   │
│                              │                                  │
│   ┌──────────┬───────────┬───────────┬───────────┬──────────┐   │
│   │ Analyzer │ Synthesis │  Critic   │   Trend   │ Thinker  │   │
│   │  Agent   │   Agent   │   Agent   │   Agent   │  (Base)  │   │
│   └──────────┴───────────┴───────────┴───────────┴──────────┘   │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                     GEMINI 2.5 FLASH API                        │
│              Extended Thinking • 1M Token Context               │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                       DATA SOURCES                              │
│  ┌────────┐ ┌────────┐ ┌────────┐ ┌────────┐ ┌────────┐ ┌────┐  │
│  │ arXiv  │ │Semantic│ │ PubMed │ │OpenAlex│ │CrossRef│ │CORE│  │
│  └────────┘ └────────┘ └────────┘ └────────┘ └────────┘ └────┘  │
└─────────────────────────────────────────────────────────────────┘
```

---

## 📁 File Structure

```
project/
├── app.py                         # Streamlit UI application
├── gemini3_research_system.py     # Core research orchestrator
├── gemini3_enhanced_features.py   # Extended thinking features
├── requirements.txt               # Python dependencies
├── README.md                      # Project overview
├── DOCUMENTATION.md               # This file
├── .env                           # API keys (create this)
└── .venv/                         # Virtual environment
```

---

## 🔧 Core Classes

### 1. ResearchSession

**File:** `gemini3_research_system.py` (Line 62)

**Purpose:** Tracks research sessions spanning hours/days. Maintains continuity and self-corrects across multi-step analysis.

```python
class ResearchSession:
    def __init__(self, query: str)
```

#### Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `query` | str | The research topic being investigated |
| `start_time` | datetime | When the session started |
| `papers_analyzed` | list | All papers processed in this session |
| `insights` | list | Generated insights with confidence scores |
| `corrections` | list | Self-corrections made during analysis |
| `agent_logs` | defaultdict | Logs from each agent |
| `session_id` | str | Unique identifier for the session |

#### Methods

| Method | Parameters | Returns | Description |
|--------|------------|---------|-------------|
| `log_agent_action()` | agent_name, action, result | None | Tracks all agent actions for continuity |
| `add_insight()` | insight, confidence | None | Track insights with confidence scores |
| `add_correction()` | original, corrected, reason | None | Self-correction tracking for Thinking Mode |
| `get_session_context()` | None | str | Generate context for maintaining continuity |

---

### 2. ThinkingAgent (Base Class)

**File:** `gemini3_research_system.py` (Line 126)

**Purpose:** Base agent with extended thinking capabilities using Gemini's thinking mode for deep reasoning.

```python
class ThinkingAgent:
    def __init__(self, name: str, role: str, session: ResearchSession)
```

#### Methods

| Method | Parameters | Returns | Description |
|--------|------------|---------|-------------|
| `think_and_analyze()` | content, instruction | Dict | Uses Gemini's extended thinking mode for analysis |
| `_parse_response()` | text | Dict | Parses JSON response from AI |

---

### 3. ResearchOrchestrator

**File:** `gemini3_research_system.py` (Line 440)

**Purpose:** Main orchestrator coordinating all agents. This is the central controller that manages the entire research workflow.

```python
class ResearchOrchestrator:
    def __init__(self, query: str)
```

#### Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `session` | ResearchSession | The current research session |
| `query` | str | The research topic |
| `analyzer` | DeepAnalyzerAgent | Agent for deep paper analysis |
| `synthesizer` | SynthesisAgent | Agent for literature synthesis |
| `critic` | CriticAgent | Agent for gap identification |
| `trends` | TrendPredictionAgent | Agent for trend prediction |

#### Methods

| Method | Parameters | Returns | Description |
|--------|------------|---------|-------------|
| `fetch_papers_parallel()` | max_per_source (int) | List[Dict] | Parallel fetching from 6 sources |
| `run_marathon_analysis()` | None | Dict | Full marathon analysis pipeline |
| `_fetch_arxiv()` | query, max_results | List[Dict] | Fetch papers from arXiv |
| `_fetch_semantic_scholar()` | query, max_results | List[Dict] | Fetch from Semantic Scholar |
| `_fetch_pubmed()` | query, max_results | List[Dict] | Fetch from PubMed |
| `_fetch_openalex()` | query, max_results | List[Dict] | Fetch from OpenAlex |
| `_fetch_crossref()` | query, max_results | List[Dict] | Fetch from CrossRef |
| `_fetch_core()` | query, max_results | List[Dict] | Fetch from CORE |
| `_deduplicate_papers()` | papers | List[Dict] | Remove duplicate papers |

---

## 🤖 Agent System

### Agent Overview

The system uses 5 specialized agents, each inheriting from `ThinkingAgent`:

```
                    ThinkingAgent (Base)
                           │
         ┌─────────────────┼─────────────────┐
         │                 │                 │
         ▼                 ▼                 ▼
  DeepAnalyzerAgent  SynthesisAgent   CriticAgent
                                             │
                                             ▼
                                   TrendPredictionAgent
```

---

### 4. DeepAnalyzerAgent

**File:** `gemini3_research_system.py` (Line 208)

**Purpose:** Analyzes individual papers deeply using AI.

```python
class DeepAnalyzerAgent(ThinkingAgent):
    def __init__(self, session: ResearchSession)
```

#### Method: `analyze_paper_deeply(paper: Dict) -> Dict`

**Input:** A paper dictionary with title, summary, authors, etc.

**Output:** Analysis dictionary containing:
```python
{
    "main_idea": str,           # Main idea of the paper
    "methodology": str,         # Research methodology used
    "contribution": list,       # List of key contributions
    "limitations": list,        # Identified limitations
    "relevance_score": float,   # 0-1 relevance to query
    "confidence_in_analysis": float  # Confidence score
}
```

---

### 5. SynthesisAgent

**File:** `gemini3_research_system.py` (Line 270)

**Purpose:** Generates comprehensive literature reviews by synthesizing findings across all papers.

```python
class SynthesisAgent(ThinkingAgent):
    def __init__(self, session: ResearchSession)
```

#### Method: `synthesize_literature(papers: List[Dict]) -> str`

**Input:** List of paper dictionaries

**Output:** Markdown-formatted literature review string including:
- Introduction and scope
- Thematic analysis
- Methodology comparison
- Key findings synthesis
- Conclusion

---

### 6. CriticAgent

**File:** `gemini3_research_system.py` (Line 331)

**Purpose:** Identifies research gaps and future opportunities.

```python
class CriticAgent(ThinkingAgent):
    def __init__(self, session: ResearchSession)
```

#### Method: `identify_gaps_and_opportunities(papers: List[Dict]) -> Dict`

**Input:** List of paper dictionaries

**Output:** Dictionary containing:
```python
{
    "major_gaps": [
        {
            "gap": str,
            "why_important": str
        }
    ],
    "future_directions": [
        {
            "direction": str
        }
    ],
    "unexplored_methods": list
}
```

---

### 7. TrendPredictionAgent

**File:** `gemini3_research_system.py` (Line 385)

**Purpose:** Predicts emerging research trends and provides forecasts.

```python
class TrendPredictionAgent(ThinkingAgent):
    def __init__(self, session: ResearchSession)
```

#### Methods

| Method | Parameters | Returns | Description |
|--------|------------|---------|-------------|
| `predict_trends()` | papers | Dict | Predict future research trends |
| `_extract_year()` | date_string | int or None | Extract year from date string |

**Output Structure:**
```python
{
    "growing_trends": [
        {
            "trend": str,
            "growth_rate": str
        }
    ],
    "declining_trends": list,
    "predictions_2026": list,
    "emerging_topics": list
}
```

---

## 📡 Data Sources

### Source Configuration

Each source has a dedicated fetch method with:
- Error handling
- Rate limiting
- Relevance scoring
- Standardized output format

### Standardized Paper Format

All sources return papers in this format:

```python
{
    "title": str,           # Paper title
    "summary": str,         # Abstract/summary
    "authors": List[str],   # List of author names
    "published": str,       # Publication date (YYYY-MM-DD)
    "link": str,           # URL to paper
    "pdf_link": str,       # Direct PDF URL (if available)
    "source": str,         # Source name (e.g., "arXiv")
    "citation_count": int, # Number of citations (if available)
    "relevance_score": float  # 0-1 relevance to query
}
```

### Source Details

#### 1. arXiv
- **API:** `http://export.arxiv.org/api/query`
- **Method:** `_fetch_arxiv()`
- **Features:** 
  - Searches title + abstract
  - Uses AND for multi-word queries
  - Returns PDF links directly

#### 2. Semantic Scholar
- **API:** `https://api.semanticscholar.org/graph/v1/paper/search`
- **Method:** `_fetch_semantic_scholar()`
- **Features:**
  - Includes citation counts
  - Open access PDF links
  - Large database (200M+ papers)

#### 3. PubMed
- **API:** `https://eutils.ncbi.nlm.nih.gov/entrez/eutils/`
- **Method:** `_fetch_pubmed()`
- **Features:**
  - Two-step: search then fetch details
  - Biomedical focus
  - Includes DOI links

#### 4. OpenAlex
- **API:** `https://api.openalex.org/works`
- **Method:** `_fetch_openalex()`
- **Features:**
  - 250M+ works
  - Fully open access
  - Citation counts included

#### 5. CrossRef
- **API:** `https://api.crossref.org/works`
- **Method:** `_fetch_crossref()`
- **Features:**
  - 140M+ DOI registrations
  - Comprehensive metadata
  - Publisher information

#### 6. CORE
- **API:** `https://api.core.ac.uk/v3/search/outputs`
- **Method:** `_fetch_core()`
- **Features:**
  - 200M+ open access papers
  - Full text access
  - Institutional repositories

---

## 🖥️ UI Components (app.py)

### Main Functions

#### `collect_papers(query, sources, limit)`
**Line:** 549

Collects papers from the orchestrator.

```python
def collect_papers(query, sources, limit):
    """
    Parameters:
        query (str): Search query
        sources (list): Selected data sources
        limit (int): Max papers per source
    
    Returns:
        tuple: (papers_list, orchestrator_instance)
    """
```

#### `analyze_papers(papers, orchestrator, deep=False)`
**Line:** 567

Analyzes papers using the DeepAnalyzerAgent.

```python
def analyze_papers(papers, orchestrator, deep=False):
    """
    Parameters:
        papers (list): Papers to analyze
        orchestrator: ResearchOrchestrator instance
        deep (bool): Whether to do deep analysis
    
    Returns:
        list: Analysis results for each paper
    """
```

#### `synthesize_literature(papers, orchestrator)`
**Line:** 583

Generates literature review.

#### `find_research_gaps(papers, orchestrator)`
**Line:** 586

Identifies research gaps.

#### `predict_trends(papers, orchestrator)`
**Line:** 589

Predicts future trends.

#### `escape_html(text)`
**Line:** 592

Escapes HTML special characters for safe rendering.

---

### UI Tabs

| Tab | Purpose | Agent Used |
|-----|---------|------------|
| 📄 Papers | Display fetched papers | Collector |
| 🧠 Analysis | Deep paper analysis | DeepAnalyzerAgent |
| 📚 Literature | Synthesized literature review | SynthesisAgent |
| 🔍 Gaps | Research gaps | CriticAgent |
| 📈 Trends | Future predictions | TrendPredictionAgent |
| 🤖 Agents | Agent status monitoring | All |

---

### Session State Variables

Streamlit session state variables used:

```python
st.session_state.papers        # List of fetched papers
st.session_state.analyses      # Deep analysis results
st.session_state.lit_review    # Literature review text
st.session_state.gaps          # Research gaps
st.session_state.trends        # Trend predictions
st.session_state.error         # Error messages
st.session_state.search_started # Search in progress flag
st.session_state.step          # Current workflow step
st.session_state.agent_status  # Status of each agent
```

---

## ⚙️ Configuration

### Environment Variables

Create a `.env` file:

```env
GEMINI_API_KEY=your_api_key_here
```

### Sidebar Options

| Option | Default | Description |
|--------|---------|-------------|
| Max Papers per Source | 5 | Number of papers to fetch from each source |
| Enable Deep Analysis | True | Use AI for paper analysis |
| Enable Literature Review | True | Generate synthesized review |
| Enable Gap Analysis | True | Identify research gaps |
| Enable Trend Prediction | True | Predict future trends |

---

## 🔄 Workflow

### Complete Research Workflow

```
1. USER INPUT
   └── Enter research query
   
2. PAPER COLLECTION (Parallel)
   ├── arXiv
   ├── Semantic Scholar
   ├── PubMed
   ├── OpenAlex
   ├── CrossRef
   └── CORE

3. DEDUPLICATION
   └── Remove duplicate papers by title
   
4. RELEVANCE SORTING
   └── Sort by relevance score

5. DEEP ANALYSIS (Optional)
   └── Analyze each paper with AI

6. SYNTHESIS (Optional)
   └── Generate literature review

7. GAP ANALYSIS (Optional)
   └── Identify research gaps

8. TREND PREDICTION (Optional)
   └── Predict future trends

9. DISPLAY RESULTS
   └── Show in UI tabs
```

### Marathon Analysis Phases

When running `run_marathon_analysis()`:

| Phase | Description | Duration |
|-------|-------------|----------|
| Phase 1 | Multi-Source Data Collection | ~30 seconds |
| Phase 2 | Deep Analysis with Extended Thinking | ~2-5 minutes |
| Phase 3 | Literature Synthesis | ~1-2 minutes |
| Phase 4 | Critical Gap Analysis | ~1 minute |
| Phase 5 | Trend Prediction | ~1 minute |
| Phase 6 | Session Summary | ~10 seconds |

---

## 🔌 API Reference

### Gemini API Usage

```python
from google import genai

# Initialize client
genai_client = genai.Client(api_key=GEMINI_API_KEY)

# Generate content
response = genai_client.models.generate_content(
    model="models/gemini-2.5-flash",
    contents=prompt
)

# Get response text
text = response.text
```

### Rate Limiting

- Each API call includes a 0.5 second delay
- Timeout set to 30 seconds for external APIs
- Error handling with graceful fallbacks

---

## 🐛 Error Handling

### Common Errors

| Error | Cause | Solution |
|-------|-------|----------|
| `GEMINI_API_KEY not set` | Missing .env file | Create .env with API key |
| `404 NOT_FOUND` | Invalid model name | Use `gemini-2.5-flash` |
| `Timeout` | Slow API response | Increase timeout or retry |
| `JSON Parse Error` | Invalid AI response | Falls back to empty dict |

### Error Recovery

The system includes:
- Try-catch blocks around all API calls
- Fallback values for failed operations
- User-friendly error messages in UI
- Agent status tracking for debugging

---

## 📊 Performance Tips

1. **Reduce API calls:** Lower max papers per source
2. **Skip optional features:** Disable deep analysis for faster results
3. **Use parallel fetching:** Already implemented for data collection
4. **Cache results:** Session state maintains results during session

---

## 🔒 Security

- API keys stored in `.env` (not in code)
- `.env` file should be in `.gitignore`
- No credentials logged or displayed
- HTML escaping prevents XSS

---

## 📝 Example Usage

```python
from gemini3_research_system import ResearchOrchestrator

# Initialize
orchestrator = ResearchOrchestrator("transformer architectures")

# Fetch papers (async)
import asyncio
papers = asyncio.run(orchestrator.fetch_papers_parallel(max_per_source=10))

# Analyze a paper
analysis = orchestrator.analyzer.analyze_paper_deeply(papers[0])

# Get literature review
review = orchestrator.synthesizer.synthesize_literature(papers)

# Find gaps
gaps = orchestrator.critic.identify_gaps_and_opportunities(papers)

# Predict trends
trends = orchestrator.trends.predict_trends(papers)
```

---

<div align="center">

**📖 Documentation Complete**

*For questions or issues, please refer to the README.md*

</div>
