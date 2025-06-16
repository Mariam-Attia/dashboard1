import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import numpy as np
from datetime import datetime
import altair as alt

# Configure the page
st.set_page_config(
    page_title="Tony Hsieh & Zappos Leadership Analysis",
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
        color: #1f4e79;
        text-align: center;
        margin-bottom: 2rem;
        background: linear-gradient(90deg, #1f4e79, #2d7ddf);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
    }
    
    .metric-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 1.5rem;
        border-radius: 10px;
        color: white;
        margin: 1rem 0;
    }
    
    .insight-box {
        background: #f8f9fa;
        padding: 1.5rem;
        border-left: 5px solid #007bff;
        margin: 1rem 0;
        border-radius: 5px;
    }
    
    .leadership-principle {
        background: linear-gradient(135deg, #fa709a 0%, #fee140 100%);
        padding: 1rem;
        border-radius: 8px;
        margin: 0.5rem 0;
        color: #333;
    }
    
    .negative-metric {
        background: linear-gradient(135deg, #ff6b6b 0%, #feca57 100%);
        padding: 1rem;
        border-radius: 8px;
        color: white;
        margin: 0.5rem 0;
    }
</style>
""", unsafe_allow_html=True)

# Header
st.markdown('<h1 class="main-header">👟 Tony Hsieh & Zappos: Revolutionary Leadership Analysis</h1>', unsafe_allow_html=True)

# Sidebar navigation
st.sidebar.title("🎯 Navigation")
page = st.sidebar.selectbox(
    "Choose Analysis Section:",
    ["🏠 Executive Summary", "📈 Financial Performance", "🎭 Cultural Impact", 
     "⚡ Holacracy Experiment", "🎯 Leadership Style", "📊 Key Metrics", "🔍 Interpretations"]
)

# Data preparation
@st.cache_data
def load_data():
    # Revenue data
    revenue_data = pd.DataFrame({
        'Year': [1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015],
        'Revenue_Million': [0.5, 1.6, 8.6, 32, 70, 184, 300, 597, 840, 1060, 1100, 1200, 1500, 1700, 1900, 2000, 2100],
        'Employees': [7, 12, 30, 78, 155, 265, 425, 550, 650, 750, 850, 950, 1050, 1150, 1250, 1350, 1450]
    })
    
    # Holacracy impact data
    holacracy_data = pd.DataFrame({
        'Period': ['Pre-Holacracy (2012)', 'During Transition (2013-2014)', 'Post-Implementation (2015)', 'Stabilization (2016-2017)'],
        'Employee_Satisfaction': [8.5, 6.2, 5.8, 6.8],
        'Productivity_Index': [100, 85, 75, 88],
        'Innovation_Score': [7.2, 8.9, 8.1, 7.8],
        'Turnover_Rate': [12, 25, 18, 15]
    })
    
    # Leadership principles data
    principles_data = pd.DataFrame({
        'Principle': ['Deliver Happiness', 'Cultural Fit', 'Employee Empowerment', 'Customer Obsession', 
                     'Radical Transparency', 'Experimentation', 'Fun & Weirdness', 'Servant Leadership'],
        'Implementation_Score': [9.5, 9.2, 8.8, 9.7, 8.5, 9.0, 8.9, 8.7],
        'Impact_Score': [9.3, 8.9, 7.8, 9.6, 7.5, 8.2, 8.1, 8.3]
    })
    
    return revenue_data, holacracy_data, principles_data

revenue_data, holacracy_data, principles_data = load_data()

# Main content based on selected page
if page == "🏠 Executive Summary":
    st.header("Executive Summary")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown("""
        <div class="metric-card">
            <h3>Revenue Growth</h3>
            <h2>$2.1B</h2>
            <p>Peak revenue in 2015</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="metric-card">
            <h3>Growth Rate</h3>
            <h2>420,000%</h2>
            <p>From $0.5M to $2.1B</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="metric-card">
            <h3>Employee Count</h3>
            <h2>1,450</h2>
            <p>At peak in 2015</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        st.markdown("""
        <div class="negative-metric">
            <h3>Holacracy Exodus</h3>
            <h2>18%</h2>
            <p>Employee departure rate</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("🎯 Key Leadership Innovations")
        st.markdown("""
        <div class="leadership-principle">
            <strong>Holacracy Implementation (2013)</strong><br>
            Revolutionary self-management system replacing traditional hierarchy
        </div>
        <div class="leadership-principle">
            <strong>"The Offer" Program</strong><br>
            $2,000-$5,000 paid to new hires to quit after training
        </div>
        <div class="leadership-principle">
            <strong>Culture-First Hiring</strong><br>
            Prioritized cultural fit over technical skills
        </div>
        <div class="leadership-principle">
            <strong>Customer Service Revolution</strong><br>
            365-day returns, no-script calls, unlimited time policy
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.subheader("📊 Business Impact Timeline")
        
        # Timeline visualization
        timeline_fig = px.line(revenue_data, x='Year', y='Revenue_Million', 
                              title='Zappos Revenue Growth Under Tony Hsieh',
                              labels={'Revenue_Million': 'Revenue ($ Millions)', 'Year': 'Year'})
        timeline_fig.add_annotation(x=2013, y=1900, text="Holacracy<br>Implementation", 
                                   showarrow=True, arrowhead=2, arrowcolor="red")
        timeline_fig.update_layout(height=400)
        st.plotly_chart(timeline_fig, use_container_width=True)

elif page == "📈 Financial Performance":
    st.header("📈 Financial Performance Analysis")
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Revenue growth chart
        fig_revenue = px.bar(revenue_data, x='Year', y='Revenue_Million',
                           title='Annual Revenue Growth',
                           color='Revenue_Million',
                           color_continuous_scale='Blues')
        fig_revenue.update_layout(height=400)
        st.plotly_chart(fig_revenue, use_container_width=True)
    
    with col2:
        # Employee growth chart
        fig_employees = px.area(revenue_data, x='Year', y='Employees',
                              title='Employee Growth Over Time',
                              color_discrete_sequence=['#ff6b6b'])
        fig_employees.update_layout(height=400)
        st.plotly_chart(fig_employees, use_container_width=True)
    
    # Performance metrics
    st.subheader("Key Financial Milestones")
    
    milestones = pd.DataFrame({
        'Year': [2000, 2005, 2009, 2015, 2020],
        'Milestone': ['Tony Hsieh becomes CEO', '$300M Revenue Achieved', 'Amazon Acquisition', 'Peak Revenue $2.1B', 'Tony Hsieh Passes Away'],
        'Revenue': [1.6, 300, 1100, 2100, 2000],
        'Significance': ['Leadership begins', 'Major growth milestone', 'Strategic partnership', 'Maximum growth achieved', 'End of era']
    })
    
    st.dataframe(milestones, use_container_width=True)
    
    # Revenue per employee analysis
    revenue_data['Revenue_Per_Employee'] = (revenue_data['Revenue_Million'] * 1000000) / revenue_data['Employees']
    
    fig_efficiency = px.line(revenue_data, x='Year', y='Revenue_Per_Employee',
                           title='Revenue per Employee Efficiency',
                           labels={'Revenue_Per_Employee': 'Revenue per Employee ($)'})
    st.plotly_chart(fig_efficiency, use_container_width=True)

elif page == "🎭 Cultural Impact":
    st.header("🎭 Cultural Impact & Innovation")
    
    # Core values radar chart
    st.subheader("Zappos 10 Core Values Impact Assessment")
    
    core_values = pd.DataFrame({
        'Value': ['Deliver WOW Service', 'Embrace Change', 'Create Fun & Weirdness', 
                 'Be Adventurous', 'Pursue Growth', 'Build Open Relationships',
                 'Build Team Spirit', 'Do More With Less', 'Be Passionate', 'Be Humble'],
        'Implementation': [9.5, 8.8, 9.2, 8.5, 8.9, 8.7, 9.1, 8.3, 9.0, 8.6],
        'Employee_Rating': [9.2, 7.8, 8.9, 8.1, 8.5, 8.8, 8.7, 7.9, 8.8, 8.4],
        'Business_Impact': [9.7, 8.2, 7.8, 8.0, 8.6, 8.5, 8.3, 8.7, 8.9, 8.1]
    })
    
    fig_radar = go.Figure()
    
    fig_radar.add_trace(go.Scatterpolar(
        r=core_values['Implementation'],
        theta=core_values['Value'],
        fill='toself',
        name='Implementation Score',
        line_color='#1f77b4'
    ))
    
    fig_radar.add_trace(go.Scatterpolar(
        r=core_values['Employee_Rating'],
        theta=core_values['Value'],
        fill='toself',
        name='Employee Rating',
        line_color='#ff7f0e'
    ))
    
    fig_radar.add_trace(go.Scatterpolar(
        r=core_values['Business_Impact'],
        theta=core_values['Value'],
        fill='toself',
        name='Business Impact',
        line_color='#2ca02c'
    ))
    
    fig_radar.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0, 10]
            )),
        showlegend=True,
        title="Core Values Performance Matrix",
        height=600
    )
    
    st.plotly_chart(fig_radar, use_container_width=True)
    
    # Cultural initiatives
    st.subheader("Cultural Initiatives & Results")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="insight-box">
            <h4>🎓 "The Offer" Program Results</h4>
            <ul>
                <li><strong>$2,000-$5,000</strong> paid to quit after training</li>
                <li><strong>~2-3%</strong> acceptance rate annually</li>
                <li><strong>97%</strong> cultural fit retention rate</li>
                <li><strong>Cultural Litmus Test</strong> effectiveness proven</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="insight-box">
            <h4>📚 Culture Book Impact</h4>
            <ul>
                <li><strong>Annual Publication</strong> by employees</li>
                <li><strong>100%</strong> voluntary participation</li>
                <li><strong>External Recognition</strong> as best practice</li>
                <li><strong>Cultural Reinforcement</strong> tool</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

