# OSINT Warning Dashboard Prototype

This repository contains a minimal prototype of an OSINT‑powered warning dashboard for monitoring
indicators of Chinese coercion or invasion against Taiwan.  It implements two major
components:

1. **Backend (FastAPI)** – serves indicator definitions and evaluates simulated events using a simple
   rule engine.
2. **Frontend (Next.js)** – displays the list of indicators and allows users to simulate an event and view
   the resulting evaluation.

## Structure

```
osint-website/
├── backend/
│   ├── main.py               # FastAPI app
│   ├── requirements.txt      # Python dependencies
│   ├── rule_engine.py        # Simple rule engine
│   ├── __init__.py           # Makes `backend` a package
│
├── data/
│   └── indicator_definitions.yaml  # YAML indicator definitions

├── frontend/
│   ├── package.json          # Node.js dependencies
│   └── pages/                # Next.js pages

└── README.md
```

## Running the prototype

1. **Backend:**
   ```bash
   cd osint-website/backend
   # Create a virtual environment
   python -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   uvicorn main:app --reload --host 0.0.0.0 --port 8000
   ```
   This starts the FastAPI server on port 8000.  You can access the API documentation at
   `http://localhost:8000/docs`.

2. **Frontend:**
   ```bash
   cd osint-website/frontend
   npm install
   npm run dev
   ```
   This starts the Next.js development server on port 3000.  Navigate to
   `http://localhost:3000` to view the dashboard.  Each indicator links to a detail
   page where you can simulate an event.  The front‑end will POST to the backend’s
   `/event` endpoint and display the returned confidence and recommendation.

## Extending this prototype

This code is a starting point, not a production system.  To turn it into a
fully‑functional OSINT tool you would:

* Replace the dummy rule engine with logic that ingests real sensor data and
  applies thresholds/statistical models to trigger alerts.
* Add a database (e.g., PostgreSQL or DynamoDB) to persist indicators,
  events and analyst annotations.
* Implement WebSockets or server‑sent events so the front‑end can receive live
  updates when new alerts are generated.
* Secure the APIs with authentication and HTTPS.
* Expand the front‑end to include dashboards, heat maps and historical trend
  visualisations.

Nevertheless, this prototype demonstrates the architectural pattern described in the
collection‑management report: a micro‑service back end, a rule engine and a
client‑side application for analysts.