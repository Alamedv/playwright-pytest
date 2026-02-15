# 📄 Documentação de Testes – API JSONPlaceholder

---

## 🌐 Ambiente e Dados de Teste

### URL da API

- **Base URL:** `https://jsonplaceholder.typicode.com`
- **Recurso:** `/posts`

---

## 📌 Informações Gerais

API pública utilizada para testes e simulações.  
Não requer autenticação e retorna dados mockados.

---

# 🧪 Casos de Teste – API /posts

---

## 👤 História do Usuário

Como desenvolvedor ou QA  
Quero validar os endpoints da API de posts  
Para garantir que as operações de consulta e criação funcionam corretamente  

---

## ✅ Critérios de Aceite

1. O endpoint GET `/posts` deve retornar status **200**.
2. O retorno do GET deve ser uma lista de objetos.
3. Cada objeto deve conter os campos obrigatórios:
   - userId
   - id
   - title
   - body
4. O endpoint POST `/posts` deve retornar status **201**.
5. O POST deve aceitar dados dinâmicos (massa aleatória).
6. A resposta do POST deve conter um **ID único** gerado pela API.
7. O ID retornado não deve ser nulo.

---

## 📌 Pré-condições

1. Python 3.x instalado.
2. Biblioteca `requests` disponível.
3. Biblioteca de testes (ex: `pytest`) configurada.
4. Acesso à internet.

---

## 🧪 CT001 – GET /posts com sucesso

### 🎯 Objetivo
Validar que o endpoint GET retorna os dados corretamente.

| Passo | Ação | Resultado Esperado |
|------|------|-------------------|
| 1 | Enviar requisição GET para `/posts` | Requisição executada com sucesso |
| 2 | Validar status code | Status **200** |
| 3 | Validar tipo da resposta | JSON |
| 4 | Validar estrutura | Lista de objetos |
| 5 | Validar campos obrigatórios | userId, id, title, body |

---

## 🧪 CT002 – Validação do conteúdo da resposta GET

### 🎯 Objetivo
Garantir a integridade dos dados retornados.

| Validação | Resultado Esperado |
|----------|-------------------|
| Quantidade de registros | Maior que 0 |
| Tipo de `id` | Numérico |
| Tipo de `userId` | Numérico |
| Tipo de `title` | String |
| Tipo de `body` | String |

---

## 🧪 CT003 – POST /posts com massa de dados aleatória

### 🎯 Objetivo
Validar a criação de um novo post via POST.

### 📥 Massa de Dados (Exemplo)

- userId: valor inteiro aleatório
- title: string gerada dinamicamente
- body: string gerada dinamicamente

| Passo | Ação | Resultado Esperado |
|------|------|-------------------|
| 1 | Gerar payload com dados aleatórios | Payload válido |
| 2 | Enviar requisição POST para `/posts` | Requisição executada |
| 3 | Validar status code | Status **201** |
| 4 | Validar retorno da API | JSON retornado |

---

## 🧪 CT004 – Validação do ID retornado no POST

### 🎯 Objetivo
Garantir que a API retorna um identificador único.

| Validação | Resultado Esperado |
|----------|-------------------|
| Campo `id` existe | Sim |
| Valor do `id` | Não nulo |
| Tipo do `id` | Numérico |
| ID gerado pela API | Sim |

---

## 🧪 CT005 – Validação da estrutura da resposta POST

### 🎯 Objetivo
Garantir que a resposta do POST contém todos os campos esperados.

| Campo | Resultado Esperado |
|------|-------------------|
| userId | Presente |
| title | Presente |
| body | Presente |
| id | Presente |

---

# 📊 Estratégia de Automação

- Utilizar a biblioteca `requests` para chamadas HTTP.
- Utilizar assertions claras para status code e estrutura.
- Implementar tratamento básico de erros.
- Evitar dependência entre testes.
- Gerar massa de dados dinâmica para o POST.
- Validar tipos e existência dos campos.

---

# 📌 Observações

- A API retorna dados mockados, porém os testes devem validar comportamento esperado.
- O ID retornado no POST é simulado, mas deve existir e ser único na resposta.
- O teste deve falhar caso qualquer validação não seja atendida.
