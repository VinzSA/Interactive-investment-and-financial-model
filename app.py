import streamlit as st
import plotly.graph_objects as go

st.set_page_config(page_title="Animal Capital — Window Pane Manufacturing", page_icon="🏭", layout="wide", initial_sidebar_state="expanded")

# --- PALETTE ---
BG="#FAF5EF"; CARD="#FFFFFF"; TX="#1A1A1A"; TX2="#555555"; DIM="#999999"
PK="#E8527A"; OR="#E8943A"; GR="#2EA66F"; RD="#D44040"; BL="#3E7FBF"; BD="#E0D8D0"

st.markdown(f"""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&family=JetBrains+Mono:wght@400;500;600;700&display=swap');
html,body,[class*="css"]{{font-family:'Inter',sans-serif;color:{TX};}}
.stApp{{background-color:{BG};}}
.main .block-container{{max-width:900px;padding-top:1rem;}}
h1{{color:{TX}!important;font-weight:900!important;letter-spacing:-0.03em;}}
h2{{color:{TX}!important;font-weight:800!important;letter-spacing:-0.02em;font-size:28px!important;}}
h3{{color:{TX}!important;font-weight:700!important;font-size:18px!important;}}
section[data-testid="stSidebar"]{{background:{CARD};border-right:1px solid {BD};}}
div[data-testid="stMetricValue"],div[data-testid="stMetricLabel"],div[data-testid="stMetricDelta"]{{display:none;}}

.prose{{font-size:15.5px;line-height:1.85;color:{TX2};margin-bottom:16px;}}
.prose b{{color:{TX};font-weight:700;}}

/* HERO */
.hero{{text-align:center;padding:56px 24px 36px;position:relative;overflow:hidden;}}
.hero::before{{content:'';position:absolute;top:0;left:50%;transform:translateX(-50%);width:600px;height:600px;background:radial-gradient(circle,rgba(232,82,122,0.06) 0%,transparent 70%);pointer-events:none;}}
.hero-badge{{display:inline-block;font-family:'JetBrains Mono';font-size:10px;font-weight:700;letter-spacing:2px;text-transform:uppercase;padding:6px 16px;border-radius:100px;margin:0 4px 8px;}}
.hero-dark{{background:{TX};color:white;}}
.hero-or{{color:{OR};background:rgba(232,148,58,0.1);border:1px solid rgba(232,148,58,0.25);}}
.hero h1{{font-size:clamp(36px,6vw,58px);line-height:1.05;margin:24px 0 16px;position:relative;}}
.hero-sub{{font-size:17px;color:{TX2};max-width:580px;margin:0 auto 20px;line-height:1.65;}}
.hero-verdict{{display:inline-block;background:{CARD};border:2px solid {BD};border-radius:12px;padding:12px 28px;margin-top:12px;font-size:15px;font-weight:700;color:{TX};}}
.hero-verdict span{{color:{OR};}}

/* NAV */
.cnav{{display:flex;justify-content:center;gap:6px;flex-wrap:wrap;padding:16px 0;margin-bottom:36px;border-bottom:1px solid {BD};}}
.cnav a{{font-family:'JetBrains Mono';font-size:11px;font-weight:600;letter-spacing:0.5px;text-transform:uppercase;color:{DIM};text-decoration:none;padding:8px 16px;border-radius:100px;border:1px solid {BD};background:{CARD};transition:all 0.2s;}}
.cnav a:hover{{color:{TX};border-color:{TX};}}

/* ASSUMPTION CARDS */
.a-grid{{display:grid;grid-template-columns:repeat(5,1fr);gap:12px;margin-bottom:40px;}}
.a-card{{background:{CARD};border:1px solid {BD};border-radius:14px;padding:18px 16px;text-align:center;}}
.a-icon{{font-size:22px;margin-bottom:8px;}}
.a-label{{font-family:'JetBrains Mono';font-size:9px;font-weight:700;letter-spacing:1.5px;text-transform:uppercase;color:{DIM};margin-bottom:4px;}}
.a-value{{font-size:16px;font-weight:800;color:{TX};}}

/* BLOOMBERG METRIC */
.m-grid{{display:grid;grid-template-columns:repeat(4,1fr);gap:12px;margin-bottom:28px;}}
.m-card{{background:{CARD};border:1px solid {BD};border-left:4px solid {BD};border-radius:12px;padding:20px 18px;}}
.m-card-green{{border-left-color:{GR};}}
.m-card-red{{border-left-color:{RD};}}
.m-card-orange{{border-left-color:{OR};}}
.m-card-blue{{border-left-color:{BL};}}
.m-card-pink{{border-left-color:{PK};}}
.m-label{{font-family:'JetBrains Mono';font-size:9px;font-weight:700;letter-spacing:1.5px;text-transform:uppercase;color:{DIM};margin-bottom:6px;}}
.m-val{{font-family:'JetBrains Mono';font-size:28px;font-weight:800;color:{TX};line-height:1.1;}}
.m-sub{{font-family:'JetBrains Mono';font-size:11px;color:{DIM};margin-top:4px;}}

/* SECTION HEADER */
.sec{{display:flex;align-items:flex-start;gap:20px;margin-bottom:32px;}}
.sec-num{{font-family:'JetBrains Mono';font-size:64px;font-weight:900;color:rgba(232,82,122,0.12);line-height:1;flex-shrink:0;margin-top:-8px;}}
.sec-content{{flex:1;}}
.sec-tag{{font-family:'JetBrains Mono';font-size:10px;font-weight:700;letter-spacing:2px;text-transform:uppercase;color:{PK};margin-bottom:6px;}}

/* CARDS & CALLOUTS */
.card{{background:{CARD};border:1px solid {BD};border-radius:16px;padding:28px;margin-bottom:16px;}}
.callout{{border-radius:12px;padding:22px 26px;margin:24px 0;}}
.callout-red{{background:rgba(212,64,64,0.05);border:1px solid rgba(212,64,64,0.18);border-left:4px solid {RD};}}
.c-title{{color:{RD};font-weight:800;font-size:14px;margin-bottom:8px;}}
.c-body{{color:{TX2};font-size:14px;line-height:1.75;}}
.c-body b{{color:{TX};}}

/* COMP CARDS */
.comp-card{{background:{CARD};border:1px solid {BD};border-radius:14px;padding:22px;margin-bottom:12px;transition:box-shadow 0.2s;}}
.comp-card:hover{{box-shadow:0 4px 20px rgba(0,0,0,0.06);}}

/* VERDICT */
.verdict-box{{background:{CARD};border-radius:20px;padding:44px;border:2px solid {BD};margin:24px 0 32px;position:relative;overflow:hidden;}}
.verdict-box::before{{content:'';position:absolute;top:0;right:0;width:200px;height:200px;background:radial-gradient(circle,rgba(232,148,58,0.08) 0%,transparent 70%);pointer-events:none;}}
.bull-item{{font-size:14px;color:{TX2};line-height:1.75;margin-bottom:10px;padding-left:16px;border-left:3px solid {GR};}}
.bear-item{{font-size:14px;color:{TX2};line-height:1.75;margin-bottom:10px;padding-left:16px;border-left:3px solid {RD};}}

/* P&L */
.pl-row{{display:flex;justify-content:space-between;padding:12px 0;border-bottom:1px solid {BD};font-size:14px;}}
.pl-label{{color:{TX2};}}
.pl-bold{{color:{TX};font-weight:800;}}
.pl-val{{font-family:'JetBrains Mono';font-weight:600;color:{TX};}}
.pl-green{{font-family:'JetBrains Mono';font-weight:800;color:{GR};}}
.pl-red{{font-family:'JetBrains Mono';font-weight:800;color:{RD};}}

/* LOC */
.loc-best{{border-top:4px solid {GR};}}
.loc-good{{border-top:4px solid {OR};}}
.loc-weak{{border-top:4px solid {RD};}}

.divider{{border:none;border-top:1px solid {BD};margin:56px 0 40px;}}
.footer{{text-align:center;font-family:'JetBrains Mono';font-size:11px;color:{DIM};padding-top:32px;border-top:1px solid {BD};margin-top:48px;}}
</style>
""", unsafe_allow_html=True)

