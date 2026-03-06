import streamlit as st
import plotly.graph_objects as go

st.set_page_config(
    page_title="Animal Capital — Window Pane Manufacturing",
    page_icon="🏭",
    layout="wide",
    initial_sidebar_state="expanded",
)

# --- COLORS matching Piccoli Mondi aesthetic ---
BG = "#FAF5EF"
CARD = "#FFFFFF"
TEXT = "#1A1A1A"
TEXT_SEC = "#6B6B6B"
TEXT_DIM = "#A0A0A0"
PINK = "#F2639A"
ORANGE = "#F5A623"
GREEN = "#34C48B"
RED = "#E5534B"
BLUE = "#4A90D9"
BORDER = "#E8E0D8"

st.markdown(f"""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&family=IBM+Plex+Mono:wght@400;500;600;700&display=swap');

html, body, [class*="css"] {{
    font-family: 'Inter', sans-serif;
    color: {TEXT};
}}

.stApp {{
    background-color: {BG};
}}

.main .block-container {{
    max-width: 880px;
    padding-top: 1rem;
}}

h1 {{ color: {TEXT} !important; font-weight: 900 !important; letter-spacing: -0.03em; }}
h2 {{ color: {TEXT} !important; font-weight: 800 !important; letter-spacing: -0.02em; }}
h3, h4 {{ color: {TEXT} !important; font-weight: 700 !important; }}

p, li, .stMarkdown {{ color: {TEXT_SEC}; }}

/* Sidebar */
section[data-testid="stSidebar"] {{
    background-color: {CARD};
    border-right: 1px solid {BORDER};
}}

section[data-testid="stSidebar"] .stMarkdown p,
section[data-testid="stSidebar"] .stMarkdown li {{
    color: {TEXT_SEC};
}}

section[data-testid="stSidebar"] h1,
section[data-testid="stSidebar"] h2,
section[data-testid="stSidebar"] h3 {{
    color: {TEXT} !important;
}}

/* Metrics */
div[data-testid="stMetricValue"] {{
    font-family: 'IBM Plex Mono', monospace;
    font-weight: 800;
    color: {TEXT} !important;
}}

div[data-testid="stMetricLabel"] {{
    font-family: 'IBM Plex Mono', monospace;
    font-size: 10px !important;
    text-transform: uppercase;
    letter-spacing: 1.5px;
    color: {TEXT_DIM} !important;
}}

div[data-testid="stMetricDelta"] {{
    font-family: 'IBM Plex Mono', monospace;
}}

/* Badge */
.badge {{
    display: inline-block;
    font-family: 'IBM Plex Mono', monospace;
    font-size: 10px;
    font-weight: 700;
    letter-spacing: 2px;
    text-transform: uppercase;
    padding: 6px 16px;
    border-radius: 100px;
    margin-right: 8px;
    margin-bottom: 8px;
}}

.badge-pink {{
    color: {PINK};
    background: rgba(242,99,154,0.1);
    border: 1px solid rgba(242,99,154,0.25);
}}

.badge-orange {{
    color: {ORANGE};
    background: rgba(245,166,35,0.1);
    border: 1px solid rgba(245,166,35,0.25);
}}

.badge-dark {{
    color: {TEXT};
    background: {TEXT};
    color: white;
    border: none;
}}

/* Cards */
.card {{
    background: {CARD};
    border: 1px solid {BORDER};
    border-radius: 16px;
    padding: 24px;
    margin-bottom: 16px;
}}

/* Callout */
.callout {{
    border-radius: 12px;
    padding: 20px 24px;
    margin: 20px 0;
}}

.callout-red {{
    background: rgba(229,83,75,0.06);
    border: 1px solid rgba(229,83,75,0.2);
    border-left: 4px solid {RED};
}}

.callout-red .c-title {{
    color: {RED};
    font-weight: 800;
    font-size: 14px;
    margin-bottom: 8px;
}}

.callout-red .c-body {{
    color: {TEXT_SEC};
    font-size: 14px;
    line-height: 1.7;
}}

/* Competitor cards */
.comp-card {{
    background: {CARD};
    border: 1px solid {BORDER};
    border-radius: 14px;
    padding: 20px;
    margin-bottom: 12px;
}}

.comp-name {{
    font-size: 18px;
    font-weight: 800;
    color: {TEXT};
}}

.comp-hq {{
    font-family: 'IBM Plex Mono', monospace;
    font-size: 10px;
    color: {TEXT_DIM};
    background: {BG};
    padding: 3px 10px;
    border-radius: 100px;
    border: 1px solid {BORDER};
}}

.comp-rev {{
    font-family: 'IBM Plex Mono', monospace;
    font-size: 13px;
    color: {PINK};
    margin: 8px 0;
}}

.comp-edge {{
    font-size: 13px;
    color: {TEXT_SEC};
    line-height: 1.6;
}}

/* Verdict box */
.verdict-box {{
    background: {CARD};
    border-radius: 20px;
    padding: 36px;
    border: 2px solid {BORDER};
    margin: 20px 0 28px 0;
}}

/* Bull/Bear items */
.bull-item {{
    font-size: 14px;
    color: {TEXT_SEC};
    line-height: 1.7;
    margin-bottom: 10px;
    padding-left: 16px;
    border-left: 3px solid {GREEN};
}}

.bear-item {{
    font-size: 14px;
    color: {TEXT_SEC};
    line-height: 1.7;
    margin-bottom: 10px;
    padding-left: 16px;
    border-left: 3px solid {RED};
}}

/* Section divider */
.section-divider {{
    border: none;
    border-top: 1px solid {BORDER};
    margin: 56px 0 40px 0;
}}

/* Central nav */
.center-nav {{
    display: flex;
    justify-content: center;
    gap: 6px;
    flex-wrap: wrap;
    padding: 16px 0;
    margin-bottom: 32px;
    border-bottom: 1px solid {BORDER};
}}

.center-nav a {{
    font-family: 'IBM Plex Mono', monospace;
    font-size: 11px;
    font-weight: 600;
    letter-spacing: 0.5px;
    text-transform: uppercase;
    color: {TEXT_DIM};
    text-decoration: none;
    padding: 8px 16px;
    border-radius: 100px;
    border: 1px solid {BORDER};
    background: {CARD};
    transition: all 0.2s;
}}

.center-nav a:hover {{
    color: {TEXT};
    border-color: {TEXT};
    background: {CARD};
}}

/* Footer */
.footer {{
    text-align: center;
    font-family: 'IBM Plex Mono', monospace;
    font-size: 11px;
    color: {TEXT_DIM};
    padding-top: 32px;
    border-top: 1px solid {BORDER};
    margin-top: 48px;
}}

/* PL Table */
.pl-row {{
    display: flex;
    justify-content: space-between;
    padding: 12px 0;
    border-bottom: 1px solid {BORDER};
    font-size: 14px;
}}

.pl-label {{ color: {TEXT_SEC}; }}
.pl-label-bold {{ color: {TEXT}; font-weight: 800; }}
.pl-val {{ font-family: 'IBM Plex Mono', monospace; font-weight: 600; color: {TEXT}; }}
.pl-val-green {{ font-family: 'IBM Plex Mono', monospace; font-weight: 800; color: {GREEN}; }}
.pl-val-red {{ font-family: 'IBM Plex Mono', monospace; font-weight: 800; color: {RED}; }}

/* Location cards */
.loc-best {{ border-top: 4px solid {GREEN}; }}
.loc-good {{ border-top: 4px solid {ORANGE}; }}
.loc-weak {{ border-top: 4px solid {RED}; }}
</style>
""", unsafe_allow_html=True)


