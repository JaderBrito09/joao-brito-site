# PDR - Plano de Desenvolvimento e Redesign (Product Requirements Document)
## Website Oficial e Blog: João de Brito Freires

**Domínio Oficial:** [www.jbritopensamentos.com.br](https://www.jbritopensamentos.com.br)  
**Data de Atualização:** Agosto de 2026  
**Status do Projeto:** Fase de Implementação, Migração e Deploy em VPS  
**Infraestrutura:** VPS Hostinger com Easypanel (Docker)  
**Gestão de Conteúdo:** Workflow GitOps alimentado pelo **Hermes Agent**  

---

## 1. Visão Geral & Objetivos do Projeto

### 1.1 Objetivo Principal
Reformular integralmente a presença digital de **João de Brito Freires**, transformando o site legado criado no construtor da Hostinger num **Portal/Blog Editorial Moderno, Responsivo e Orientado a Conteúdo**, hospedado em VPS própria via **Easypanel** e gerenciado de forma autônoma pelo **Hermes Agent**.

### 1.2 Objetivos Secundários
* **Valorizar a Identidade do Autor:** Evidenciar a trajetória multifacetada de João de Brito Freires como ex-assessor na Câmara Federal, fundador e ex-presidente partidário em Goiás por 10 anos, empresário, escritor e compositor de mais de 40 músicas registradas.
* **Organização do Acervo Histórico e Cultural:** Categorizar adequadamente artigos de opinião recente e ensaios históricos datados a partir de 1985 (como a crônica sobre Tancredo Neves e ensaios sobre a vocação política).
* **Experiência Multimídia Integradora:** Dar destaque aos vídeos do YouTube, músicas gravadas, declamações de poesia e registros em áudio.
* **Manutenção Autônoma via AI (Hermes Agent):** Eliminar a necessidade de um CMS pesado (como WordPress). O Hermes Agent cria, formata, revisa e publica novos artigos diretamente em arquivos Markdown no Git.
* **Zero Custo de Licenciamento & Desempenho Extremo:** Conteúdo estático compilado/servido por contêiner ultraleve em Docker/Nginx via Easypanel.

---

## 2. Diagnóstico & Estratégia de Migração do Site Legado

### 2.1 Matriz de Comparação

| Aspecto | Situação Atual (Legado Zyro/Hostinger) | Solução Proposta no Redesign |
| :--- | :--- | :--- |
| **Estética & Layout** | Layout genérico de construtor de site com blocos desalinhados e falta de hierarquia tipográfica. | Design editorial estilo *Substack / Medium / Ghost* com tipografia *Playfair Display* e *Inter*. |
| **Hospedagem & Controle** | Construtor proprietário travado da Hostinger. | VPS própria na Hostinger gerenciada via **Easypanel (Docker Container)**. |
| **Publicação de Conteúdo** | Painel WYSIWYG lento do construtor de páginas. | **Hermes Agent GitOps:** Publicação via Markdown (`content/posts/*.md`) com re-deploy automático via Webhook do Easypanel. |
| **Organização do Blog** | Listagem plana de artigos sem filtro ou busca por categoria. | Sistema de abas com filtros (*Política*, *Pensamentos*, *Acervo Histórico*, *Músicas*). |
| **Multimídia** | Vídeos e áudios soltos na página sem contexto. | Player integrado com playlist estilizada e marcadores de categoria. |
| **Navegação Mobile** | Desproporcional em telas pequenas. | Layout 100% responsivo com abordagem *Mobile-First* e suporte a Dark Mode. |

### 2.2 Migração de Conteúdo Concluída
Todos os artigos, crônicas e páginas do site original foram extraídos e convertidos em arquivos Markdown padronizados com metadados Frontmatter no repositório (`content/posts/`):
* `o-politico.md` (1985 - Crônica política histórica)
* `tancredo-tiradentes.md` (1985 - Ensaio sobre a morte de Tancredo Neves)
* `nossa-vida.md` (Reflexão sobre responsabilidade e fé)
* `os-obstaculos.md` (Reflexão sobre perseverança e superação)
* `artigosblog01.md` ("Salve o Brasil" - Apelo contra a corrupção)
* `angustias.md` (Poesia e reflexão sobre família)
* `feliz-natal-e-ano-novo.md` (Mensagens natalinas)
* `o-homem-de-mola-copy.md` (Pensamentos diversos)
* `pensamentos.md` (Acervo de frases e reflexões)
* `sobre.md` (Trajetória biográfica do autor)
* `videos.md` (Catálogo de vídeos e composições)
* `artigos.md` (Índice de postagens)

---

## 3. Arquitetura da Solução & Workflow de Publicação

```text
  [ Usuário / Autor ]
         │ (Informa novo artigo / alteração)
         ▼
  [ Hermes Agent ] ──────────► Cria/Edita Markdown (`content/posts/artigo.md`)
         │
         ▼ (Git Commit & Push)
  [ Repositório GitHub / Git ]
         │
         ▼ (Webhook Trigger)
  [ VPS Hostinger + Easypanel ] ──► Auto Re-build Docker Container (Nginx/Astro)
         │
         ▼
  [ www.jbritopensamentos.com.br (HTTPS / Let's Encrypt) ]
```

---

## 4. Requisitos do Sistema

### 4.1 Requisitos Funcionais (RF)
* **RF-01:** O site deve renderizar os artigos a partir dos arquivos Markdown localizados na pasta `content/posts/`.
* **RF-02:** O leitor deve conseguir alternar entre o modo claro (*Light*) e escuro (*Dark*).
* **RF-03:** O site deve categorizar visualmente os artigos novos e os documentos históricos (década de 80).
* **RF-04:** O formulário de contato deve validar nome, e-mail e mensagem e enviar dados ao endpoint configurado no `.env`.
* **RF-05:** O bloco multimídia deve permitir a reprodução direta de vídeos do YouTube e links de áudio.
* **RF-06 (Hermes Agent GitOps):** O sistema deve aceitar atualização automática e re-deploy no Easypanel a cada `git push` realizado pelo Hermes.

### 4.2 Requisitos Não-Funcionais (RNF)
* **RNF-01 (Desempenho):** O tempo de carregamento da página deve ser inferior a 1,5 segundos (Pontuação Lighthouse > 90).
* **RNF-02 (Acessibilidade):** Contraste tipográfico adequado (WCAG AA) e suporte a leitores de tela.
* **RNF-03 (SEO):** Metatags OpenGraph e Twitter Cards configuradas para compartilhamento em redes sociais e WhatsApp.
* **RNF-04 (Segurança):** Zero banco de dados exposto; SSL HTTPS automático provido pelo Nginx/Easypanel.

---

## 5. Guia de Estilo (Design System)

### 5.1 Paleta de Cores
* **Azul Nobre / Institucional:** `#1d4ed8` (Blue 600) e `#0f172a` (Slate 900) — Credibilidade e política.
* **Âmbar Histórico:** `#d97706` (Amber 600) — Destaque para acervo de 1985 e poesia.
* **Verde Cívico:** `#059669` (Emerald 600) — Mensagens cívicas e republicanas.
* **Fundo Claro:** `#f8fafc` (Slate 50) | **Fundo Escuro:** `#020617` (Slate 950).

### 5.2 Tipografia
* **Títulos e Cabeçalhos:** *Playfair Display* (Serif) — Tom jornalístico e editorial.
* **Corpo de Texto e Interface:** *Inter* (Sans-Serif) — Máxima legibilidade.

---

## 6. Variáveis de Ambiente (`.env`)

O projeto utiliza variáveis de ambiente centralizadas para configuração no Easypanel:
* `PORT`: Porta do contêiner Docker (Padrão: `80`).
* `SITE_URL`: URL base do site (`https://www.jbritopensamentos.com.br`).
* `CONTACT_FORM_ENDPOINT`: Webhook/endpoint para recebimento de formulário de contato.
* `NEWSLETTER_ENDPOINT`: Webhook/API para cadastro de leitores na newsletter.
* `EASYPANEL_WEBHOOK_URL`: URL do webhook do Easypanel para trigger manual de deploy.
