"""
Tests unitaires pour l'API Credit Scoring
"""

import requests
import pytest

# URL de l'API (à changer selon l'environnement)
API_URL = "https://projet7-credit-scoring-api.onrender.com"


def test_root_endpoint():
    """Test que l'endpoint racine répond"""
    response = requests.get(f"{API_URL}/")
    assert response.status_code == 200
    data = response.json()
    assert "message" in data
    assert data["status"] == "active"


def test_health_endpoint():
    """Test que l'endpoint health répond"""
    response = requests.get(f"{API_URL}/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "healthy"
    assert data["model_loaded"] == True


def test_predict_endpoint():
    """Test qu'on peut faire une prédiction"""
    client_data = {
        "data": {
            "EXT_SOURCES_MEAN": 0.65,
            "AMT_CREDIT": 300000,
            "AMT_INCOME_TOTAL": 200000
        },
        "client_id": "TEST_001"
    }
    
    response = requests.post(f"{API_URL}/predict", json=client_data)
    assert response.status_code == 200
    
    data = response.json()
    assert "client_id" in data
    assert "default_probability" in data
    assert "prediction" in data
    assert "risk_level" in data
    assert data["client_id"] == "TEST_001"


def test_predict_high_risk():
    """Test prédiction client à haut risque"""
    client_data = {
        "data": {
            "EXT_SOURCES_MEAN": 0.2,
            "AMT_CREDIT": 900000,
            "AMT_INCOME_TOTAL": 50000
        },
        "client_id": "TEST_RISK"
    }
    
    response = requests.post(f"{API_URL}/predict", json=client_data)
    assert response.status_code == 200
    
    data = response.json()
    # Le client à haut risque devrait avoir une probabilité élevée
    assert data["default_probability"] > 0.3


if __name__ == "__main__":
    print("Lancement des tests...")
    pytest.main([__file__, "-v"])
