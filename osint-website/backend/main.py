"""
FastAPI application for the OSINT warning dashboard backend.

The API exposes two primary endpoints:
  * **GET /indicators** – returns the available indicator definitions.
  * **POST /event** – accepts a JSON event with at least an
    'indicator_id' field and returns the rule engine's evaluation of
    that event.

This backend is intentionally simple.  It demonstrates how you might
integrate the rule engine into an API.  In a real system you would
likely have additional endpoints for ingesting raw sensor data,
persisting alerts to a database, and streaming events via WebSockets.
"""

from __future__ import annotations

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from pathlib import Path
from typing import Dict, Any

from rule_engine import load_definitions, RuleEngine

app = FastAPI(title="OSINT Warning Dashboard Backend")

# Load indicator definitions at startup
definitions_path = Path(__file__).resolve().parent.parent / "data" / "indicator_definitions.yaml"
definitions = load_definitions(definitions_path)
rule_engine = RuleEngine(definitions)


class Event(BaseModel):
    """Pydantic model for incoming events."""
    indicator_id: str
    payload: Dict[str, Any] = {}


@app.get("/indicators")
async def get_indicators() -> Dict[str, Any]:
    """Return all indicator definitions."""
    return {"indicators": list(definitions.values())}


@app.post("/event")
async def post_event(event: Event) -> Dict[str, Any]:
    """Evaluate an incoming event against the rule engine."""
    result = rule_engine.evaluate_event(event.dict())
    if not result.get('matched'):
        raise HTTPException(status_code=400, detail=result.get('reason'))
    return result
