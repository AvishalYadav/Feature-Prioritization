import json
from typing import Dict, List

def load_customer_insights(file_path: str) -> Dict:
    """Load and process customer insight data"""
    with open(file_path, 'r') as f:
        return json.load(f)

def process_feature_metrics(raw_data: Dict) -> List[Dict]:
    """Process raw feature metrics into structured format"""
    processed_data = []
    for feature in raw_data:
        processed_data.append({
            'feature_id': feature['id'],
            'metrics': {
                'usage_rate': feature.get('usage_rate', 0),
                'customer_satisfaction': feature.get('satisfaction', 0),
                'feature_requests': feature.get('requests', 0)
            }
        })
    return processed_data