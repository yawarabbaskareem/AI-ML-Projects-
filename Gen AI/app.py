import requests
import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="AI Internship Application Tracker",
    page_icon="🚀",
    layout="centered",
)

st.title("🚀 AI Internship Application Tracker")
st.write(
    "Type or paste your job application details below, and let the AI agent log"
    " it straight into your tracker."
)

# Input form
with st.form("tracker_form"):
  user_input = st.text_area(
      "Application Details",
      placeholder=(
          "e.g., I just applied to Microsoft for the AI Engineer Intern role."
          " Status is Applied, link is careers.microsoft.com"
      ),
  )
  submit_button = st.form_submit_button(label="Log Application")

if submit_button:
  if user_input.strip() == "":
    st.warning("Please enter some application details first!")
  else:
    with st.spinner("AI Agent is processing and updating your sheet..."):
      # Your live n8n Production Webhook URL
      n8n_webhook_url = (
          "https://yawar12.app.n8n.cloud/webhook-test/e809deb9-bea3-42e7-8632-d0459be2c2b2"
      )

      try:
        # Send data to n8n webhook
        response = requests.post(
            n8n_webhook_url, json={"chatInput": user_input}
        )

        if response.status_code == 200:
          st.success(
              "Success! Your application has been logged to Google Sheets."
          )
        else:
          st.error(
              f"Failed to reach n8n workflow. Status code:"
              f" {response.status_code}"
          )
      except Exception as e:
        st.error(f"An error occurred: {e}")