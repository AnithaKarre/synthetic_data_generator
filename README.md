# 🦢 Synthetic Sample Data Generator

> **Generate realistic sample data effortlessly** for development, testing, and demos using AI‑powered schema inference and Faker.

---

## 🌟 Key Highlights

* **AI‑Driven Schema Inference**: Automatically detect data schema from your CSV using LangChain Groq.
* **Domain‑Specific Faker Integration**: Generate realistic medicine names via DynamicProvider or DailyMed API.
* **Interactive Streamlit UI**: Upload CSV, preview input/output, and chat‑style prompts (e.g., “generate 5 more”).
* **One‑Click Download**: Export generated data as CSV with a single click.

---

## 🚀 Features

| Feature                   | Description                                                     |
| ------------------------- | --------------------------------------------------------------- |
| Schema Inference          | Extract column names, types, and faker functions automatically. |
| Initial Sample Generation | Instantly produce **10** synthetic rows on upload.              |
| Chat‑Style Prompts        | Ask follow‑ups like “generate 5 more” without reuploading CSV.  |
| Flexible Output           | Download any number of rows as a CSV file.                      |
| Modular Backend           | `backend.py` easily reusable in other applications or APIs.     |

---

## 📦 Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/<username>/sample-data-generator.git
   cd sample-data-generator
   ```

2. **Create & activate a virtual environment**

   ```bash
   python -m venv .venv
   # macOS/Linux
   source .venv/bin/activate
   # Windows
   .venv\Scripts\activate
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables**

   ```bash
   echo "GROQ_API_KEY=your_api_key" > .env
   ```

---

## 🎯 Usage

### Run Streamlit App

```bash
streamlit run streamlit_ui.py
```

1. **Upload** your CSV via the sidebar 📁
2. **Preview** the input schema and data 📝
3. **Download** initial synthetic samples 🚀
4. **Interact** via chat: “generate X more” 💬
5. **Export** updated CSV anytime 📥

---

## 🧩 Project Structure

```
sample-data-generator/
├── generator_data/
│   └── data_genarater.py   # Core logic
├── streamlit_ui.py         # Streamlit frontend
├── requirements.txt        # Python dependencies
├── .env                    # Environment variables (excluded from Git)
└── README.md               # Project documentation
```

---

## 🤝 Contributing

Contributions are welcome! Please:

1. Fork the repo
2. Create a feature branch (`git checkout -b feature/YourFeature`)
3. Commit changes (`git commit -m 'Add YourFeature'`)
4. Push to branch (`git push origin feature/YourFeature`)
5. Open a Pull Request

---