# --- HELPERS ---
def fmt(v):
    if abs(v)>=1e9: return f"${v/1e9:.1f}B"
    if abs(v)>=1e6: return f"${v/1e6:.1f}M"
    if abs(v)>=1e3: return f"${v/1e3:.0f}K"
    return f"${v:.0f}"
def pct(v): return f"{v*100:.1f}%"
def prose(t): st.markdown(f'<div class="prose">{t}</div>', unsafe_allow_html=True)
def sec(num, tag, title, anchor):
    st.markdown(f"""<div class="sec" id="{anchor}">
    <div class="sec-num">{num}</div>
    <div class="sec-content"><div class="sec-tag">{tag}</div><h2 style="margin:0;">{title}</h2></div>
    </div>""", unsafe_allow_html=True)
def metric(label, value, sub="", tone="blue"):
    st.markdown(f"""<div class="m-card m-card-{tone}">
    <div class="m-label">{label}</div><div class="m-val">{value}</div>
    {"<div class='m-sub'>"+sub+"</div>" if sub else ""}
    </div>""", unsafe_allow_html=True)

PL = dict(plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)', font=dict(family="Inter",color=TX2), margin=dict(l=10,r=10,t=10,b=10))

# --- SIDEBAR ---
with st.sidebar:
    st.markdown("### ▸ Financial Model")
    st.markdown(f'<div class="prose" style="font-size:13px;">Adjust assumptions — all outputs update live.</div>', unsafe_allow_html=True)
    st.markdown("---")
    capex = st.slider("Total Capex ($M)", 40, 120, 75, 5, format="$%dM") * 1e6
    energy_pct = st.slider("Energy (% of COGS)", 10, 35, 22, 1, format="%d%%") / 100
    gross_margin = st.slider("Gross Margin (%)", 18, 42, 30, 1, format="%d%%") / 100
    utilization = st.slider("Utilization Rate (%)", 50, 95, 85, 5, format="%d%%") / 100
    soda_ash = st.slider("Soda Ash Price ($/MT)", 150, 400, 280, 10, format="$%d")
    st.markdown("---")
    st.markdown(f"""<div style="font-size:12px;color:{DIM};line-height:1.7;">
    <b style="color:{TX};">Model Basis</b><br>250 TPD float glass plant<br>US Southeast location<br>$850/tonne ASP<br>15-year depreciation<br>25% corporate tax</div>""", unsafe_allow_html=True)