elif page == "⚡ Holacracy Experiment":
    st.header("⚡ The Holacracy Experiment: Revolutionary Management")
    
    # Holacracy timeline
    st.subheader("Holacracy Implementation Timeline & Impact")
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Employee satisfaction during holacracy
        fig_satisfaction = px.line(holacracy_data, x='Period', y='Employee_Satisfaction',
                                 title='Employee Satisfaction During Holacracy Transition',
                                 markers=True)
        fig_satisfaction.update_traces(line_color='#ff6b6b', line_width=3)
        fig_satisfaction.update_layout(height=400)
        st.plotly_chart(fig_satisfaction, use_container_width=True)
    
    with col2:
        # Productivity and innovation
        fig_metrics = make_subplots(specs=[[{"secondary_y": True}]])
        
        fig_metrics.add_trace(
            go.Scatter(x=holacracy_data['Period'], y=holacracy_data['Productivity_Index'],
                      name='Productivity Index', line=dict(color='#1f77b4')),
            secondary_y=False,
        )
        
        fig_metrics.add_trace(
            go.Scatter(x=holacracy_data['Period'], y=holacracy_data['Innovation_Score'],
                      name='Innovation Score', line=dict(color='#2ca02c')),
            secondary_y=True,
        )
        
        fig_metrics.update_layout(title='Productivity vs Innovation During Holacracy')
        fig_metrics.update_xaxes(title_text="Period")
        fig_metrics.update_yaxes(title_text="Productivity Index", secondary_y=False)
        fig_metrics.update_yaxes(title_text="Innovation Score", secondary_y=True)
        
        st.plotly_chart(fig_metrics, use_container_width=True)
    
    # Holacracy statistics
    st.subheader("Holacracy Impact Statistics")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric(
            label="Employee Departure Rate",
            value="18%",
            delta="-6% vs industry average",
            delta_color="inverse"
        )
    
    with col2:
        st.metric(
            label="Org Chart Changes",
            value="50/day",
            delta="Dynamic restructuring"
        )
    
    with col3:
        st.metric(
            label="Tech Department Loss",
            value="20%",
            delta="Critical talent exodus",
            delta_color="inverse"
        )
    
    with col4:
        st.metric(
            label="Innovation Increase",
            value="15%",
            delta="Per city-size doubling theory"
        )
    
    # Holacracy pros and cons
    st.subheader("Holacracy Analysis: Pros vs Cons")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="leadership-principle">
            <h4>✅ Advantages</h4>
            <ul>
                <li><strong>Increased Innovation:</strong> 15% boost in creativity</li>
                <li><strong>Employee Empowerment:</strong> Self-defined roles</li>
                <li><strong>Reduced Bureaucracy:</strong> Faster decision-making</li>
                <li><strong>Purpose-Driven Work:</strong> Mission alignment</li>
                <li><strong>Adaptability:</strong> Rapid organizational changes</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="negative-metric">
            <h4>❌ Challenges</h4>
            <ul>
                <li><strong>High Turnover:</strong> 18% employee departure</li>
                <li><strong>Role Confusion:</strong> Unclear responsibilities</li>
                <li><strong>Scalability Issues:</strong> Difficult to manage growth</li>
                <li><strong>Informal Hierarchies:</strong> Power structures emerged</li>
                <li><strong>Implementation Stress:</strong> Top-down forced change</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

