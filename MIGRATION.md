# Relatório e Guia de Migração de Conteúdo

**Data da Migração:** Agosto de 2026  
**Origem:** Construtor de Sites Legado Hostinger (Zyro) — `https://www.jbritopensamentos.com.br`  
**Destino:** Arquivos Markdown (`content/posts/*.md`) no repositório do projeto  

---

## 1. Resumo da Migração

A extração de dados foi realizada com sucesso através do script automatizado em Python (`scripts/migrate.py`), que varreu a estrutura de páginas do site original e converteu todo o conteúdo editorial e histórico em arquivos Markdown formatados com metadados Frontmatter.

### 📄 Artigos e Páginas Extraídos (12 no total):

| Título Original | Slug | Data de Origem | Categoria / Descrição | Arquivo Gerado |
| :--- | :--- | :--- | :--- | :--- |
| **O Político** | `o-politico` | 12/02/1985 | Opinião / Ensaio Histórico | `content/posts/o-politico.md` |
| **Tancredo Tiradentes** | `tancredo-tiradentes` | 22/04/1985 | Artigo Histórico pós-morte de Tancredo | `content/posts/tancredo-tiradentes.md` |
| **Nossa Vida** | `nossa-vida` | 08/05/2024 | Reflexão sobre responsabilidade e fé | `content/posts/nossa-vida.md` |
| **Os Obstáculos** | `os-obstaculos` | 08/05/2024 | Reflexão sobre perseverança e propósito | `content/posts/os-obstaculos.md` |
| **Salve o Brasil** | `artigosblog01` | 08/05/2024 | Apelo cívico contra a corrupção | `content/posts/artigosblog01.md` |
| **Angústrias** | `angustias` | 14/10/2025 | Poesia / Família e distância | `content/posts/angustias.md` |
| **Feliz Natal e Ano Novo** | `feliz-natal-e-ano-novo` | 13/12/2025 | Mensagem de Felicitações Natalinas | `content/posts/feliz-natal-e-ano-novo.md` |
| **O Homem de Mola** | `o-homem-de-mola-copy` | 18/10/2025 | Pensamentos e Reflexões | `content/posts/o-homem-de-mola-copy.md` |
| **Pensamentos** | `pensamentos` | 14/10/2025 | Frases e Pensamentos Diversos | `content/posts/pensamentos.md` |
| **Sobre o Autor** | `sobre` | — | Perfil Biográfico de João de Brito | `content/posts/sobre.md` |
| **Vídeos & Músicas** | `videos` | — | Catálogo Multimídia e composições | `content/posts/videos.md` |
| **Índice do Blog** | `artigos` | — | Estrutura de Listagem de Artigos | `content/posts/artigos.md` |

---

## 2. Estrutura dos Arquivos Markdown Gerados

Cada postagem segue o seguinte padrão Frontmatter em YAML:

```markdown
---
title: "Título da Postagem"
date: "YYYY-MM-DDTHH:MM:SS.000Z"
slug: "slug-da-url"
author: "João de Brito Freires"
source_url: "https://www.jbritopensamentos.com.br/slug"
---

# Título da Postagem

[Corpo do texto formatado em parágrafos Markdown...]
```

---

## 3. Como o Hermes Agent gerenciará novas postagens

Para incluir uma nova postagem no futuro, você só precisa solicitar ao **Hermes Agent** em linguagem natural:

> *"Hermes, adicione um novo artigo intitulado 'A Força do Trabalho' na categoria 'Pensamentos'."*

O Hermes Agent criará automaticamente o arquivo `.md` correspondente na pasta `content/posts/`, executará o `git commit` e enviará ao repositório GitHub. O **Easypanel** na sua VPS Hostinger detectará o update e recompilará o site em questão de segundos.
