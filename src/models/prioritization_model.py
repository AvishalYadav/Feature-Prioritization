from dataclasses import dataclass
from typing import List, Dict
import numpy as np

@dataclass
class FeatureScore:
    feature_id: str
    name: str
    customer_impact: float
    development_effort: float
    strategic_alignment: float
    total_score: float = 0.0

class FeaturePrioritizationModel:
    def __init__(self, weights: Dict[str, float]):
        """
        Initialize the prioritization model with weights for different factors
        
        Args:
            weights: Dictionary containing weights for customer_impact,
                    development_effort, and strategic_alignment
        """
        self.weights = weights
        
    def calculate_feature_score(self, feature: FeatureScore) -> float:
        """Calculate the weighted score for a feature"""
        score = (
            feature.customer_impact * self.weights['customer_impact'] +
            (1 / feature.development_effort) * self.weights['development_effort'] +
            feature.strategic_alignment * self.weights['strategic_alignment']
        )
        return score
    
    def prioritize_features(self, features: List[FeatureScore]) -> List[FeatureScore]:
        """Sort features based on their calculated scores"""
        for feature in features:
            feature.total_score = self.calculate_feature_score(feature)
        
        return sorted(features, key=lambda x: x.total_score, reverse=True)