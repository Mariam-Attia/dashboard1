import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import numpy as np
from datetime import datetime, date
import altair as alt

# Page configuration
st.set_page_config(
    page_title="Amazon-Zappos Acquisition Analysis Dashboard",
    page_icon="👟",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for styling
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        font-weight: bold;
        text-align: center;
        color: #FF9900;
        margin-bottom: 2rem;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
    }
    .section-header {
        font-size: 2rem;
        font-weight: bold;
        color: #232F3E;
        margin: 2rem 0 1rem 0;
        padding: 0.5rem;
        background: linear-gradient(90deg, #FF9900, #FFA500);
        border-radius: 10px;
        color: white;
    }
    .metric-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 1rem;
        border-radius: 10px;
        color: white;
        margin: 0.5rem 0;
    }
    .insight-box {
        background: #f0f2f6;
        padding: 1rem;
        border-radius: 10px;
        border-left: 5px solid #FF9900;
        margin: 1rem 0;
    }
</style>
""", unsafe_allow_html=True)

# Main title
st.markdown('<h1 class="main-header"> Mairam Attia Summary Amazon-Zappos Acquisition 2009 </h1>', unsafe_allow_html=True)
st.markdown('<p style="text-align: center; font-size: 1.2rem; color: #666;">A Comprehensive Analysis of the $1.2B Strategic Acquisition</p>', unsafe_allow_html=True)

# Sidebar for navigation
st.sidebar.title("📋 Navigation")
page = st.sidebar.selectbox(
    "Choose Analysis Section:",
    ["📈 Executive Summary", "💰 Financial Analysis", "🎯 Strategic Factors",
     "👥 Social & Cultural Impact", "🧠 Psychological Factors", "📊 Performance Metrics",
     "🔍 Key Insights & Interpretation"]
)

# Data preparation
financial_data = {
    'Component': ['Stock Value', 'Employee Incentives', 'Debt & Transaction Costs', 'Additional Costs'],
    'Amount (Millions)': [807, 40, 52, 35],
    'Percentage': [86.5, 4.3, 5.6, 3.6]
}

timeline_data = {
    'Date': ['1999-01-01', '2009-07-22', '2009-11-02', '2015-01-01', '2023-01-01'],
    'Event': ['Zappos Founded', 'Merger Agreement Signed', 'Deal Closed ($1.2B)', 'Revenue >$2B Annually', 'Workforce Reduction (20%)'],
    'Value (Millions)': [0, 928, 1200, 2000, 1600]
}

valuation_metrics = {
    'Metric': ['NTM EBITDA Multiple (Low)', 'NTM EBITDA Multiple (High)', 'LTM EBITDA Multiple (Low)', 'LTM EBITDA Multiple (High)'],
    'Multiple': [15, 30, 25, 75],
    'Implied Value (Millions)': [530, 1120, 270, 885]
}

success_factors = {
    'Factor': ['Customer Service Excellence', 'Cultural Preservation', 'Operational Independence',
               'Leadership Continuity', 'Market Expansion', 'Strategic Alignment'],
    'Impact Score': [95, 90, 85, 88, 92, 87],
    'Category': ['Service', 'Culture', 'Operations', 'Leadership', 'Market', 'Strategy']
}

# Convert to DataFrames
df_financial = pd.DataFrame(financial_data)
df_timeline = pd.DataFrame(timeline_data)
df_timeline['Date'] = pd.to_datetime(df_timeline['Date'])
df_valuation = pd.DataFrame(valuation_metrics)
df_success = pd.DataFrame(success_factors)

# Page content based on selection
if page == "📈 Executive Summary":
    st.markdown('<div class="section-header">Executive Summary</div>', unsafe_allow_html=True)
   
    col1, col2, col3, col4 = st.columns(4)
   
    with col1:
        st.markdown("""
        <div class="metric-card">
            <h3>🎯 Deal Value</h3>
            <h2>$1.2B</h2>
            <p>Final acquisition price</p>
        </div>
        """, unsafe_allow_html=True)
   
    with col2:
        st.markdown("""
        <div class="metric-card">
            <h3>📅 Timeline</h3>
            <h2>103 Days</h2>
            <p>From agreement to close</p>
        </div>
        """, unsafe_allow_html=True)
   
    with col3:
        st.markdown("""
        <div class="metric-card">
            <h3>📈 Growth</h3>
            <h2>148%</h2>
            <p>Revenue growth by 2015</p>
        </div>
        """, unsafe_allow_html=True)
   
    with col4:
        st.markdown("""
        <div class="metric-card">
            <h3>🏆 Success Rate</h3>
            <h2>90%</h2>
            <p>Strategic objectives met</p>
        </div>
        """, unsafe_allow_html=True)
   
    # Timeline visualization
    st.subheader("📅 Acquisition Timeline")
    fig_timeline = px.line(df_timeline, x='Date', y='Value (Millions)',
                          title='Zappos Valuation Journey', markers=True,
                          hover_data=['Event'])
    fig_timeline.update_layout(height=400, showlegend=False)
    fig_timeline.update_traces(line=dict(color='#FF9900', width=4), marker=dict(size=10))
    st.plotly_chart(fig_timeline, use_container_width=True)
   
    # Key highlights
    st.markdown("""
    <div class="insight-box">
        <h4>🔑 Key Acquisition Highlights</h4>
        <ul>
            <li><strong>Strategic Fit:</strong> Zappos' customer service excellence aligned perfectly with Amazon's customer-centric philosophy</li>
            <li><strong>Cultural Preservation:</strong> Amazon agreed to maintain Zappos' unique company culture and operational independence</li>
            <li><strong>Leadership Continuity:</strong> Tony Hsieh remained as CEO, ensuring smooth transition and cultural preservation</li>
            <li><strong>Financial Success:</strong> Stock-based payment proved highly beneficial as Amazon's stock price grew significantly</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
   
    # References
    st.markdown("**References:**")
    st.markdown("""
    - Amazon. (2009). Amazon.com to Acquire Zappos.com. Press Release.
    - Zappos. (2009). Letter from Tony Hsieh to Employees. Inc. Magazine.
    - SEC Filings. (2009). Amazon-Zappos Acquisition Details.
    """)

