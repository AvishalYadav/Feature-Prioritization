import unittest
from src.models.prioritization_model import FeaturePrioritizationModel, FeatureScore

class TestPrioritization(unittest.TestCase):
    def setUp(self):
        self.weights = {
            'customer_impact': 0.4,
            'development_effort': 0.3,
            'strategic_alignment': 0.3
        }
        self.model = FeaturePrioritizationModel(self.weights)
        
    def test_feature_scoring(self):
        feature = FeatureScore(
            feature_id="TEST1",
            name="Test Feature",
            customer_impact=0.8,
            development_effort=0.5,
            strategic_alignment=0.7
        )
        
        score = self.model.calculate_feature_score(feature)
        self.assertGreater(score, 0)
        
    def test_feature_prioritization(self):
        features = [
            FeatureScore("F1", "Feature 1", 0.8, 0.5, 0.7),
            FeatureScore("F2", "Feature 2", 0.9, 0.3, 0.8)
        ]
        
        prioritized = self.model.prioritize_features(features)
        self.assertEqual(len(prioritized), 2)
        self.assertGreater(prioritized[0].total_score, 
                          prioritized[1].total_score)

if __name__ == '__main__':
    unittest.main()