# trade-opportunities-api
trade-opportunities-api
📊 Trade Opportunities API

A FastAPI-based backend service that analyzes Indian market sectors and generates trade opportunity insights using AI (Google Gemini) and current market data.
The API returns a structured Markdown report that can be saved as a .md file.

🚀 Features

✅ Single API endpoint to analyze a market sector

✅ AI-powered analysis using Google Gemini API

✅ Structured Markdown report output

✅ JWT-based authentication

✅ Rate limiting to prevent abuse

✅ Input validation

✅ In-memory session tracking

✅ Clean, modular architecture

✅ Auto-generated API documentation (Swagger)

🛠️ Tech Stack

Backend Framework: FastAPI (Python)

AI Model: Google Gemini API

HTTP Client: httpx

Authentication: JWT

Rate Limiting: SlowAPI

Storage: In-memory (No database)

Documentation: Swagger UI

📁 Project Structure
trade-opportunities-api/
│
├── app/
│   ├── main.py                # FastAPI entry point
│   ├── config.py              # Environment configuration
│   ├── security.py            # JWT authentication
│   ├── rate_limiter.py        # Rate limiting logic
│   ├── models.py              # Input validation schemas
│   ├── services/
│   │   ├── search_service.py  # Market data collection
│   │   ├── ai_service.py      # Gemini AI integration
│   │   └── report_service.py  # Markdown report generator
│   └── utils/
│       └── session_store.py   # In-memory session tracking
│
├── requirements.txt
├── .gitignore
└── README.md

🔐 Authentication

Uses JWT (JSON Web Tokens)

Each request must include an Authorization header

Authorization: Bearer <JWT_TOKEN>

🚦 Rate Limiting

5 requests per minute per client

Implemented using SlowAPI

Prevents API abuse and excessive usage

📌 API Endpoint
Analyze Sector
GET /analyze/{sector}

Example
GET /analyze/pharmaceuticals

Headers
Authorization: Bearer <JWT_TOKEN>

Sample Response
{
  "report": "# Trade Opportunities Report – Pharmaceuticals\n\n## Market Overview\n...\n"
}

🧪 Running Locally
1️⃣ Clone the Repository
git clone https://github.com/TamilarasiRadhakrishnan/trade-opportunities-api.git
cd trade-opportunities-api

2️⃣ Create Virtual Environment
python -m venv venv
source venv/bin/activate


(Windows)

venv\Scripts\activate

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Set Environment Variables

Create a .env file:

GEMINI_API_KEY=your_gemini_api_key_here
JWT_SECRET_KEY=supersecretkey123


⚠️ Do not commit .env

5️⃣ Start the Server
uvicorn app.main:app --reload


Server will run at:

http://127.0.0.1:8000

📘 API Documentation

Swagger UI is available at:

http://127.0.0.1:8000/docs

🔑 Generate JWT Token (For Testing)

Run in Python shell:

from jose import jwt
jwt.encode({"user_id": "testuser"}, "supersecretkey123", algorithm="HS256")


Use the generated token in Swagger or API calls.

🛡️ Security Best Practices

JWT authentication

Rate limiting per client

Input validation using Pydantic

Environment variables for secrets

No database or sensitive data storage

🎯 Evaluation Checklist (Covered)

✔ FastAPI async implementation

✔ AI integration (Gemini)

✔ Data collection workflow

✔ Authentication & rate limiting

✔ Clean architecture & error handling

✔ Markdown report generation

✔ API documentation

✔ Ready for GitHub Codespaces