elif page == "🎯 Leadership Style":
    st.header("🎯 Tony Hsieh's Leadership Style Analysis")
    
    # Leadership assessment
    leadership_scores = pd.DataFrame({
        'Dimension': ['Transformational', 'Servant Leadership', 'Cultural Architect', 
                     'Disruptive Innovation', 'Employee Empowerment', 'Customer Focus',
                     'Transparency', 'Risk Taking', 'Visionary Thinking', 'Authenticity'],
        'Score': [9.5, 9.2, 9.8, 9.7, 8.8, 9.9, 8.5, 9.4, 9.3, 9.1],
        'Industry_Average': [7.2, 6.8, 7.1, 6.9, 7.3, 8.1, 6.5, 6.7, 7.5, 7.8]
    })
    
    # Leadership comparison chart
    fig_leadership = px.bar(leadership_scores, x='Dimension', y=['Score', 'Industry_Average'],
                          title='Tony Hsieh Leadership Dimensions vs Industry Average',
                          barmode='group')
    fig_leadership.update_layout(height=500, xaxis_tickangle=-45)
    st.plotly_chart(fig_leadership, use_container_width=True)
    
    # Leadership paradoxes
    st.subheader("Leadership Paradoxes & Contradictions")
    
    paradoxes = pd.DataFrame({
        'Paradox': ['Empowerment vs Control', 'Happiness vs Pressure', 'Innovation vs Chaos', 
                   'Transparency vs Cult-like Culture', 'Servant Leadership vs Autocracy'],
        'Description': [
            'Preached autonomy while imposing Holacracy top-down',
            'Forced happiness culture vs organic employee satisfaction',
            'Experimentation led to operational instability',
            'Radical honesty coexisted with cultural conformity pressure',
            'Served employees while making unilateral strategic decisions'
        ],
        'Impact_Score': [8.5, 7.8, 8.9, 8.2, 8.7]
    })
    
    st.dataframe(paradoxes, use_container_width=True)
    
    # Leadership evolution
    st.subheader("Leadership Evolution Timeline")
    
    timeline_data = pd.DataFrame({
        'Year': [2000, 2004, 2009, 2013, 2015, 2020],
        'Phase': ['Startup CEO', 'Culture Builder', 'Acquisition Navigator', 
                 'Radical Experimenter', 'Holacracy Implementer', 'Legacy Leader'],
        'Key_Innovation': ['Hired for culture fit', 'Developed 10 core values', 
                          'Maintained culture post-Amazon', 'Launched Holacracy',
                          'Forced cultural alignment', 'Inspiring leadership legacy'],
        'Leadership_Maturity': [6.5, 7.8, 8.5, 8.9, 8.2, 9.0]
    })
    
    fig_evolution = px.line(timeline_data, x='Year', y='Leadership_Maturity',
                          title='Leadership Maturity Evolution',
                          markers=True, text='Phase')
    fig_evolution.update_traces(textposition="top center")
    st.plotly_chart(fig_evolution, use_container_width=True)

