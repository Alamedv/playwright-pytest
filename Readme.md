# 🎭 Playwright Pytest – E2E e API

Projeto de automação com **testes E2E** (Playwright) e **testes de API** (requests + pytest), alinhado à documentação de casos de teste em `docs/`.

---

## 📖 Como funciona o projeto

Dois tipos de automação em um único projeto: testes no navegador (**E2E**) e testes de API (**HTTP**). Tudo roda com **pytest**.

| Tipo | Ferramenta | Pasta | O que testa |
|------|------------|--------|-------------|
| **E2E** | Playwright | `playwright/e2e/` | Interface (ex.: Amazon.com.br – busca de livro) |
| **API** | requests + pytest | `playwright/api/` | REST (ex.: JSONPlaceholder – GET/POST `/posts`) |

- **Documentação:** casos de teste em `docs/test-cases-e2e.md` e `docs/test-cases-api.md`; o código segue essa documentação.
- **Execução:** `pytest` roda tudo; use `pytest -m e2e` (só E2E) ou `pytest -m api` (só API).
- **Configuração:** `pytest.ini` define `pythonpath` e os markers `e2e` e `api`.

---

## 📋 Pré-requisitos e instalação

- Python 3.11+
- pip
- Acesso à internet (para Amazon.com.br e JSONPlaceholder)

## 🚀 Instalação

```bash
git clone <url-do-repositorio>
cd playwright-pytest
pip install -r requirements.txt
playwright install   # só para testes E2E
```

---

## 🧪 Executando os testes

```bash
pytest                    # todos
pytest -m e2e            # só E2E
pytest -m api             # só API (rápido, sem browser)
pytest -v                 # verboso
pytest playwright/e2e/ -v
pytest playwright/api/test_api_posts.py -v

python -m pytest playwright/e2e/test_amazon_busca_livro.py -v --headed | *comando alternativo*


```

E2E em modo visual: `pytest playwright/e2e/test_amazon_busca_livro.py -v --headed`

---

## 📊 Relatório Allure

Cada execução do `pytest` grava resultados em `allure-results/` (configurado no `pytest.ini`). O relatório em HTML é gerado a partir dessa pasta.

### Ver localmente

