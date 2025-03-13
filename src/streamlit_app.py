import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from models.prioritization_model import FeaturePrioritizationModel, FeatureScore

def create_priority_matrix(features_df):
    fig = px.scatter(
        features_df,
        x="development_effort",
        y="customer_impact",
        size="strategic_alignment",
        text="name",
        size_max=60,
        color="total_score",
        color_continuous_scale="Viridis",
        title="Feature Priority Matrix"
    )
    
    fig.update_traces(textposition='top center')
    fig.update_layout(
        height=600,
        template="plotly_dark",
        xaxis_title="Development Effort",
        yaxis_title="Customer Impact"
    )
    return fig

def create_roadmap_timeline(features_df):
    fig = go.Figure()
    
    features_df = features_df.sort_values('total_score', ascending=True)
    
    fig.add_trace(go.Bar(
        y=features_df['name'],
        x=features_df['total_score'],
        orientation='h',
        marker=dict(
            color=features_df['total_score'],
            colorscale='Viridis'
        )
    ))
    
    fig.update_layout(
        title="Feature Roadmap Timeline",
        height=400,
        template="plotly_dark",
        xaxis_title="Priority Score",
        yaxis_title="Features"
    )
    return fig

def main():
    st.set_page_config(
        page_title="AI-LMS Feature Prioritization",
        page_icon="📊",
        layout="wide"
    )
    
    st.title("🎯 AI-LMS Feature Prioritization Dashboard")
    
    # Sidebar controls
    st.sidebar.header("Weights Configuration")
    customer_impact_weight = st.sidebar.slider("Customer Impact Weight", 0.0, 1.0, 0.4)
    dev_effort_weight = st.sidebar.slider("Development Effort Weight", 0.0, 1.0, 0.3)
    strategic_weight = st.sidebar.slider("Strategic Alignment Weight", 0.0, 1.0, 0.3)
    
    # Normalize weights
    total = customer_impact_weight + dev_effort_weight + strategic_weight
    weights = {
        'customer_impact': customer_impact_weight / total,
        'development_effort': dev_effort_weight / total,
        'strategic_alignment': strategic_weight / total
    }
    
    # Initialize model and features
    model = FeaturePrioritizationModel(weights)
    features = [
        FeatureScore(
            feature_id="F1",
            name="AI-Powered Content Recommendations",
            customer_impact=0.9,
            development_effort=0.7,
            strategic_alignment=0.8
        ),
        FeatureScore(
            feature_id="F2",
            name="Automated Assessment Generation",
            customer_impact=0.8,
            development_effort=0.5,
            strategic_alignment=0.7
        ),
        FeatureScore(
            feature_id="F3",
            name="Adaptive Learning Paths",
            customer_impact=0.95,
            development_effort=0.6,
            strategic_alignment=0.9
        )
    ]
    
    # Calculate priorities
    prioritized_features = model.prioritize_features(features)
    
    # Convert to DataFrame for visualization
    features_df = pd.DataFrame([
        {
            'name': f.name,
            'customer_impact': f.customer_impact,
            'development_effort': f.development_effort,
            'strategic_alignment': f.strategic_alignment,
            'total_score': f.total_score
        } for f in prioritized_features
    ])
    
    # Display metrics
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Top Priority", features_df.iloc[0]['name'])
    with col2:
        st.metric("Highest Impact", features_df.loc[features_df['customer_impact'].idxmax()]['name'])
    with col3:
        st.metric("Quickest Win", features_df.loc[features_df['development_effort'].idxmin()]['name'])
    
    # Display visualizations
    col1, col2 = st.columns(2)
    
    with col1:
        st.plotly_chart(create_priority_matrix(features_df), use_container_width=True)
    
    with col2:
        st.plotly_chart(create_roadmap_timeline(features_df), use_container_width=True)
    
    # Display detailed table
    st.subheader("Detailed Feature Analysis")
    st.dataframe(
        features_df.round(2),  # Round numbers to 2 decimal places
        use_container_width=True
    )

if __name__ == "__main__":
    main()