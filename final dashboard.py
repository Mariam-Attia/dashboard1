import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import numpy as np
from datetime import datetime, timedelta

# Page configuration
st.set_page_config(
    page_title="Tony Hsieh Leadership Analysis",
    page_icon="👔",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        font-weight: bold;
        text-align: center;
        color: #1f77b4;
        margin-bottom: 2rem;
    }
    .section-header {
        font-size: 2rem;
        font-weight: bold;
        color: #ff7f0e;
        margin-top: 2rem;
        margin-bottom: 1rem;
    }
    .metric-card {
        background-color: #f0f2f6;
        padding: 1rem;
        border-radius: 0.5rem;
        border-left: 5px solid #1f77b4;
    }
    .quote-box {
        background-color: #e8f4f8;
        padding: 1rem;
        border-radius: 0.5rem;
        border-left: 5px solid #2ca02c;
        font-style: italic;
        margin: 1rem 0;
    }
    .sidebar .sidebar-content {
        background-color: #f8f9fa;
    }
    .insight-box {
        background-color: #fff3cd;
        padding: 1rem;
        border-radius: 0.5rem;
        border-left: 5px solid #ffc107;
        margin: 1rem 0;
    }
    .leadership-principle {
        background-color: #d1ecf1;
        padding: 0.8rem;
        border-radius: 0.3rem;
        margin: 0.5rem 0;
        border-left: 3px solid #bee5eb;
    }