# --- CALC ---
cap=250*365*utilization; rev=cap*850; cogs=rev*(1-gross_margin); gp=rev-cogs
energy=cogs*energy_pct; soda_cost=cap*0.2*soda_ash; other_raw=max(0,cogs*0.4-soda_cost)
raw_total=soda_cost+other_raw; labor=max(0,cogs-energy-raw_total); sga=rev*0.08
ebitda=gp-sga; ebitda_m=ebitda/rev if rev else 0; da=capex/15; ebit=ebitda-da
tax=max(0,ebit*0.25); ni=ebit-tax; ni_m=ni/rev if rev else 0
payback=capex/ebitda if ebitda>0 else float('inf')
roic=(ebit*0.75)/capex if capex>0 and ebit>0 else 0

# ============ HERO ============
st.markdown(f"""<div class="hero">
<span class="hero-badge hero-dark">Animal Capital</span>
<span class="hero-badge hero-or">Track 2 — Incubation Assessment</span>
<h1>Window Pane <span style="color:{PK};">Manufacturing</span></h1>
<p class="hero-sub">A comprehensive evaluation of a greenfield float glass facility in the US Southeast — analyzing market dynamics, cost structure, competitive positioning, and investment returns.</p>
<div class="hero-verdict">Verdict: <span>PE / Infrastructure play</span> — not a venture bet</div>
<p style="font-family:'JetBrains Mono';font-size:12px;color:{DIM};margin-top:20px;">
Vincenzo Salerno &bull; MSc Quantitative Finance, Bocconi University &bull; March 2026</p>
</div>""", unsafe_allow_html=True)

# --- NAV ---
st.markdown(f"""<div class="cnav">
<a href="#executive-summary">Summary</a><a href="#market-analysis">Market</a><a href="#supply-chain">Supply Chain</a>
<a href="#competition">Competition</a><a href="#financial-model">Model</a><a href="#location">Location</a><a href="#verdict">Verdict</a>
</div>""", unsafe_allow_html=True)

