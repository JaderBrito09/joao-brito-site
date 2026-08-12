import urllib.request
import json
import re
import os
from bs4 import BeautifulSoup

urls = [
    "https://www.jbritopensamentos.com.br/o-politico",
    "https://www.jbritopensamentos.com.br/o-homem-de-mola-copy",
    "https://www.jbritopensamentos.com.br/nossa-vida",
    "https://www.jbritopensamentos.com.br/angustias",
    "https://www.jbritopensamentos.com.br/artigosblog01",
    "https://www.jbritopensamentos.com.br/feliz-natal-e-ano-novo",
    "https://www.jbritopensamentos.com.br/pensamentos",
    "https://www.jbritopensamentos.com.br/os-obstaculos",
    "https://www.jbritopensamentos.com.br/tancredo-tiradentes",
    "https://www.jbritopensamentos.com.br/sobre",
    "https://www.jbritopensamentos.com.br/videos",
    "https://www.jbritopensamentos.com.br/artigos"
]

os.makedirs("content/posts", exist_ok=True)

for url in urls:
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)'})
        html = urllib.request.urlopen(req, timeout=10).read().decode('utf-8')
        soup = BeautifulSoup(html, 'html.parser')
        
        title = ""
        og_title = soup.find('meta', property='og:title')
        if og_title and og_title.get('content'):
            title = og_title['content'].split('|')[0].strip()
        elif soup.title:
            title = soup.title.string.split('|')[0].strip()
            
        date = ""
        script_ld = soup.find('script', type='application/ld+json')
        if script_ld and script_ld.string:
            try:
                ld = json.loads(script_ld.string)
                if 'datePublished' in ld:
                    date = ld['datePublished']
            except:
                pass
                
        paragraphs = []
        for p in soup.find_all(['p', 'h2', 'h3', 'h4']):
            text = p.get_text().strip()
            if text and not any(k in text.lower() for k in ['cookie', 'direitos reservados', 'início', 'blog', 'vídeos', 'sobre', 'min read']):
                paragraphs.append(text)
                
        slug = url.split('/')[-1] or 'home'
        
        # Save as Markdown file
        md_content = f"""---
title: "{title}"
date: "{date}"
slug: "{slug}"
author: "João de Brito Freires"
source_url: "{url}"
---

# {title}

""" + "\n\n".join(paragraphs)

        filename = f"content/posts/{slug}.md"
        with open(filename, "w", encoding="utf-8") as f:
            f.write(md_content)
            
        print(f"Successfully saved {filename}")
    except Exception as e:
        print(f"Error scraping {url}: {e}")

print("Migration script finished.")