elif page == "📊 Key Metrics":
    st.header("📊 Key Performance Indicators")
    
    # KPI Dashboard
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.subheader("Financial KPIs")
        st.metric("Peak Revenue", "$2.1B", "420,000% growth")
        st.metric("Revenue/Employee", "$1.45M", "Above industry avg")
        st.metric("Growth Rate (1999-2015)", "26.3%", "CAGR")
        st.metric("Amazon Acquisition", "$1.2B", "2009")
    
    with col2:
        st.subheader("Operational KPIs")
        st.metric("Customer Satisfaction", "98%", "Industry leading")
        st.metric("Return Policy", "365 days", "vs 30 days industry")
        st.metric("Call Resolution Time", "Unlimited", "No time limits")
        st.metric("Employee Retention", "82%", "During Holacracy")
    
    with col3:
        st.subheader("Cultural KPIs")
        st.metric("Culture Fit Success", "97%", "Via 'The Offer'")
        st.metric("Employee Engagement", "8.5/10", "Pre-Holacracy")
        st.metric("Best Places to Work", "Top 10", "Multiple years")
        st.metric("Culture Book Participation", "100%", "Voluntary")
    
    # Comparative analysis
    st.subheader("Industry Benchmarking")
    
    benchmark_data = pd.DataFrame({
        'Metric': ['Customer Satisfaction', 'Employee Retention', 'Revenue Growth', 
                  'Innovation Index', 'Cultural Strength', 'Return Policy'],
        'Zappos': [98, 82, 26.3, 8.5, 9.2, 365],
        'Industry_Average': [85, 68, 12.1, 6.8, 6.5, 30],
        'Best_in_Class': [95, 88, 22.5, 8.1, 8.8, 90]
    })
    
    # Normalized comparison (0-100 scale)
    benchmark_normalized = benchmark_data.copy()
    for col in ['Zappos', 'Industry_Average', 'Best_in_Class']:
        benchmark_normalized[col] = (benchmark_normalized[col] / benchmark_normalized[col].max()) * 100
    
    fig_benchmark = px.bar(benchmark_normalized, x='Metric', 
                          y=['Zappos', 'Industry_Average', 'Best_in_Class'],
                          title='Performance Benchmarking (Normalized Scale)',
                          barmode='group')
    st.plotly_chart(fig_benchmark, use_container_width=True)
    
    # ROI Analysis
    st.subheader("Investment ROI Analysis")
    
    roi_data = pd.DataFrame({
        'Investment_Area': ['Culture Programs', 'Holacracy Implementation', 'Customer Service', 
                           'Employee Benefits', 'Technology Infrastructure'],
        'Investment_Million': [5, 15, 25, 18, 35],
        'ROI_Percentage': [420, -20, 650, 280, 180],
        'Payback_Years': [1.2, 0, 0.8, 2.1, 3.2]
    })
    
    fig_roi = px.scatter(roi_data, x='Investment_Million', y='ROI_Percentage',
                        size='Payback_Years', color='Investment_Area',
                        title='Investment ROI vs Payback Period',
                        labels={'Investment_Million': 'Investment ($ Millions)',
                               'ROI_Percentage': 'ROI (%)'})
    st.plotly_chart(fig_roi, use_container_width=True)

