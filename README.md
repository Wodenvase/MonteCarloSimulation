# 📈 Monte Carlo Portfolio Value Simulator

A lightweight Python microservice for simulating long-term investment portfolio value using Monte Carlo techniques. It estimates the future value distribution based on user-defined investment parameters — and exposes a clean, testable REST API via **FastAPI**.

---

## 🚀 Features

- 📊 **Monte Carlo Simulation** of daily compounded returns
- 📈 **Percentile Output**: P10, P50, P90 portfolio values
- 🧮 Uses **NumPy** for statistical modeling
- ⚡ Built with **FastAPI** for blazing-fast API performance
- 🦀 Managed using **[uv](https://github.com/astral-sh/uv)** – a Rust-based Python package manager
- 🔬 Swagger-based interactive API docs at `/docs`

---

## 📦 Tech Stack

| Component           | Tool                    |
|--------------------|-------------------------|
| Language           | Python                  |
| API Framework      | FastAPI                 |
| Simulation         | NumPy                   |
| Package Manager    | [uv (by Astral)](https://github.com/astral-sh/uv) |
| Dev Server         | Uvicorn                 |
| Testing Tools      | Postman / Swagger UI    |

---

## 📥 API Usage

### ▶️ Endpoint

```http
POST /simulate
```

🧾 Request Body

```
{
  "initial_investment": 1000,
  "expected_return": 0.09,
  "volatility": 0.18,
  "years": 15,
  "iterations": 10000
}
```

| Field               | Type   | Description                                 |
|---------------------|--------|---------------------------------------------|
| initial_investment  | float  | Initial amount invested                     |
| expected_return     | float  | Annual expected return (e.g., 0.09 = 9%)    |
| volatility          | float  | Annual return volatility (e.g., 0.18 = 18%) |
| years               | int    | Investment duration in years                |
| iterations          | int    | Number of Monte Carlo simulations           |

⸻

✅ Response (200 OK)

```
{
  "P10": 1240.43,
  "P50": 3048.63,
  "P90": 7287.86
}
```

| Percentile | Meaning                        |
|------------|-------------------------------|
| P10        | Worst-case scenario (bottom 10%) |
| P50        | Median value (most likely outcome) |
| P90        | Best-case scenario (top 10%)      |

⸻

🧠 How It Works
1. Converts annual return and volatility into daily equivalents.
2. For each simulation iteration:
   - Simulates daily returns as random values from a normal distribution.
   - Compounds returns over years × 252 days.
3. Collects final portfolio values and calculates percentiles.

⸻

🔧 Getting Started

1. Install dependencies using uv

```
pip install uv
uv venv
uv pip install -r requirements.txt
```

2. Run the server

```
uvicorn main:app --reload
```

Navigate to: http://127.0.0.1:8000/docs to use the Swagger UI.

⸻

🛠 To-Do & Enhancements
- 🎨 Add histogram chart in API response
- 🌐 Streamlit web dashboard
- ☁️ Deploy to Fly.io or Railway
- 🔒 Add user auth and API key support
- 📁 Database logging (SQLite/PostgreSQL)

⸻

📂 Project Structure

montecarlo-simulator/
│
├── main.py               # FastAPI app logic
├── simulator.py          # Core Monte Carlo simulation logic
├── requirements.txt      # Project dependencies
├── README.md             # You're reading this!

⸻

🧪 Example Curl Request

```
curl -X POST http://127.0.0.1:8000/simulate \
-H "Content-Type: application/json" \
-d '{
  "initial_investment": 1000,
  "expected_return": 0.09,
  "volatility": 0.18,
  "years": 15,
  "iterations": 10000
}'
``` 