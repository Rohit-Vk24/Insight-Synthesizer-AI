
import streamlit as st
import json
from prompt_template import build_prompt
from llm_handler import get_insights_from_llm
from ui_renderer import display_insight_cards

def main():
    st.set_page_config(page_title="Insight Synthesizer")
    st.title("🧠 Insight Synthesizer for Survey Feedback")

    st.markdown("Paste raw survey responses (one per line):")
    raw_input = st.text_area("Survey Responses", height=300)

    if st.button("Generate Insight Cards") and raw_input.strip():
        responses = [r.strip() for r in raw_input.split("\n") if r.strip()]
        prompt = build_prompt(responses)

        with st.spinner("Generating insights..."):
            try:
                raw_output = get_insights_from_llm(prompt)
                try:
                    insights = json.loads(raw_output)
                    st.success("✅ Insight Cards Generated")
                    display_insight_cards(insights)
                except json.JSONDecodeError:
                    st.error("⚠️ Failed to parse JSON. Raw model output:")
                    st.code(raw_output)

            except Exception as e:
                st.error(f"❌ Error: {e}")

if __name__ == "__main__":
    main()