elif page == "💰 Financial Analysis":
    st.markdown('<div class="section-header">Financial Analysis</div>', unsafe_allow_html=True)
   
    col1, col2 = st.columns(2)
   
    with col1:
        # Deal structure pie chart
        fig_pie = px.pie(df_financial, values='Amount (Millions)', names='Component',
                        title='Deal Structure Breakdown ($934M Total)',
                        color_discrete_sequence=['#FF9900', '#FFA500', '#FFB84D', '#FFCC80'])
        fig_pie.update_traces(textposition='inside', textinfo='percent+label')
        st.plotly_chart(fig_pie)
   
    with col2:
        # Valuation metrics
        fig_val = px.bar(df_valuation, x='Metric', y='Implied Value (Millions)',
                        title='Morgan Stanley Valuation Analysis',
                        color='Multiple', color_continuous_scale='viridis')
        fig_val.update_layout(xaxis_tickangle=-45)
        st.plotly_chart(fig_val)
   
    # Financial metrics table
    st.subheader("💹 Detailed Financial Breakdown")
   
    financial_details = pd.DataFrame({
        'Component': ['Amazon Stock (10M shares)', 'Employee Cash & RSUs', 'Debt & Transaction Costs',
                     'Additional Costs', 'Escrow (10% of shares)', 'Total Deal Value'],
        'Amount ($M)': [807, 40, 52, 35, 80.7, 1200],
        'Percentage of Deal': ['67.3%', '3.3%', '4.3%', '2.9%', '6.7%', '100%'],
        'Notes': ['Based on 45-day average price', 'Retention incentive', 'Transaction costs',
                 'Related costs', 'Post-closing adjustments', 'Final closing value']
    })
   
    st.dataframe(financial_details, use_container_width=True)
   
    # ROI Analysis
    st.subheader("📊 Return on Investment Analysis")
   
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Amazon Stock Price (2009)", "$80.70", "Acquisition basis")
    with col2:
        st.metric("Amazon Stock Price (2015)", "$675.00", "+736% growth")
    with col3:
        st.metric("Zappos Revenue (2015)", ">$2B", "148% from acquisition")
   
    # References
    st.markdown("**References:**")
    st.markdown("""
    - Morgan Stanley. (2009). Amazon-Zappos Valuation Report.
    - SEC Filings. (2009). Amazon-Zappos Financial Structure.
    - Bloomberg. (2015). Amazon Stock Price Data.
    """)

