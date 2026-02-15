# 🎭 Playwright Pytest – E2E e API

Projeto de automação com **testes E2E** (Playwright) e **testes de API** (requests + pytest), alinhado à documentação de casos de teste em `docs/`.

---

## 📖 Como funciona o projeto

Este repositório reúne **dois tipos de automação** em um único projeto: testes que simulam o uso do navegador (**E2E**) e testes que chamam APIs HTTP diretamente (**API**). Tudo é executado pelo **pytest**.

### Onde está cada tipo de teste

| Tipo | Ferramenta | Pasta | O que testa |
|------|------------|--------|-------------|
| **E2E** | Playwright (pytest-playwright) | `playwright/e2e/` | Fluxos na interface (ex.: Amazon.com.br – busca de livro) |
| **API** | requests + pytest | `playwright/api/` | Endpoints REST (ex.: JSONPlaceholder – GET/POST `/posts`) |

Os testes **E2E** ficam em `playwright/e2e/` porque usam browser (Playwright). Os testes **API** ficam em `playwright/api/` porque não usam interface gráfica — apenas chamadas HTTP. Assim fica claro o que é cada coisa e fácil rodar só um tipo.

### Fluxo de uso

1. **Documentação primeiro** — Os casos de teste (CT001, CT002, etc.) estão descritos em `docs/`: `test-cases-e2e.md` (E2E) e `test-cases-api.md` (API). O código em `playwright/e2e/` e `playwright/api/` segue essa documentação.
2. **Um comando roda tudo** — `pytest` executa E2E e API. Você pode rodar só E2E (`pytest -m e2e`), só API (`pytest -m api`) ou por pasta/arquivo.
3. **Configuração central** — O `pytest.ini` na raiz define o `pythonpath` e as **markers** (`e2e` e `api`) para filtrar testes.

### Markers (filtrar o que rodar)

| Marker | Uso | Exemplo |
|--------|-----|--------|
| `e2e` | Apenas testes E2E (browser) | `pytest -m e2e` |
| `api` | Apenas testes de API (HTTP) | `pytest -m api` |

**Resumo:** `docs/` = *o quê* testar; `playwright/e2e/` = testes de interface; `playwright/api/` = testes de API; `pytest` orquestra a execução. Instale as dependências, rode `playwright install` se for executar E2E, e use `pytest` (ou `pytest -m e2e` / `pytest -m api`) para rodar os testes.

---

## 📋 Pré-requisitos

- Python 3.11+
- pip
- Acesso à internet (para Amazon.com.br e JSONPlaceholder)

## 🚀 Instalação

```bash
# Clone o repositório
git clone <url-do-repositorio>
cd playwright-pytest

# Instale as dependências
pip install -r requirements.txt

# Browsers (necessário apenas para testes E2E)
playwright install
```

## 🧪 Executando os Testes

```bash
# Todos os testes (E2E + API)
pytest

# Apenas testes E2E (browser)
pytest -m e2e

# Apenas testes de API (sem abrir browser)
pytest -m api

# Com relatório detalhado
pytest -v

# Por pasta
pytest playwright/e2e/ -v          # só E2E
pytest playwright/api/ -v          # só API

# E2E em modo visual (headed)
pytest playwright/e2e/test_amazon_busca_livro.py -v --headed

# Testes de API (JSONPlaceholder /posts)
pytest playwright/api/test_api_posts.py -v

# Teste específico
pytest playwright/e2e/test_amazon_busca_livro.py::test_ct001_busca_livro_com_sucesso -v --headed
pytest playwright/api/test_api_posts.py::test_ct001_get_posts_status_200 -v
```

**Dica:** Para validar só a API (mais rápido, sem browser), use `pytest -m api` ou `pytest playwright/api/`.

## 📚 Documentação dos Casos de Teste

| Documento | Descrição | Arquivo de teste |
|-----------|-----------|------------------|
| **[docs/test-cases-e2e.md](docs/test-cases-e2e.md)** | E2E Amazon.com.br – busca de livro, fluxo de compra | `playwright/e2e/test_amazon_busca_livro.py` |
| **[docs/test-cases-api.md](docs/test-cases-api.md)** | API JSONPlaceholder – GET/POST `/posts` | `playwright/api/test_api_posts.py` |

### Testes E2E (Amazon)

- **Ambiente:** `https://www.amazon.com.br/`
- **CT001:** Busca do livro com sucesso (acesso, busca, resultados, página do produto).
- Detalhes e demais casos: [docs/test-cases-e2e.md](docs/test-cases-e2e.md).

### Testes de API (JSONPlaceholder)

