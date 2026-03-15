# 🧬 Synthetic Sample Data Generator

> Generate realistic sample data effortlessly for development, testing, and demos using AI-powered schema inference and Faker.

![Python](https://img.shields.io/badge/python-3.11%2B-brightgreen)
![Streamlit](https://img.shields.io/badge/Streamlit-UI-FF4B4B)
![Groq](https://img.shields.io/badge/Groq-LangChain-purple)
![Faker](https://img.shields.io/badge/Faker-Data%20Generation-blue)

---

## What is this?

Upload a CSV, and the system **automatically infers the schema** — column names, types, and appropriate Faker functions — using LangChain + Groq. It then generates realistic synthetic rows on the fly. Need more? Just type "generate 5 more" in the chat. Download everything as CSV when you're done.

No manual schema definitions. No tedious scripting. Just upload and go.

---

## 🌟 Key Highlights

- **AI-Driven Schema Inference** — Automatically detect data schema from your CSV using LangChain Groq
- **Domain-Specific Faker Integration** — Generate realistic values (e.g., medicine names via DynamicProvider or DailyMed API)
- **Interactive Streamlit UI** — Upload CSV, preview input/output, and use chat-style prompts
- **One-Click Download** — Export generated data as CSV instantly

---

## 🚀 Features

| Feature | Description |
|---|---|
| **Schema Inference** | Extract column names, types, and faker functions automatically |
| **Initial Sample Generation** | Instantly produce 10 synthetic rows on upload |
| **Chat-Style Prompts** | Ask follow-ups like "generate 5 more" without re-uploading |
| **Flexible Output** | Download any number of rows as a CSV file |
| **Modular Backend** | `data_genarater.py` easily reusable in other apps or APIs |

---

## 🏗️ How It Works

```
 Upload CSV
     │
     ▼
 ┌──────────────────────┐
 │  Schema Inference     │  ← LangChain + Groq detects columns, types, faker mappings
 └──────────┬───────────┘
            ▼
 ┌──────────────────────┐
 │  Faker Generation     │  ← Generates realistic rows using inferred schema
 └──────────┬───────────┘
            ▼
 ┌──────────────────────┐
 │  Streamlit UI         │  ← Preview, chat for more rows, download CSV
 └──────────────────────┘
```

---

## 📦 Getting Started

**Prerequisites:** Python 3.11+ and a Groq API key.

```bash
# 1. Clone
git clone https://github.com/AnithaKarre/synthetic_data_generator.git
cd synthetic_data_generator

# 2. Virtual environment
python -m venv .venv
.venv\Scripts\activate          # Windows
# source .venv/bin/activate     # macOS/Linux

# 3. Install dependencies
pip install -r requirement.txt

# 4. Configure environment
echo "GROQ_API_KEY=your_api_key" > .env

# 5. Run
streamlit run streamlit_ui.py
```

---

## 🎯 Usage

1. **Upload** your CSV via the sidebar 📁
2. **Preview** the inferred schema and input data 📝
3. **Download** initial synthetic samples (10 rows auto-generated) 🚀
4. **Chat** to generate more: *"generate 5 more"* 💬
5. **Export** updated CSV anytime 📥

---

## 📂 Project Structure

```
synthetic_data_generator/
├── main.py                        # Entry point
├── streamlit_ui.py                # Streamlit frontend
├── requirement.txt                # Python dependencies
├── pyproject.toml                 # Project configuration
├── uv.lock                        # Lock file for reproducible installs
├── generator_data/
│   └── data_genarater.py          # Core generation logic (schema + Faker)
├── sample_data/                   # Example input CSVs
└── generator_data/                # Output / generated data
```

---

## 🛠️ Tech Stack

**AI/LLM:** LangChain · Groq

**Data Generation:** Faker · DynamicProvider · DailyMed API

**Frontend:** Streamlit

**Core:** Python 3.11+ · pandas

---

## 🤝 Contributing

1. Fork the repo
2. Create a feature branch (`git checkout -b feature/YourFeature`)
3. Commit changes (`git commit -m 'Add YourFeature'`)
4. Push to branch (`git push origin feature/YourFeature`)
5. Open a Pull Request