# --- ASSUMPTION CARDS ---
st.markdown(f"""<div class="a-grid">
<div class="a-card"><div class="a-icon">📍</div><div class="a-label">Location</div><div class="a-value">US Southeast</div></div>
<div class="a-card"><div class="a-icon">🏭</div><div class="a-label">Product</div><div class="a-value">Float Glass</div></div>
<div class="a-card"><div class="a-icon">⚡</div><div class="a-label">Capacity</div><div class="a-value">250 TPD</div></div>
<div class="a-card"><div class="a-icon">💰</div><div class="a-label">Capex</div><div class="a-value">{fmt(capex)}</div></div>
<div class="a-card"><div class="a-icon">🏗️</div><div class="a-label">Type</div><div class="a-value">Greenfield</div></div>
</div>""", unsafe_allow_html=True)

# ============ 01 SUMMARY ============
sec("01","Executive Summary","The Opportunity at a Glance","executive-summary")

c1,c2,c3,c4 = st.columns(4)
with c1: metric("Global Market","$156–180B","4.2–8% CAGR → 2030","pink")
with c2: metric("US Market","$12.3B","5.1% CAGR → $15.7B","blue")
with c3: metric("Capex Required",fmt(capex),"250 TPD greenfield","orange")
pb_tone = "green" if payback<4.5 else ("orange" if payback<6 else "red")
with c4: metric("Payback",f"{payback:.1f}y","✓ Strong" if payback<4.5 else ("△ Moderate" if payback<6 else "✗ Long"),pb_tone)

prose(f"""The global flat glass market is estimated at <b>$156–180 billion in 2025</b> (Global Market Insights: $156.2B; MarketsandMarkets: $179.8B), growing at 4.2–8.0% CAGR through 2030. The <b>US market alone is worth $12.3 billion</b>, expanding at 5.1% CAGR to $15.7B by 2030, with building &amp; construction accounting for <b>78.6% of demand</b>. Solar glass is the fastest US segment at <b>7.35% CAGR</b>, driven by Inflation Reduction Act incentives.""")

prose(f"""The cautionary tale of <b>View Inc. and Halio</b> — two smart glass ventures that <b>burned $3B and went bankrupt</b> capturing less than 0.05% of the architectural glass market — empirically demonstrates why this sector punishes VC-style capital deployment.""")


# ============ 02 MARKET ============
st.markdown('<hr class="divider">', unsafe_allow_html=True)
sec("02","Market Analysis","A $156–180B Market with Structural Tailwinds","market-analysis")

col1,col2 = st.columns(2)
with col1:
    st.markdown("#### US Market by End Use (2024)")
    fig = go.Figure()
    fig.add_trace(go.Bar(x=[78.6,12,5,4.4], y=["Building &<br>Construction","Automotive","Solar Glass","Electronics<br>& Other"],
        orientation='h', marker=dict(color=[PK,PK,GR,OR], cornerradius=4),
        text=["78.6%","12%","5%","4.4%"], textposition='auto', textfont=dict(family="JetBrains Mono",size=13,color="white")))
    fig.update_layout(**PL, height=220, xaxis=dict(showgrid=False,showticklabels=False,range=[0,100]),
        yaxis=dict(showgrid=False,autorange="reversed"), bargap=0.35)
    st.plotly_chart(fig, use_container_width=True)

with col2:
    st.markdown("#### Key Demand Drivers")
    st.markdown(f"""<div class="card" style="padding:20px;">
<div style="margin-bottom:14px;"><b style="color:{GR};">⬤ EU EPBD Directive</b><br><span style="color:{TX2};font-size:13px;">16% worst buildings renovated by 2030. All new buildings zero-emission by 2030.</span></div>
<div style="margin-bottom:14px;"><b style="color:{BL};">⬤ US Inflation Reduction Act</b><br><span style="color:{TX2};font-size:13px;">Manufacturing tax credits. 47% YoY solar capacity increase (Q1 2023).</span></div>
<div style="margin-bottom:14px;"><b style="color:{OR};">⬤ Low-E Glass Adoption</b><br><span style="color:{TX2};font-size:13px;">40.4% of US revenue (2024). $43.8B global market at 6.0% CAGR.</span></div>
<div><b style="color:{GR};">⬤ US Tariff Regime</b><br><span style="color:{TX2};font-size:13px;">Reshaping supply chains toward domestic production.</span></div>
</div>""", unsafe_allow_html=True)

