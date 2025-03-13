import matplotlib.pyplot as plt
import seaborn as sns
from typing import List, Dict
import pandas as pd

class RoadmapVisualizer:
    def __init__(self):
        self.colors = ['#FF9999', '#66B2FF', '#99FF99']
        
    def create_priority_matrix(self, features: List[Dict]) -> None:
        """Create priority matrix visualization"""
        df = pd.DataFrame(features)
        
        plt.figure(figsize=(10, 8))
        plt.scatter(df['development_effort'], df['customer_impact'], 
                   s=df['strategic_alignment']*500, alpha=0.6)
        
        for i, txt in enumerate(df['name']):
            plt.annotate(txt, (df['development_effort'].iloc[i], 
                             df['customer_impact'].iloc[i]))
            
        plt.xlabel('Development Effort')
        plt.ylabel('Customer Impact')
        plt.title('Feature Priority Matrix')
        plt.grid(True)
        plt.savefig('docs/priority_matrix.png')
        plt.close()
    
    def create_roadmap_timeline(self, features: List[Dict]) -> None:
        """Create roadmap timeline visualization"""
        df = pd.DataFrame(features)
        
        fig, ax = plt.subplots(figsize=(12, 6))
        
        y_positions = range(len(df))
        ax.barh(y_positions, df['development_effort']*10, 
                left=df.index*5, color=self.colors[:len(df)])
        
        ax.set_yticks(y_positions)
        ax.set_yticklabels(df['name'])
        ax.set_xlabel('Weeks')
        ax.set_title('Feature Development Timeline')
        
        plt.savefig('docs/roadmap_timeline.png')
        plt.close()

def generate_roadmap_visualization(features: List[Dict]) -> None:
    """Helper function to generate roadmap visualization"""
    visualizer = RoadmapVisualizer()
    visualizer.create_priority_matrix(features)
    visualizer.create_roadmap_timeline(features)