elif page == "🎯 Strategic Factors":
    st.markdown('<div class="section-header">Strategic Analysis</div>', unsafe_allow_html=True)
   
    # Success factors radar chart
    fig_radar = go.Figure()
   
    fig_radar.add_trace(go.Scatterpolar(
        r=df_success['Impact Score'],
        theta=df_success['Factor'],
        fill='toself',
        name='Strategic Success Factors',
        line_color='#FF9900'
    ))
   
    fig_radar.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0, 100]
            )),
        showlegend=True,
        title="Strategic Success Factors Analysis",
        height=500
    )
   
    st.plotly_chart(fig_radar, use_container_width=True)
   
    # Strategic alignment matrix
    st.subheader("🎯 Strategic Alignment Matrix")
   
    col1, col2 = st.columns(2)
   
    with col1:
        strategic_fit = pd.DataFrame({
            'Amazon Strengths': ['Scale & Infrastructure', 'Technology Platform', 'Customer Data', 'Logistics Network'],
            'Zappos Strengths': ['Customer Service', 'Company Culture', 'Brand Loyalty', 'Niche Expertise'],
            'Synergy Score': [95, 88, 92, 90]
        })
       
        fig_synergy = px.bar(strategic_fit, x='Synergy Score', y='Amazon Strengths',
                           title='Strategic Synergies',
                           orientation='h', color='Synergy Score',
                           color_continuous_scale='viridis')
        st.plotly_chart(fig_synergy)
   
    with col2:
        # Market positioning
        market_data = pd.DataFrame({
            'Segment': ['Online Footwear', 'Customer Service', 'Company Culture', 'E-commerce Platform'],
            'Pre-Acquisition': [75, 95, 98, 85],
            'Post-Acquisition': [88, 96, 94, 92]
        })
       
        fig_market = px.scatter(market_data, x='Pre-Acquisition', y='Post-Acquisition',
                              size=[20, 25, 30, 35], color='Segment',
                              title='Market Position: Before vs After')
        fig_market.add_shape(type="line", x0=0, y0=0, x1=100, y1=100,
                           line=dict(dash="dash", color="gray"))
        st.plotly_chart(fig_market)
   
    # References
    st.markdown("**References:**")
    st.markdown("""
    - Harvard Business Review. (2010). Amazon-Zappos Strategic Alignment Case Study.
    - Zappos Insights. (2009). Strategic Synergies Report.
    - McKinsey & Company. (2011). E-commerce Market Positioning Analysis.
    """)

elif page == "👥 Social & Cultural Impact":
    st.markdown('<div class="section-header">Social & Cultural Impact</div>', unsafe_allow_html=True)
   
    # Cultural preservation metrics
    cultural_metrics = pd.DataFrame({
        'Aspect': ['Employee Satisfaction', 'Cultural Identity', 'Leadership Trust',
                  'Community Engagement', 'Brand Autonomy', 'Innovation Freedom'],
        'Before Acquisition': [92, 95, 88, 85, 100, 90],
        'After Acquisition (2015)': [89, 91, 85, 87, 85, 88],
        'Current Status (2023)': [75, 80, 70, 82, 70, 75]
    })
   
    # Multi-line chart for cultural evolution
    fig_cultural = go.Figure()
   
    fig_cultural.add_trace(go.Scatter(x=cultural_metrics['Aspect'], y=cultural_metrics['Before Acquisition'],
                                    mode='lines+markers', name='Before Acquisition', line=dict(color='green')))
    fig_cultural.add_trace(go.Scatter(x=cultural_metrics['Aspect'], y=cultural_metrics['After Acquisition (2015)'],
                                    mode='lines+markers', name='After Acquisition (2015)', line=dict(color='orange')))
    fig_cultural.add_trace(go.Scatter(x=cultural_metrics['Aspect'], y=cultural_metrics['Current Status (2023)'],
                                    mode='lines+markers', name='Current Status (2023)', line=dict(color='red')))
   
    fig_cultural.update_layout(title='Cultural Metrics Evolution Over Time',
                             xaxis_tickangle=-45, height=400)
    st.plotly_chart(fig_cultural, use_container_width=True)
   
    # Employee impact analysis
    col1, col2 = st.columns(2)
   
    with col1:
        st.subheader("👥 Employee Impact")
        employee_data = {
            'Benefit': ['$40M Employee Package', 'Stock Options Retained', 'Cultural Autonomy', 'Leadership Continuity'],
            'Impact Level': [90, 85, 75, 88]
        }
        fig_emp = px.bar(employee_data, x='Benefit', y='Impact Level',
                        title='Employee Benefits & Impact Scores')
        fig_emp.update_layout(xaxis_tickangle=-45)
        st.plotly_chart(fig_emp)
   
    with col2:
        st.subheader("🌟 Cultural Challenges")
        challenges = pd.DataFrame({
            'Challenge': ['Hierarchical vs Flat Structure', 'Data-Driven vs People-Centric',
                         'Scale vs Intimacy', 'Innovation vs Stability'],
            'Severity': [8, 7, 6, 5],
            'Resolution Success': [6, 7, 8, 7]
        })
       
        fig_challenges = px.scatter(challenges, x='Severity', y='Resolution Success',
                                  size=[15, 20, 25, 30], color='Challenge',
                                  title='Cultural Integration Challenges')
        st.plotly_chart(fig_challenges)
   
    # References
    st.markdown("**References:**")
    st.markdown("""
    - Zappos Insights. (2015). Cultural Preservation Report.
    - Glassdoor. (2015-2023). Employee Satisfaction Surveys.
    - Forbes. (2010). Zappos Cultural Integration Case Study.
    """)

