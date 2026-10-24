# Pydantic Data Validation for AI Agents

Foundational data validation and schema enforcement for LLM agent workflows using **Pydantic v2**.

---

## 📌 Concepts Covered

* **Type Enforcement:** Moving from manual Python type/value checks to declarative schemas.
* **Specialized Validators:** Using `EmailStr`, `AnyUrl`, and numeric constraints (`Field(gt=..., lt=...)`).
* **Metadata & LLM Guidance:** `Annotated` types with `Field(title=..., description=..., examples=...)` to generate rich JSON schemas for tool-calling LLMs.
* **Custom Validators:**
  * `@field_validator`: Field-level sanitization and domain checks.
  * `@model_validator`: Cross-field validation (e.g., verifying emergency contacts for seniors).
* **Computed Fields:** `@computed_field` for dynamic attributes like BMI.
* **Nested Models:** Composable hierarchical structures (`Address` within `PatientData`).
* **Serialization:** Exporting validated models with `.model_dump()` (dict) and `.model_dump_json()` (JSON string) for prompt injection and API payloads.

---

## 📂 Structure

```text
01-pydantic-validation/
├── notebooks/
│   └── pydantic.ipynb       # Hands-on interactive walkthrough
├── requirements.txt         # Dependencies (pydantic, email-validator)
└── README.md
```

---

## 🚀 How to Run

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Open and run the notebook:
   ```bash
   jupyter notebook notebooks/pydantic.ipynb
   ```
