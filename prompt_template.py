
import json

def build_prompt(responses):
    return f"""
You are an Insight Synthesizer for user feedback.
Given the following survey responses, identify the top 3 themes that emerge.
For each theme, return:
1. A short title (2-4 words)
2. 1-12 direct quotes from the responses that support this theme
3. An overall sentiment: positive, negative, or neutral only one of them
nothing else just the JSON!!! NO EXTRA TEXT!!!

Survey Responses:
{json.dumps(responses, indent=2)}

Format your response as JSON:
[
  {{
    "theme": "Theme title",
    "quotes": ["quote1", "quote2", ...],
    "sentiment": "positive|negative|neutral"
  }},
  ...
]
"""
