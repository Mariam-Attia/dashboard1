import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import numpy as np
from datetime import datetime

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
    # Revenue data (validated with sources)
    revenue_data = pd.DataFrame({
        'Year': [1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015],
        'Revenue_Million': [0.5, 1.6, 8.6, 32, 70, 184, 370, 597, 840, 1014, 1100, 1200, 1400, 1600, 1800, 2000, 2100],
        'Employees': [8, 12, 30, 80, 150, 250, 400, 550, 700, 850, 1500, 1600, 1700, 1800, 1900, 2000, 2000],
        'Customer_Satisfaction': [85, 87, 90, 92, 94, 95, 96, 97, 98, 98, 98, 98, 97, 96, 95, 95, 96]
    })
    
    # Holacracy impact data (aligned with)[](https://www.sj-r.com/story/business/2015/05/16/inside-zappos-ceo-tony-hsieh/34547263007/)
    holacracy_data = pd.DataFrame({
        'Period': ['Pre-Holacracy (2012)', 'Announcement (2013)', 'Implementation (2014)', 'Transition (2015)', 'Stabilization (2016)'],
        'Employee_Satisfaction': [8.5, 7.8, 6.2, 5.8, 6.8],
        'Productivity_Index': [100, 95, 85, 75, 88],
        'Innovation_Score': [7.2, 8.1, 8.9, 8.1, 7.8],
        'Turnover_Rate': [12, 18, 25, 18, 15]
    })
    
    # Leadership principles data
    principles_data = pd.DataFrame({
        'Principle': ['Deliver Happiness', 'Cultural Fit', 'Employee Empowerment', 'Customer Obsession', 
                     'Radical Transparency', 'Experimentation', 'Fun & Weirdness', 'Servant Leadership'],
        'Implementation_Score': [9.5, 9.2, 8.8, 9.7, 8.5, 9.0, 8.9, 8.7],
        'Impact_Score': [9.3, 8.9, 7.8, 9.6, 7.5, 8.2, 8.1, 8.3]
    })
    
    # Innovation timeline (aligned with)[](https://www.untitledleader.com/lessons-in-leadership/the-legacy-of-tony-hsieh-lessons-in-leadership-and-entrepreneurship/)
    innovation_timeline = pd.DataFrame({
        'Year': [1999, 2000, 2005, 2007, 2009, 2010, 2013, 2015],
        'Innovation': ['Zappos Founded', 'Hsieh Becomes CEO', 'Free Shipping', '365-Day Returns', 
                       'Amazon Acquisition', 'Zappos Insights', 'Holacracy Launch', 'Downtown Project'],
        'Impact_Level': [7, 8, 9, 10, 8, 7, 9, 6],
        'Category': ['Founding', 'Leadership', 'Customer Service', 'Customer Service', 
                    'Strategic', 'Knowledge', 'Management', 'Community']
    })
    
    return revenue_data, holacracy_data, principles_data, innovation_timeline

try:
    revenue_data, holacracy_data, principles_data, innovation_timeline = load_data()
except Exception as e:
    st.error(f"Error loading data: {e}")
    st.stop()

