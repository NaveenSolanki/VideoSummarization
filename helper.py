import numpy as np
import pandas as pd

class getevaluation():
    def __init__(self):
        # Simulated model predictions
        self.model_metrics = {
            "Diversity Score": 0.70,               
            "Representativeness Score": 0.74,      
            "Inference Time per Frame (ms)": 110,   
            "Summarization Ratio": 0.28,         
            "Memory Efficiency (GB)": 5.8
        }

        # Baseline metrics for comparison
        self.baseline_metrics = {
            "Diversity Score": 0.65,
            "Representativeness Score": 0.70,
            "Inference Time per Frame (ms)": 120,
            "Summarization Ratio": 0.30,
            "Memory Efficiency (GB)": 6.2
        }
    def eval(self):
        # Calculate improvement for each metric
        improvements = {metric: self.model_metrics[metric] - self.baseline_metrics[metric] for metric in self.baseline_metrics}

        # Prepare data for the table
        data = {
            "Metric": list(self.baseline_metrics.keys()),
            "Baseline": list(self.baseline_metrics.values()),
            "Our Model": list(self.model_metrics.values()),
            "Improvement": list(improvements.values())
        }

        # Create a DataFrame for the table
        df = pd.DataFrame(data)

        # Format the improvement column to include signs (+/-)
        df['Improvement'] = df['Improvement'].apply(lambda x: f"+{x:.2f}" if x > 0 else f"{x:.2f}")
        
        styled_df = df.style.set_table_styles([
            {'selector': 'thead th', 'props': [
                ('background-color', '#1C1C1C'),  # Dark header
                ('color', 'white'),               # White text
                ('border', '1px solid #ddd'), 
                ('font-weight', 'bold'),
                ('text-align', 'center')
            ]},
            {'selector': 'tbody td', 'props': [
                ('border', '1px solid #ddd'),
                ('padding', '10px'),
                ('text-align', 'center')
            ]},
            {'selector': 'tbody tr:nth-child(even)', 'props': [
                ('background-color', 'lilac')  # Subtle alternating row color
            ]},
            {'selector': 'tbody tr:nth-child(odd)', 'props': [
                ('background-color', 'lilac')
            ]},
        ]).set_caption("Professional Metrics Comparison").set_properties(**{
            'text-align': 'center',
            'font-family': 'Arial, sans-serif',
            'font-size': '14px'
        })
        # Display the table
        return styled_df
