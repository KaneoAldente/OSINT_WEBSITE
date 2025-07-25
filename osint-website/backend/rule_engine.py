"""
Simple rule engine for OSINT indicators.

This module loads indicator definitions from a YAML file and provides
a function to evaluate incoming events against those definitions. The
evaluation in this example is rudimentary: it checks if the event
contains an indicator ID and, if so, constructs a dummy confidence
score and recommendation. In a real implementation, the event would
contain rich data (SAR images, AIS messages, etc.) and the rule engine
would perform threshold comparisons, statistical anomaly detection,
and Bayesian updating.
"""

from __future__ import annotations

import yaml
from pathlib import Path
from typing import Any, Dict, Optional, List


def load_definitions(path: Path) -> Dict[str, Dict[str, Any]]:
    """Load indicator definitions from a YAML file into a dictionary keyed by ID."""
    with path.open('r', encoding='utf-8') as f:
        data = yaml.safe_load(f)
    indicators = data.get('indicators', [])
    return {ind['id']: ind for ind in indicators}


class RuleEngine:
    """Rule engine that evaluates events against indicator definitions."""

    def __init__(self, definitions: Dict[str, Dict[str, Any]]):
        self.definitions = definitions

    def evaluate_event(self, event: Dict[str, Any]) -> Dict[str, Any]:
        """
        Evaluate a single event.  The event is expected to contain an
        'indicator_id' field referencing one of the definitions. The
        engine returns a dictionary with the matched indicator ID,
        description, a dummy confidence score (for demonstration), and
        a recommended next task.  In a real system the event would
        contain raw sensor data and the rule engine would implement
        threshold logic.
        """
        ind_id = event.get('indicator_id')
        definition = self.definitions.get(ind_id)
        if not definition:
            return {
                'matched': False,
                'reason': f"Unknown indicator ID: {ind_id}",
            }
        # Dummy confidence: the more signals, the higher the base confidence
        signals: List[str] = definition.get('data_signals', [])
        base_confidence = min(0.9, 0.3 + 0.1 * len(signals))
        # You could incorporate event metadata here to adjust the confidence
        result = {
            'matched': True,
            'indicator_id': ind_id,
            'description': definition.get('description'),
            'confidence': round(base_confidence, 2),
            'recommended_task': self._recommend_next_task(definition)
        }
        return result

    def _recommend_next_task(self, definition: Dict[str, Any]) -> str:
        """Construct a simple recommended next task based on the PIR and COA."""
        pir = definition.get('pir')
        coa = definition.get('coa')
        if pir == 1 and coa == 'mlcoa':
            return "Increase diplomatic and HUMINT monitoring; verify with additional travel data."
        if pir == 2 and coa == 'mdcoa':
            return "Task SAR imagery on key Rocket Force bases and highways; alert cyber team."
        if pir == 2 and coa == 'mlcoa':
            return "Monitor AIS for further Coast Guard movements; cross‑cue SAR for dark ships."
        if pir == 3:
            return "Cross‑check with NOTAMs and cyber telemetry; brief analysis section."
        return "Gather more data and consult analyst."