prose("""The <b>energy-efficient glass</b> sub-market is valued at <b>$47.6B in 2025</b> (5.7% CAGR → $78.2B by 2034). <b>Low-E glass</b> — a $43.8B market projected to reach $65.8B by 2031 — is the growth story, with <b>45% of new construction</b> now specifying it. Incumbents with proprietary magnetron sputtering lines capture disproportionate value; commodity float producers compete on price alone.""")


# ============ 03 SUPPLY CHAIN ============
st.markdown('<hr class="divider">', unsafe_allow_html=True)
sec("03","Supply Chain & Raw Material Risk","The Soda Ash Problem","supply-chain")

col1,col2 = st.columns(2)
with col1:
    st.markdown("#### Batch Cost Breakdown")
    fig = go.Figure()
    fig.add_trace(go.Bar(x=[60,20,15,5], y=["Soda Ash<br>(60% batch)","Silica Sand","Energy<br>(nat. gas)","Other"],
        orientation='h', marker=dict(color=[RD,OR,OR,BL], cornerradius=4),
        text=["60%","20%","15%","5%"], textposition='auto', textfont=dict(family="JetBrains Mono",size=13,color="white")))
    fig.update_layout(**PL, height=200, xaxis=dict(showgrid=False,showticklabels=False,range=[0,75]),
        yaxis=dict(showgrid=False,autorange="reversed"), bargap=0.35)
    st.plotly_chart(fig, use_container_width=True)

with col2:
    st.markdown("#### US Soda Ash Price Trajectory (2025)")
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=["Q1 '25","Q2 '25","Q3 '25"], y=[180,257,280],
        mode='lines+markers+text', text=["$180","$257","$280"], textposition='top center',
        textfont=dict(family="JetBrains Mono",size=13,color=TX),
        line=dict(color=RD, width=3), marker=dict(size=10, color=RD)))
    fig.update_layout(**PL, height=200, yaxis=dict(showgrid=True,gridcolor=BD,range=[140,320]),
        xaxis=dict(showgrid=False))
    st.plotly_chart(fig, use_container_width=True)
    st.markdown(f'<p style="text-align:center;color:{RD};font-weight:700;font-size:13px;">+55.6% increase Jan → Sep 2025</p>', unsafe_allow_html=True)

st.markdown(f"""<div class="callout callout-red">
<div class="c-title">⚠ Critical Risk: Soda Ash Volatility</div>
<div class="c-body">Soda ash constitutes <b>60% of batch costs</b>. In Q1 2025, spot prices spiked 18% month-on-month, triggering output cuts at two Midwestern plants. US prices rose from <b>$180/MT to $280/MT</b> in 9 months. Glass manufacturing consumes <b>51%+ of global soda ash</b>. Without long-term supply contracts, expect margin compression of 3–5pp during spikes.</div>
</div>""", unsafe_allow_html=True)

prose("""Float glass requires approximately <b>9 GJ/tonne</b> with furnaces at 1,500°C+ continuously. Producing 1 MT of soda ash alone needs <b>~10,000 kWh</b>. Result: <b>60–75% of variable costs are commodity-linked</b> — a structural disadvantage for undercapitalized entrants.""")


# ============ 04 COMPETITION ============
st.markdown('<hr class="divider">', unsafe_allow_html=True)
sec("04","Competitive Landscape","Five Incumbents, Accelerating Investment","competition")

# Competitive matrix
st.markdown("#### Competitive Positioning Matrix")
fig = go.Figure()
comps_data = [
    ("Saint-Gobain", 12, 11.7, 50, PK),
    ("AGC Inc.", 6, 10, 40, BL),
    ("Guardian (Koch)", 5, 9, 35, OR),
    ("Şişecam", 3, 8, 45, GR),
    ("New Entrant (proposed)", 0.066, 5, 20, RD),
]
for name, rev_b, margin, size, color in comps_data:
    fig.add_trace(go.Scatter(
        x=[rev_b], y=[margin], mode='markers+text', name=name,
        text=[name], textposition='top center',
        textfont=dict(family="Inter", size=11, color=TX),
        marker=dict(size=size, color=color, opacity=0.7, line=dict(width=2, color="white"))))