# --- HELPERS ---
def fmt(v):
    if abs(v) >= 1e9: return f"${v/1e9:.1f}B"
    if abs(v) >= 1e6: return f"${v/1e6:.1f}M"
    if abs(v) >= 1e3: return f"${v/1e3:.0f}K"
    return f"${v:.0f}"

def pct(v): return f"{v*100:.1f}%"

PLOT_LAYOUT = dict(
    plot_bgcolor='rgba(0,0,0,0)',
    paper_bgcolor='rgba(0,0,0,0)',
    font=dict(family="Inter", color=TEXT_SEC),
    margin=dict(l=10, r=10, t=10, b=10),
)


# --- SIDEBAR: ALWAYS-VISIBLE SLIDERS ---
with st.sidebar:
    st.markdown(f"### ▸ Financial Model")
    st.markdown("Adjust assumptions — all outputs update live.")
    st.markdown("---")

    capex = st.slider("Total Capex ($M)", 40, 120, 75, 5, format="$%dM") * 1e6
    energy_pct = st.slider("Energy (% of COGS)", 10, 35, 22, 1, format="%d%%") / 100
    gross_margin = st.slider("Gross Margin (%)", 18, 42, 30, 1, format="%d%%") / 100
    utilization = st.slider("Utilization Rate (%)", 50, 95, 85, 5, format="%d%%") / 100
    soda_ash = st.slider("Soda Ash Price ($/MT)", 150, 400, 280, 10, format="$%d")

    st.markdown("---")
    st.markdown(f"""
    <div style="font-size: 12px; color: {TEXT_DIM}; line-height: 1.7;">
        <strong style="color: {TEXT};">Model Basis</strong><br>
        250 TPD float glass plant<br>
        US Southeast location<br>
        $850/tonne ASP<br>
        15-year depreciation<br>
        25% corporate tax
    </div>
    """, unsafe_allow_html=True)


