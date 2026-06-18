import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as px_go

# --- STREAMLIT CONFIGURATION ---
st.set_page_config(
    page_title="JK Tyre Forensic Analysis Dashboard",
    page_icon="🛞",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for polished financial branding
st.markdown("""
<style>
    .reportview-container { background: #f5f7f9; }
    .metric-box { padding: 15px; background: white; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.05); }
    .flag-high { color: #dc3545; font-weight: bold; }
    .flag-low { color: #28a745; font-weight: bold; }
</style>
""", unsafe_allow_html=True)

# --- DATA STRUCTURES (PARSING THE REPORT) ---

# Peer Data (Point 111)
peer_data = pd.DataFrame({
    'Company': ['MRF', 'Balkrishna', 'Apollo', 'JK Tyre'],
    'CMP (₹)': [125515, 2013, 396, 378],
    'PE': [21.5, 31.3, 12.1, 12.3],
    'Market Cap (₹ Cr)': [53232, 38916, 25169, 10904],
    'OPM %': [15.7, 21.2, 14.5, 12.4],
    'ROE %': [12.5, 11.6, 13.2, 16.2],
    'DE': [0.15, 0.38, 0.22, 0.81]
})

# Shareholding Trajectory (Points 124-128)
shareholding_data = pd.DataFrame({
    'Metric': ['FII Holding %', 'DII Holding %', 'Public Float %', 'Individual Shareholders'],
    'Past (Jun 23)': [8.69, 1.22, 33.83, 358475],
    'Current (Mar 26)': [18.59, 7.45, 22.23, 284107],
    'Trend': ['💥 Aggressive Buying', '📈 Strong Accumulation', '📉 Retail Capitulation', '🚪 74k+ Retail Exits']
})

# Multi-Year Financial P&L (Points 31-35, 56)
historical_p_l = pd.DataFrame({
    'Year / Metric': ['Sales (₹ Cr)', 'Operating Profit (₹ Cr)', 'CFO (₹ Cr)', 'PAT (₹ Cr)', 'OPM %'],
    'FY19': [10368, 912, 820, 180, 8.8],
    'FY25': [14693, 1836, 1290, 610, 12.5],
    'FY26 (TTM)': [16327, 2031, 1444, 776, 12.4]
})

# --- SIDEBAR & FILTER ARCHITECTURE ---
st.sidebar.title("🛞 JK Tyre Forensic Control Tower")
st.sidebar.markdown("**Institutional Core Intelligence Engine (2026)**")
st.sidebar.divider()

# Master Analysis Mode Filter
app_mode = st.sidebar.radio(
    "Choose Analysis Layer:",
    ["1. Executive Summary & Thesis", 
     "2. Business Model & Operations", 
     "3. Financial & Forensic Deep-Dive", 
     "4. Valuation & Peer Matrix", 
     "5. Technicals & Shareholding Flux"]
)

st.sidebar.divider()
st.sidebar.subheader("Key Risk Warning System")
st.sidebar.markdown("🚨 **Debt Anchor Value:** ₹4,882 Cr")
st.sidebar.markdown("🛢️ **Sensitivity Parameter:** High Crude & Rubber Vulnerability")
st.sidebar.markdown("⭐ **Overall Score:** `79/100` (Accumulate)")

# --- PAGE LAYOUTS ---

# LAYER 1: EXECUTIVE SUMMARY
if app_mode == "1. Executive Summary & Thesis":
    st.title("JK Tyre & Industries Ltd — Structural Deep-Dive & Forensic Verdict")
    st.caption("Comprehensive Multi-Timeframe Institutional Intelligence Engine")
    
    # Hero Metric Row
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Hedge Fund Verdict", "ACCUMULATE", "Score: 79/100")
    with col2:
        st.metric("Current Market Price (CMP)", "₹378", "PE: 12.3x (Discounted)")
    with col3:
        st.metric("Return on Equity (ROE)", "16.21%", "Highest in Peer Group")
    with col4:
        st.metric("Free Cash Flow (FY26)", "₹838 Cr", "CFO: ₹1,444 Cr")
        
    st.divider()
    
    # Thesis Layout
    left_col, right_col = st.columns(2)
    with left_col:
        st.subheader("💡 The One-Sentence Structural Investment Thesis")
        st.info("**Point 165:** JK Tyre is a deeply undervalued commercial tyre titan generating massive cash flow and experiencing historic institutional accumulation, offering highly asymmetric upside if management successfully deleverages the balance sheet.")
        
        st.subheader("📊 Scenario-Based Valuation Matrix (Point 87)")
        scenario_df = pd.DataFrame({
            'Scenario': ['Bull Case (30%)', 'Base Case (50%)', 'Bear Case (20%)'],
            'Target Price': ['₹550+', '₹420 – ₹450', '₹310'],
            'Triggers / Conditions': ['Rubber prices collapse, aggressive debt paydown.', 'Steady volume growth, stable margins.', 'Crude oil spikes, OEM auto sales slump.']
        })
        st.table(scenario_df)
        
    with right_col:
        st.subheader("🎯 Tactical Institutional Action Zones (Point 164)")
        st.markdown("- 📥 **Accumulate Zone:** ₹311 – ₹380 *(Current Price is in this golden pocket)*")
        st.markdown("- 🪵 **Hold Pocket:** ₹381 – ₹499")
        st.markdown("- ✂️ **Trim Zone:** ₹500 – ₹550")
        st.markdown("- 🚨 **Liquidate Momentum:** ₹600+")
        
        st.subheader("🛡️ Executive Action Plan (Point 145)")
        st.success("**Moderate Execution Track:** Stagger entries within the current base, setting hard structural risk limits below the macro floor of ₹310.")

# LAYER 2: BUSINESS MODEL & OPERATIONS
elif app_mode == "2. Business Model & Operations":
    st.title("⚙️ Core Business Reality & Operational Logistics Friction")
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.subheader("The Reality & Moat Framework (Points 1–13)")
        st.markdown(f"**Description:** Flagship enterprise of the JK Group, ranking in top 25 globally. **Pioneer of radial technology in India.**")
        st.markdown(f"**Target Customer:** Highly concentrated B2B OEM base (Tata Motors, Ashok Leyland, Maruti) paired with high-margin Replacement Market.")
        st.warning("**The Input Cost Trap (Point 7):** Gross margins are at the complete mercy of global natural rubber and Brent crude oil prices with a 1-2 quarter lag in passing costs to OEMs.")
        st.markdown("**Moat KPI Indicators:** TBR Market Share, Gross Margin spreads vs crude volatility, and Replacement vs OEM revenue ratios.")
        
    with col2:
        st.subheader("Operational Infrastructure & Cycles (Points 14–30)")
        st.markdown("🔄 **Cash Conversion Cycle (Point 54):** `90 Days` (Debtor Days: 72 + Inventory Days: 96 - Payable Days: 78). Perfectly flat and optimized for a decade.")
        st.markdown("🏭 **Capacity Framework:** Carrying ₹7,192 Cr in Gross Fixed Assets. Capacity utilization below 75% destroys margins due to massive structural fixed costs.")
        st.markdown("🛡️ **Sovereign Shield (Point 29-30):** Anti-dumping duties on cheap Chinese radial tyres act as a powerful barrier protecting domestic price parity.")

# LAYER 3: FINANCIAL & FORENSIC DEEP-DIVE
elif app_mode == "3. Financial & Forensic Deep-Dive":
    st.title("🔍 Cash Flow Forensics & Quality of Earnings Engine")
    
    # Transform P&L table format for easier processing
    p_l_transposed = historical_p_l.set_index('Year / Metric').T.reset_index()
    
    # 1. Quality of Earnings Visualizer (Point 57 Chart Concept)
    st.subheader("The Earnings Verification Vector: Net Profit vs Operating Cash Flow")
    st.markdown("*Forensic Check: Standard operating profit vs actual hard cash moving into the bank.*")
    
    fig_cfo = px_go.Figure()
    fig_cfo.add_trace(px_go.Bar(x=p_l_transposed['index'], y=p_l_transposed['Operating Profit (₹ Cr)'], name='Operating Profit (₹ Cr)', marker_color='#002B49'))
    fig_cfo.add_trace(px_go.Bar(x=p_l_transposed['index'], y=p_l_transposed['CFO (₹ Cr)'], name='Cash From Operations (CFO)', marker_color='#008080'))
    fig_cfo.add_trace(px_go.Scatter(x=p_l_transposed['index'], y=p_l_transposed['PAT (₹ Cr)'], name='Net Profit (PAT)', line=dict(color='#FF4B4B', width=3)))
    
    fig_cfo.update_layout(barmode='group', title_text="Financial Disconnect Auditing", template="plotly_white")
    st.plotly_chart(fig_cfo, use_container_width=True)
    
    # Forensic metrics column split
    f1, f2 = st.columns(2)
    with f1:
        st.subheader("Accounting Integrity Checks (Points 64–70)")
        st.markdown("✅ **Altman Z-Score:** `3.12` — Comfortably inside the Safe Zone.")
        st.markdown("✅ **Beneish M-Score:** Passing indicators. CFO conversion metrics effectively rule out manipulation.")
        st.markdown("👥 **Related Party Transactions:** Standard cross-holdings across the wider industrial conglomerate, no cash-drain flags.")
        
    with f2:
        st.subheader("The Structural Liability Profile (Points 46–50)")
        st.error("🚨 **The Debt Elephant:** ₹4,882 Cr total debt payload against an equity capital base of ₹58 Cr.")
        st.markdown("⚖️ **Debt/Equity Ratio:** `0.81` — Manageable due to strong cash flow, but restricts AAA rating ceiling.")
        st.success("💰 **Earnings Quality (Point 42):** High. Heavy depreciation loaded appropriately (₹472 Cr) leaving clean accounting entries.")

# LAYER 4: VALUATION & PEER MATRIX
elif app_mode == "4. Valuation & Peer Matrix":
    st.title("📊 Relative Valuation Engine & Industry Peer Matrix")
    
    # Visualizing Risk-Return Matrix via Scatter (Point 111-112)
    st.subheader("The Levered Value Quadrant (Scatter Analysis)")
    
    fig_scatter = px.scatter(
        peer_data, 
        x="DE", 
        y="ROE %", 
        size="Market Cap (₹ Cr)", 
        color="Company",
        hover_name="Company",
        text="Company",
        title="Oligopoly Evaluation Matrix (X: Debt/Equity, Y: ROE %, Bubble Size: Market Cap)",
        labels={'DE': 'Debt to Equity Ratio (Leverage Risk)', 'ROE %': 'Return on Equity (Capital Efficiency)'}
    )
    fig_scatter.update_traces(textposition='top center')
    fig_scatter.update_layout(template="plotly_white")
    st.plotly_chart(fig_scatter, use_container_width=True)
    
    # Display precise matrix data frame
    st.subheader("Apple-to-Apple Peer Metric Comparison (Point 111)")
    st.dataframe(peer_data.style.background_gradient(subset=['ROE %', 'OPM %'], cmap='Blues').background_gradient(subset=['DE', 'PE'], cmap='Reds'))
    
    st.subheader("Deep-Value Metric Parameters (Points 71–80)")
    v1, v2, v3 = st.columns(3)
    with v1:
        st.metric("EV / EBITDA", "7.77x", "Deep Value Multiplier")
    with v2:
        st.metric("PEG Ratio Value", "0.51", "Undervalued (<1.0 Benchmark)")
    with v3:
        st.metric("Market Cap / Sales", "0.66x", "Priced heavily for debt risk")

# LAYER 5: TECHNICALS & SHAREHOLDING FLUX
elif app_mode == "5. Technicals & Shareholding Flux":
    st.title("📈 Market Microstructure, Wyckoff Phases & Smart Money Accumulation")
    
    # Data Frame Output for shareholding
    st.subheader("The Great Retail to Institutional Equity Migration (Points 124–130)")
    st.markdown("Over **74,000 retail accounts** capitulated, moving floating stock supply into institutional vaults.")
    st.table(shareholding_data)
    
    st.divider()
    
    # Wyckoff & Technical Execution parameters
    t1, t2 = st.columns(2)
    with t1:
        st.subheader("🔄 Multi-Timeframe Wyckoff Analysis (Point 131)")
        st.info("**Current Phase:** Stage 1 Accumulation Base. The asset is building structure following a markdown from its peak of ₹612. Smart money is holding prices stable within the Volume Point of Control.")
        
        st.subheader("📊 Volume Profile Point of Control (Point 135)")
        st.markdown("- **Maximum Institutional Absorption Node:** `₹350 – ₹380` zone.")
        st.markdown("- **Dynamic Psychological Tracker:** Price is tightly winding between the 50-DMA and 200-DMA pivot lines.")
        
    with t2:
        st.subheader("🛡️ Key Execution Support and Resistance Ledges (Point 132)")
        st.markdown("🟥 **Macro Supply Ceiling / Trapped Retail Block:** `₹612` (Historical Peak)")
        st.markdown("🟨 **Immediate Algorithmic Momentum Breakout Line:** `₹420` (Weekly Close needed)")
        st.markdown("🟩 **Absolute Structural Demand Floor / Validation Stop:** `₹311` (Invalidation Line)")
        
        st.subheader("🎯 Automated GTT Limit Alert Configurations (Point 146)")
        st.code("""
# Algorithmic Trading Orders Setup
LIMIT_ACCUMULATION_TRIGGER = 355.00
BREAKOUT_CONFIRMATION_ALERT = 422.00
CRITICAL_STOP_LOSS = 310.00
        """, language="python")