fig.update_layout(**PL, height=340, showlegend=False,
    xaxis=dict(title="Revenue ($B)", showgrid=True, gridcolor=BD, type="log", range=[-1.5, 1.3]),
    yaxis=dict(title="Operating Margin (%)", showgrid=True, gridcolor=BD, range=[3,14]))
st.plotly_chart(fig, use_container_width=True)
st.markdown(f'<p style="text-align:center;font-size:12px;color:{DIM};margin-top:-10px;">Bubble size represents estimated market power. New entrant shown in <span style="color:{RD};">red</span> for comparison.</p>', unsafe_allow_html=True)

# Comp cards
comps = [
    ("Saint-Gobain","France","~€12B glass","Record 11.7% op. margin (H1 2024). Volta low-CO₂ furnace with AGC. $970M India expansion (2022–25)."),
    ("AGC Inc.","Japan","~$6B glass","Volta hybrid furnace. Leading magnetron sputtering IP. Largest flat glass plant in Italy (Cuneo, 600 TPD)."),
    ("Şişecam","Turkey","~$3B","$470M in 2 new float lines. $114M in 3 coating lines across Turkey, Italy, Bulgaria. Coated capacity: 22M → 42M m²."),
    ("Guardian (Koch)","USA","~$5B","Dominant US market position. Koch Industries vertical integration. Deep construction supply chain distribution."),
]
c1,c2 = st.columns(2)
for i,(name,hq,rev_s,edge) in enumerate(comps):
    with (c1 if i%2==0 else c2):
        st.markdown(f"""<div class="comp-card">
<div style="display:flex;justify-content:space-between;align-items:center;">
<span style="font-size:18px;font-weight:800;color:{TX};">{name}</span>
<span style="font-family:'JetBrains Mono';font-size:10px;color:{DIM};background:{BG};padding:4px 10px;border-radius:100px;border:1px solid {BD};">{hq}</span>
</div>
<div style="font-family:'JetBrains Mono';font-size:13px;color:{PK};margin:8px 0;">{rev_s}</div>
<div style="font-size:13px;color:{TX2};line-height:1.65;">{edge}</div>
</div>""", unsafe_allow_html=True)

st.markdown(f"""<div class="callout callout-red">
<div class="c-title">📉 The Smart Glass Graveyard</div>
<div class="c-body">View Inc. and Halio Inc. — two VC-backed smart glass companies — went bankrupt with a combined <b>$3B loss</b>, capturing <b>less than 0.05%</b> of the architectural glass market. Scale, distribution, and coating IP are the moats — not technology alone.</div>
</div>""", unsafe_allow_html=True)

prose("""<b>NSG/Pilkington</b> shuttered Gladbeck (Jan 2025) while converting Rossford, Ohio to TCO solar glass (Mar 2025). Incumbents pivot to <b>high-margin specialty glass</b>, not commodity float. <b>Şişecam's $114M coating investment</b> — nearly doubling coated capacity — shows the value chain migrating from raw float to processed glass.""")


# ============ 05 MODEL ============
st.markdown('<hr class="divider">', unsafe_allow_html=True)
sec("05","Interactive Financial Model","Stress-Test the Unit Economics","financial-model")

prose("Use the <b>sidebar sliders</b> to adjust assumptions. All outputs update in real-time. Try setting soda ash to $180 (Q1 2025) vs $280 (Q3 2025) to see the margin impact.")

# Bloomberg-style metrics
st.markdown("#### Key Outputs — Steady State")
c1,c2,c3,c4 = st.columns(4)
ebitda_tone = "green" if ebitda_m>0.15 else ("orange" if ebitda_m>0.08 else "red")
ni_tone = "green" if ni>0 else "red"
roic_tone = "green" if roic>0.12 else ("orange" if roic>0.06 else "red")
with c1: metric("Revenue",fmt(rev),f"{cap:,.0f} MT/yr","blue")
with c2: metric("EBITDA",fmt(ebitda),f"Margin: {pct(ebitda_m)}",ebitda_tone)
with c3: metric("Net Income",fmt(ni),f"Margin: {pct(ni_m)}",ni_tone)
with c4: metric("ROIC",pct(roic),f"Payback: {payback:.1f}y",roic_tone)