# --- FINANCIAL MODEL CALC ---
cap = 250 * 365 * utilization
rev = cap * 850
cogs = rev * (1 - gross_margin)
gp = rev - cogs
energy = cogs * energy_pct
soda_cost = cap * 0.2 * soda_ash
other_raw = max(0, cogs * 0.4 - soda_cost)
raw_total = soda_cost + other_raw
labor = max(0, cogs - energy - raw_total)
sga = rev * 0.08
ebitda = gp - sga
ebitda_m = ebitda / rev if rev else 0
da = capex / 15
ebit = ebitda - da
tax = max(0, ebit * 0.25)
ni = ebit - tax
ni_m = ni / rev if rev else 0
payback = capex / ebitda if ebitda > 0 else float('inf')
roic = (ebit * 0.75) / capex if capex > 0 and ebit > 0 else 0


# ========== HERO ==========
st.markdown(f"""
<div style="text-align: center; padding: 48px 0 32px 0;">
    <span class="badge badge-dark">Animal Capital</span>
    <span class="badge badge-orange">Track 2 — Incubation Assessment</span>
    <h1 style="font-size: clamp(36px, 6vw, 60px); line-height: 1.05; margin: 24px 0 16px 0;">
        Window Pane<br><span style="color: {PINK};">Manufacturing</span>
    </h1>
    <p style="font-size: 17px; color: {TEXT_SEC}; max-width: 560px; margin: 0 auto 24px; line-height: 1.6;">
        A structurally sound, cash-generating business with regulatory tailwinds — but a PE/infrastructure play, not a venture-scale opportunity.
    </p>
    <p style="font-family: 'IBM Plex Mono', monospace; font-size: 12px; color: {TEXT_DIM};">
        Vincenzo — MSc Quantitative Finance, Bocconi University &nbsp;&bull;&nbsp; March 2026
    </p>
</div>
""", unsafe_allow_html=True)

# --- CENTRAL NAVIGATION ---
st.markdown("""
<div class="center-nav">
    <a href="#executive-summary">Summary</a>
    <a href="#market-analysis">Market</a>
    <a href="#supply-chain">Supply Chain</a>
    <a href="#competition">Competition</a>
    <a href="#financial-model">Model</a>
    <a href="#location">Location</a>
    <a href="#verdict">Verdict</a>
</div>
""", unsafe_allow_html=True)


# ========== 01: EXECUTIVE SUMMARY ==========
st.markdown(f'<span class="badge badge-pink">01 — Executive Summary</span>', unsafe_allow_html=True)
st.header("Executive Summary", anchor="executive-summary")

c1, c2, c3, c4 = st.columns(4)
c1.metric("Global Market", "$156–180B", "4.2–8% CAGR")
c2.metric("US Market", "$12.3B", "5.1% → $15.7B")
c3.metric("Capex Required", fmt(capex))
pb_label = "✓ Strong" if payback < 4.5 else ("⚠ Moderate" if payback < 6 else "✗ Long")
c4.metric("Payback", f"{payback:.1f}y", pb_label)