</style>
""", unsafe_allow_html=True)

# Sidebar navigation
st.sidebar.title("🎯 Navigation")
page = st.sidebar.selectbox(
    "Choose a section:",
    ["🏠 Overview", "📊 Leadership Analysis", "🏢 Zappos Journey", "⚡ Holacracy Experiment",
     "📈 Business Metrics", "🎭 Culture & Values", "🎯 Leadership Principles", "🔍 Interpretation & Insights"]
)

# Main title
st.markdown('<h1 class="main-header">Tony Hsieh: Revolutionary Leadership at Zappos</h1>', unsafe_allow_html=True)
st.markdown("*Exploring the visionary leadership that transformed an online shoe store into a billion-dollar culture-driven empire*")

if page == "🏠 Overview":
    col1, col2 = st.columns([2, 1])
   
    with col1:
        st.markdown('<h2 class="section-header">About Tony Hsieh (1973-2020)</h2>', unsafe_allow_html=True)
       
        st.markdown("""
        **Tony Hsieh** was a visionary entrepreneur and CEO who revolutionized corporate culture and customer service
        through his leadership at Zappos. Born to a Taiwanese American family, Hsieh graduated from Harvard with a
        computer science degree and went on to build multiple successful companies.
       
        ### Key Achievements:
        - 🚀 **Link Exchange**: Co-founded and sold to Microsoft for $265M (1998)
        - 👟 **Zappos**: Transformed from struggling startup to $1B+ revenue company
        - 📚 **Author**: "Delivering Happiness" became a business bestseller
        - 🏙️ **Downtown Project**: Invested $350M to revitalize Las Vegas downtown
        """)
       
        # Timeline
        st.markdown('<h3 class="section-header">Career Timeline</h3>', unsafe_allow_html=True)
       
        timeline_data = {
            'Year': [1995, 1996, 1998, 1999, 2009, 2010, 2013, 2020],
            'Event': [
                'Harvard Graduation',
                'Founded Link Exchange',
                'Sold Link Exchange to Microsoft',
                'Joined Zappos as Investor',
                'Amazon Acquired Zappos',
                'Published "Delivering Happiness"',
                'Implemented Holacracy',
                'Passed Away'
            ],
            'Impact': [4, 6, 8, 7, 9, 8, 6, 10]
        }
       
        fig_timeline = px.scatter(timeline_data, x='Year', y='Impact', size='Impact',
                                hover_data=['Event'], title="Tony Hsieh's Career Milestones")
        fig_timeline.update_traces(marker=dict(sizemode='diameter', sizeref=0.5))
        st.plotly_chart(fig_timeline, use_container_width=True)
   
    with col2:
        st.markdown('<div class="metric-card">', unsafe_allow_html=True)
        st.metric("Net Worth at Peak", "$840M", "+2000%")
        st.markdown('</div>', unsafe_allow_html=True)
       
        st.markdown('<div class="metric-card">', unsafe_allow_html=True)
        st.metric("Zappos Revenue (2008)", "$1B", "+62400%")
        st.markdown('</div>', unsafe_allow_html=True)
       
        st.markdown('<div class="metric-card">', unsafe_allow_html=True)
        st.metric("Years as Zappos CEO", "21", "1999-2020")
        st.markdown('</div>', unsafe_allow_html=True)
       
        st.markdown('<div class="quote-box">', unsafe_allow_html=True)
        st.markdown('💭 **"Our goal is to build a company where culture is the number one priority."**')
        st.markdown('</div>', unsafe_allow_html=True)

elif page == "📊 Leadership Analysis":
    st.markdown('<h2 class="section-header">Leadership Style Analysis</h2>', unsafe_allow_html=True)
   
    # Leadership characteristics radar chart
    leadership_traits = {
        'Trait': ['Transformational', 'Servant Leadership', 'Cultural Architect',
                 'Innovation Focus', 'Risk Taking', 'Employee Empowerment',
                 'Customer Obsession', 'Transparency'],
        'Score': [9, 10, 10, 8, 9, 8, 10, 9],
        'Description': [
            'Drove radical organizational changes',
            'Prioritized employee wellbeing and growth',
            'Built unique organizational culture',
            'Encouraged experimentation and creativity',
            'Took bold business and management risks',
            'Gave employees autonomy and decision-making power',
            'Made customer satisfaction the top priority',
            'Promoted open communication and feedback'
        ]
    }
   
    col1, col2 = st.columns(2)
   
    with col1:
        # Radar chart
        fig_radar = go.Figure()
        fig_radar.add_trace(go.Scatterpolar(
            r=leadership_traits['Score'],
            theta=leadership_traits['Trait'],
            fill='toself',
            name='Tony Hsieh Leadership Profile'
        ))
        fig_radar.update_layout(
            polar=dict(
                radialaxis=dict(
                    visible=True,
                    range=[0, 10]
                )),
            showlegend=True,
            title="Leadership Traits Assessment"
        )
        st.plotly_chart(fig_radar, use_container_width=True)
   
    with col2:
        # Leadership styles breakdown
        styles_data = {
            'Style': ['Transformational', 'Servant', 'Charismatic', 'Experimental'],
            'Influence': [35, 30, 20, 15],
            'Examples': [
                'Holacracy implementation, radical culture changes',
                'Employee happiness focus, empowerment initiatives',
                'Inspiring vision, personal brand building',
                'Bold experiments, "fail fast" mentality'
            ]
        }
       
        fig_pie = px.pie(styles_data, values='Influence', names='Style',
                        title="Leadership Style Composition")
        st.plotly_chart(fig_pie, use_container_width=True)
   
    # Leadership lessons
    st.markdown('<h3 class="section-header">Key Leadership Lessons</h3>', unsafe_allow_html=True)
   
    lessons = {
        'Lesson': [
            '1. Define Core Values',
            '2. Train Your Leaders',
            '3. Drive Employee Engagement',
            '4. Focus on Wowing Customers',
            '5. Look for New Ideas Everywhere'
        ],
        'Implementation': [
            'Created 10 core values, used "Zollars" reward system',
            'Holacracy training, self-organized teams, lead links',
            'Fun office environment, culture-first hiring',
            'No-script customer service, 365-day returns',
            'Employee idea sensors, vendor partnerships'
        ],
        'Impact_Score': [9, 7, 8, 10, 6]
    }
   
    fig_lessons = px.bar(lessons, x='Lesson', y='Impact_Score',
                        title="Effectiveness of Leadership Lessons",
                        hover_data=['Implementation'])
    st.plotly_chart(fig_lessons, use_container_width=True)

elif page == "🏢 Zappos Journey":
    st.markdown('<h2 class="section-header">The Zappos Transformation</h2>', unsafe_allow_html=True)
   
    # Revenue growth over time
    revenue_data = {
        'Year': [2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2015, 2020],
        'Revenue_Million': [1.6, 8.6, 32, 70, 184, 370, 597, 840, 1000, 1200, 1500, 2000, 2200],
        'Employees': [50, 100, 200, 300, 500, 800, 1200, 1400, 1500, 1600, 1700, 1800, 1900]
    }
   
    col1, col2 = st.columns(2)
   
    with col1:
        # Revenue growth
        fig_revenue = px.line(revenue_data, x='Year', y='Revenue_Million',
                            title="Zappos Revenue Growth Under Hsieh",
                            markers=True)
        fig_revenue.update_layout(yaxis_title="Revenue ($ Millions)")
        st.plotly_chart(fig_revenue, use_container_width=True)
   
    with col2:
        # Employee growth
        fig_employees = px.area(revenue_data, x='Year', y='Employees',
                              title="Employee Growth at Zappos")
        st.plotly_chart(fig_employees, use_container_width=True)
   
    # Transformation phases
    st.markdown('<h3 class="section-header">Transformation Phases</h3>', unsafe_allow_html=True)
   
    phases_data = {
        'Phase': ['Startup\n(1999-2003)', 'Growth\n(2004-2008)', 'Maturity\n(2009-2013)', 'Innovation\n(2014-2020)'],
        'Revenue_Growth': [85, 45, 25, 15],
        'Culture_Focus': [30, 60, 90, 85],
        'Innovation_Level': [70, 40, 60, 95],
        'Risk_Level': [90, 60, 40, 80]
    }
   
    fig_phases = go.Figure()
   
    x = phases_data['Phase']
   
    fig_phases.add_trace(go.Bar(name='Revenue Growth %', x=x, y=phases_data['Revenue_Growth']))
    fig_phases.add_trace(go.Bar(name='Culture Focus %', x=x, y=phases_data['Culture_Focus']))
    fig_phases.add_trace(go.Bar(name='Innovation Level %', x=x, y=phases_data['Innovation_Level']))
    fig_phases.add_trace(go.Bar(name='Risk Level %', x=x, y=phases_data['Risk_Level']))
   
    fig_phases.update_layout(
        title='Zappos Transformation Phases Analysis',
        barmode='group',
        xaxis_title='Business Phase',
        yaxis_title='Intensity (%)'
    )
   
    st.plotly_chart(fig_phases, use_container_width=True)
   
    # Key milestones
    st.markdown('<h3 class="section-header">Major Milestones</h3>', unsafe_allow_html=True)
   
    milestones = [
        {"Year": 1999, "Event": "Tony Hsieh invests in Zappos", "Impact": "Provided crucial funding and leadership"},
        {"Year": 2000, "Event": "Became CEO", "Impact": "Started culture transformation"},
        {"Year": 2005, "Event": "Moved headquarters to Vegas", "Impact": "Created unique work environment"},
        {"Year": 2009, "Event": "Amazon acquisition", "Impact": "$1.2B deal while maintaining independence"},
        {"Year": 2010, "Event": "Published 'Delivering Happiness'", "Impact": "Shared leadership philosophy globally"},
        {"Year": 2013, "Event": "Implemented Holacracy", "Impact": "Revolutionary management experiment"}
    ]
   
    for milestone in milestones:
        with st.expander(f"📅 {milestone['Year']}: {milestone['Event']}"):
            st.write(f"**Impact:** {milestone['Impact']}")
   
    # Success metrics
    st.markdown('<h3 class="section-header">Success Metrics</h3>', unsafe_allow_html=True)
   
    col1, col2, col3, col4 = st.columns(4)
   
    with col1:
        st.metric("Peak Revenue", "$2.2B", "+137,400% from 2000")
    with col2:
        st.metric("Customer Retention", "90%+", "Industry leading")
    with col3:
        st.metric("Employee Satisfaction", "85%", "Above industry average")
    with col4:
        st.metric("Return Policy", "365 days", "Industry revolutionary")

elif page == "⚡ Holacracy Experiment":
    st.markdown('<h2 class="section-header">The Holacracy Revolution</h2>', unsafe_allow_html=True)
   
    st.markdown("""
    In 2013, Tony Hsieh made one of the most radical organizational decisions in corporate history:
    **eliminating all managers** and implementing Holacracy, a self-management system.
    """)
   
    # Before vs After comparison
    col1, col2 = st.columns(2)
   
    with col1:
        st.markdown("### 🏢 Traditional Hierarchy (Before)")
        st.markdown("""
        - Clear reporting structure
        - Managers make decisions
        - Job titles and descriptions
        - Top-down communication
        - Performance reviews by supervisors
        """)
       
        # Hierarchical visualization
        hierarchy_data = {
            'Level': ['CEO', 'VPs', 'Directors', 'Managers', 'Employees'],
            'Count': [1, 5, 15, 50, 200],
            'Authority': [100, 80, 60, 40, 20]
        }
       
        fig_hierarchy = px.funnel(hierarchy_data, x='Count', y='Level',
                                title="Traditional Organizational Structure")
        st.plotly_chart(fig_hierarchy, use_container_width=True)
   
    with col2:
        st.markdown("### ⭕ Holacracy Circles (After)")
        st.markdown("""
        - Self-organizing circles
        - Distributed decision-making
        - Multiple roles per person
        - Peer-to-peer communication
        - Continuous feedback loops
        """)
       
        # Holacracy visualization
        circles_data = {
            'Circle': ['General Circle', 'Customer Service', 'Marketing',
                      'Technology', 'Operations', 'Culture'],
            'Members': [20, 150, 80, 120, 100, 50],
            'Autonomy_Level': [90, 85, 80, 88, 82, 95]
        }
       
        fig_circles = px.scatter(circles_data, x='Members', y='Autonomy_Level',
                               size='Members', hover_name='Circle',
                               title="Holacracy Circle Structure")
        st.plotly_chart(fig_circles, use_container_width=True)
   
    # Implementation timeline
    st.markdown('<h3 class="section-header">Holacracy Implementation Timeline</h3>', unsafe_allow_html=True)
   
    implementation_data = {
        'Phase': ['Announcement', '3 Months', '6 Months', '1 Year', '2 Years', '3 Years'],
        'Employee_Satisfaction': [75, 65, 60, 58, 62, 68],
        'Productivity': [80, 70, 65, 68, 72, 75],
        'Turnover_Rate': [10, 18, 22, 25, 20, 16]
    }
   
    fig_implementation = make_subplots(specs=[[{"secondary_y": True}]])
   
    fig_implementation.add_trace(
        go.Scatter(x=implementation_data['Phase'], y=implementation_data['Employee_Satisfaction'],
                  mode='lines+markers', name='Employee Satisfaction (%)', line=dict(color='blue')),
        secondary_y=False,
    )
   
    fig_implementation.add_trace(
        go.Scatter(x=implementation_data['Phase'], y=implementation_data['Productivity'],
                  mode='lines+markers', name='Productivity (%)', line=dict(color='green')),
        secondary_y=False,
    )
   
    fig_implementation.add_trace(
        go.Scatter(x=implementation_data['Phase'], y=implementation_data['Turnover_Rate'],
                  mode='lines+markers', name='Turnover Rate (%)', line=dict(color='red')),
        secondary_y=True,
    )
   
    fig_implementation.update_yaxes(title_text="Satisfaction & Productivity (%)", secondary_y=False)
    fig_implementation.update_yaxes(title_text="Turnover Rate (%)", secondary_y=True)
    fig_implementation.update_layout(title='Holacracy Implementation Impact Over Time')
   
    st.plotly_chart(fig_implementation, use_container_width=True)
   
    # Impact analysis
    st.markdown('<h3 class="section-header">Holacracy Impact Analysis</h3>', unsafe_allow_html=True)
   
    impact_data = {
        'Metric': ['Employee Satisfaction', 'Decision Speed', 'Innovation Rate',
                  'Employee Retention', 'Operational Efficiency', 'Customer Satisfaction'],
        'Before_Holacracy': [75, 60, 65, 85, 80, 90],
        'After_Holacracy': [70, 85, 80, 65, 70, 88],
        'Change': [-5, 25, 15, -20, -10, -2]
    }
   
    fig_impact = go.Figure()
    fig_impact.add_trace(go.Bar(name='Before Holacracy', x=impact_data['Metric'],
                               y=impact_data['Before_Holacracy'], marker_color='lightblue'))
    fig_impact.add_trace(go.Bar(name='After Holacracy', x=impact_data['Metric'],
                               y=impact_data['After_Holacracy'], marker_color='darkblue'))
    fig_impact.update_layout(title='Holacracy Impact on Key Metrics', barmode='group')
    st.plotly_chart(fig_impact, use_container_width=True)
   
    # Pros and Cons
    col1, col2 = st.columns(2)
   
    with col1:
        st.markdown("### ✅ Holacracy Benefits")
        benefits = [
            "Faster decision-making in some areas",
            "Increased employee autonomy",
            "Enhanced innovation and experimentation",
            "Reduced bureaucracy",
            "Better adaptation to change"
        ]
        for benefit in benefits:
            st.write(f"• {benefit}")
   
    with col2:
        st.markdown("### ❌ Holacracy Challenges")
        challenges = [
            "18% employee turnover initially",
            "Role confusion and ambiguity",
            "Difficulty in performance evaluation",
            "Coordination challenges",
            "Not suitable for all personality types"
        ]
        for challenge in challenges:
            st.write(f"• {challenge}")

elif page == "📈 Business Metrics":
    st.markdown('<h2 class="section-header">Zappos Business Performance</h2>', unsafe_allow_html=True)
   
    # Financial metrics
    financial_data = {
        'Year': [2000, 2002, 2004, 2006, 2008, 2010, 2015, 2020],
        'Revenue': [1.6, 32, 184, 597, 1000, 1500, 2000, 2200],
        'Profit_Margin': [5, 8, 12, 15, 11, 13, 14, 12],
        'Customer_Base': [1000, 50000, 200000, 800000, 2000000, 3000000, 4500000, 5000000]
    }
   
    # Revenue and profitability
    fig_financial = make_subplots(specs=[[{"secondary_y": True}]])
   
    fig_financial.add_trace(
        go.Scatter(x=financial_data['Year'], y=financial_data['Revenue'],
                  mode='lines+markers', name='Revenue ($M)', line=dict(color='blue')),
        secondary_y=False,
    )
   
    fig_financial.add_trace(
        go.Scatter(x=financial_data['Year'], y=financial_data['Profit_Margin'],
                  mode='lines+markers', name='Profit Margin (%)', line=dict(color='red')),
        secondary_y=True,
    )
   
    fig_financial.update_xaxes(title_text="Year")
    fig_financial.update_yaxes(title_text="Revenue ($ Millions)", secondary_y=False)
    fig_financial.update_yaxes(title_text="Profit Margin (%)", secondary_y=True)
    fig_financial.update_layout(title_text="Zappos Financial Performance")
   
    st.plotly_chart(fig_financial, use_container_width=True)
   
    # Customer metrics
    col1, col2 = st.columns(2)
   
    with col1:
        # Customer growth
        fig_customers = px.line(financial_data, x='Year', y='Customer_Base',
                              title="Customer Base Growth", markers=True)
        fig_customers.update_layout(yaxis_title="Number of Customers")
        st.plotly_chart(fig_customers, use_container_width=True)
   
    with col2:
        # Customer satisfaction metrics
        satisfaction_data = {
            'Metric': ['Net Promoter Score', 'Customer Retention', 'Repeat Purchase Rate',
                      'Customer Service Rating', 'Return Rate Satisfaction'],
            'Score': [75, 90, 85, 95, 88]
        }
       
        fig_satisfaction = px.bar(satisfaction_data, x='Metric', y='Score',
                                title="Customer Satisfaction Metrics")
        fig_satisfaction.update_xaxes(tickangle=45)
        st.plotly_chart(fig_satisfaction, use_container_width=True)
   
    # Competitive analysis
    st.markdown('<h3 class="section-header">Competitive Analysis</h3>', unsafe_allow_html=True)
   
    competitive_data = {
        'Company': ['Zappos', 'Amazon Fashion', 'DSW', 'Foot Locker', 'Nordstrom'],
        'Customer_Satisfaction': [95, 85, 78, 80, 88],
        'Employee_Satisfaction': [85, 70, 65, 68, 75],
        'Innovation_Score': [90, 95, 60, 65, 80],
        'Culture_Rating': [98, 75, 70, 72, 85]
    }
   
    fig_competitive = px.scatter(competitive_data, x='Customer_Satisfaction', y='Employee_Satisfaction',
                               size='Innovation_Score', hover_name='Company', color='Culture_Rating',
                               title="Competitive Positioning: Customer vs Employee Satisfaction")
    fig_competitive.update_layout(
        xaxis_title="Customer Satisfaction Score",
        yaxis_title="Employee Satisfaction Score"
    )
    st.plotly_chart(fig_competitive, use_container_width=True)
   
    # Key performance indicators
    st.markdown('<h3 class="section-header">Key Performance Indicators</h3>', unsafe_allow_html=True)
   
    col1, col2, col3, col4 = st.columns(4)
   
    with col1:
        st.metric("Revenue Growth Rate", "15-25%", "Annual average")
        st.metric("Market Share", "12%", "Online footwear")
   
    with col2:
        st.metric("Customer Lifetime Value", "$3,500", "+40% vs industry")
        st.metric("Average Order Value", "$85", "Above industry avg")
   
    with col3:
        st.metric("Return Processing Time", "24 hours", "Industry leading")
        st.metric("Call Resolution Rate", "95%", "First call")
   
    with col4:
        st.metric("Employee Productivity", "125%", "vs industry benchmark")
        st.metric("Culture Score", "4.2/5", "Employee rating")

elif page == "🎭 Culture & Values":
    st.markdown('<h2 class="section-header">Zappos Culture Revolution</h2>', unsafe_allow_html=True)
   
    # 10 Core Values
    st.markdown('<h3 class="section-header">The 10 Core Values</h3>', unsafe_allow_html=True)
   
    core_values = [
        {"Value": "Deliver WOW Through Service", "Description": "Go above and beyond to create memorable customer experiences"},
        {"Value": "Embrace and Drive Change", "Description": "Be adaptable and actively seek opportunities for growth"},
        {"Value": "Create Fun and A Little Weirdness", "Description": "Maintain a positive, unique workplace atmosphere"},
        {"Value": "Be Adventurous, Creative, and Open-Minded", "Description": "Take risks and think outside the box"},
        {"Value": "Pursue Growth and Learning", "Description": "Continuously develop personally and professionally"},
        {"Value": "Build Open and Honest Relationships", "Description": "Foster trust through transparent communication"},
        {"Value": "Build a Positive Team and Family Spirit", "Description": "Create strong bonds and collaboration"},
        {"Value": "Do More with Less", "Description": "Be resourceful and efficient in all endeavors"},
        {"Value": "Be Passionate and Determined", "Description": "Show enthusiasm and persistence in work"},
        {"Value": "Be Humble", "Description": "Stay grounded and treat everyone with respect"}
    ]
   
    # Values importance rating
    values_data = {
        'Value': [v['Value WORK IN PROGRESS