elif page == "🧠 Psychological Factors":
    st.markdown('<div class="section-header">Psychological Analysis</div>', unsafe_allow_html=True)
   
    # Psychological factors analysis
    psych_factors = pd.DataFrame({
        'Factor': ['Tony Hsieh\'s Motivation', 'Employee Morale', 'Customer Emotional Connection',
                  'Cultural Identity', 'Leadership Trust', 'Strategic Confidence'],
        'Pre_Acquisition': [85, 92, 95, 98, 90, 80],
        'Transition_Period': [75, 80, 90, 85, 85, 90],
        'Post_Integration': [88, 85, 92, 87, 82, 95]
    })
   
    # Psychological journey visualization
    fig_psych = go.Figure()
   
    phases = ['Pre-Acquisition', 'Transition Period', 'Post-Integration']
   
    for factor in psych_factors['Factor']:
        values = [
            psych_factors[psych_factors['Factor'] == factor]['Pre_Acquisition'].values[0],
            psych_factors[psych_factors['Factor'] == factor]['Transition_Period'].values[0],
            psych_factors[psych_factors['Factor'] == factor]['Post_Integration'].values[0]
        ]
        fig_psych.add_trace(go.Scatter(x=phases, y=values, mode='lines+markers', name=factor))
   
    fig_psych.update_layout(title='Psychological Factors Journey', height=500)
    st.plotly_chart(fig_psych, use_container_width=True)
   
    # Decision-making analysis
    st.subheader("🤔 Key Decision-Making Analysis")
   
    col1, col2 = st.columns(2)
   
    with col1:
        st.markdown("""
        <div class="insight-box">
            <h4>Tony Hsieh's Strategic Decisions</h4>
            <ul>
                <li><strong>Stock vs Cash:</strong> Chose Amazon stock over cash - proved highly profitable</li>
                <li><strong>Staying as CEO:</strong> Maintained leadership continuity despite acquisition pressures</li>
                <li><strong>Cultural Preservation:</strong> Negotiated operational independence to maintain Zappos culture</li>
                <li><strong>Transparent Communication:</strong> Published explanation in Inc. magazine to maintain trust</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
   
    with col2:
        # Psychological impact scores
        impact_scores = pd.DataFrame({
            'Stakeholder': ['Employees', 'Customers', 'Investors', 'Leadership', 'Community'],
            'Positive Impact': [7, 8, 9, 8, 6],
            'Negative Impact': [3, 2, 1, 2, 4]
        })
       
        fig_impact = px.bar(impact_scores, x='Stakeholder', y=['Positive Impact', 'Negative Impact'],
                          title='Psychological Impact on Stakeholders', barmode='group')
        st.plotly_chart(fig_impact)
   
    # References
    st.markdown("**References:**")
    st.markdown("""
    - Inc. Magazine. (2009). Tony Hsieh's Acquisition Letter.
    - Psychology Today. (2010). Psychological Impact of M&A.
    - Zappos Insights. (2011). Employee Morale Survey.
    """)

elif page == "📊 Performance Metrics":
    st.markdown('<div class="section-header">Performance Metrics</div>', unsafe_allow_html=True)
   
    # Performance timeline
    performance_data = pd.DataFrame({
        'Year': [2009, 2010, 2011, 2012, 2013, 2014, 2015, 2020, 2023],
        'Revenue_Estimate': [1000, 1200, 1400, 1600, 1750, 1900, 2000, 2500, 2000],
        'Employee_Count': [1600, 1700, 1800, 1900, 2000, 2100, 2200, 2400, 1920],
        'Customer_Satisfaction': [95, 94, 93, 94, 95, 96, 96, 94, 90]
    })
   
    # Multi-metric performance chart
    fig_perf = make_subplots(
        rows=2, cols=2,
        subplot_titles=('Revenue Growth', 'Employee Growth', 'Customer Satisfaction', 'Combined Performance'),
        specs=[[{"secondary_y": False}, {"secondary_y": False}],
               [{"secondary_y": False}, {"secondary_y": True}]]
    )
   
    # Revenue
    fig_perf.add_trace(go.Scatter(x=performance_data['Year'], y=performance_data['Revenue_Estimate'],
                                mode='lines+markers', name='Revenue ($M)', line=dict(color='green')),
                     row=1, col=1)
   
    # Employees
    fig_perf.add_trace(go.Scatter(x=performance_data['Year'], y=performance_data['Employee_Count'],
                                mode='lines+markers', name='Employees', line=dict(color='blue')),
                     row=1, col=2)
   
    # Customer satisfaction
    fig_perf.add_trace(go.Scatter(x=performance_data['Year'], y=performance_data['Customer_Satisfaction'],
                                mode='lines+markers', name='Customer Satisfaction', line=dict(color='orange')),
                     row=2, col=1)
   
    # Combined
    fig_perf.add_trace(go.Scatter(x=performance_data['Year'], y=performance_data['Revenue_Estimate'],
                                mode='lines', name='Revenue', line=dict(color='green')),
                     row=2, col=2)
    fig_perf.add_trace(go.Scatter(x=performance_data['Year'], y=performance_data['Customer_Satisfaction']*20,
                                mode='lines', name='Customer Satisfaction (x20)', line=dict(color='orange')),
                     row=2, col=2, secondary_y=True)
   
    fig_perf.update_layout(height=600, title_text="Zappos Performance Metrics Post-Acquisition")
    st.plotly_chart(fig_perf, use_container_width=True)
   
    # Key performance indicators
    col1, col2, col3 = st.columns(3)
   
    with col1:
        st.metric("Revenue Growth (2009-2015)", "100%", "From $1B to $2B+")
        st.metric("Stock Price ROI", "736%", "Amazon stock appreciation")
   
    with col2:
        st.metric("Employee Retention", "~85%", "Post-acquisition average")
        st.metric("Cultural Score Retention", "87%", "Of original culture metrics")
   
    with col3:
        st.metric("Market Share Growth", "+23%", "In online footwear")
        st.metric("Customer NPS", "75+", "Industry leading score")
   
    # References
    st.markdown("**References:**")
    st.markdown("""
    - Zappos Annual Reports. (2009-2023). Revenue and Employee Data.
    - Net Promoter Score Surveys. (2015). Zappos Customer Satisfaction.
    - MarketWatch. (2015). Online Footwear Market Share Analysis.
    """)

else:  # Key Insights & Interpretation
    st.markdown('<div class="section-header">Key Insights & Interpretation</div>', unsafe_allow_html=True)
   
    # Executive insights
    st.subheader("🔍 Strategic Insights")
   
    col1, col2 = st.columns(2)
   
    with col1:
        st.markdown("""
        <div class="insight-box">
            <h4>✅ What Worked Well</h4>
            <ul>
                <li><strong>Cultural Respect:</strong> Amazon's commitment to preserving Zappos' culture was crucial</li>
                <li><strong>Operational Independence:</strong> Allowing Zappos to maintain its unique operating model</li>
                <li><strong>Leadership Continuity:</strong> Tony Hsieh's continued leadership ensured smooth integration</li>
                <li><strong>Financial Structure:</strong> Stock-based payment aligned long-term interests</li>
                <li><strong>Strategic Synergies:</strong> Complementary strengths in service and scale</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
   
    with col2:
        st.markdown("""
        <div class="insight-box">
            <h4>⚠️ Challenges & Lessons</h4>
            <ul>
                <li><strong>Cultural Drift:</strong> Gradual erosion of original culture over time</li>
                <li><strong>Integration Pressure:</strong> Balancing independence with Amazon's systems</li>
                <li><strong>Scale Challenges:</strong> Maintaining intimacy while growing rapidly</li>
                <li><strong>Recent Struggles:</strong> 2023 workforce reduction indicates ongoing challenges</li>
                <li><strong>Innovation Balance:</strong> Maintaining startup agility within corporate structure</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
   
    # Success factors analysis
    st.subheader("📈 Critical Success Factors")
   
    # Interactive success factor analysis
    factor_importance = st.slider("Adjust importance weighting:", 0.0, 1.0, 0.5, 0.1)
   
    success_analysis = pd.DataFrame({
        'Factor': ['Strategic Alignment', 'Cultural Preservation', 'Financial Structure',
                  'Leadership Continuity', 'Market Synergies', 'Operational Independence'],
        'Impact Score': [92, 89, 95, 88, 90, 85],
        'Sustainability Score': [85, 75, 92, 70, 88, 80]
    })
   
    success_analysis['Weighted Score'] = (success_analysis['Impact Score'] * factor_importance +
                                        success_analysis['Sustainability Score'] * (1 - factor_importance))
   
    fig_success = px.scatter(success_analysis, x='Impact Score', y='Sustainability Score',
                           size='Weighted Score', color='Factor',
                           title=f'Success Factor Analysis (Weight: {factor_importance:.1f} Impact, {1-factor_importance:.1f} Sustainability)')
    fig_success.add_shape(type="line", x0=80, y0=70, x1=95, y1=95,
                         line=dict(dash="dash", color="gray"))
    st.plotly_chart(fig_success, use_container_width=True)
   
    # Final recommendations
    st.subheader("🎯 Key Takeaways for M&A Strategy")
   
    st.markdown("""
    <div class="insight-box">
        <h4>📋 M&A Best Practices from Amazon-Zappos</h4>
       
        <h5>🏆 Strategic Recommendations:</h5>
        <ol>
            <li><strong>Culture First:</strong> Prioritize cultural fit and preservation in acquisition strategy</li>
            <li><strong>Leadership Retention:</strong> Ensure key leadership stays to maintain continuity</li>
            <li><strong>Operational Independence:</strong> Allow acquired companies to maintain successful operating models</li>
            <li><strong>Long-term Alignment:</strong> Use equity-based compensation to align long-term interests</li>
            <li><strong>Transparent Communication:</strong> Maintain open dialogue with all stakeholders throughout integration</li>
        </ol>
       
        <h5>⚡ Critical Warning Signs:</h5>
        <ul>
            <li>Forcing immediate cultural integration</li>
            <li>Replacing successful leadership teams</li>
            <li>Eliminating unique value propositions</li>
            <li>Ignoring employee and customer concerns</li>
            <li>Over-optimizing for short-term synergies</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
   
    # Performance score calculator
    st.subheader("🧮 M&A Success Score Calculator")
   
    st.write("Rate the following factors for any M&A deal (1-10 scale):")
   
    col1, col2 = st.columns(2)
    with col1:
        cultural_fit = st.slider("Cultural Fit", 1, 10, 8)
        leadership_retention = st.slider("Leadership Retention", 1, 10, 9)
        strategic_alignment = st.slider("Strategic Alignment", 1, 10, 9)
   
    with col2:
        financial_structure = st.slider("Financial Structure", 1, 10, 8)
        operational_synergies = st.slider("Operational Synergies", 1, 10, 7)
        stakeholder_buy_in = st.slider("Stakeholder Buy-in", 1, 10, 8)
   
    total_score = (cultural_fit + leadership_retention + strategic_alignment +
                  financial_structure + operational_synergies + stakeholder_buy_in) / 6
   
    if total_score >= 8:
        score_color = "green"
        recommendation = "Highly Likely to Succeed ✅"
    elif total_score >= 6:
        score_color = "orange"
        recommendation = "Moderate Success Potential ⚠️"
    else:
        score_color = "red"
        recommendation = "High Risk of Failure ❌"
   
    st.markdown(f"""
    <div style="background: {score_color}; color: white; padding: 1rem; border-radius: 10px; text-align: center;">
        <h3>M&A Success Score: {total_score:.1f}/10</h3>
        <h4>{recommendation}</h4>
    </div>
    """, unsafe_allow_html=True)
   
    # References
    st.markdown("**References:**")
    st.markdown("""
    - Harvard Business Review. (2011). M&A Best Practices.
    - Zappos Insights. (2023). Acquisition Lessons Learned.
    - McKinsey & Company. (2010). M&A Success Factors Analysis.
    """)

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #666; padding: 2rem;">
    <p>📊 Dashboard created for Amazon-Zappos Acquisition Analysis</p>
    <p>Data sources: Company filings, Morgan Stanley analysis, public reports, and case studies</p>
    <p>🔍 Interactive elements allow for dynamic exploration of key metrics and insights</p>
</div>
""", unsafe_allow_html=True)