st.markdown(f"""
The global flat glass market is estimated at **$156–180B in 2025** (Global Market Insights: $156.2B; 
MarketsandMarkets: $179.8B), growing at 4.2–8.0% CAGR through 2030. The **US market is $12.3B**, expanding 
at 5.1% to $15.7B by 2030, with building & construction at **78.6% of demand**. Solar glass is the fastest 
US segment at **7.35% CAGR**, driven by IRA incentives.

The cautionary tale of **View Inc. and Halio** — two smart glass ventures that **burned $3B and went bankrupt** 
capturing <0.05% of the architectural glass market — reinforces why this sector punishes VC-style capital deployment.
""")


# ========== 02: MARKET ==========
st.markdown('<hr class="section-divider">', unsafe_allow_html=True)
st.markdown(f'<span class="badge badge-pink">02 — Market Analysis</span>', unsafe_allow_html=True)
st.header("A $156–180B Market with Structural Tailwinds", anchor="market-analysis")

col1, col2 = st.columns(2)

with col1:
    st.markdown(f"#### US Market by End Use (2024)")
    fig = go.Figure()
    fig.add_trace(go.Bar(
        x=[78.6, 12, 5, 4.4],
        y=["Building &\nConstruction", "Automotive", "Solar Glass", "Electronics\n& Other"],
        orientation='h',
        marker=dict(color=[PINK, PINK, GREEN, ORANGE]),
        text=["78.6%", "12%", "5%", "4.4%"],
        textposition='auto',
        textfont=dict(family="IBM Plex Mono", size=13, color="white"),
    ))
    fig.update_layout(**PLOT_LAYOUT, height=220, xaxis=dict(showgrid=False, showticklabels=False, range=[0, 100]),
                      yaxis=dict(showgrid=False, autorange="reversed"), bargap=0.35)
    st.plotly_chart(fig, use_container_width=True)

with col2:
    st.markdown("#### Key Demand Drivers")
    st.markdown(f"""
    **EU EPBD Directive**  
    16% worst buildings renovated by 2030. All new buildings zero-emission by 2030.
    
    **US Inflation Reduction Act**  
    Manufacturing tax credits. 47% YoY solar capacity increase (Q1 2023).
    
    **Low-E Glass Adoption**  
    40.4% of US revenue (2024). $43.8B global market at 6.0% CAGR.
    
    **US Tariff Regime**  
    Reshaping supply chains toward domestic production.
    """)

st.markdown("""
The **energy-efficient glass** sub-market is $47.6B in 2025 (5.7% CAGR → $78.2B by 2034). 
**Low-E glass** — $43.8B projected to $65.8B by 2031 — is the growth story, with **45% of new construction** 
now specifying it. Incumbents with proprietary magnetron sputtering capture disproportionate value; 
commodity float producers compete on price alone.
""")


# ========== 03: SUPPLY CHAIN ==========
st.markdown('<hr class="section-divider">', unsafe_allow_html=True)
st.markdown(f'<span class="badge badge-pink">03 — Supply Chain & Raw Material Risk</span>', unsafe_allow_html=True)
st.header("The Soda Ash Problem", anchor="supply-chain")

col1, col2 = st.columns(2)

with col1:
    st.markdown("#### Batch Cost Breakdown")
    fig = go.Figure()
    fig.add_trace(go.Bar(
        x=[60, 20, 15, 5],
        y=["Soda Ash\n(60% batch)", "Silica Sand", "Energy\n(nat. gas)", "Other"],
        orientation='h',
        marker=dict(color=[RED, ORANGE, ORANGE, BLUE]),
        text=["60%", "20%", "15%", "5%"],
        textposition='auto',
        textfont=dict(family="IBM Plex Mono", size=13, color="white"),
    ))
    fig.update_layout(**PLOT_LAYOUT, height=200, xaxis=dict(showgrid=False, showticklabels=False, range=[0, 75]),
                      yaxis=dict(showgrid=False, autorange="reversed"), bargap=0.35)
    st.plotly_chart(fig, use_container_width=True)