- **Base URL:** `https://jsonplaceholder.typicode.com` — recurso `/posts`
- **CT001–CT002:** GET `/posts` (status 200, JSON, lista, campos obrigatórios e tipos).
- **CT003–CT005:** POST `/posts` (status 201, massa aleatória, id e estrutura da resposta).
- Detalhes: [docs/test-cases-api.md](docs/test-cases-api.md).

## 📁 Estrutura do Projeto

```
playwright-pytest/
├── docs/
│   ├── test-cases-e2e.md              # Casos de teste E2E – Amazon
│   └── test-cases-api.md              # Casos de teste API – JSONPlaceholder
├── playwright/
│   ├── e2e/                            # Testes E2E (browser)
│   │   └── test_amazon_busca_livro.py # CT001 E2E (busca livro)
│   └── api/                            # Testes de API (HTTP)
│       └── test_api_posts.py           # CT001–CT005 API (/posts)
├── prompts/
│   └── sdet-automator.prompt.md       # Fluxo SDET (exploração + implementação)
├── requirements.txt
├── pytest.ini
└── README.md
```

- **`playwright/e2e/`** — testes que usam o navegador (Playwright). Exige `playwright install`.
- **`playwright/api/`** — testes que só fazem requisições HTTP. Não precisa de browser.

## 🔧 Configuração

### pytest.ini

```ini
[pytest]
pythonpath = .
markers =
    e2e: end-to-end test (browser/UI)
    api: API test (HTTP requests)
```

- **`e2e`** — testes em `playwright/e2e/` (interface com Playwright).
- **`api`** — testes em `playwright/api/` (chamadas HTTP com requests).

### Variáveis de ambiente (opcional)

- Para E2E: uso de URL base ou headless pode ser configurado conforme necessidade.
- Para API: a base URL do JSONPlaceholder está fixa no código; pode ser externalizada se desejar.

## 🐛 Debug

```bash
# Modo debug com Playwright Inspector (E2E)
PWDEBUG=1 pytest playwright/e2e/test_amazon_busca_livro.py

# Screenshots e vídeos (E2E)
pytest playwright/e2e/test_amazon_busca_livro.py --screenshot on --video on
```

## 🔄 CI (GitHub Actions)

O projeto está configurado para rodar no **GitHub Actions**:

- **Workflow:** `.github/workflows/ci.yml`
- **Gatilhos:** push e pull request nas branches `main` e `master`
- **Passos:** checkout → Python 3.11 → cache pip → `pip install -r requirements.txt` → `playwright install --with-deps` → `pytest -v`

Não é necessário configurar secrets para os testes atuais (E2E na Amazon e API no JSONPlaceholder).

## 📦 Dependências

- **pytest** – execução dos testes
- **pytest-playwright** – testes E2E no browser
- **playwright** – automação de browser
- **requests** – chamadas HTTP nos testes de API

Definidas em `requirements.txt`.

---

## 🤖 Respostas do Desafio Técnico

### Questão 4 – Inteligência Artificial

**1. Quais aspectos você avaliaria ao testar uma aplicação similar ao ChatGPT ([chatgpt.com](https://chatgpt.com/))?**

Ao testar uma aplicação baseada em IA, eu avaliaria:

Quando se trata de utilização de IA tenho algumas considerações a serem avaliadas e respeitadas. A principal é **se ela está criando a mais do que se é pedido** (por exemplo: uma pessoa com 6 dedos ou braço a mais, ou código duplicado no caso do mundo dev). Outros fatores são a **performance**, o **desempenho** e também a **segurança**.

---

### Uso de IA no Processo de QA

**1. Qual ferramenta ou técnica de IA foi utilizada?**  
*(Ex: TestRigor, Mabl, Applitools com IA visual, ChatGPT para geração de testes)*

As questões 1 e 2 foram respondidas com auxílio da IA através da IDE **Cursor**. O programa é derivado do VS Code e tem uma inteligência artificial integrada que auxilia (via chat), inclusive refatorando código ou testando manualmente (SIM, você pode configurar pra IA testar manualmente os cenários antes de automatizar).

**2. Para qual propósito a IA foi aplicada?**  
*(Ex: geração automática de casos de teste, detecção de falhas visuais, automação de scripts)*

Além dos exemplos citados acima, conforme poderá ver no código e nos scripts de automação, a IA foi aplicada para fazer uma **exploração e análise inteligente** do caso de teste e somente depois disso começar a codificar os testes automatizados. Caso algo dê errado no caminho, ela procura alternativas (de acordo com o ranking de correção disponibilizado).

Isso permitiu mais confiabilidade na criação da automatização dos testes.

**3. Como a IA impactou o processo de QA e os resultados obtidos?**

Os pontos principais foram:

- **Redução do tempo** na criação de código
- **Aumento da estabilidade** dos testes (evitando seletores frágeis)
- Possibilidade de **focar em lapidar a arquitetura** dos testes de imediato
