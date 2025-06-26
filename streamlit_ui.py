import os
import re
import streamlit as st
from generator_data.data_genarater import (
    load_csv,
    fetch_medicine_list,
    infer_schema,
    generate_fake_rows
)

st.set_page_config(page_title="Sample Data Generator", layout="wide")
st.title("Synthetic Sample Data Generator")

# --- Sidebar: CSV Upload ---
uploaded = st.sidebar.file_uploader("📁 Upload your CSV here", type="csv")

# If no file and nothing in session, stop execution
if not uploaded and "schema" not in st.session_state:
    st.stop()

# --- Load CSV and generate initial schema/data ---
if uploaded and "schema" not in st.session_state:
    with st.spinner("Generating sample data..."):
        try:
            df = load_csv(uploaded)
            st.session_state.df_input = df
            st.session_state.schema = infer_schema(df)
            st.session_state.med_list = fetch_medicine_list(df)
            st.session_state.last_n = 10
            st.session_state.last_df = generate_fake_rows(
                st.session_state.schema,
                st.session_state.med_list,
                st.session_state.last_n
            )
            st.session_state.messages = []
            st.success("✅ Initial data generated!")
        except Exception as e:
            st.error(f"❌ Failed to process CSV: {e}")
            st.stop()

# --- Show original CSV preview ---
st.write("### 📜 Input Preview")
st.dataframe(st.session_state.df_input, use_container_width=True)

# --- Show Generated Data ---
st.markdown("---")
st.text(f"🦢 Generated Sample Data ({st.session_state.last_n} rows)")
st.dataframe(st.session_state.last_df, use_container_width=True)

csv = st.session_state.last_df.to_csv(index=False).encode("utf-8")
st.download_button(
    "📅 Download CSV",
    data=csv,
    file_name=f"sample_data_{st.session_state.last_n}.csv",
    mime="text/csv",
    key="download_initial"
)

# --- Chat-style Input ---
st.markdown("---")
try:
    user_input = st.chat_input("Ask: e.g., 'generate 5 more'")
except AttributeError:
    user_input = st.text_input("Ask: e.g., 'generate 5 more'")

# --- Display chat history ---
if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# --- Handle New Input ---
if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.write(user_input)

    # Spinner + try block
    with st.chat_message("assistant"):
        with st.spinner("Generating sample data..."):
            match = re.search(r"(\d+)", user_input)
            n = int(match.group(1)) if match else st.session_state.last_n

            try:
                df_new = generate_fake_rows(
                    st.session_state.schema,
                    st.session_state.med_list,
                    n
                )
                st.session_state.last_n = n
                st.session_state.last_df = df_new
                assistant_reply = f"✅ Generated {n} new samples."
            except Exception as e:
                assistant_reply = f"❌ Error: {e}"

        st.write(assistant_reply)
        st.session_state.messages.append({"role": "assistant", "content": assistant_reply})

    # Refresh output
    st.markdown("---")
    st.write(f"### 🦢 Generated Sample Data ({st.session_state.last_n} rows)")
    st.dataframe(st.session_state.last_df, use_container_width=True)
    csv = st.session_state.last_df.to_csv(index=False).encode("utf-8")
    st.download_button(
        "📅 Download CSV",
        data=csv,
        file_name=f"sample_data_{st.session_state.last_n}.csv",
        mime="text/csv",
        key="download_updated"
    )