with col2:
    st.markdown("#### US Soda Ash Price (2025)")
    fig = go.Figure()
    fig.add_trace(go.Bar(
        x=["Q1 '25", "Q2 '25", "Q3 '25"], y=[180, 257, 280],
        marker=dict(color=[BLUE, ORANGE, RED], line=dict(width=0)),
        text=["$180", "$257", "$280"], textposition='outside',
        textfont=dict(family="IBM Plex Mono", size=14, color=TEXT),
    ))
    fig.update_layout(**PLOT_LAYOUT, height=200, yaxis=dict(showgrid=False, showticklabels=False, range=[0, 340]),
                      xaxis=dict(showgrid=False), bargap=0.4)
    st.plotly_chart(fig, use_container_width=True)
    st.markdown(f'<p style="text-align:center; color:{RED}; font-weight:700; font-size:13px;">+55.6% increase Jan → Sep 2025</p>', unsafe_allow_html=True)

st.markdown(f"""
<div class="callout callout-red">
    <div class="c-title">⚠ Critical Risk: Soda Ash Volatility</div>
    <div class="c-body">
        Soda ash = 60% of batch costs. Q1 2025 spot prices spiked 18% month-on-month, triggering output cuts at 
        two Midwestern plants. US prices: $180 → $280/MT in 9 months. Glass manufacturing consumes 51%+ of global 
        soda ash. Without long-term supply contracts, margin compression of 3–5pp during spikes. Wyoming's Green River 
        Basin (90% of US production, 127B tonnes trona) offers geographic advantage — but only with secured offtake.
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown("""
Float glass requires **~9 GJ/tonne** with furnaces at 1,500°C+ continuously. Producing 1 MT of soda ash needs 
**~10,000 kWh**. Result: **60–75% of variable costs are commodity-linked** — structural disadvantage for 
undercapitalized entrants without hedging.
""")


# ========== 04: COMPETITION ==========
st.markdown('<hr class="section-divider">', unsafe_allow_html=True)
st.markdown(f'<span class="badge badge-pink">04 — Competitive Landscape</span>', unsafe_allow_html=True)
st.header("Five Incumbents, Accelerating Investment", anchor="competition")

comps = [
    ("Saint-Gobain", "France", "~€12B glass", "Record 11.7% op. margin (H1 2024). Volta low-CO₂ furnace with AGC. $970M India expansion."),
    ("AGC Inc.", "Japan", "~$6B glass", "Volta hybrid furnace co-dev. Leading magnetron sputtering IP. Deep R&D moat in coatings."),
    ("Şişecam", "Turkey", "~$3B", "$470M: 2 new float lines. $114M: 3 coating lines (Turkey, Italy, Bulgaria). Capacity: 22M→42M m²."),
    ("Guardian (Koch)", "USA", "~$5B", "Dominant US position. Koch vertical integration. Deep construction supply chain distribution."),
]

c1, c2 = st.columns(2)
for i, (name, hq, comp_rev, edge) in enumerate(comps):
    with (c1 if i % 2 == 0 else c2):
        st.markdown(f"""
<div class="comp-card">
    <div style="display: flex; justify-content: space-between; align-items: center;">
        <span class="comp-name">{name}</span>
        <span class="comp-hq">{hq}</span>
    </div>
    <div class="comp-rev">{comp_rev}</div>
    <div class="comp-edge">{edge}</div>
</div>
""", unsafe_allow_html=True)

st.markdown(f"""
<div class="callout callout-red">
    <div class="c-title">📉 The Smart Glass Graveyard</div>
    <div class="c-body">
        View Inc. and Halio Inc. — two VC-backed smart glass companies — went bankrupt with a combined 
        <strong>$3B loss</strong>, capturing <strong>&lt;0.05%</strong> of the architectural glass market. 
        Scale, distribution, and coating IP are the moats — not technology alone.
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown("""
**NSG/Pilkington** shuttered Gladbeck (Jan 2025) while converting Rossford, Ohio to TCO solar glass (Mar 2025). 
Incumbents pivot to **high-margin specialty**, not commodity float. Şişecam's $114M coating investment — 
nearly doubling coated capacity — shows the value chain migrating from raw float to processed glass.
""")


# ========== 05: FINANCIAL MODEL ==========
st.markdown('<hr class="section-divider">', unsafe_allow_html=True)
st.markdown(f'<span class="badge badge-pink">05 — Interactive Financial Model</span>', unsafe_allow_html=True)
st.header("Stress-Test the Unit Economics", anchor="financial-model")

st.markdown("*Use the **sidebar sliders** to adjust assumptions. All outputs below update in real-time.*")

# Key Outputs
st.markdown("#### Key Outputs — Steady State")
c1, c2, c3 = st.columns(3)
c1.metric("Revenue", fmt(rev))
c2.metric("EBITDA", fmt(ebitda), f"Margin: {pct(ebitda_m)}")
c3.metric("Net Income", fmt(ni), f"Margin: {pct(ni_m)}")

c4, c5, c6 = st.columns(3)
c4.metric("ROIC", pct(roic), "✓" if roic > 0.12 else ("⚠" if roic > 0.06 else "✗"))
c5.metric("Payback", f"{payback:.1f}y", "✓" if payback < 4.5 else ("⚠" if payback < 6 else "✗"))
c6.metric("Capacity", f"{cap:,.0f} MT/yr", f"{250} TPD × {utilization*100:.0f}%")

# 5-Year Ramp
st.markdown("#### 5-Year Revenue & EBITDA Ramp")
ramp = [0.55, 0.75, 0.90, 1.0, 1.0]
fig = go.Figure()
fig.add_trace(go.Bar(
    x=[f"Year {i+1}" for i in range(5)], y=[rev * r for r in ramp],
    name="Revenue", marker=dict(color=PINK),
    text=[fmt(rev * r) for r in ramp], textposition='outside',
    textfont=dict(family="IBM Plex Mono", size=11, color=PINK),
))
fig.add_trace(go.Bar(
    x=[f"Year {i+1}" for i in range(5)], y=[ebitda * r for r in ramp],
    name="EBITDA", marker=dict(color=GREEN),
    text=[fmt(ebitda * r) for r in ramp], textposition='outside',
    textfont=dict(family="IBM Plex Mono", size=11, color=GREEN),
))
fig.update_layout(**PLOT_LAYOUT, height=340,
    yaxis=dict(showgrid=True, gridcolor=BORDER, tickformat="$,.0f"),
    xaxis=dict(showgrid=False), barmode='group', bargap=0.3, bargroupgap=0.1,
    legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1, font=dict(size=12, color=TEXT)),
)
st.plotly_chart(fig, use_container_width=True)

