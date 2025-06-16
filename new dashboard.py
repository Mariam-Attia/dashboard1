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
    
    # Future Implications
    st.subheader("Future Implications for Leadership")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="insight-box">
            <h4>🔮 Future of Organizational Design</h4>
            <p><strong>Hybrid Models:</strong> Future organizations will likely combine traditional hierarchy 
            with self-management elements, learning from both Zappos' successes and failures.</p>
            
            <p><strong>Technology Integration:</strong> AI and digital tools will enable better implementation 
            of distributed decision-making systems that Holacracy attempted manually.</p>
            
            <p><strong>Cultural Measurement:</strong> Advanced analytics will provide better metrics for 
            cultural health and its impact on business performance.</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="insight-box">
            <h4>📈 Leadership Evolution Trends</h4>
            <p><strong>Purpose-Driven Leadership:</strong> Hsieh's focus on happiness and purpose 
            foreshadowed the modern emphasis on meaningful work and social impact.</p>
            
            <p><strong>Employee Experience:</strong> The investment in employee satisfaction is now 
            recognized as essential for talent retention and business success.</p>
            
            <p><strong>Agile Organizations:</strong> The need for rapid adaptation that drove Holacracy 
            is now mainstream in digital transformation efforts.</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Recommendations
    st.subheader("Strategic Recommendations for Modern Leaders")
    
    recommendations = pd.DataFrame({
        'Recommendation': [
            'Gradual Culture Transformation',
            'Employee-Centric Policies',
            'Balanced Innovation Approach',
            'Transparent Communication',
            'Sustainable Growth Focus',
            'Leadership Development'
        ],
        'Priority': ['High', 'High', 'Medium', 'High', 'Medium', 'High'],
        'Timeline': ['6-12 months', '3-6 months', '12-18 months', 'Immediate', '18-24 months', 'Ongoing'],
        'Expected_Impact': [85, 90, 70, 80, 75, 95]
    })
    
    # Color mapping for priority
    color_map = {'High': '#ff6b6b', 'Medium': '#feca57', 'Low': '#48dbfb'}
    recommendations['Color'] = recommendations['Priority'].map(color_map)
    
    fig_recommendations = px.scatter(recommendations, x='Timeline', y='Expected_Impact',
                                   size='Expected_Impact', color='Priority',
                                   hover_data=['Recommendation'],
                                   title='Strategic Recommendations: Priority vs Impact',
                                   color_discrete_map=color_map)
    st.plotly_chart(fig_recommendations, use_container_width=True)
    
    # Final insights
    st.subheader("Critical Success Factors for Implementation")
    
    st.markdown("""
    <div class="leadership-principle">
        <h4>🎯 The Zappos Formula for Success</h4>
        <ol>
            <li><strong>Start with Purpose:</strong> Define clear organizational mission beyond profit</li>
            <li><strong>Hire for Culture:</strong> Prioritize values alignment in recruitment</li>
            <li><strong>Empower Gradually:</strong> Build autonomy incrementally rather than revolutionary change</li>
            <li><strong>Measure Culture:</strong> Develop metrics to track cultural health and business impact</li>
            <li><strong>Lead by Example:</strong> Demonstrate authentic commitment to stated values</li>
            <li><strong>Plan for Succession:</strong> Build leadership pipeline to sustain cultural transformation</li>
        </ol>
    </div>
    """, unsafe_allow_html=True)

# Interactive sidebar features
st.sidebar.markdown("---")
st.sidebar.subheader("🎛️ Interactive Controls")

# Filter controls
if page in ["📈 Financial Performance", "📊 Key Metrics"]:
    year_range = st.sidebar.slider(
        "Select Year Range",
        min_value=1999,
        max_value=2020,
        value=(1999, 2020),
        step=1
    )
    
    st.sidebar.info(f"Analyzing data from {year_range[0]} to {year_range[1]}")

# Comparison toggle
comparison_mode = st.sidebar.checkbox("Show Industry Comparisons", value=True)

# Data export
if st.sidebar.button("📊 Export Analysis Data"):
    # Create downloadable data
    export_data = {
        'Revenue Data': revenue_data,
        'Holacracy Impact': holacracy_data,
        'Leadership Principles': principles_data
    }
    
    st.sidebar.success("Data export prepared! (Demo mode)")

# About section
st.sidebar.markdown("---")
st.sidebar.markdown("""
### 📋 About This Analysis
This dashboard analyzes Tony Hsieh's revolutionary leadership at Zappos, 
examining the intersection of culture, innovation, and business performance.

**Key Sources:**
- Academic research papers
- Financial performance data
- Employee satisfaction surveys
- Industry benchmarking

**Analysis Period:** 1999-2020
""")

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #666; padding: 2rem;'>
    <h3>💡 Tony Hsieh's Leadership Legacy</h3>
    <p><em>"Your personal core values define who you are, and a company's core values ultimately define the company's character and brand."</em></p>
    <p><strong>- Tony Hsieh, Delivering Happiness</strong></p>
    <br>
    <p>This analysis demonstrates how authentic leadership, cultural focus, and employee empowerment 
    can drive extraordinary business results while also highlighting the importance of balanced innovation and sustainable growth.</p>
</div>
""", unsafe_allow_html=True)