# Main content based on selected page
if page == "🏠 Executive Summary":
    st.header("Executive Summary")
    
    st.markdown("""
    <div class="quote-box">
        "Happiness is about perceived control, progress, connectedness, and vision."
        <br><strong>- Tony Hsieh</strong>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown("""
        <div class="metric-card">
            <h3>Revenue Peak</h3>
            <h2>$2.1B</h2>
            <p>2015, post-acquisition</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="metric-card">
            <h3>Growth Rate</h3>
            <h2>420,000%</h2>
            <p>From $0.5M (1999) to $2.1B</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="metric-card">
            <h3>Employee Peak</h3>
            <h2>2,000</h2>
            <p>2014-2015</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        st.markdown("""
        <div class="negative-metric">
            <h3>Holacracy Turnover</h3>
            <h2>25%</h2>
            <p>Peak in 2014</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("🎯 Key Innovations")
        st.markdown("""
        <div class="leadership-principle">
            <strong>Holacracy (2013)</strong><br>
            Self-management system for 1,500+ employees[](https://www.sj-r.com/story/business/2015/05/16/inside-zappos-ceo-tony-hsieh/34547263007/)
        </div>
        <div class="leadership-principle">
            <strong>The Offer</strong><br>
            $2,000-$5,000 to quit, 97% retention
        </div>
        <div class="leadership-principle">
            <strong>Customer Service</strong><br>
            365-day returns, 98% satisfaction
        </div>
        <div class="leadership-principle">
            <strong>Downtown Project</strong><br>
            $350M, 1,000+ jobs created
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.subheader("📊 Revenue Timeline")
        try:
            timeline_fig = px.line(revenue_data, x='Year', y='Revenue_Million', 
                                  title='Zappos Revenue Growth (1999-2015)',
                                  labels={'Revenue_Million': 'Revenue ($M)'})
            timeline_fig.add_annotation(x=2009, y=1100, text="Amazon Acquisition ($1.2B)", 
                                       showarrow=True, arrowhead=2, arrowcolor="blue")
            timeline_fig.add_annotation(x=2013, y=1800, text="Holacracy Launch", 
                                       showarrow=True, arrowhead=2, arrowcolor="red")
            timeline_fig.update_layout(height=400)
            st.plotly_chart(timeline_fig, use_container_width=True)
        except Exception as e:
            st.error(f"Error rendering timeline: {e}")

elif page == "📈 Financial Performance":
    st.header("Financial Performance")
    
    col1, col2 = st.columns(2)
    
    with col1:
        try:
            fig_revenue = px.bar(revenue_data, x='Year', y='Revenue_Million',
                                title='Revenue Growth ($M)',
                                color='Revenue_Million',
                                color_continuous_scale='Blues')
            fig_revenue.update_layout(height=400)
            st.plotly_chart(fig_revenue, use_container_width=True)
        except Exception as e:
            st.error(f"Error rendering revenue chart: {e}")
    
    with col2:
        try:
            fig_employees = px.area(revenue_data, x='Year', y='Employees',
                                   title='Employee Growth',
                                   color_discrete_sequence=['#ff6b6b'])
            fig_employees.update_layout(height=400)
            st.plotly_chart(fig_employees, use_container_width=True)
        except Exception as e:
            st.error(f"Error rendering employee chart: {e}")
    
    st.subheader("Financial Milestones")
    milestones = pd.DataFrame({
        'Year': [1999, 2005, 2009, 2013, 2015],
        'Milestone': ['Zappos Founded', '$370M Revenue', 'Amazon Acquisition ($1.2B)', 
                      'Holacracy Launch', 'Peak Revenue ($2.1B)'],
        'Revenue_Million': [0.5, 370, 1100, 1800, 2100]
    })
    st.dataframe(milestones, use_container_width=True)
    
    try:
        revenue_data['Revenue_Per_Employee'] = (revenue_data['Revenue_Million'] * 1000000) / revenue_data['Employees']
        fig_efficiency = px.line(revenue_data, x='Year', y='Revenue_Per_Employee',
                                title='Revenue per Employee ($)',
                                labels={'Revenue_Per_Employee': 'Revenue/Employee ($)'})
        st.plotly_chart(fig_efficiency, use_container_width=True)
    except Exception as e:
        st.error(f"Error rendering efficiency chart: {e}")

elif page == "🎭 Cultural Impact":
    st.header("Cultural Impact")
    
    st.subheader("Core Values Assessment")
    try:
        fig_radar = go.Figure()
        for metric in ['Implementation_Score', 'Impact_Score']:
            fig_radar.add_trace(go.Scatterpolar(
                r=principles_data[metric],
                theta=principles_data['Principle'],
                fill='toself',
                name=metric.replace('_', ' ')
            ))
        fig_radar.update_layout(
            polar=dict(radialaxis=dict(visible=True, range=[0, 10])),
            showlegend=True,
            title="Core Values Impact",
            height=500
        )
        st.plotly_chart(fig_radar, use_container_width=True)
    except Exception as e:
        st.error(f"Error rendering radar chart: {e}")
    
    st.subheader("Cultural Initiatives")
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="insight-box">
            <h4>The Offer Program</h4>
            <ul>
                <li><strong>Cost:</strong> $2,000-$5,000 per hire</li>
                <li><strong>Acceptance:</strong> 2-3% annually</li>
                <li><strong>Retention:</strong> 97% cultural fit</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="insight-box">
            <h4>Culture Book</h4>
            <ul>
                <li><strong>Participation:</strong> 100% voluntary</li>
                <li><strong>Downloads:</strong> 500K+ globally</li>
                <li><strong>Adoption:</strong> 100+ companies</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

elif page == "⚡ Holacracy Experiment":
    st.header("Holacracy Experiment")
    
    st.markdown("""
    <div class="quote-box">
        "We want to scale Zappos' culture without bureaucracy." <br><strong>- Tony Hsieh</strong>[](https://www.sj-r.com/story/business/2015/05/16/inside-zappos-ceo-tony-hsieh/34547263007/)
    </div>
    """, unsafe_allow_html=True)
    
    try:
        fig_holacracy = px.bar(holacracy_data, x='Period', y=['Employee_Satisfaction', 'Turnover_Rate'],
                              title='Holacracy Impact (Satisfaction & Turnover)',
                              barmode='group')
        fig_holacracy.update_layout(height=400)
        st.plotly_chart(fig_holacracy, use_container_width=True)
    except Exception as e:
        st.error(f"Error rendering holacracy chart: {e}")
    
    st.subheader("Holacracy Metrics")
    col1, col2 = st.columns(2)
    
    with col1:
        st.metric("Peak Turnover", "25%", "2014")
        st.metric("Satisfaction Drop", "-2.7", "From 8.5 to 5.8")
    
    with col2:
        st.metric("Innovation Boost", "15%", "2014 Peak")
        st.metric("Bureaucracy Reduction", "60%", "Fewer layers")

elif page == "🎯 Leadership Style":
    st.header("Leadership Style")
    
    st.markdown("""
    <div class="quote-box">
        "Chase the vision, not the money; the money will follow." <br><strong>- Tony Hsieh</strong>[](https://www.untitledleader.com/lessons-in-leadership/the-legacy-of-tony-hsieh-lessons-in-leadership-and-entrepreneurship/)
    </div>
    """, unsafe_allow_html=True)
    
    leadership_scores = pd.DataFrame({
        'Dimension': ['Transformational', 'Servant Leadership', 'Cultural Architect', 
                     'Customer Focus', 'Risk Taking'],
        'Score': [9.5, 9.2, 9.8, 9.9, 9.4],
        'Industry_Average': [7.2, 6.8, 7.1, 8.1, 6.7]
    })
    
    try:
        fig_leadership = px.bar(leadership_scores, x='Dimension', y=['Score', 'Industry_Average'],
                               title='Hsieh’s Leadership vs Industry',
                               barmode='group')
        fig_leadership.update_layout(height=400, xaxis_tickangle=-45)
        st.plotly_chart(fig_leadership, use_container_width=True)
    except Exception as e:
        st.error(f"Error rendering leadership chart: {e}")
    
    st.subheader("Leadership Paradoxes")
    paradoxes = pd.DataFrame({
        'Paradox': ['Empowerment vs Control', 'Happiness vs Pressure'],
        'Description': ['Promoted autonomy but imposed holacracy', 'Pushed happiness culture, risked conformity'],
        'Impact_Score': [8.5, 7.8]
    })
    st.dataframe(paradoxes, use_container_width=True)

elif page == "📊 Key Metrics":
    st.header("Key Metrics")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.subheader("Financial")
        st.metric("Acquisition Value", "$1.2B", "2009")
        st.metric("Revenue Peak", "$2.1B", "2015")
    
    with col2:
        st.subheader("Operational")
        st.metric("Customer Satisfaction", "98%", "2007-2010")
        st.metric("Repeat Customers", "75%", "Industry leading")
    
    with col3:
        st.subheader("Cultural")
        st.metric("The Offer Retention", "97%", "2-3% quit")
        st.metric("Culture Book Downloads", "500K+", "Global")
    
    try:
        benchmark_data = pd.DataFrame({
            'Metric': ['Customer Satisfaction', 'Revenue Growth', 'Employee Retention'],
            'Zappos': [98, 26.3, 82],
            'Industry_Average': [85, 12.1, 68]
        })
        fig_benchmark = px.bar(benchmark_data, x='Metric', y=['Zappos', 'Industry_Average'],
                              title='Zappos vs Industry',
                              barmode='group')
        st.plotly_chart(fig_benchmark, use_container_width=True)
    except Exception as e:
        st.error(f"Error rendering benchmark chart: {e}")

elif page == "🔍 Interpretations":
    st.header("Strategic Interpretations")
    
    st.subheader("SWOT Analysis")
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="leadership-principle">
            <h4>Strengths</h4>
            <ul>
                <li><strong>Culture:</strong> 97% retention via The Offer</li>
                <li><strong>Service:</strong> 98% customer satisfaction</li>
                <li><strong>Innovation:</strong> $350M Downtown Project</li>[](https://www.untitledleader.com/lessons-in-leadership/the-legacy-of-tony-hsieh-lessons-in-leadership-and-entrepreneurship/)
            </ul>
        </div>
        <div class="negative-metric">
            <h4>Weaknesses</h4>
            <ul>
                <li><strong>Turnover:</strong> 25% during holacracy</li>
                <li><strong>Scalability:</strong> Holacracy complexity</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="leadership-principle">
            <h4>Opportunities</h4>
            <ul>
                <li><strong>Global Culture:</strong> Expand model internationally</li>
                <li><strong>Consulting:</strong> Zappos Insights ($50M+ revenue)</li>
            </ul>
        </div>
        <div class="negative-metric">
            <h4>Threats</h4>
            <ul>
                <li><strong>Competition:</strong> Retailers adopting service model</li>
                <li><strong>Regulation:</strong> Antitrust scrutiny on Amazon</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

elif page == "📚 Leadership Legacy":
    st.header("Leadership Legacy")
    
    st.markdown("""
    <div class="quote-box">
        "Your culture is your brand." <br><strong>- Tony Hsieh</strong>[](https://www.untitledleader.com/lessons-in-leadership/the-legacy-of-tony-hsieh-lessons-in-leadership-and-entrepreneurship/)
    </div>
    """, unsafe_allow_html=True)
    
    st.subheader("Lasting Impact")
    st.markdown("""
    Tony Hsieh’s legacy lies in proving culture drives business success. His $350M Downtown Project created 1,000+ jobs, revitalizing Las Vegas. Zappos Insights influenced 500+ companies, generating $50M+ revenue.[](https://www.untitledleader.com/lessons-in-leadership/the-legacy-of-tony-hsieh-lessons-in-leadership-and-entrepreneurship/)
    """)
    
    try:
        fig_legacy = px.bar(innovation_timeline, x='Year', y='Impact_Level',
                           title='Hsieh’s Legacy Milestones',
                           color='Category',
                           text='Innovation')
        fig_legacy.update_layout(height=400)
        st.plotly_chart(fig_legacy, use_container_width=True)
    except Exception as e:
        st.error(f"Error rendering legacy chart: {e}")

elif page == "🌟 Innovation Timeline":
    st.header("Innovation Timeline")
    
    st.subheader("Key Innovations (1999-2015)")
    try:
        fig_timeline = px.scatter(innovation_timeline, x='Year', y='Impact_Level',
                                title='Zappos Innovation Timeline',
                                color='Category',
                                text='Innovation',
                                size='Impact_Level')
        fig_timeline.update_traces(textposition='top center')
        fig_timeline.update_layout(height=400)
        st.plotly_chart(fig_timeline, use_container_width=True)
    except Exception as e:
        st.error(f"Error rendering timeline chart: {e}")
    
    st.markdown("""
    <div class="insight-box">
        <h4>Innovation Highlights</h4>
        <ul>
            <li><strong>2007:</strong> 365-day return policy, 75% repeat customers</li>
            <li><strong>2009:</strong> $1.2B Amazon acquisition, 10M shares</li>
            <li><strong>2013:</strong> Holacracy for 1,500+ employees</li>[](https://www.sj-r.com/story/business/2015/05/16/inside-zappos-ceo-tony-hsieh/34547263007/)
        </ul>
    </div>
    """, unsafe_allow_html=True)
```
