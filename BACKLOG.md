# Product Backlog & Roadmap de Execução
## Website e Portal Editorial: João de Brito Freires

**Projeto:** Redesign e Hospedagem VPS (Hostinger + Easypanel + Hermes Agent)  
**Metodologia:** Sprints de Entrega Contínua via GitOps  

---

## 📊 Visão Geral dos Sprints

| Sprint | Foco Principal | Status |
| :--- | :--- | :--- |
| **Sprint 1** | Migração do Conteúdo Legado & Estrutura Markdown | 🟢 Concluído |
| **Sprint 2** | Infraestrutura Docker, GitHub, `.env` & Easypanel Setup | 🟢 Concluído |
| **Sprint 3** | Layout Frontend Editorial (Curadoria de Posts + Dark Mode) | 🟢 Concluído |
| **Sprint 4** | Módulo Multimídia & Integração de Formulários | 🟡 Em Progresso |
| **Sprint 5** | Otimização SEO, Performance Lighthouse & Go-Live | 🟡 Finalizando (Aguardando SSL) |

---

## 🔴 EPIC 1: Migração de Conteúdo & Gestão via Markdown (Hermes Agent)

### US-01: Extração e Conversão dos Artigos Legados
* **Como** Desenvolvedor / Hermes Agent,
* **Quero** converter todas as postagens e páginas do site anterior em arquivos Markdown com Frontmatter,
* **Para que** todo o acervo histórico de João de Brito Freires esteja preservado e pronto para o novo design.
* **Critérios de Aceite:**
  - [x] Extração de 100% das postagens (12 páginas/artigos identificados no sitemap).
  - [x] Criação da pasta `content/posts/` com arquivos `.md`.
  - [x] Preservação de datas originais (ex: artigos históricos de 1985 sobre Tancredo Neves e O Político).
  - [x] Frontmatter contendo `title`, `date`, `slug`, `author`, `source_url`.

### US-02: Workflow de Publicação Autônoma com Hermes Agent
* **Como** Autor / Administrador,
* **Quero** solicitar ao Hermes Agent a criação ou edição de novos artigos por linguagem natural,
* **Para que** o site seja atualizado sem necessidade de acessar painéis complexos.
* **Critérios de Aceite:**
  - [x] Script de migração e estrutura de arquivos em repositório Git (`JaderBrito09/joao-brito-site`).
  - [x] Instruções e automação de `git commit` e `git push` executadas pelo Hermes.
  - [x] Repositório público no GitHub sincronizado e pronto para Webhook do Easypanel.

---

## 🟢 EPIC 2: Infraestrutura Docker & Easypanel (VPS Hostinger)

### US-03: Configuração de Contêiner Docker & Server Nginx
* **Como** Engenheiro de DevOps,
* **Quero** empacotar o projeto em um `Dockerfile` otimizado com Nginx e compressão Gzip,
* **Para que** o site rode na VPS com baixíssimo consumo de memória (< 50MB RAM).
* **Critérios de Aceite:**
  - [x] `Dockerfile` baseado em `nginx:alpine`.
  - [x] `nginx.conf` com suporte a compressão Gzip, cache de ativos e SPA routing.
  - [x] Teste de build e execução do contêiner Docker no Easypanel.

### US-04: Gestão de Variáveis de Ambiente (`.env`)
* **Como** Desenvolvedor,
* **Quero** criar os arquivos `.env` e `.env.example`,
* **Para que** chaves de API e URLs de webhooks não fiquem hardcoded no repositório.
* **Critérios de Aceite:**
  - [x] Criado `.env.example` com todas as chaves requeridas.
  - [x] Criado `.env` local com as variáveis ativas.
  - [x] Variáveis incluídas: `PORT`, `SITE_URL`, `CONTACT_FORM_ENDPOINT`, `NEWSLETTER_ENDPOINT`, `EASYPANEL_WEBHOOK_URL`, `GITHUB_REPOSITORY`.

---

## 🔵 EPIC 3: Frontend & Design System Editorial

### US-05: Layout Editorial Responsivo & Dark Mode
* **Como** Leitor do Blog,
* **Quero** visualizar os artigos com tipografia legível (*Playfair Display* e *Inter*) e alternar entre Modo Claro e Escuro,
* **Para que** a leitura seja confortável em qualquer ambiente ou dispositivo.
* **Critérios de Aceite:**
  - [x] Header fixo com logotipo "JB", menu de navegação e botão de alternância de tema.
  - [x] Hero section com badge de credibilidade e destaque da trajetória.
  - [x] Suporte 100% responsivo para mobile, tablet e desktop.
  - [ ] Leitura dinâmica dos arquivos da pasta `content/posts/`.

### US-06: Sistema de Filtros por Categoria & Busca
* **Como** Leitor,
* **Quero** filtrar as postagens por categorias (*Política*, *Pensamentos*, *Acervo Histórico de 1985*, *Músicas*),
* **Para que** eu encontre rapidamente os ensaios de meu interesse.
* **Critérios de Aceite:**
  - [ ] Abas de filtro interativas no grid de artigos.
  - [ ] Modal ou barra de busca em tempo real por palavras-chave nos títulos e resumos.

---

## 🟣 EPIC 4: Módulo Multimídia & Formas de Contato

### US-07: Player de Vídeos e Composições Musicais
* **Como** Fã do Autor / Compositor,
* **Quero** assistir às vídeo-mensagens cívicas e ouvir as composições gravadas diretamente no site,
* **Para que** eu conheça a produção musical (+40 faixas) e poética de João de Brito Freires.
* **Critérios de Aceite:**
  - [ ] Componente de player de vídeo responsivo (YouTube Embed com modo privativo).
  - [ ] Seção dedicada a poesias declamadas e composições sertanejas/MPB.

### US-08: Captura de Newsletter & Formulário de Contato
* **Como** Leitor,
* **Quero** enviar mensagens diretas ao autor e me inscrever para receber novas reflexões por e-mail,
* **Para que** eu mantenha contato e receba os artigos em primeira mão.
* **Critérios de Aceite:**
  - [ ] Formulário de contato com validação nativa de campos (nome, e-mail, mensagem).
  - [ ] Disparo dos dados para o `CONTACT_FORM_ENDPOINT` via Fetch API com tratamento de erros.
  - [ ] Campo de inscrição de newsletter integrado ao `NEWSLETTER_ENDPOINT`.

---

## 🟢 EPIC 5: SEO, Performance & Go-Live (Easypanel)

### US-09: Otimização de Performance (Lighthouse > 90)
* **Como** Administrador,
* **Quero** garantir que o tempo de carregamento da página seja inferior a 1,5s,
* **Para que** o site cumpra com o requisito RNF-01 do PDR.
* **Critérios de Aceite:**
  - [ ] Pontuação no Google Lighthouse igual ou superior a 90 em Performance, Acessibilidade e SEO.
  - [ ] Imagens otimizadas em formato WebP.

### US-10: Configuração de Domínio & SSL no Easypanel
* **Como** Administrador,
* **Quero** apontar o domínio `www.jbritopensamentos.com.br` para o IP da VPS Hostinger,
* **Para que** o público acesse o novo portal sob conexão segura HTTPS.
* **Critérios de Aceite:**
  - [ ] Apontamento de registro A no Registro.br / DNS Hostinger.
  - [ ] Certificado SSL (Let's Encrypt) gerado automaticamente pelo Easypanel.
  - [ ] Redirecionamento automático de HTTP para HTTPS.
