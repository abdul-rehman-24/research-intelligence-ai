import streamlit as st
import time
from datetime import datetime
import html

# --- Backend imports ---
from gemini3_research_system import ResearchOrchestrator

# ============================================
# 🎨 MODERN UI CONFIGURATION
# ============================================

st.set_page_config(
    page_title="🧠 AI Research Intelligence",
    page_icon="🔬",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- Custom CSS - Impressive Neon Cyberpunk Theme ---
st.markdown("""
<style>
    /* Import Google Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;500;600;700;800;900&family=Rajdhani:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap');
    
    /* Root variables for easy theming */
    :root {
        --neon-cyan: #00f5ff;
        --neon-pink: #ff00e4;
        --neon-purple: #b026ff;
        --neon-blue: #4361ee;
        --neon-green: #39ff14;
        --dark-bg: #0a0a0f;
        --card-bg: rgba(15, 15, 25, 0.95);
        --glass-border: rgba(0, 245, 255, 0.2);
    }
    
    /* Global Styles */
    .stApp {
        background: radial-gradient(ellipse at top, #1a0a2e 0%, #0a0a0f 50%, #050510 100%);
    }
    
    /* Hide Streamlit branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Custom scrollbar */
    ::-webkit-scrollbar {width: 6px; height: 6px;}
    ::-webkit-scrollbar-track {background: transparent;}
    ::-webkit-scrollbar-thumb {
        background: linear-gradient(180deg, var(--neon-cyan) 0%, var(--neon-purple) 100%);
        border-radius: 3px;
    }
    
    /* Main Header */
    .main-header {
        font-family: 'Orbitron', sans-serif;
        font-size: 3rem;
        font-weight: 800;
        text-align: center;
        margin-bottom: 0.3rem;
        background: linear-gradient(90deg, var(--neon-cyan), var(--neon-pink), var(--neon-purple), var(--neon-cyan));
        background-size: 300% 100%;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        animation: gradient-shift 4s ease infinite;
        text-shadow: 0 0 40px rgba(0, 245, 255, 0.5);
    }
    
    @keyframes gradient-shift {
        0%, 100% {background-position: 0% 50%;}
        50% {background-position: 100% 50%;}
    }
    
    .sub-header {
        font-family: 'Rajdhani', sans-serif;
        color: rgba(255, 255, 255, 0.6);
        font-size: 1.1rem;
        text-align: center;
        margin-bottom: 2rem;
        letter-spacing: 3px;
        text-transform: uppercase;
    }
    
    /* Neon Paper Cards */
    .paper-card {
        background: linear-gradient(145deg, rgba(15, 15, 30, 0.9) 0%, rgba(25, 15, 45, 0.9) 100%);
        border: 1px solid rgba(0, 245, 255, 0.15);
        border-left: 3px solid var(--neon-cyan);
        border-radius: 12px;
        padding: 24px 28px;
        margin: 16px 0;
        position: relative;
        overflow: hidden;
        transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
    }
    
    .paper-card::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background: linear-gradient(135deg, rgba(0, 245, 255, 0.03) 0%, transparent 50%);
        pointer-events: none;
    }
    
    .paper-card:hover {
        border-color: var(--neon-cyan);
        transform: translateY(-4px);
        box-shadow: 
            0 0 30px rgba(0, 245, 255, 0.15),
            0 20px 40px rgba(0, 0, 0, 0.4),
            inset 0 1px 0 rgba(255, 255, 255, 0.05);
    }
    
    .paper-title {
        font-family: 'Rajdhani', sans-serif;
        color: #ffffff;
        font-size: 1.2rem;
        font-weight: 600;
        margin-bottom: 12px;
        line-height: 1.4;
        letter-spacing: 0.3px;
    }
    
    .paper-meta {
        font-family: 'Rajdhani', sans-serif;
        color: rgba(255, 255, 255, 0.5);
        font-size: 0.9rem;
        margin-bottom: 16px;
        display: flex;
        flex-wrap: wrap;
        align-items: center;
        gap: 20px;
    }
    
    .paper-meta span {
        display: inline-flex;
        align-items: center;
        gap: 6px;
    }
    
    .paper-abstract {
        font-family: 'Rajdhani', sans-serif;
        color: rgba(255, 255, 255, 0.7);
        font-size: 0.95rem;
        line-height: 1.7;
        margin-bottom: 20px;
        padding: 16px;
        background: rgba(0, 0, 0, 0.3);
        border-radius: 8px;
        border-left: 2px solid rgba(0, 245, 255, 0.3);
    }
    
    .paper-actions {
        display: flex;
        gap: 12px;
        flex-wrap: wrap;
    }
    
    .btn-neon {
        display: inline-flex;
        align-items: center;
        gap: 8px;
        padding: 10px 20px;
        font-family: 'Rajdhani', sans-serif;
        font-weight: 600;
        font-size: 0.9rem;
        text-decoration: none;
        border-radius: 6px;
        transition: all 0.3s ease;
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    
    .btn-primary {
        background: linear-gradient(135deg, var(--neon-cyan) 0%, var(--neon-blue) 100%);
        color: #0a0a0f !important;
        border: none;
    }
    
    .btn-primary:hover {
        box-shadow: 0 0 25px rgba(0, 245, 255, 0.5);
        transform: translateY(-2px);
    }
    
    .btn-secondary {
        background: transparent;
        color: var(--neon-pink) !important;
        border: 1px solid var(--neon-pink);
    }
    
    .btn-secondary:hover {
        background: rgba(255, 0, 228, 0.1);
        box-shadow: 0 0 20px rgba(255, 0, 228, 0.3);
    }
    
    .source-tag {
        font-family: 'JetBrains Mono', monospace;
        font-size: 0.7rem;
        padding: 5px 12px;
        background: linear-gradient(135deg, rgba(176, 38, 255, 0.2) 0%, rgba(67, 97, 238, 0.2) 100%);
        border: 1px solid rgba(176, 38, 255, 0.4);
        border-radius: 20px;
        color: var(--neon-purple);
        text-transform: uppercase;
        letter-spacing: 1px;
        white-space: nowrap;
    }
    
    /* NEW: Card header with flex layout */
    .card-header {
        display: flex;
        justify-content: space-between;
        align-items: flex-start;
        gap: 16px;
        margin-bottom: 12px;
    }
    
    .card-header h3.paper-title {
        margin: 0;
        flex: 1;
    }
    
    .source-badge {
        font-family: 'JetBrains Mono', monospace;
        font-size: 0.7rem;
        padding: 5px 12px;
        background: linear-gradient(135deg, rgba(176, 38, 255, 0.2) 0%, rgba(67, 97, 238, 0.2) 100%);
        border: 1px solid rgba(176, 38, 255, 0.4);
        border-radius: 20px;
        color: #b026ff;
        text-transform: uppercase;
        letter-spacing: 1px;
        white-space: nowrap;
        flex-shrink: 0;
    }
    
    .meta-badge {
        padding: 3px 10px;
        background: rgba(0, 245, 255, 0.1);
        border-radius: 12px;
        color: #00f5ff;
        font-size: 0.85rem;
    }
    
    .rel-badge {
        background: rgba(57, 255, 20, 0.15);
        color: #39ff14;
    }
    
    .btn-action {
        display: inline-flex;
        align-items: center;
        gap: 8px;
        padding: 10px 20px;
        font-family: 'Rajdhani', sans-serif;
        font-weight: 600;
        font-size: 0.9rem;
        text-decoration: none;
        border-radius: 6px;
        transition: all 0.3s ease;
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    
    .btn-view {
        background: linear-gradient(135deg, #00f5ff 0%, #4361ee 100%);
        color: #0a0a0f !important;
        border: none;
    }
    
    .btn-view:hover {
        box-shadow: 0 0 25px rgba(0, 245, 255, 0.5);
        transform: translateY(-2px);
        text-decoration: none;
        color: #0a0a0f !important;
    }
    
    .btn-pdf {
        background: transparent;
        color: #ff00e4 !important;
        border: 1px solid #ff00e4;
    }
    
    .btn-pdf:hover {
        background: rgba(255, 0, 228, 0.1);
        box-shadow: 0 0 20px rgba(255, 0, 228, 0.3);
        text-decoration: none;
        color: #ff00e4 !important;
    }
    
    /* Stats Cards */
    .stats-container {
        display: grid;
        grid-template-columns: repeat(4, 1fr);
        gap: 20px;
        margin: 30px 0;
    }
    
    .stat-card {
        background: linear-gradient(145deg, rgba(15, 15, 30, 0.8) 0%, rgba(25, 15, 45, 0.8) 100%);
        border: 1px solid rgba(0, 245, 255, 0.1);
        border-radius: 16px;
        padding: 24px;
        text-align: center;
        position: relative;
        overflow: hidden;
    }
    
    .stat-card::after {
        content: '';
        position: absolute;
        bottom: 0;
        left: 0;
        right: 0;
        height: 3px;
        background: linear-gradient(90deg, var(--neon-cyan), var(--neon-purple));
    }
    
    .stat-icon {
        font-size: 2rem;
        margin-bottom: 8px;
    }
    
    .stat-number {
        font-family: 'Orbitron', sans-serif;
        font-size: 2.5rem;
        font-weight: 700;
        background: linear-gradient(135deg, var(--neon-cyan) 0%, var(--neon-pink) 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    
    .stat-label {
        font-family: 'Rajdhani', sans-serif;
        color: rgba(255, 255, 255, 0.5);
        font-size: 0.85rem;
        text-transform: uppercase;
        letter-spacing: 2px;
        margin-top: 8px;
    }
    
    /* Tabs styling */
    .stTabs [data-baseweb="tab-list"] {
        gap: 4px;
        background: rgba(15, 15, 25, 0.6);
        padding: 6px;
        border-radius: 10px;
        border: 1px solid rgba(0, 245, 255, 0.1);
    }
    
    .stTabs [data-baseweb="tab"] {
        font-family: 'Rajdhani', sans-serif;
        font-weight: 600;
        background: transparent;
        border-radius: 8px;
        color: rgba(255, 255, 255, 0.6);
        padding: 10px 20px;
        letter-spacing: 0.5px;
    }
    
    .stTabs [aria-selected="true"] {
        background: linear-gradient(135deg, var(--neon-cyan) 0%, var(--neon-blue) 100%) !important;
        color: #0a0a0f !important;
    }
    
    /* Progress bar */
    .stProgress > div > div {
        background: linear-gradient(90deg, var(--neon-cyan) 0%, var(--neon-pink) 50%, var(--neon-purple) 100%);
        border-radius: 10px;
        box-shadow: 0 0 20px rgba(0, 245, 255, 0.5);
    }
    
    /* Sidebar */
    section[data-testid="stSidebar"] {
        background: linear-gradient(180deg, rgba(15, 10, 30, 0.98) 0%, rgba(5, 5, 15, 0.98) 100%);
        border-right: 1px solid rgba(0, 245, 255, 0.1);
    }
    
    section[data-testid="stSidebar"] .stButton button {
        font-family: 'Orbitron', sans-serif;
        background: linear-gradient(135deg, var(--neon-cyan) 0%, var(--neon-blue) 100%);
        color: #0a0a0f;
        border: none;
        border-radius: 8px;
        padding: 14px 24px;
        font-weight: 700;
        width: 100%;
        text-transform: uppercase;
        letter-spacing: 2px;
        transition: all 0.3s ease;
    }
    
    section[data-testid="stSidebar"] .stButton button:hover {
        box-shadow: 0 0 30px rgba(0, 245, 255, 0.6);
        transform: scale(1.02);
    }
    
    /* Agent Cards */
    .agent-card {
        background: linear-gradient(145deg, rgba(15, 15, 30, 0.9) 0%, rgba(25, 15, 45, 0.9) 100%);
        border: 1px solid rgba(0, 245, 255, 0.1);
        border-radius: 12px;
        padding: 20px;
        margin-bottom: 16px;
        display: flex;
        align-items: center;
        gap: 20px;
    }
    
    .agent-avatar {
        width: 56px;
        height: 56px;
        border-radius: 12px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 1.8rem;
    }
    
    .agent-running {
        background: linear-gradient(135deg, var(--neon-pink) 0%, var(--neon-purple) 100%);
        animation: pulse-glow 2s ease-in-out infinite;
    }
    
    .agent-done {
        background: linear-gradient(135deg, var(--neon-cyan) 0%, var(--neon-green) 100%);
    }
    
    .agent-waiting {
        background: rgba(255, 255, 255, 0.05);
        border: 1px dashed rgba(255, 255, 255, 0.2);
    }
    
    @keyframes pulse-glow {
        0%, 100% {box-shadow: 0 0 20px rgba(255, 0, 228, 0.5);}
        50% {box-shadow: 0 0 40px rgba(255, 0, 228, 0.8);}
    }
    
    .agent-name {
        font-family: 'Rajdhani', sans-serif;
        font-size: 1.1rem;
        font-weight: 600;
        color: #ffffff;
        margin: 0;
    }
    
    .agent-desc {
        font-family: 'Rajdhani', sans-serif;
        font-size: 0.85rem;
        color: rgba(255, 255, 255, 0.5);
        margin: 4px 0 0 0;
    }
    
    .agent-status {
        font-family: 'JetBrains Mono', monospace;
        font-size: 0.8rem;
        padding: 6px 14px;
        border-radius: 20px;
        margin-left: auto;
    }
    
    .status-running {
        background: rgba(255, 0, 228, 0.2);
        color: var(--neon-pink);
        border: 1px solid var(--neon-pink);
    }
    
    .status-done {
        background: rgba(0, 245, 255, 0.2);
        color: var(--neon-cyan);
        border: 1px solid var(--neon-cyan);
    }
    
    .status-waiting {
        background: rgba(255, 255, 255, 0.05);
        color: rgba(255, 255, 255, 0.4);
        border: 1px solid rgba(255, 255, 255, 0.2);
    }
    
    /* Empty State */
    .empty-state {
        text-align: center;
        padding: 80px 40px;
    }
    
    .empty-state .icon {
        font-size: 5rem;
        margin-bottom: 24px;
        opacity: 0.3;
    }
    
    .empty-state h3 {
        font-family: 'Rajdhani', sans-serif;
        color: rgba(255, 255, 255, 0.6);
        font-size: 1.5rem;
        margin-bottom: 12px;
    }
    
    .empty-state p {
        font-family: 'Rajdhani', sans-serif;
        color: rgba(255, 255, 255, 0.4);
        font-size: 1rem;
    }
    
    /* Glass Card */
    .glass-card {
        background: linear-gradient(145deg, rgba(15, 15, 30, 0.9) 0%, rgba(25, 15, 45, 0.9) 100%);
        border: 1px solid rgba(0, 245, 255, 0.1);
        border-radius: 16px;
        padding: 24px;
        margin-bottom: 20px;
    }
    
    /* Filter row */
    .filter-row {
        display: flex;
        gap: 16px;
        margin-bottom: 24px;
        align-items: center;
    }
    
    /* Metric highlight */
    .metric-highlight {
        font-family: 'Orbitron', sans-serif;
        color: var(--neon-cyan);
    }
    
    /* Section headers */
    .section-header {
        font-family: 'Orbitron', sans-serif;
        font-size: 1.2rem;
        color: var(--neon-cyan);
        margin-bottom: 20px;
        padding-bottom: 10px;
        border-bottom: 1px solid rgba(0, 245, 255, 0.2);
    }
</style>
""", unsafe_allow_html=True)

# ============================================
# 🔧 BACKEND FUNCTIONS
# ============================================

def collect_papers(query, sources, limit):
    orchestrator = ResearchOrchestrator(query)
    papers = []
    if "arXiv" in sources:
        papers += orchestrator._fetch_arxiv(query, limit)
    if "Semantic Scholar" in sources:
        papers += orchestrator._fetch_semantic_scholar(query, limit)
    if "PubMed" in sources:
        papers += orchestrator._fetch_pubmed(query, limit)
    if "OpenAlex" in sources:
        papers += orchestrator._fetch_openalex(query, limit)
    if "CrossRef" in sources:
        papers += orchestrator._fetch_crossref(query, limit)
    if "CORE" in sources:
        papers += orchestrator._fetch_core(query, limit)
    papers = orchestrator._deduplicate_papers(papers)
    return papers

def analyze_papers(papers, orchestrator, deep=False):
    analyses = []
    for paper in papers[:10]:
        analysis = orchestrator.analyzer.analyze_paper_deeply(paper)
        paper['analysis'] = analysis
        analyses.append({
            'title': paper.get('title', ''),
            'main_idea': analysis.get('main_contribution', ''),
            'contribution': analysis.get('novel_aspects', []),
            'limitations': analysis.get('limitations', []),
            'novelty_score': analysis.get('technical_novelty', 0),
            'innovation_score': analysis.get('innovation_score', 0),
            'self_corrections': analysis.get('self_corrections', [])
        })
    return analyses

def synthesize_literature(papers, orchestrator):
    return orchestrator.synthesizer.synthesize_literature(papers)

def find_research_gaps(papers, orchestrator):
    return orchestrator.critic.identify_gaps_and_opportunities(papers)

def predict_trends(papers, orchestrator):
    return orchestrator.trends.predict_trends(papers)

def escape_html(text):
    """Safely escape HTML to prevent rendering issues"""
    if text is None:
        return ""
    return html.escape(str(text))

# ============================================
# 🎯 SESSION STATE
# ============================================

defaults = {
    'step': 0,
    'papers': [],
    'analyses': [],
    'literature': '',
    'gaps': {},
    'trends': {},
    'agent_status': {},
    'error': None,
    'search_started': False,
    'orchestrator': None
}

for key, value in defaults.items():
    if key not in st.session_state:
        st.session_state[key] = value

# ============================================
# 🎨 SIDEBAR
# ============================================

with st.sidebar:
    st.markdown("""
    <div style="text-align: center; padding: 30px 0 20px 0;">
        <div style="font-size: 3.5rem; margin-bottom: 12px; filter: drop-shadow(0 0 20px rgba(0, 245, 255, 0.5));">🧠</div>
        <h2 style="font-family: 'Orbitron', sans-serif; color: #00f5ff; margin: 0; font-size: 1.1rem; letter-spacing: 3px;">RESEARCH AI</h2>
        <p style="font-family: 'Rajdhani', sans-serif; color: rgba(255,255,255,0.4); font-size: 0.8rem; margin-top: 8px; letter-spacing: 2px;">POWERED BY GEMINI 3</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    st.markdown('<p style="font-family: Rajdhani; color: #00f5ff; font-size: 0.9rem; letter-spacing: 2px; margin-bottom: 8px;">🎯 RESEARCH TOPIC</p>', unsafe_allow_html=True)
    query = st.text_input("Topic", placeholder="e.g., transformer models in healthcare", label_visibility="collapsed")
    
    st.markdown("")
    st.markdown('<p style="font-family: Rajdhani; color: #00f5ff; font-size: 0.9rem; letter-spacing: 2px; margin-bottom: 8px;">📚 DATA SOURCES</p>', unsafe_allow_html=True)
    sources = st.multiselect(
        "Sources",
        ["arXiv", "Semantic Scholar", "PubMed", "OpenAlex", "CrossRef", "CORE"],
        default=["arXiv", "Semantic Scholar", "OpenAlex"],
        label_visibility="collapsed"
    )
    
    st.markdown("")
    st.markdown('<p style="font-family: Rajdhani; color: #00f5ff; font-size: 0.9rem; letter-spacing: 2px; margin-bottom: 8px;">📊 PAPERS PER SOURCE</p>', unsafe_allow_html=True)
    limit = st.slider("Limit", 5, 30, 10, label_visibility="collapsed")
    
    st.markdown("")
    st.markdown('<p style="font-family: Rajdhani; color: #00f5ff; font-size: 0.9rem; letter-spacing: 2px; margin-bottom: 8px;">⚙️ ANALYSIS OPTIONS</p>', unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        deep_analysis = st.checkbox("Deep Analysis", value=True)
        gap_analysis = st.checkbox("Gap Analysis", value=True)
    with col2:
        trend_prediction = st.checkbox("Trends", value=True)
        quota_safe = st.checkbox("Lite Mode", value=False)
    
    st.markdown("")
    st.markdown("")
    start_btn = st.button("⚡ LAUNCH RESEARCH", use_container_width=True, type="primary")
    
    if st.session_state.papers:
        st.markdown("---")
        st.markdown('<p style="font-family: Orbitron; color: #00f5ff; font-size: 0.8rem; letter-spacing: 2px;">SESSION STATS</p>', unsafe_allow_html=True)
        num_papers = len(st.session_state.papers)
        num_sources = len(set(p.get('source', '') for p in st.session_state.papers))
        num_analyzed = len(st.session_state.analyses)
        sidebar_stats = '<div style="background: rgba(0, 245, 255, 0.05); border: 1px solid rgba(0, 245, 255, 0.1); border-radius: 12px; padding: 16px; margin-top: 12px;">'
        sidebar_stats += f'<div style="display: flex; justify-content: space-between; margin-bottom: 10px; font-family: Rajdhani;"><span style="color: rgba(255,255,255,0.5);">Papers</span><span style="color: #00f5ff; font-weight: 600;">{num_papers}</span></div>'
        sidebar_stats += f'<div style="display: flex; justify-content: space-between; margin-bottom: 10px; font-family: Rajdhani;"><span style="color: rgba(255,255,255,0.5);">Sources</span><span style="color: #00f5ff; font-weight: 600;">{num_sources}</span></div>'
        sidebar_stats += f'<div style="display: flex; justify-content: space-between; font-family: Rajdhani;"><span style="color: rgba(255,255,255,0.5);">Analyzed</span><span style="color: #00f5ff; font-weight: 600;">{num_analyzed}</span></div>'
        sidebar_stats += '</div>'
        st.markdown(sidebar_stats, unsafe_allow_html=True)

# ============================================
# 🎬 MAIN CONTENT
# ============================================

st.markdown('<h1 class="main-header">🔬 AI RESEARCH INTELLIGENCE</h1>', unsafe_allow_html=True)
st.markdown('<p class="sub-header">Multi-Agent Academic Discovery System</p>', unsafe_allow_html=True)

# Progress
if st.session_state.search_started:
    st.progress(min(st.session_state.step / 5, 1.0))

# ============================================
# 🔄 ORCHESTRATION
# ============================================

if start_btn and query:
    st.session_state.error = None
    st.session_state.step = 0
    st.session_state.search_started = True
    st.session_state.orchestrator = ResearchOrchestrator(query)
    
    try:
        st.session_state.agent_status = {"Collector": "running"}
        with st.spinner("🔍 Scanning academic databases..."):
            st.session_state.papers = collect_papers(query, sources, limit)
        st.session_state.agent_status["Collector"] = "done"
        st.session_state.step = 1
        
        if st.session_state.papers and not quota_safe:
            st.session_state.agent_status["Analyzer"] = "running"
            with st.spinner("🧠 Deep analysis with Gemini 3..."):
                if deep_analysis:
                    st.session_state.analyses = analyze_papers(
                        st.session_state.papers, 
                        st.session_state.orchestrator, 
                        deep=True
                    )
            st.session_state.agent_status["Analyzer"] = "done"
            st.session_state.step = 2
            
            st.session_state.agent_status["Synthesis"] = "running"
            with st.spinner("📚 Synthesizing literature..."):
                st.session_state.literature = synthesize_literature(
                    st.session_state.papers,
                    st.session_state.orchestrator
                )
            st.session_state.agent_status["Synthesis"] = "done"
            st.session_state.step = 3
            
            if gap_analysis:
                st.session_state.agent_status["Critic"] = "running"
                with st.spinner("🔍 Identifying gaps..."):
                    st.session_state.gaps = find_research_gaps(
                        st.session_state.papers,
                        st.session_state.orchestrator
                    )
                st.session_state.agent_status["Critic"] = "done"
                st.session_state.step = 4
            
            if trend_prediction:
                st.session_state.agent_status["Trends"] = "running"
                with st.spinner("📈 Predicting trends..."):
                    st.session_state.trends = predict_trends(
                        st.session_state.papers,
                        st.session_state.orchestrator
                    )
                st.session_state.agent_status["Trends"] = "done"
                st.session_state.step = 5
        
        st.rerun()
        
    except Exception as e:
        st.session_state.error = f"❌ {str(e)}"

# ============================================
# 📊 STATS
# ============================================

if st.session_state.papers:
    cols = st.columns(4)
    stats = [
        ("📄", len(st.session_state.papers), "Papers"),
        ("🌐", len(set(p.get('source', '') for p in st.session_state.papers)), "Sources"),
        ("🧠", len(st.session_state.analyses), "Analyzed"),
        ("⚡", len(st.session_state.agent_status), "Agents")
    ]
    
    for col, (icon, num, label) in zip(cols, stats):
        with col:
            stat_html = f'<div class="stat-card"><div class="stat-icon">{icon}</div><div class="stat-number">{num}</div><div class="stat-label">{label}</div></div>'
            st.markdown(stat_html, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ============================================
# 📑 TABS
# ============================================

tabs = st.tabs(["📄 Papers", "🧠 Analysis", "📚 Literature", "🔍 Gaps", "📈 Trends", "🤖 Agents"])

# --- Papers Tab ---
with tabs[0]:
    if st.session_state.error:
        st.error(st.session_state.error)
    elif st.session_state.papers:
        col1, col2, col3 = st.columns([3, 1, 1])
        with col1:
            search_filter = st.text_input("Search", placeholder="Search by title...", label_visibility="collapsed")
        with col2:
            source_filter = st.selectbox("Source", ["All Sources"] + list(set(p.get('source', '') for p in st.session_state.papers)), label_visibility="collapsed")
        with col3:
            sort_by = st.selectbox("Sort", ["Relevance", "Date", "Citations"], label_visibility="collapsed")
        
        filtered_papers = st.session_state.papers
        if search_filter:
            filtered_papers = [p for p in filtered_papers if search_filter.lower() in p.get('title', '').lower()]
        if source_filter != "All Sources":
            filtered_papers = [p for p in filtered_papers if p.get('source') == source_filter]
        
        for paper in filtered_papers:
            title = escape_html(paper.get('title', 'Untitled'))
            authors_list = paper.get('authors', [])[:3]
            authors = escape_html(', '.join(authors_list)) if authors_list else 'Unknown'
            if len(paper.get('authors', [])) > 3:
                authors += f" +{len(paper.get('authors', [])) - 3}"
            
            pub = paper.get('published', '')[:10] if paper.get('published') else 'N/A'
            summary_raw = paper.get('summary', '') or ''
            summary = escape_html(summary_raw[:400] + '...' if len(summary_raw) > 400 else summary_raw)
            source = escape_html(paper.get('source', 'Unknown'))
            link = paper.get('link', '#')
            pdf = paper.get('pdf_link', '')
            
            citations = paper.get('citation_count', 0)
            cit_html = f'<span class="meta-badge">📊 {citations} citations</span>' if citations else ''
            
            relevance = paper.get('relevance_score', 0)
            rel_html = f'<span class="meta-badge rel-badge">🎯 {int(relevance*100)}%</span>' if relevance else ''
            
            pdf_btn = f'<a href="{pdf}" target="_blank" class="btn-action btn-pdf">📄 PDF</a>' if pdf else ''
            
            # Build HTML without multi-line formatting to avoid rendering issues
            card_html = '<div class="paper-card">'
            card_html += f'<div class="card-header"><h3 class="paper-title">{title}</h3><span class="source-badge">{source}</span></div>'
            card_html += f'<div class="paper-meta"><span>👥 {authors}</span><span>📅 {pub}</span>{cit_html}{rel_html}</div>'
            card_html += f'<p class="paper-abstract">{summary if summary else "No abstract available."}</p>'
            card_html += f'<div class="paper-actions"><a href="{link}" target="_blank" class="btn-action btn-view">🔗 View Paper</a>{pdf_btn}</div>'
            card_html += '</div>'
            
            st.markdown(card_html, unsafe_allow_html=True)
    else:
        empty_html = '<div class="empty-state"><div class="icon">🔬</div><h3>Ready to Discover</h3><p>Enter a research topic and launch your AI-powered search</p></div>'
        st.markdown(empty_html, unsafe_allow_html=True)

# --- Analysis Tab ---
with tabs[1]:
    if st.session_state.analyses:
        for i, a in enumerate(st.session_state.analyses, 1):
            with st.expander(f"📊 {a.get('title', f'Paper {i}')[:70]}...", expanded=i==1):
                c1, c2 = st.columns(2)
                with c1:
                    st.markdown("**🎯 Main Contribution**")
                    st.info(a.get('main_idea', 'Not analyzed'))
                    st.markdown("**💡 Novel Aspects**")
                    aspects = a.get('contribution', [])
                    if isinstance(aspects, list):
                        for asp in aspects[:3]:
                            st.markdown(f"• {asp}")
                with c2:
                    st.markdown("**⚠️ Limitations**")
                    lims = a.get('limitations', [])
                    if isinstance(lims, list):
                        for lim in lims[:3]:
                            st.markdown(f"• {lim}")
                    st.markdown("**📈 Scores**")
                    sc1, sc2 = st.columns(2)
                    sc1.metric("Innovation", f"{a.get('innovation_score', 0)}/10")
                    sc2.metric("Novelty", f"{a.get('novelty_score', 0)}/10")
    else:
        st.markdown('<div class="empty-state"><div class="icon">🧠</div><h3>No Analysis Yet</h3><p>Enable Deep Analysis and run a search</p></div>', unsafe_allow_html=True)

# --- Literature Tab ---
with tabs[2]:
    if st.session_state.literature:
        st.markdown('<div class="section-header">📚 AI-Generated Literature Review</div>', unsafe_allow_html=True)
        lit = st.session_state.literature
        if isinstance(lit, dict):
            lit = lit.get('raw_response', str(lit))
        st.markdown(lit)
    else:
        st.markdown('<div class="empty-state"><div class="icon">📚</div><h3>No Literature Review</h3><p>Run Deep Analysis to generate</p></div>', unsafe_allow_html=True)

# --- Gaps Tab ---
with tabs[3]:
    if st.session_state.gaps and isinstance(st.session_state.gaps, dict):
        gaps = st.session_state.gaps
        c1, c2 = st.columns(2)
        with c1:
            st.markdown('<div class="section-header">🎯 Research Gaps</div>', unsafe_allow_html=True)
            for gap in gaps.get('major_gaps', [])[:5]:
                if isinstance(gap, dict):
                    gap_html = f'<div class="glass-card"><strong style="color: #ff00e4;">{escape_html(gap.get("gap", ""))}</strong><p style="color: rgba(255,255,255,0.6); margin-top: 8px;">{escape_html(gap.get("why_important", ""))}</p></div>'
                    st.markdown(gap_html, unsafe_allow_html=True)
                else:
                    st.info(gap)
        with c2:
            st.markdown('<div class="section-header">🚀 Future Directions</div>', unsafe_allow_html=True)
            for d in gaps.get('future_directions', [])[:5]:
                if isinstance(d, dict):
                    dir_html = f'<div class="glass-card"><strong style="color: #00f5ff;">{escape_html(d.get("direction", ""))}</strong></div>'
                    st.markdown(dir_html, unsafe_allow_html=True)
                else:
                    st.info(d)
    else:
        st.markdown('<div class="empty-state"><div class="icon">🔍</div><h3>No Gaps Identified</h3><p>Enable Gap Analysis</p></div>', unsafe_allow_html=True)

# --- Trends Tab ---
with tabs[4]:
    if st.session_state.trends and isinstance(st.session_state.trends, dict):
        trends = st.session_state.trends
        c1, c2 = st.columns(2)
        with c1:
            st.markdown('<div class="section-header">📈 Growing Trends</div>', unsafe_allow_html=True)
            for t in trends.get('growing_trends', [])[:5]:
                if isinstance(t, dict):
                    st.success(f"📈 {t.get('trend', '')} ({t.get('growth_rate', 'N/A')})")
                else:
                    st.success(f"📈 {t}")
        with c2:
            st.markdown('<div class="section-header">🔮 2026 Predictions</div>', unsafe_allow_html=True)
            for p in trends.get('predictions_2026', [])[:5]:
                st.info(f"🔮 {p}")
    else:
        st.markdown('<div class="empty-state"><div class="icon">📈</div><h3>No Trends</h3><p>Enable Trend Prediction</p></div>', unsafe_allow_html=True)

# --- Agents Tab ---  
with tabs[5]:
    st.markdown('<div class="section-header">🤖 Multi-Agent Orchestration</div>', unsafe_allow_html=True)
    
    agents = [
        ("🔍", "Collector Agent", "Parallel fetch from 6 academic APIs"),
        ("🧠", "Analyzer Agent", "Deep analysis with Gemini 3 Extended Thinking"),
        ("📚", "Synthesis Agent", "Literature review generation"),
        ("🔍", "Critic Agent", "Research gap identification"),
        ("📈", "Trend Agent", "Future trend prediction"),
    ]
    
    for icon, name, desc in agents:
        key = name.split()[0]
        status = st.session_state.agent_status.get(key, "waiting")
        
        if status == "running":
            avatar_class = "agent-running"
            status_class = "status-running"
            status_text = "● RUNNING"
        elif status == "done":
            avatar_class = "agent-done"
            status_class = "status-done"
            status_text = "✓ COMPLETE"
        else:
            avatar_class = "agent-waiting"
            status_class = "status-waiting"
            status_text = "○ STANDBY"
        
        agent_html = f'<div class="agent-card"><div class="agent-avatar {avatar_class}">{icon}</div><div style="flex: 1;"><p class="agent-name">{name}</p><p class="agent-desc">{desc}</p></div><span class="agent-status {status_class}">{status_text}</span></div>'
        st.markdown(agent_html, unsafe_allow_html=True)

# ============================================
# 📝 FOOTER
# ============================================

st.markdown("<br><hr style='border-color: rgba(0,245,255,0.1);'>", unsafe_allow_html=True)
footer_html = '<div style="text-align: center; padding: 20px; font-family: Rajdhani;"><p style="color: rgba(255,255,255,0.4); font-size: 0.9rem;">🏆 <strong style="color: #00f5ff;">GEMINI 3 HACKATHON</strong> • Multi-Agent Research Intelligence System</p></div>'
st.markdown(footer_html, unsafe_allow_html=True)