# Waterfall P&L
st.markdown("#### P&L Waterfall — Revenue to Net Income")
wf_labels = ["Revenue","Raw Mat.","Energy","Labor","Gross Profit","SG&A","EBITDA","D&A","EBIT","Tax","Net Income"]
wf_values = [rev, -raw_total, -energy, -labor, 0, -sga, 0, -da, 0, -tax, 0]
wf_measures = ["absolute","relative","relative","relative","total","relative","total","relative","total","relative","total"]
wf_text = [fmt(rev), fmt(-raw_total), fmt(-energy), fmt(-labor), fmt(gp), fmt(-sga), fmt(ebitda), fmt(-da), fmt(ebit), fmt(-tax), fmt(ni)]
fig = go.Figure(go.Waterfall(
    x=wf_labels, y=wf_values, measure=wf_measures, text=wf_text, textposition="outside",
    textfont=dict(family="JetBrains Mono", size=11),
    connector=dict(line=dict(color=BD, width=1)),
    increasing=dict(marker=dict(color=GR, cornerradius=4)),
    decreasing=dict(marker=dict(color=RD, cornerradius=4)),
    totals=dict(marker=dict(color=BL, cornerradius=4))))
fig.update_layout(**PL, height=380, yaxis=dict(showgrid=True, gridcolor=BD, tickformat="$,.0f"),
    xaxis=dict(showgrid=False, tickangle=-35))
st.plotly_chart(fig, use_container_width=True)

# 5-Year Ramp
st.markdown("#### 5-Year Revenue & EBITDA Ramp")
ramp = [0.55,0.75,0.90,1.0,1.0]
fig = go.Figure()
fig.add_trace(go.Bar(x=[f"Year {i+1}" for i in range(5)], y=[rev*r for r in ramp],
    name="Revenue", marker=dict(color=PK, cornerradius=4),
    text=[fmt(rev*r) for r in ramp], textposition='outside', textfont=dict(family="JetBrains Mono",size=11,color=PK)))
fig.add_trace(go.Bar(x=[f"Year {i+1}" for i in range(5)], y=[ebitda*r for r in ramp],
    name="EBITDA", marker=dict(color=GR, cornerradius=4),
    text=[fmt(ebitda*r) for r in ramp], textposition='outside', textfont=dict(family="JetBrains Mono",size=11,color=GR)))
fig.update_layout(**PL, height=340, yaxis=dict(showgrid=True,gridcolor=BD,tickformat="$,.0f"),
    xaxis=dict(showgrid=False), barmode='group', bargap=0.3, bargroupgap=0.1,
    legend=dict(orientation="h",yanchor="bottom",y=1.02,xanchor="right",x=1,font=dict(size=12,color=TX)))
st.plotly_chart(fig, use_container_width=True)

# P&L Table
st.markdown("#### Detailed P&L — Steady State")
items = [
    ("Revenue",rev,True,None), ("Raw Materials",-raw_total,False,None), ("Energy Costs",-energy,False,None),
    ("Labor & Other",-labor,False,None), ("Gross Profit",gp,True,"g"), ("SG&A (8%)",-sga,False,None),
    ("EBITDA",ebitda,True,"g" if ebitda>0 else "r"), ("Depreciation",-da,False,None),
    ("EBIT",ebit,True,"g" if ebit>0 else "r"), ("Tax (25%)",-tax,False,None),
    ("Net Income",ni,True,"g" if ni>0 else "r")]
html='<div class="card">'
for label,val,bold,tone in items:
    lc="pl-bold" if bold else "pl-label"
    vc="pl-green" if tone=="g" else ("pl-red" if tone=="r" else "pl-val")
    html+=f'<div class="pl-row"><span class="{lc}">{label}</span><span class="{vc}">{fmt(val)}</span></div>'
html+='</div>'
st.markdown(html, unsafe_allow_html=True)


