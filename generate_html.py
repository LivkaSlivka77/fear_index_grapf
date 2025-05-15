from fredapi import Fred
import plotly.graph_objects as go

def generate_risk_index_html():
    fred = Fred(api_key='71288ba48f6b5bba8ebaec021399806b')
    vix_data = fred.get_series('VIXCLS')

    latest_vix = vix_data.iloc[-1]

    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=latest_vix,
        title={'text': "Fear and Greed Index"},
        gauge={
            'axis': {'range': [40, 0], 'tickwidth': 1, 'tickcolor': "darkgray"},
            'bar': {'color': "black"},
            'steps': [
                {'range': [40, 30], 'color': "#FF4500"},
                {'range': [30, 22], 'color': "#FFA500"},
                {'range': [22, 17], 'color': "#FFFF00"},
                {'range': [17, 12], 'color': "#7CFC00"},
                {'range': [12, 0], 'color': "#006400"},
            ],
            'threshold': {
                'line': {'color': "black", 'width': 4},
                'thickness': 0.8,
                'value': latest_vix
            }
        }
    ))

    fig.update_layout(
        font={'color': "black", 'family': "Arial"},
        margin=dict(l=20, r=20, t=60, b=20),
        annotations=[
            dict(x=0.85, y=0.75, text="Extreme Fear", showarrow=False, font=dict(size=12)),
            dict(x=0.68, y=0.9, text="Fear", showarrow=False, font=dict(size=12)),
            dict(x=0.5, y=0.97, text="Neutral", showarrow=False, font=dict(size=12)),
            dict(x=0.32, y=0.9, text="Greed", showarrow=False, font=dict(size=12)),
            dict(x=0.15, y=0.75, text="Extreme Greed", showarrow=False, font=dict(size=12)),
        ]
    )

    fig.write_html("risk_index.html", full_html=True, include_plotlyjs='cdn')

if __name__ == "__main__":
    generate_risk_index_html()
