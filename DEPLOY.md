# Guia de Deploy no Easypanel (VPS Hostinger)

Este documento orienta a publicação do site de **João de Brito Freires** na sua VPS Hostinger utilizando o **Easypanel** e integração contínua via Git (GitOps).

---

## 1. Pré-requisitos
1. **VPS Hostinger** ativa com **Easypanel** instalado.
2. Repositório Git contendo o código do projeto (`Dockerfile`, `nginx.conf`, `.env`, `index.html` e `content/posts/`).

---

## 2. Passo a Passo no Easypanel

### Passo 1: Criar o Projeto
1. Acesse o painel do seu Easypanel (`https://seu-easypanel.ip.com`).
2. Clique em **+ New Project** e nomeie como `joao-brito-site`.

### Passo 2: Criar a Aplicação (App)
1. Dentro do projeto, clique em **+ Service** -> **App**.
2. Nomeie o serviço como `web`.

### Passo 3: Configurar a Fonte do Código (Git Repository)
1. Na aba **Source**, selecione **Git Repository**.
2. Cole a URL do seu repositório no GitHub/GitLab.
3. Defina a branch principal (ex: `main`).
4. Selecione o tipo de Build: **Dockerfile**.

### Passo 4: Configurar Variáveis de Ambiente
1. Na aba **Environment**, adicione as variáveis presentes no seu `.env`:
   - `PORT=80`
   - `SITE_URL=https://www.jbritopensamentos.com.br`
   - `CONTACT_FORM_ENDPOINT=https://formspree.io/f/SUA_CHAVE`
   - `NEWSLETTER_ENDPOINT=https://api.brevo.com/v3/contacts`

### Passo 5: Domínio & SSL
1. Na aba **Domains**, adicione os domínios:
   - `jbritopensamentos.com.br`
   - `www.jbritopensamentos.com.br`
2. Ative a chave **Auto SSL (Let's Encrypt)**.

### Passo 6: Deploy & Webhook de Automação
1. Clique em **Deploy**. O Easypanel fará o build do contêiner Docker e subirá a aplicação.
2. Copie a URL do **Deploy Webhook** fornecida pelo Easypanel e salve no arquivo `.env` no campo `EASYPANEL_WEBHOOK_URL`.
3. No GitHub, adicione essa URL em **Settings > Webhooks** para que cada `push` feito pelo Hermes Agent atualize o site automaticamente no ar.
