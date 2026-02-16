"""
CT001: Busca do Livro com Sucesso (Amazon.com.br)
Valida que o usuário consegue localizar o livro desejado através da busca.
"""
import re
import pytest
from playwright.sync_api import expect

BASE_URL = "https://www.amazon.com.br/"
BOOK_TITLE = "AI Engineering: Building Applications with Foundation Models"
EXPECTED_AUTHOR = "Chip Huyen"


@pytest.mark.e2e
def test_ct001_busca_livro_com_sucesso(page):
    # Passo 1: Acessar a URL → Página inicial carregada
    page.goto(BASE_URL)
    expect(page).to_have_url(re.compile(r"amazon\.com\.br"))
    expect(page).to_have_title(re.compile(r"Amazon\.com\.br"))

    # Passo 2: Preencher o campo de busca → Campo preenchido
    # Locator por role (independente do texto do placeholder/label que a Amazon exibe)
    searchbox = page.get_by_role("searchbox").first
    searchbox.fill(BOOK_TITLE)
    expect(searchbox).to_have_value(BOOK_TITLE)

    # Passo 3: Clicar no botão de busca → Lista de resultados exibida
    page.get_by_role("button", name="Ir", exact=True).click()
    expect(page).to_have_url(re.compile(r"keywords=|/s\?"))
    expect(page).to_have_title(re.compile(r"AI Engineering", re.I))

    # Passo 4: Selecionar o livro correspondente → Página do produto aberta
    page.get_by_role("link", name=BOOK_TITLE).first.click()
    expect(page).to_have_title(re.compile(r"AI Engineering: Building Applications with Foundation Models"))
    expect(page).to_have_title(re.compile(r"Amazon\.com\.br"))
    expect(page.get_by_role("link", name=EXPECTED_AUTHOR).first).to_be_visible()
