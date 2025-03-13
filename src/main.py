from models.prioritization_model import FeaturePrioritizationModel, FeatureScore
from utils.data_processor import load_customer_insights
from utils.visualization import generate_roadmap_visualization
import json

def main():
    # Load configuration
    weights = {
        'customer_impact': 0.4,
        'development_effort': 0.3,
        'strategic_alignment': 0.3
    }
    
    # Initialize prioritization model
    model = FeaturePrioritizationModel(weights)
    
    # Load and process feature data
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
    
    # Prioritize features
    prioritized_features = model.prioritize_features(features)
    
    # Generate roadmap
    for idx, feature in enumerate(prioritized_features, 1):
        print(f"{idx}. {feature.name} (Score: {feature.total_score:.2f})")

    # Generate visualizations
    generate_roadmap_visualization([f.__dict__ for f in prioritized_features])

if __name__ == "__main__":
    main()