# P&L Table
st.markdown("#### Simplified P&L — Steady State")
pl_items = [
    ("Revenue", rev, True, None),
    ("Raw Materials", -raw_total, False, None),
    ("Energy Costs", -energy, False, None),
    ("Labor & Other", -labor, False, None),
    ("Gross Profit", gp, True, "green"),
    ("SG&A (8%)", -sga, False, None),
    ("EBITDA", ebitda, True, "green" if ebitda > 0 else "red"),
    ("D&A (15y)", -da, False, None),
    ("EBIT", ebit, True, "green" if ebit > 0 else "red"),
    ("Tax (25%)", -tax, False, None),
    ("Net Income", ni, True, "green" if ni > 0 else "red"),
]

pl_html = f'<div class="card">'
for label, val, bold, tone in pl_items:
    lbl_cls = "pl-label-bold" if bold else "pl-label"
    val_cls = "pl-val-green" if tone == "green" else ("pl-val-red" if tone == "red" else "pl-val")
    if bold:
        val_cls = "pl-val-green" if tone == "green" else ("pl-val-red" if tone == "red" else "pl-val")
    pl_html += f'<div class="pl-row"><span class="{lbl_cls}">{label}</span><span class="{val_cls}">{fmt(val)}</span></div>'
pl_html += '</div>'
st.markdown(pl_html, unsafe_allow_html=True)