# ============ 06 LOCATION ============
st.markdown('<hr class="divider">', unsafe_allow_html=True)
sec("06","Location Strategy","US Southeast: The Optimal Entry Point","location")

c1,c2,c3 = st.columns(3)
locs = [
    ("US Southeast","Best","Energy: $0.07–0.09/kWh. Largest US construction corridor ($2.16T, +6.7% YoY). IRA credits. Right-to-work. Rail from Wyoming soda ash.","loc-best",GR),
    ("Turkey / E. Europe","Good","Şişecam investing $470M+. Labor cost advantage. EU EPBD demand. Currency risk, geopolitical instability, no IRA credits.","loc-good",OR),
    ("US NE / West Coast","Weak","Energy $0.12+/kWh. Regulatory burden. Higher labor costs. Guardian dominant. No cost advantage vs Southeast.","loc-weak",RD),
]
for col,(region,score,factors,cls,clr) in zip([c1,c2,c3],locs):
    with col:
        st.markdown(f"""<div class="comp-card {cls}">
<div style="font-weight:800;font-size:16px;color:{TX};">{region}</div>
<div style="font-family:'JetBrains Mono';font-size:12px;color:{clr};font-weight:700;margin:6px 0 12px;">{score}</div>
<div style="font-size:13px;color:{TX2};line-height:1.65;">{factors}</div>
</div>""", unsafe_allow_html=True)

prose("""<b>Georgia, Alabama, and South Carolina</b> offer the optimal balance: competitive energy, proximity to construction demand, IRA credits, right-to-work labor, and established rail from Wyoming soda ash mines. US construction spending reached <b>$2.16 trillion annualized</b> in mid-2024, up 6.7% YoY.""")


# ============ 07 VERDICT ============
st.markdown('<hr class="divider">', unsafe_allow_html=True)
sec("07","Investment Verdict","Should This Business Exist?","verdict")

st.markdown(f"""<div class="verdict-box">
<h2 style="font-size:26px;line-height:1.3;margin:0;position:relative;">
Yes — as a <span style="color:{OR};border-bottom:3px solid {OR};padding-bottom:2px;">PE / Infrastructure</span> investment.<br>
<span style="color:{RD};">Not as a venture bet.</span>
</h2>
</div>""", unsafe_allow_html=True)

c1,c2 = st.columns(2)
with c1:
    st.markdown("#### Bull Case")
    for b in ["Regulatory tailwinds (EPBD + IRA) create 5–10 year demand window",
              "25–35% gross margins with stable construction demand floor",
              "US tariffs provide natural moat; domestic supply gap exists",
              "~3-year payback at base case; strong cash generation at scale",
              "Low-E adoption (45% of new construction) drives premiumization"]:
        st.markdown(f'<div class="bull-item">{b}</div>', unsafe_allow_html=True)
with c2:
    st.markdown("#### Bear Case")
    for b in ["$75M+ capex is PE-scale (View/Halio burned $3B and failed)",
              "10–15% net margins: healthy for PE, insufficient for 10x VC returns",
              "Soda ash volatility (+55.6% in 2025) compresses margins unpredictably",
              "Incumbents investing $1B+ to expand coated glass capacity",
              "Without coating IP, new entrant competes on price alone — structurally weak"]:
        st.markdown(f'<div class="bear-item">{b}</div>', unsafe_allow_html=True)

prose("""The ideal buyer is a <b>mid-market PE fund with an industrial or building materials focus</b> — one with portfolio companies providing distribution into US construction. The wrong buyer is a venture fund expecting software-like returns from capital-intensive manufacturing.""")

prose("""<b>For Animal Capital specifically:</b> monitor this space for technology-enabled disruption — AI furnace optimization, novel coatings, ultra-thin glass for electronics — where smaller capital deployment could achieve venture-scale returns. The commodity manufacturing layer itself belongs in a PE portfolio.""")

# --- FOOTER ---
st.markdown(f"""<div class="footer">
Prepared by Vincenzo Salerno — MSc Quantitative Finance, Bocconi University — March 2026<br>
Sources: Grand View Research, MarketsandMarkets, Mordor Intelligence, IMARC, Global Market Insights, Glass International, ChemAnalyst, PitchBook
</div>""", unsafe_allow_html=True)

