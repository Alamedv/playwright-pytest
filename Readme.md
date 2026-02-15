# 🎭 Playwright Pytest – E2E e API

Projeto de automação com **testes E2E** (Playwright) e **testes de API** (requests + pytest), alinhado à documentação de casos de teste em `docs/`.

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

# Apenas testes marcados como E2E
pytest -m e2e

# Com relatório detalhado
pytest -v

# E2E em modo visual (headed)
pytest playwright/e2e/test_amazon_busca_livro.py -v --headed

# Testes de API (JSONPlaceholder /posts)
pytest playwright/e2e/test_api_posts.py -v

# Teste específico
pytest playwright/e2e/test_amazon_busca_livro.py::test_ct001_busca_livro_com_sucesso -v --headed
pytest playwright/e2e/test_api_posts.py::test_ct001_get_posts_status_200 -v
```

## 📚 Documentação dos Casos de Teste

| Documento | Descrição | Arquivos de teste |
|-----------|-----------|-------------------|
| **[docs/test-cases.md](docs/test-cases.md)** | E2E Amazon.com.br – busca de livro, fluxo de compra | `playwright/e2e/test_amazon_busca_livro.py` |
| **[docs/test-cases-api.md](docs/test-cases-api.md)** | API JSONPlaceholder – GET/POST `/posts` | `playwright/e2e/test_api_posts.py` |

### Testes E2E (Amazon)

- **Ambiente:** `https://www.amazon.com.br/`
- **CT001:** Busca do livro com sucesso (acesso, busca, resultados, página do produto).
- Detalhes e demais casos: [docs/test-cases.md](docs/test-cases.md).

### Testes de API (JSONPlaceholder)

- **Base URL:** `https://jsonplaceholder.typicode.com` — recurso `/posts`
- **CT001–CT002:** GET `/posts` (status 200, JSON, lista, campos obrigatórios e tipos).
- **CT003–CT005:** POST `/posts` (status 201, massa aleatória, id e estrutura da resposta).
- Detalhes: [docs/test-cases-api.md](docs/test-cases-api.md).

## 📁 Estrutura do Projeto

```
playwright-pytest/
├── docs/
│   ├── test-cases-e2e.md          # Casos de teste E2E – Amazon
│   └── test-cases-api.md      # Casos de teste API – JSONPlaceholder
├── playwright/
│   └── e2e/
│       ├── test_amazon_busca_livro.py   # CT001 E2E (busca livro)
│       └── test_api_posts.py            # CT001–CT005 API (/posts)
├── prompts/
│   └── sdet-automator.prompt.md        # Fluxo SDET (exploração + implementação)
├── requirements.txt
├── pytest.ini
└── README.md
```

## 🔧 Configuração

### pytest.ini

```ini
[pytest]
pythonpath = .
markers =
    e2e: end-to-end test
```

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

As questões 1 e 2 foram respondidas com auxílio da IA através da IDE **Cursor**. O programa é derivado do VS Code e tem uma inteligência artificial integrada que auxilia (via chat), inclusive refatorando código ou testando manualmente — é possível configurar para a IA testar manualmente os cenários antes de automatizar.

**2. Para qual propósito a IA foi aplicada?**  
*(Ex: geração automática de casos de teste, detecção de falhas visuais, automação de scripts)*

Além dos exemplos citados acima, conforme poderá ver no código e nos scripts de automação, a IA foi aplicada para fazer uma **exploração e análise inteligente** do caso de teste e somente depois disso começar a codificar os testes automatizados. Caso algo dê errado no caminho, ela procura alternativas (de acordo com o ranking de correção disponibilizado).

Isso permitiu mais confiabilidade na criação da automatização dos testes.

**3. Como a IA impactou o processo de QA e os resultados obtidos?**

Os pontos principais foram:

- **Redução do tempo** na criação de código
- **Aumento da estabilidade** dos testes (evitando seletores frágeis)
- Possibilidade de **focar em lapidar a arquitetura** dos testes de imediato
