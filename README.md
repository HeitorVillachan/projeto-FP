# 🏋️ HYROX Planner

Sistema de planejamento e acompanhamento de treinos para atletas de HYROX, desenvolvido em Python. Permite gerenciar treinos, exercícios e competições, visualizar a evolução do atleta e contar com sugestões personalizadas de um coach com IA.

---

## 📋 Funcionalidades

- **Treinos** — cadastrar, listar, buscar, editar e excluir sessões de treino
- **Exercícios** — registrar desempenho por exercício (carga, repetições, distância, tempo) ao longo do tempo
- **Competições** — agendar e gerenciar competições por local e categoria
- **Resumo de evolução** — relatórios de frequência de treinos, evolução por exercício e histórico de competições
- **IA Coach** — sugestões de treino personalizadas e chat interativo com um coach especialista em HYROX (via Ollama + LLaMA 3.2)
- **Persistência** — todos os dados são salvos automaticamente em arquivo `.txt` local

---

## 🗂️ Estrutura dos Dados

| Entidade     | Campos |
|--------------|--------|
| Treino       | ID, Nome, Tipo, Data, Duração (min), Intensidade |
| Exercício    | ID, Nome, Tempo (min), Distância (m), Carga (kg), Repetições, Data |
| Competição   | ID, Local, Categoria, Data |

Os dados são armazenados no arquivo `HYROX_Planner.txt`, criado automaticamente na primeira execução.

---

## 🚀 Como executar

### Pré-requisitos

- Python 3.8 ou superior

### Instalação e execução

```bash
# Clone o repositório ou copie o arquivo
git clone <url-do-repositorio>
cd hyrox-planner

# Execute o programa
python hyrox_planner.py
```

---

## 🤖 Funcionalidades com IA (opcional)

A IA utiliza o **Ollama** com o modelo **LLaMA 3.2** localmente. Para ativá-la:

### 1. Instale o Ollama

Acesse [https://ollama.com](https://ollama.com) e siga as instruções para o seu sistema operacional.

### 2. Baixe o modelo

```bash
ollama pull llama3.2
```

### 3. Instale a biblioteca Python

```bash
pip install ollama
```

### 4. Certifique-se que o Ollama está rodando

```bash
ollama serve
```

> Sem o Ollama, o programa funciona normalmente — apenas as funções de IA ficam indisponíveis.

---

## 🖥️ Menu Principal

```
MENU PRINCIPAL
1 - Treinos
2 - Exercícios
3 - Competições
4 - Resumo de Evolução
5 - Chat com IA HYROX
0 - Encerrar
```

---

## 📊 Relatórios disponíveis

- **Frequência de treinos** — total, por tipo, duração média e frequência semanal/mensal
- **Evolução dos exercícios** — comparação entre primeiro e último registro (carga, reps, distância, tempo)
- **Resumo de competições** — total, por categoria e lista de locais
- **Sugestão de treino com IA** — plano semanal personalizado com base no nível do atleta (iniciante / intermediário / avançado)

---

## 📁 Arquivo de dados

Os dados são salvos em `HYROX_Planner.txt` no mesmo diretório do script. O arquivo é atualizado automaticamente a cada operação e lido ao iniciar o programa.

---

## 🛠️ Tecnologias utilizadas

- **Python 3** — linguagem principal
- **Ollama** — execução local de modelos de linguagem
- **LLaMA 3.2** — modelo de IA para sugestões e chat
- **Biblioteca padrão** — `os`, `datetime`

---

## 📌 Observações

- As datas devem ser informadas no formato `DD/MM/AAAA`
- Campos numéricos (duração, carga, repetições etc.) aceitam apenas inteiros
- O programa valida todas as entradas e informa erros de formato
