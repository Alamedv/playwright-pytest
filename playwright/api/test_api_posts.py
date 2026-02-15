"""
Casos de teste API JSONPlaceholder /posts (CT001–CT005).
Valida GET e POST conforme docs/test-cases-api.md.
"""
import random
import string
import pytest
import requests

BASE_URL = "https://jsonplaceholder.typicode.com"
POSTS_URL = f"{BASE_URL}/posts"
REQUIRED_FIELDS = ("userId", "id", "title", "body")


def _random_string(length=12):
    return "".join(random.choices(string.ascii_letters + string.digits, k=length))


# --- CT001: GET /posts com sucesso ---


@pytest.mark.api
def test_ct001_get_posts_status_200():
    """Passo 1–2: GET /posts executado com sucesso, status 200."""
    resp = requests.get(POSTS_URL)
    assert resp.status_code == 200


@pytest.mark.api
def test_ct001_get_posts_response_is_json():
    """Passo 3: Resposta é JSON."""
    resp = requests.get(POSTS_URL)
    assert resp.headers.get("content-type", "").startswith("application/json")
    resp.json()


@pytest.mark.api
def test_ct001_get_posts_response_is_list():
    """Passo 4: Resposta é lista de objetos."""
    data = requests.get(POSTS_URL).json()
    assert isinstance(data, list)


@pytest.mark.api
def test_ct001_get_posts_required_fields():
    """Passo 5: Cada objeto tem userId, id, title, body."""
    data = requests.get(POSTS_URL).json()
    assert len(data) > 0
    for item in data:
        for field in REQUIRED_FIELDS:
            assert field in item, f"Campo obrigatório ausente: {field}"


# --- CT002: Validação do conteúdo da resposta GET ---


@pytest.mark.api
def test_ct002_get_count_greater_than_zero():
    """Quantidade de registros > 0."""
    data = requests.get(POSTS_URL).json()
    assert len(data) > 0


@pytest.mark.api
def test_ct002_get_id_is_numeric():
    """Tipo de id é numérico."""
    data = requests.get(POSTS_URL).json()
    for item in data[:5]:
        assert isinstance(item["id"], (int, float))


@pytest.mark.api
def test_ct002_get_user_id_is_numeric():
    """Tipo de userId é numérico."""
    data = requests.get(POSTS_URL).json()
    for item in data[:5]:
        assert isinstance(item["userId"], (int, float))


@pytest.mark.api
def test_ct002_get_title_is_string():
    """Tipo de title é string."""
    data = requests.get(POSTS_URL).json()
    for item in data[:5]:
        assert isinstance(item["title"], str)


@pytest.mark.api
def test_ct002_get_body_is_string():
    """Tipo de body é string."""
    data = requests.get(POSTS_URL).json()
    for item in data[:5]:
        assert isinstance(item["body"], str)


# --- CT003: POST /posts com massa aleatória ---


def _post_random_payload():
    """Gera payload aleatório e envia POST."""
    payload = {
        "userId": random.randint(1, 999),
        "title": _random_string(20),
        "body": _random_string(80),
    }
    return requests.post(POSTS_URL, json=payload)


@pytest.mark.api
def test_ct003_post_status_201():
    """POST executado, status 201."""
    resp = _post_random_payload()
    assert resp.status_code == 201


@pytest.mark.api
def test_ct003_post_returns_json():
    """Resposta do POST é JSON."""
    resp = _post_random_payload()
    assert resp.headers.get("content-type", "").startswith("application/json")
    resp.json()


# --- CT004: Validação do ID retornado no POST ---


@pytest.mark.api
def test_ct004_post_id_exists_and_not_null():
    """Campo id existe e não é nulo."""
    resp = _post_random_payload()
    data = resp.json()
    assert "id" in data
    assert data["id"] is not None


@pytest.mark.api
def test_ct004_post_id_is_numeric():
    """Tipo do id é numérico."""
    resp = _post_random_payload()
    data = resp.json()
    assert isinstance(data["id"], (int, float))


# --- CT005: Estrutura da resposta POST ---


@pytest.mark.api
def test_ct005_post_response_has_all_fields():
    """Resposta contém userId, title, body, id."""
    resp = _post_random_payload()
    data = resp.json()
    for field in ("userId", "title", "body", "id"):
        assert field in data, f"Campo ausente na resposta POST: {field}"
