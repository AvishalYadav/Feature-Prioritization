from dataclasses import dataclass
from typing import Dict, List
import numpy as np

@dataclass
class ImpactMetrics:
    user_adoption: float
    revenue_impact: float
    technical_complexity: float
    resource_requirements: Dict[str, int]

class ImpactAnalysis:
    def __init__(self):
        self.impact_threshold = 0.7
        
    def calculate_roi(self, revenue_impact: float, costs: Dict[str, float]) -> float:
        """Calculate ROI for a feature"""
        total_cost = sum(costs.values())
        return (revenue_impact - total_cost) / total_cost if total_cost > 0 else 0
    
    def assess_technical_feasibility(self, complexity: float, 
                                   available_resources: Dict[str, int],
                                   required_resources: Dict[str, int]) -> bool:
        """Assess if feature is technically feasible with current resources"""
        if complexity > 0.8:  # High complexity threshold
            return False
            
        for resource, required in required_resources.items():
            if available_resources.get(resource, 0) < required:
                return False
        return True
    
    def analyze_feature_impact(self, metrics: ImpactMetrics) -> Dict[str, float]:
        """Analyze overall feature impact"""
        return {
            "adoption_score": metrics.user_adoption,
            "roi_score": self.calculate_roi(
                metrics.revenue_impact,
                {"development": 100000, "maintenance": 20000}
            ),
            "feasibility_score": 1 - metrics.technical_complexity
        }