# 📄 Documentação de Testes – Amazon E2E

---

## 🌐 Ambiente e Dados de Teste

### URL do Sistema

- **Ambiente de Testes:** `https://www.amazon.com.br/`

---

## 📚 Produto Alvo

| Campo | Valor |
|-------|-------|
| **Título** | AI Engineering: Building Applications with Foundation Models |
| **Autor Esperado** | Chip Huyen |
| **Idioma** | Inglês |
| **Formato** | Livro físico |
| **Condição** | Novo |

---

# 🧪 Casos de Teste: Fluxo de Compra – Amazon

---

## 👤 História do Usuário

Como cliente da Amazon  
Quero buscar um livro específico  
Para adicioná-lo ao carrinho garantindo que estou comprando a versão correta  

---

## ✅ Critérios de Aceite

1. O sistema deve permitir buscar o livro pelo nome completo.
2. O produto selecionado deve corresponder exatamente ao título informado.
3. O autor deve ser **Chip Huyen**.
4. O idioma deve ser **Inglês**.
5. O formato deve ser **livro físico** (capa comum ou hardcover).
6. O produto deve estar na condição **novo**.
7. Ao adicionar ao carrinho, a mensagem exibida deve ser exatamente:
   **“Adicionado ao carrinho”**

---

## 📌 Pré-condições

- Ambiente configurado com Playwright.
- Usuário não precisa estar logado previamente.

---

## 🧪 CT001: Busca do Livro com Sucesso

### 🎯 Objetivo
Validar que o usuário consegue localizar o livro desejado através da busca.

| Passo | Ação | Resultado Esperado |
|-------|------|-------------------|
| 1 | Acessar a URL https://www.amazon.com.br/ | Página inicial carregada com sucesso |
| 2 | Preencher o campo de busca com “AI Engineering: Building Applications with Foundation Models” | Campo preenchido corretamente |
| 3 | Clicar no botão de busca | Lista de resultados exibida |
| 4 | Selecionar o livro correspondente | Página do produto aberta |

---

## 🧪 CT002: Validação das Informações do Produto

### 🎯 Objetivo
Garantir que o produto selecionado atende aos requisitos especificados.

| Validação | Resultado Esperado |
|-----------|-------------------|
| Título | Deve corresponder ao texto buscado |
| Autor | Deve ser Chip Huyen |
| Idioma | Deve ser Inglês |
| Formato | Deve ser livro físico |
| Condição | Deve estar como Novo |

---

## 🧪 CT003: Adicionar Produto ao Carrinho

### 🎯 Objetivo
Validar que o produto correto pode ser adicionado ao carrinho.

| Passo | Ação | Resultado Esperado |
|-------|------|-------------------|
| 1 | Clicar em “Adicionar ao carrinho” | Produto adicionado ao carrinho |
| 2 | Validar mensagem exibida | A mensagem deve ser exatamente “Adicionado ao carrinho” |

---

## 🧪 CT004: Validação da Mensagem de Confirmação

### 🎯 Objetivo
Garantir que o feedback ao usuário está correto.

| Validação | Resultado Esperado |
|-----------|-------------------|
| Texto da notificação | “Adicionado ao carrinho” (exatamente igual, incluindo acentuação) |
| Visibilidade | Mensagem visível na tela |
| Contexto | Mensagem associada ao produto adicionado |

---

# 📊 Estratégia de Automação

- Utilizar seletores robustos (data-testid, roles ou atributos estáveis).
- Implementar espera explícita para elementos dinâmicos.
- Validar textos com correspondência exata.
- Evitar uso de waits fixos (ex: sleep).
- Estruturar código seguindo boas práticas (ex: Page Object Model).

---

# 📌 Observações

- Caso existam múltiplas edições do livro, deve-se selecionar especificamente a edição que atenda aos critérios definidos.
- O teste deve ser resiliente a pequenas variações de layout.
- O teste deve falhar caso qualquer uma das validações não seja atendida.