1. **Instale o Allure CLI:** `scoop install allure` ou `choco install allure` (Windows), `brew install allure` (Mac), ou [releases](https://github.com/allure-framework/allure2/releases).
2. Depois de rodar `pytest`, abra o relatório: **`allure serve allure-results`** (sobe um servidor e abre no navegador).
3. Alternativa: `allure generate allure-results -o allure-report --clean` e depois `allure open allure-report`.

Não abra o `index.html` com duplo clique (ficará em "Loading..." por restrições do navegador). Use sempre `allure serve` ou `allure open`.

### Ver no CI (GitHub Actions)

- **URL pública (GitHub Pages):** `https://<SEU_USUARIO>.github.io/<NOME_DO_REPOSITORIO>/` - Por exemplo: https://alamedv.github.io/playwright-pytest/  
  Ative em **Settings → Pages → Source: GitHub Actions**. O relatório é atualizado a cada push em `main`/`master`.
- **Artefatos:** em **Actions** → execução → **Artifacts** baixe **allure-report** ou **allure-results** (disponíveis 14 dias).

| Se você tem… | Como visualizar |
|--------------|-----------------|
| Pasta **allure-results** (local ou descompactada) | `allure serve .` na pasta |
| Pasta **allure-report** (descompactada) | Na pasta: `python -m http.server 8800` e acesse http://localhost:8800. Não abra `index.html` direto. |

As pastas `allure-results/` e `allure-report/` estão no `.gitignore`.

---

## 📚 Casos de teste e estrutura

| Documento | Descrição | Código |
|-----------|-----------|--------|
| [docs/test-cases-e2e.md](docs/test-cases-e2e.md) | E2E Amazon.com.br – busca de livro | `playwright/e2e/test_amazon_busca_livro.py` |
| [docs/test-cases-api.md](docs/test-cases-api.md) | API JSONPlaceholder – GET/POST `/posts` | `playwright/api/test_api_posts.py` |

```
playwright-pytest/
├── docs/           # Casos de teste (E2E e API)
├── playwright/
│   ├── e2e/        # Testes no browser (Playwright)
│   └── api/        # Testes HTTP (requests)
├── prompts/
├── requirements.txt
├── pytest.ini
└── README.md
```

---

## 🔧 Configuração

**pytest.ini:** `pythonpath`, markers `e2e` e `api`, e `--alluredir=allure-results --clean-alluredir` (para o relatório Allure).

**Variáveis de ambiente (opcional):** URL base ou headless para E2E; base URL da API pode ser externalizada no código.

---

## 🐛 Debug

```bash
PWDEBUG=1 pytest playwright/e2e/test_amazon_busca_livro.py
pytest playwright/e2e/test_amazon_busca_livro.py --screenshot on --video on
```

---

## 🔄 CI (GitHub Actions)

**Workflow:** `.github/workflows/ci.yml` — push/PR em `main` e `master`. Passos: checkout, Python 3.11, dependências, Playwright, `pytest`, geração do Allure Report, upload de artefatos e deploy no GitHub Pages (em push em `main`/`master`).

Sem secrets necessários para os testes atuais. Para o relatório em URL pública, ative **Settings → Pages → Source: GitHub Actions** (detalhes na seção [Relatório Allure](#-relatório-allure)).

---

## 📦 Dependências

- **pytest** – execução dos testes
- **pytest-playwright** – testes E2E no browser
- **playwright** – automação de browser
- **requests** – chamadas HTTP nos testes de API
- **allure-pytest** – geração dos resultados para o relatório Allure

Definidas em `requirements.txt`.

---

## 🤖 Respostas do Desafio Técnico

### Questão 4 – Inteligência Artificial

**1. Quais aspectos você avaliaria ao testar uma aplicação similar ao ChatGPT ([chatgpt.com](https://chatgpt.com/))?**

R: Ao testar uma aplicação baseada em IA, eu avaliaria:

Quando se trata de utilização de IA eu tenho algumas considerações a serem avaliadas e respeitadas. A principal é se ela está criando a mais do que se é pedido (uma pessoa com 6 dedos ou braço a mais. Ou codigo duplicado no caso do mundo dev). Outros fatores são a performance, desempenho e também a segurança.

---

### Uso de IA no Processo de QA

**1. Qual ferramenta ou técnica de IA foi utilizada?**  
*(Ex: TestRigor, Mabl, Applitools com IA visual, ChatGPT para geração de testes)*

R: As questões 1 e 2 foram respondidas com auxilio da IA através da IDE chamada CURSOR. Esse programa é derivado do VS code e tem uma inteligencia artificial integrada que auxilia (via chat) inclusive refatorando código ou testando manualmente (sim, você pode configurar pra IA testar manualmente os cenários antes de automatizar).


**2. Para qual propósito a IA foi aplicada?**  
*(Ex: geração automática de casos de teste, detecção de falhas visuais, automação de scripts)*

R: Além dos exemplos citados acima, conforme poderá ver no código o script de automação, a IA foi aplicada pra fazer uma exploração e uma análise inteligente do caso de teste e somente depois disso começar a códigos para testes automatizados. Caso algo dê errado no caminho, ela vai procurando alternativas (de acordo com o ranking que foi disponibilizado de correção). 

Isso permitiu mais confiabilidade na criação da automatização dos testes.


**3. Como a IA impactou o processo de QA e os resultados obtidos?**

R: Os pontos principais foram a redução do tempo na criação de código. Aumento da estabilidade dos testes (ao evitar seletores frágeis). Com isso pude focar em lapidar a arquitetura dos testes de imediato.
