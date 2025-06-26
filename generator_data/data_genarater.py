import os, re, json, requests, pandas as pd
from faker import Faker
from dotenv import load_dotenv
from langchain_core.messages import SystemMessage, HumanMessage
from langchain_groq import ChatGroq

load_dotenv()
fake = Faker()

def load_csv(path):
    return pd.read_csv(path)

def fetch_medicine_list(df):
    if "medi" in df.to_csv(index=False).lower():
        resp = requests.get(
            "https://dailymed.nlm.nih.gov/dailymed/services/v2/drugnames.json",
            params={"pagesize": 100, "page": 1, "name_type": "both"}
        )
        names = [d["drug_name"] for d in resp.json().get("drug_names", []) if d.get("drug_name")]
        return names or ["Paracetamol", "Ibuprofen", "Amoxicillin", "Cetirizine"]
    return []

def infer_schema(df):
    system = SystemMessage(content="You are a helpful schema assistant for medicine data.")
    prompt = (
        "Return ONLY valid JSON schema with columns and faker_func:\n"
        "ProductName→medicine, Country→country(), "
        "Price→pyfloat(left_digits=3,right_digits=2,positive=True), "
        "StockQuantity→random_int(min=0,max=1000), "
        "ProductID→random_int(min=1000,max=9999)\n"
        f"CSV Input:\n{df.to_csv(index=False)}"
    )
    human = HumanMessage(content=prompt)
    model = ChatGroq(api_key=os.getenv("GROQ_API_KEY"), model_name="llama3-8b-8192")
    resp = model.invoke([system, human])
    match = re.search(r"({[\s\S]+})", resp.content)
    if not match:
        raise ValueError("JSON schema not found.")
    return json.loads(match.group(1))

def generate_fake_rows(schema: dict, medicine_list: list, num: int):
    props = schema.get("columns") or schema.get("properties")
    if isinstance(props, dict):
        columns = [{"name": name, **props[name]} for name in props]
    else:
        columns = props

    def gen_val(col):
        fn = col.get("faker_func")
        if fn == "medicine":
            return fake.random_element(elements=medicine_list)
        if fn:
            return eval(f"fake.{fn}")
        return None

    rows = []
    for _ in range(num):
        row = {col["name"]: val for col in columns if (val := gen_val(col)) is not None}
        rows.append(row)
    return pd.DataFrame(rows)

def main():
    input_path = "sample_data/sample_products.csv"
    output_path = "generated_output.csv"
    num_rows = 10

    df = load_csv(input_path)
    med_list = fetch_medicine_list(df)
    print(f"Loaded CSV: {df.shape}, medicine names: {len(med_list)}")

    schema = infer_schema(df)
    print("Schema:", schema)

    df_out = generate_fake_rows(schema, med_list, num_rows)
    df_out.to_csv(output_path, index=False)
    print(f"✅ Saved {num_rows} rows to {output_path}")
    print(df_out.head())

if __name__ == "__main__":
    main()