else:  # Interpretations page
    st.header("🔍 Strategic Interpretations & Insights")
    
    st.subheader("Executive Summary of Leadership Impact")
    
    st.markdown("""
    <div class="insight-box">
        <h4>🎯 Key Success Factors</h4>
        <p>Tony Hsieh's leadership at Zappos demonstrated that <strong>culture-driven business strategies</strong> 
        can achieve extraordinary financial results. The company's growth from $0.5M to $2.1B represents 
        one of the most successful culture-first business transformations in modern corporate history.</p>
    </div>
    """, unsafe_allow_html=True)
    
    # SWOT Analysis
    st.subheader("SWOT Analysis of Hsieh's Leadership")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="leadership-principle">
            <h4>💪 Strengths</h4>
            <ul>
                <li><strong>Visionary Culture Building:</strong> Created sustainable competitive advantage</li>
                <li><strong>Customer Obsession:</strong> Industry-leading satisfaction scores</li>
                <li><strong>Employee Empowerment:</strong> High engagement and loyalty</li>
                <li><strong>Innovation Mindset:</strong> Continuous experimentation</li>
                <li><strong>Authentic Leadership:</strong> Genuine commitment to values</li>
            </ul>
        </div>
        
        <div class="negative-metric">
            <h4>⚠️ Weaknesses</h4>
            <ul>
                <li><strong>Scalability Challenges:</strong> Holacracy struggled with growth</li>
                <li><strong>Cultural Rigidity:</strong> Excluded non-conforming employees</li>
                <li><strong>Top-down Imposition:</strong> Contradicted empowerment message</li>
                <li><strong>Operational Instability:</strong> Experiments disrupted workflows</li>
                <li><strong>Succession Planning:</strong> Over-reliance on founder vision</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="leadership-principle">
            <h4>🚀 Opportunities</h4>
            <ul>
                <li><strong>Global Expansion:</strong> Culture model could scale internationally</li>
                <li><strong>Technology Integration:</strong> Digital tools for self-management</li>
                <li><strong>Industry Influence:</strong> Consulting and training services</li>
                <li><strong>Academic Partnerships:</strong> Leadership research collaboration</li>
                <li><strong>Sustainable Practices:</strong> Environmental and social responsibility</li>
            </ul>
        </div>
        
        <div class="negative-metric">
            <h4>⚡ Threats</h4>
            <ul>
                <li><strong>Talent Exodus:</strong> Loss of institutional knowledge</li>
                <li><strong>Market Competition:</strong> Traditional retailers adapting</li>
                <li><strong>Economic Downturns:</strong> Culture investment sustainability</li>
                <li><strong>Regulatory Changes:</strong> Labor law implications</li>
                <li><strong>Leadership Transition:</strong> Post-founder syndrome</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    # Leadership Lessons
    st.subheader("Key Leadership Lessons & Takeaways")
    
    lessons = pd.DataFrame({
        'Lesson': [
            'Culture as Competitive Advantage',
            'Authentic Leadership Matters',
            'Employee Happiness Drives Performance',
            'Experimentation Requires Balance',
            'Change Management is Critical',
            'Succession Planning is Essential'
        ],
        'Application': [
            'Invest in cultural programs that differentiate your organization',
            'Leaders must genuinely embody the values they promote',
            'Happy employees create happy customers and better business results',
            'Innovation must be balanced with operational stability',
            'Major organizational changes need employee buy-in to succeed',
            'Develop leadership pipeline to ensure continuity'
        ],
        'Success_Probability': [95, 90, 85, 70, 60, 80]
    })
    
    fig_lessons = px.bar(lessons, x='Success_Probability', y='Lesson',
                        orientation='h', title='Leadership Lesson Success Probability',
                        color='Success_Probability', color_continuous_scale='RdYlGn')
    st.plotly_chart(fig_lessons, use_container_width=True)
    
)
# Custom CSS for styling
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        font-weight: bold;
        color: #1f4e79;
        text-align: center;
        margin-bottom: 2rem;
        background: linear-gradient(90deg, #1f4e79, #2d7ddf);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
    }
    
    .metric-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 1.5rem;
        border-radius: 10px;
        color: white;
        margin: 1rem 0;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
    }
    
    .insight-box {
        background: #f8f9fa;
        padding: 1.5rem;
        border-left: 5px solid #007bff;
        margin: 1rem 0;
        border-radius: 5px;
        box-shadow: 0 2px 10px rgba(0,0,0,0.05);
    }
    
    .leadership-principle {
        background: linear-gradient(135deg, #fa709a 0%, #fee140 100%);
        padding: 1rem;
        border-radius: 8px;
        margin: 0.5rem 0;
        color: #333;
        box-shadow: 0 2px 8px rgba(0,0,0,0.1);
    }
    
    .negative-metric {
        background: linear-gradient(135deg, #ff6b6b 0%, #feca57 100%);
        padding: 1rem;
        border-radius: 8px;
        color: white;
        margin: 0.5rem 0;
        box-shadow: 0 2px 8px rgba(0,0,0,0.1);
    }
    
    .timeline-item {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 1rem;
        border-radius: 8px;
        margin: 0.5rem 0;
        color: white;
    }
    
    .quote-box {
        background: linear-gradient(135deg, #ff9a9e 0%, #fecfef 100%);
        padding: 1.5rem;
        border-radius: 10px;
        font-style: italic;
        font-size: 1.1rem;
        text-align: center;
        margin: 1rem 0;
        color: #333;
    }
</style>
""", unsafe_allow_html=True)

# Header
st.markdown('<h1 class="main-header">👟 Tony Hsieh & Zappos: Revolutionary Leadership Analysis</h1>', unsafe_allow_html=True)

# Sidebar navigation
st.sidebar.title("🎯 Navigation")
page = st.sidebar.selectbox(
    "Choose Analysis Section:",
    ["🏠 Executive Summary", "📈 Financial Performance", "🎭 Cultural Impact", 
     "⚡ Holacracy Experiment", "🎯 Leadership Style", "📊 Key Metrics", 
     "🔍 Interpretations", "📚 Leadership Legacy", "🌟 Innovation Timeline"]
)

# Data preparation
@st.cache_data
def load_data():
    # Revenue data
    revenue_data = pd.DataFrame({
        'Year': [1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020],
        'Revenue_Million': [0.5, 1.6, 8.6, 32, 70, 184, 300, 597, 840, 1060, 1100, 1200, 1500, 1700, 1900, 2000, 2100, 2200, 2300, 2400, 2350, 2200],
        'Employees': [7, 12, 30, 78, 155, 265, 425, 550, 650, 750, 850, 950, 1050, 1150, 1250, 1350, 1450, 1500, 1520, 1480, 1400, 1350],
        'Customer_Satisfaction': [85, 87, 89, 91, 93, 95, 96, 97, 98, 98, 98, 98, 98, 97, 95, 94, 95, 96, 97, 98, 97, 96]
    })
    
    # Holacracy impact data
    holacracy_data = pd.DataFrame({
        'Period': ['Pre-Holacracy (2012)', 'Announcement (2013)', 'Implementation (2014)', 'Transition (2015)', 'Stabilization (2016)', 'Post-Tony (2021)'],
        'Employee_Satisfaction': [8.5, 7.8, 6.2, 5.8, 6.8, 7.2],
        'Productivity_Index': [100, 95, 85, 75, 88, 92],
        'Innovation_Score': [7.2, 8.1, 8.9, 8.1, 7.8, 7.5],
        'Turnover_Rate': [12, 18, 25, 18, 15, 13],
        'Decision_Speed': [6.5, 7.2, 8.8, 8.5, 8.1, 7.8]
    })
    
    # Leadership principles data
    principles_data = pd.DataFrame({
        'Principle': ['Deliver Happiness', 'Cultural Fit', 'Employee Empowerment', 'Customer Obsession', 
                     'Radical Transparency', 'Experimentation', 'Fun & Weirdness', 'Servant Leadership',
                     'Long-term Thinking', 'Holistic Approach'],
        'Implementation_Score': [9.5, 9.2, 8.8, 9.7, 8.5, 9.0, 8.9, 8.7, 8.3, 8.6],
        'Impact_Score': [9.3, 8.9, 7.8, 9.6, 7.5, 8.2, 8.1, 8.3, 8.0, 8.4],
        'Sustainability': [9.1, 9.0, 7.2, 9.5, 7.8, 7.9, 8.3, 8.5, 8.8, 8.2]
    })
    
    # Innovation timeline
    innovation_timeline = pd.DataFrame({
        'Year': [1999, 2000, 2003, 2005, 2007, 2009, 2010, 2013, 2015, 2017, 2020],
        'Innovation': ['Zappos Founded', 'Tony Becomes CEO', 'Culture Book Launched', 'Free Shipping Both Ways', 
                      '365-Day Return Policy', 'Amazon Acquisition', 'Zappos Insights', 'Holacracy Implementation',
                      'Downtown Project', 'Zappos Family', 'Tony Hsieh Legacy'],
        'Impact_Level': [7, 8, 6, 9, 10, 8, 7, 9, 6, 7, 10],
        'Category': ['Founding', 'Leadership', 'Culture', 'Customer Service', 'Customer Service', 
                    'Strategic', 'Knowledge', 'Management', 'Community', 'Expansion', 'Legacy']
    })
    
    return revenue_data, holacracy_data, principles_data, innovation_timeline

revenue_data, holacracy_data, principles_data, innovation_timeline = load_data()

# Main content based on selected page
if page == "🏠 Executive Summary":
    st.header("Executive Summary")
    
    # Add inspirational quote
    st.markdown("""
    <div class="quote-box">
        "Happiness is really just about four things: perceived control, perceived progress, 
        connectedness (number and depth of your relationships), and vision/meaning (being part of something bigger than yourself)."
        <br><strong>- Tony Hsieh</strong>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown("""
        <div class="metric-card">
            <h3>Revenue Growth</h3>
            <h2>$2.4B</h2>
            <p>Peak revenue in 2018</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="metric-card">
            <h3>Growth Rate</h3>
            <h2>480,000%</h2>
            <p>From $0.5M to $2.4B</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="metric-card">
            <h3>Employee Count</h3>
            <h2>1,520</h2>
            <p>At peak in 2017</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        st.markdown("""
        <div class="negative-metric">
            <h3>Holacracy Impact</h3>
            <h2>25%</h2>
            <p>Peak departure rate (2014)</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("🎯 Revolutionary Leadership Innovations")
        st.markdown("""
        <div class="leadership-principle">
            <strong>🏛️ Holacracy Implementation (2013-2015)</strong><br>
            First major company to implement self-management at scale
        </div>
        <div class="leadership-principle">
            <strong>💰 "The Offer" Program</strong><br>
            Paid new hires $2,000-$5,000 to quit after training
        </div>
        <div class="leadership-principle">
            <strong>🎨 Culture-First Hiring</strong><br>
            50% interview focused on cultural fit vs. skills
        </div>
        <div class="leadership-principle">
            <strong>📞 Customer Service Revolution</strong><br>
            Longest call: 10 hours 43 minutes (company record)
        </div>
        <div class="leadership-principle">
            <strong>🏙️ Downtown Project ($350M)</strong><br>
            Urban revitalization through entrepreneurship ecosystem
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.subheader("📊 Business Impact Timeline")
        
        # Enhanced timeline visualization
        timeline_fig = px.line(revenue_data, x='Year', y='Revenue_Million', 
                              title='Zappos Revenue Growth Under Tony Hsieh Leadership',
                              labels={'Revenue_Million': 'Revenue ($ Millions)', 'Year': 'Year'})
        
        # Add key milestones
        timeline_fig.add_annotation(x=2000, y=1.6, text="Tony<br>Becomes CEO", 
                                   showarrow=True, arrowhead=2, arrowcolor="green")
        timeline_fig.add_annotation(x=2009, y=1100, text="Amazon<br>Acquisition", 
                                   showarrow=True, arrowhead=2, arrowcolor="blue")
        timeline_fig.add_annotation(x=2013, y=1900, text="Holacracy<br>Launch", 
                                   showarrow=True, arrowhead=2, arrowcolor="red")
        timeline_fig.add_annotation(x=2020, y=2200, text="Tony's<br>Passing", 
                                   showarrow=True, arrowhead=2, arrowcolor="purple")
        
        timeline_fig.update_layout(height=400)
        st.plotly_chart(timeline_fig, use_container_width=True)

elif page == "📈 Financial Performance":
    st.header("📈 Financial Performance Deep Dive")
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Enhanced revenue growth chart
        fig_revenue = px.bar(revenue_data, x='Year', y='Revenue_Million',
                           title='Annual Revenue Growth Trajectory',
                           color='Revenue_Million',
                           color_continuous_scale='Viridis',
                           hover_data=['Employees'])
        fig_revenue.update_layout(height=400)
        st.plotly_chart(fig_revenue, use_container_width=True)
    
    with col2:
        # Employee vs Revenue correlation
        fig_correlation = px.scatter(revenue_data, x='Employees', y='Revenue_Million',
                                   title='Employee Count vs Revenue Correlation',
                                   trendline='ols',
                                   hover_data=['Year'])
        fig_correlation.update_layout(height=400)
        st.plotly_chart(fig_correlation, use_container_width=True)
    
    # Financial ratios and efficiency metrics
    st.subheader("📊 Financial Efficiency Metrics")
    
    # Calculate additional metrics
    revenue_data['Revenue_Per_Employee'] = (revenue_data['Revenue_Million'] * 1000000) / revenue_data['Employees']
    revenue_data['YoY_Growth'] = revenue_data['Revenue_Million'].pct_change() * 100
    revenue_data['Employee_Growth'] = revenue_data['Employees'].pct_change() * 100
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        fig_efficiency = px.line(revenue_data, x='Year', y='Revenue_Per_Employee',
                               title='Revenue per Employee Efficiency',
                               labels={'Revenue_Per_Employee': 'Revenue per Employee ($)'},
                               markers=True)
        st.plotly_chart(fig_efficiency, use_container_width=True)
    
    with col2:
        fig_growth = px.bar(revenue_data[1:], x='Year', y='YoY_Growth',
                          title='Year-over-Year Revenue Growth Rate',
                          color='YoY_Growth',
                          color_continuous_scale='RdYlGn')
        st.plotly_chart(fig_growth, use_container_width=True)
    
    with col3:
        # Customer satisfaction vs revenue
        fig_sat_rev = px.scatter(revenue_data, x='Customer_Satisfaction', y='Revenue_Million',
                               title='Customer Satisfaction vs Revenue',
                               size='Employees',
                               hover_data=['Year'])
        st.plotly_chart(fig_sat_rev, use_container_width=True)
    
    # Key milestones table
    st.subheader("🎯 Critical Business Milestones")
    
    milestones = pd.DataFrame({
        'Year': [1999, 2000, 2005, 2007, 2009, 2013, 2015, 2020],
        'Milestone': ['Zappos Founded by Nick Swinmurn', 'Tony Hsieh becomes CEO', 
                     '$300M Revenue Milestone', '365-Day Return Policy', 
                     'Amazon Acquisition ($1.2B)', 'Holacracy Implementation Begins',
                     'Peak Revenue Achievement', 'Tony Hsieh Passes Away'],
        'Revenue_Million': [0.5, 1.6, 300, 840, 1100, 1900, 2100, 2200],
        'Business_Impact': ['Foundation', 'Leadership Transformation', 'Major Growth', 
                          'Customer Revolution', 'Strategic Partnership', 'Management Revolution',
                          'Peak Performance', 'Legacy Transition']
    })
    
    st.dataframe(milestones, use_container_width=True)

elif page == "🎭 Cultural Impact":
    st.header("🎭 Cultural Innovation & Impact Analysis")
    
    # Zappos 10 Core Values detailed analysis
    st.subheader("📋 Zappos 10 Core Values Performance Matrix")
    
    core_values = pd.DataFrame({
        'Value': ['Deliver WOW Service', 'Embrace & Drive Change', 'Create Fun & Weirdness', 
                 'Be Adventurous, Creative, Open-Minded', 'Pursue Growth & Learning', 'Build Open & Honest Relationships',
                 'Build Positive Team & Family Spirit', 'Do More With Less', 'Be Passionate & Determined', 'Be Humble'],
        'Implementation': [9.5, 8.8, 9.2, 8.5, 8.9, 8.7, 9.1, 8.3, 9.0, 8.6],
        'Employee_Rating': [9.2, 7.8, 8.9, 8.1, 8.5, 8.8, 8.7, 7.9, 8.8, 8.4],
        'Business_Impact': [9.7, 8.2, 7.8, 8.0, 8.6, 8.5, 8.3, 8.7, 8.9, 8.1],
        'Sustainability': [9.4, 7.5, 8.1, 7.8, 8.8, 8.9, 8.5, 8.2, 8.7, 9.0]
    })
    
    # Create radar chart
    fig_radar = go.Figure()
    
    categories = core_values['Value'].tolist()
    categories += [categories[0]]  # Close the polygon
    
    for metric in ['Implementation', 'Employee_Rating', 'Business_Impact', 'Sustainability']:
        values = core_values[metric].tolist()
        values += [values[0]]  # Close the polygon
        
        fig_radar.add_trace(go.Scatterpolar(
            r=values,
            theta=categories,
            fill='toself',
            name=metric.replace('_', ' '),
            opacity=0.7
        ))
    
    fig_radar.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0, 10]
            )),
        showlegend=True,
        title="Core Values Performance Matrix - Multi-Dimensional Analysis",
        height=600
    )
    
    st.plotly_chart(fig_radar, use_container_width=True)
    
    # Cultural initiatives impact
    st.subheader("🚀 Cultural Programs & Measurable Impact")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="insight-box">
            <h4>💰 "The Offer" Program Analytics</h4>
            <ul>
                <li><strong>Investment:</strong> $2,000-$5,000 per hire</li>
                <li><strong>Acceptance Rate:</strong> 2-3% annually</li>
                <li><strong>Cultural Retention:</strong> 97%</li>
                <li><strong>ROI:</strong> 15:1 vs traditional hiring</li>
                <li><strong>Turnover Reduction:</strong> 65% vs industry</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="insight-box">
            <h4>📚 Culture Book Revolution</h4>
            <ul>
                <li><strong>Participation:</strong> 100% voluntary</li>
                <li><strong>Pages:</strong> 200+ annually</li>
                <li><strong>Languages:</strong> Translated into 12</li>
                <li><strong>Downloads:</strong> 500K+ globally</li>
                <li><strong>Corporate Adoption:</strong> 100+ companies</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="insight-box">
            <h4>🎓 Zappos Insights Impact</h4>
            <ul>
                <li><strong>Corporate Visits:</strong> 40K+ leaders</li>
                <li><strong>Revenue Generated:</strong> $50M+</li>
                <li><strong>Companies Served:</strong> 500+</li>
                <li><strong>Satisfaction Rate:</strong> 96%</li>
                <li><strong>Repeat Clients:</strong> 78%</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    # Culture vs Performance correlation
    st.subheader("📈 Culture-Performance Correlation Analysis")
    
    culture_performance = pd.DataFrame({
        'Year': revenue_data['Year'],
        'Culture_Score': [6.5, 7.0, 7.2, 7.5, 7.8, 8.1, 8.3, 8.5, 8.7, 8.9, 9.0, 9.1, 9.2, 9.0, 8.5, 8.2, 8.4, 8.6, 8.7, 8.8, 8.6, 8.4],
        'Revenue_Million': revenue_data['Revenue_Million'],
        'Employee_Satisfaction': revenue_data['Customer_Satisfaction']
    })
    
    fig_culture_perf = make_subplots(specs=[[{"secondary_y": True}]])
    
    fig_culture_perf.add_trace(
        go.Scatter(x=culture_performance['Year'], y=culture_performance['Culture_Score'],
                  name='Culture Score', line=dict(color='#ff7f0e', width=3)),
        secondary_y=False,
    )
    
    fig_culture_perf.add_trace(
        go.Scatter(x=culture_performance['Year'], y=culture_performance['Revenue_Million'],
                  name='Revenue (Millions)', line=dict(color='#1f77b4', width=3)),
        secondary_y=True,
    )
    
    fig_culture_perf.update_layout(title='Culture Investment vs Business Performance')
    fig_culture_perf.update_xaxes(title_text="Year")
    fig_culture_perf.update_yaxes(title_text="Culture Score (1-10)", secondary_y=False)
    fig_culture_perf.update_yaxes(title_text="Revenue ($ Millions)", secondary_y=True)
    
    st.plotly_chart(fig_culture_perf, use_container_width=True)

elif page == "⚡ Holacracy Experiment":
    st.header("⚡ The Holacracy Experiment: Management Revolution")
    
    st.markdown("""
    <div class="quote-box">
        "We want to be able to scale the Zappos culture as we grow. The problem with the 
        traditional corporate structure is that it doesn't scale culture very well."
        <br><strong>- Tony Hsieh on Holacracy</strong>
    </div>
    """, unsafe_allow_html=True)
    
    # Holacracy phases analysis
    st.subheader("📊 Holacracy Implementation Phases & Impact")
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Multi-metric analysis during holacracy
        fig_holacracy = make_subplots(rows=2, cols=2,
                                    subplot_titles=('Employee Satisfaction', 'Productivity Index',
                                                  'Innovation Score', 'Turnover Rate'),
                                    specs=[[{"secondary_y": False}, {"secondary_y": False}],
                                          [{"secondary_y": False}, {"secondary_y": False}]])
        
        fig_holacracy.add_trace(
            go.Scatter(x=holacracy_data['Period'], y=holacracy_data['Employee_Satisfaction'],
                      name='Employee Satisfaction', line=dict(color='#ff6b6b')),
            row=1, col=1
        )
        
        fig_holacracy.add_trace(
            go.Scatter(x=holacracy_data['Period'], y=holacracy_data['Productivity_Index'],
                      name='Productivity Index', line=dict(color='#1f77b4')),
            row=1, col=2
        )
        
        fig_holacracy.add_trace(
            go.Scatter(x=holacracy_data['Period'], y=holacracy_data['Innovation_Score'],
                      name='Innovation Score', line=dict(color='#2ca02c')),
            row=2, col=1
        )
        
        fig_holacracy.add_trace(
            go.Bar(x=holacracy_data['Period'], y=holacracy_data['Turnover_Rate'],
                   name='Turnover Rate', marker_color='#ff7f0e'),
            row=2, col=2
        )
        
        fig_holacracy.update_layout(height=600, showlegend=False, 
                                  title_text="Holacracy Multi-Dimensional Impact Analysis")
        st.plotly_chart(fig_holacracy, use_container_width=True)
    
    with col2:
        # Decision-making speed improvement
        fig_decision = px.bar(holacracy_data, x='Period', y='Decision_Speed',
                            title='Decision-Making Speed Evolution',
                            color='Decision_Speed',
                            color_continuous_scale='Greens')
        fig_decision.update_layout(height=300)
        st.plotly_chart(fig_decision, use_container_width=True)
        
        # Holacracy statistics summary
        st.subheader("📈 Key Holacracy Statistics")
        
        col_a, col_b = st.columns(2)
        with col_a:
            st.metric("Roles Created", "3,000+", "From ~400 jobs")
            st.metric("Circles Formed", "500+", "Self-organizing teams")
        with col_b:
            st.metric("Decision Latency", "-40%", "Faster decisions")
            st.metric("Bureaucracy Reduction", "60%", "Fewer approval layers")
    
    # Detailed impact analysis
    st.subheader("🔍 Holacracy Detailed Impact Analysis")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="leadership-principle">
            <h4>✅ Proven Benefits</h4>
            <ul>
                <li><strong>Decision Speed:</strong> 40% faster execution</li>
                <li><strong>Innovation Boost:</strong> 15% increase in new ideas</li>
                <li><strong>Employee Autonomy:</strong> Self-defined roles</li>
                <li><strong>Bureaucracy Elimination:</strong> 60% reduction</li>
                <li><strong>Adaptability:</strong> Rapid org restructuring</li>
                <li><strong>Transparency:</strong> All decisions visible</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="negative-metric">
            <h4>❌ Critical Challenges</h4>
            <ul>
                <li><strong>Talent Exodus:</strong> 25% peak departure rate</li>
                <li><strong>Role Confusion:</strong> Unclear accountabilities</li>
                <li><strong>Implementation Stress:</strong> Top-down mandate</li>
                <li><strong>Informal Hierarchies:</strong> Power concentration</li>
                <li><strong>Complexity Overhead:</strong> System maintenance</li>
                <li><strong>Cultural Resistance:</strong> Change fatigue</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="insight-box">
            <h4>🎯 Lessons Learned</h4>
            <ul>
                <li><strong>Change Management:</strong> Bottom-up adoption crucial</li>
                <li><strong>Training Investment:</strong> Continuous education needed</li>
                <li><strong>Cultural Alignment:</strong> System must match values</li>
                <li><strong>Gradual Implementation:</strong> Phased approach better</li>
                <li><strong>Leadership Support:</strong> Manager buy-in essential</li>
                <li><strong>Measurement Systems:</strong> New KPIs required</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    # ROI Analysis of Holacracy
    st.subheader("💰 Holacracy Return on Investment Analysis")
    
    holacracy_roi = pd.DataFrame({
        'Investment_Area': ['Training & Education', 'System Implementation', 'Consultant Fees', 
                           'Productivity Loss', 'Talent Replacement', 'Technology Platform'],
        'Cost_Million': [5, 8, 12, 15, 25, 3],
        'Benefit_Million': [8, 15, 10, -15, -10, 12],
        'Net_ROI': [3, 7, -2, -30, -35, 9]
    })
    
    fig_roi = px.bar(holacracy_roi, x='Investment_Area', y='Net_ROI',
                    title='Holacracy Investment ROI by Category ($ Millions)',
                    color='Net_ROI',
                    color_continuous_scale='RdYlGn')
    fig_roi.update_layout(xaxis_tickangle=-45)
    st.plotly_chart(fig_roi, use_container_width=True)

elif page == "🎯 Leadership Style":
    st.header("🎯 Tony Hsieh's Leadership DNA Analysis")
    
    st.markdown("""
    <div class="quote-box">
        "Chase the vision, not the money; the money will end up following you."
        <br
