import unittest
from src.models.impact_analysis import ImpactAnalysis, ImpactMetrics

class TestImpactAnalysis(unittest.TestCase):
    def setUp(self):
        self.analyzer = ImpactAnalysis()
        
    def test_roi_calculation(self):
        costs = {"development": 100000, "maintenance": 20000}
        revenue_impact = 200000
        
        roi = self.analyzer.calculate_roi(revenue_impact, costs)
        self.assertGreater(roi, 0)
        
    def test_technical_feasibility(self):
        available_resources = {"developers": 5, "designers": 2}
        required_resources = {"developers": 3, "designers": 1}
        
        feasible = self.analyzer.assess_technical_feasibility(
            complexity=0.6,
            available_resources=available_resources,
            required_resources=required_resources
        )
        self.assertTrue(feasible)

if __name__ == '__main__':
    unittest.main()