# ========== 06: LOCATION ==========
st.markdown('<hr class="section-divider">', unsafe_allow_html=True)
st.markdown(f'<span class="badge badge-pink">06 — Location Strategy</span>', unsafe_allow_html=True)
st.header("US Southeast: The Optimal Entry Point", anchor="location")

c1, c2, c3 = st.columns(3)
locs = [
    ("US Southeast", "Best", "Energy: $0.07–0.09/kWh. Largest construction corridor ($2.16T, +6.7% YoY). IRA credits. Rail from Wyoming soda ash.", "loc-best"),
    ("Turkey / E. Europe", "Good", "Şişecam investing $470M+. Labor cost advantage. EU EPBD demand. But: currency & geopolitical risk.", "loc-good"),
    ("US NE / West", "Weak", "Energy $0.12+/kWh. Regulatory burden. Higher labor. Guardian dominant. No cost advantage.", "loc-weak"),
]

for col, (region, score, factors, cls) in zip([c1, c2, c3], locs):
    score_color = GREEN if score == "Best" else (ORANGE if score == "Good" else RED)
    with col:
        st.markdown(f"""
<div class="comp-card {cls}">
    <div style="font-weight: 800; font-size: 16px; color: {TEXT};">{region}</div>
    <div style="font-family: 'IBM Plex Mono'; font-size: 12px; color: {score_color}; font-weight: 700; margin: 6px 0 12px;">{score}</div>
    <div style="font-size: 13px; color: {TEXT_SEC}; line-height: 1.6;">{factors}</div>
</div>
""", unsafe_allow_html=True)


# ========== 07: VERDICT ==========
st.markdown('<hr class="section-divider">', unsafe_allow_html=True)
st.markdown(f'<span class="badge badge-pink">07 — Investment Verdict</span>', unsafe_allow_html=True)
st.header("Should This Business Exist?", anchor="verdict")

st.markdown(f"""
<div class="verdict-box">
    <h2 style="font-size: 24px; line-height: 1.3; margin: 0;">
        Yes — as a <span style="color: {ORANGE}; border-bottom: 3px solid {ORANGE}; padding-bottom: 2px;">PE / Infrastructure</span> investment.<br>
        <span style="color: {RED};">Not as a venture bet.</span>
    </h2>
</div>
""", unsafe_allow_html=True)

c1, c2 = st.columns(2)

with c1:
    st.markdown(f"#### Bull Case")
    for b in [
        "Regulatory tailwinds (EPBD + IRA) create 5–10 year demand window",
        "25–35% gross margins with stable construction demand floor",
        "US tariffs provide natural moat; domestic supply gap exists",
        "~3-year payback at base; strong cash generation at scale",
        "Low-E adoption (45% of new construction) drives premiumization",
    ]:
        st.markdown(f'<div class="bull-item">{b}</div>', unsafe_allow_html=True)

with c2:
    st.markdown(f"#### Bear Case")
    for b in [
        "$75M+ capex is PE-scale (View/Halio burned $3B and failed)",
        "10–15% net margins: healthy for PE, insufficient for 10x VC",
        "Soda ash +55.6% in 2025 compresses margins unpredictably",
        "Incumbents investing $1B+ in coated glass expansion",
        "Without coating IP, competes on price alone — structurally weak",
    ]:
        st.markdown(f'<div class="bear-item">{b}</div>', unsafe_allow_html=True)

st.markdown(f"""
The ideal buyer is a **mid-market PE fund** with an industrial or building materials focus — 
one with portfolio companies providing distribution into US construction. The wrong buyer is a 
venture fund expecting software-like returns from capital-intensive manufacturing.

**For Animal Capital:** monitor for tech-enabled disruption — AI furnace optimization, 
novel coatings, ultra-thin glass for electronics — where smaller capital can achieve venture returns. 
The commodity layer itself belongs in a PE portfolio.
""")

# --- FOOTER ---
st.markdown(f"""
<div class="footer">
    Prepared by Vincenzo — MSc Quantitative Finance, Bocconi University — March 2026<br>
    Sources: Grand View Research, MarketsandMarkets, Mordor Intelligence, IMARC, Global Market Insights, Glass International, ChemAnalyst, PitchBook
</div>
""", unsafe_allow_html=True)
