#!/usr/bin/env python3
"""
build.py — собирает статические HTML-страницы CH PROJECT из общих партиалов
(шапка, футер, sticky CTA, AI-чат) + контента каждой страницы.
Запуск: python3 build.py
"""
import os

OUT = os.path.dirname(os.path.abspath(__file__))

FONT_LINKS = """<link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Unbounded:wght@500;600;700&family=Manrope:wght@400;500;600;700;800&display=swap" rel="stylesheet">"""

NAV_LINKS = [
    ("/index.html", "Главная"),
    ("/zabory.html", "Заборы"),
    ("/vorota.html", "Ворота"),
    ("/navesy.html", "Навесы"),
    ("/metallokonstrukcii.html", "Металлоконструкции"),
    ("/portfolio.html", "Работы"),
    ("/calculator.html", "Получить расчёт"),
    ("/contacts.html", "Контакты"),
]

def head(title, description, canonical):
    return f"""<!doctype html>
<html lang="ru">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
  <title>{title}</title>
  <meta name="description" content="{description}">
  <link rel="canonical" href="https://chproject.ru{canonical}">
  <meta property="og:title" content="{title}">
  <meta property="og:description" content="{description}">
  <meta property="og:type" content="website">
  <meta property="og:url" content="https://chproject.ru{canonical}">
  <meta property="og:image" content="https://chproject.ru/images/og-cover.jpg">
  <meta property="og:image:alt" content="CH PROJECT — заборы, ворота и металлоконструкции">
  <meta property="og:locale" content="ru_RU">
  <meta property="og:site_name" content="CH PROJECT">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{title}">
  <meta name="twitter:description" content="{description}">
  <meta name="twitter:image" content="https://chproject.ru/images/og-cover.jpg">
  <meta name="theme-color" content="#121317">
  <!-- ЗАМЕНИТЬ: /images/og-cover.jpg — картинка 1200×630 для превью в соцсетях, сейчас файла нет -->
  <meta name="robots" content="index, follow">
  {FONT_LINKS}
  <link rel="stylesheet" href="/css/styles.css">
  <!-- Яндекс.Метрика: вставьте счётчик перед </head>, см. README раздел "Аналитика" -->
  <!-- Google Analytics (если требуется): см. README -->
</head>
<body>
"""

def header():
    links = "\n      ".join(f'<a href="{href}">{label}</a>' for href, label in NAV_LINKS[:-1])
    mobile_links = "\n      ".join(f'<a href="{href}">{label}</a>' for href, label in NAV_LINKS)
    return f"""  <header class="site-header">
    <div class="container">
      <a href="/index.html" class="brand">
        <span class="brand-mark">CH</span>
        CH PROJECT
      </a>
      <nav class="main-nav">
      {links}
      </nav>
      <div class="header-actions">
        <a href="tel:+70000000000" class="phone-link">+7 000 000-00-00</a>
        <a href="/calculator.html" class="btn btn-primary btn-sm">Получить расчёт</a>
        <button class="nav-toggle" data-nav-toggle aria-label="Меню"><span></span></button>
      </div>
    </div>
    <div class="mobile-nav" data-mobile-nav>
      {mobile_links}
      <div class="cta-row">
        <a href="/calculator.html" class="btn btn-primary btn-block">Получить расчёт</a>
        <a href="tel:+70000000000" class="btn btn-ghost btn-block">Позвонить</a>
      </div>
    </div>
  </header>
"""

def footer():
    return """  <footer class="site-footer">
    <div class="container">
      <div class="footer-grid">
        <div>
          <div class="brand" style="margin-bottom:14px;">
            <span class="brand-mark">CH</span>
            CH PROJECT
          </div>
          <p style="color:var(--text-dim);font-size:.9rem;max-width:280px;">
            Заборы, ворота, навесы и металлоконструкции под ключ. Рязанская область.
          </p>
        </div>
        <div>
          <h4>Услуги</h4>
          <ul>
            <li><a href="/zabory.html">Заборы</a></li>
            <li><a href="/vorota.html">Ворота</a></li>
            <li><a href="/navesy.html">Навесы</a></li>
            <li><a href="/metallokonstrukcii.html">Металлоконструкции</a></li>
            <li><a href="/calculator.html">Получить расчёт</a></li>
          </ul>
        </div>
        <div>
          <h4>Компания</h4>
          <ul>
            <li><a href="/portfolio.html">Наши работы</a></li>
            <li><a href="/index.html#faq">Вопросы и ответы</a></li>
            <li><a href="/contacts.html">Контакты</a></li>
            <li><a href="/privacy.html">Политика конфиденциальности</a></li>
          </ul>
        </div>
        <div>
          <h4>Связь</h4>
          <ul>
            <li><a href="tel:+70000000000">+7 000 000-00-00</a></li>
            <li><a href="#" data-telegram-link>Telegram</a></li>
            <li><a href="#" data-telegram-link>ВКонтакте</a></li>
          </ul>
        </div>
      </div>
      <div class="footer-bottom">
        <span>© 2026 CH PROJECT. Рязанская область.</span>
        <span><a href="/privacy.html">Политика конфиденциальности</a> · <a href="/privacy.html#consent">Согласие на обработку данных</a></span>
      </div>
    </div>
  </footer>

  <div class="sticky-cta">
    <a href="tel:+70000000000" class="btn btn-ghost btn-icon" aria-label="Позвонить">☎</a>
    <a href="/calculator.html" class="btn btn-primary">Получить расчёт</a>
  </div>

  <button class="ai-fab" data-ai-fab aria-label="Задать вопрос">💬</button>
  <div class="ai-panel" data-ai-panel>
    <div class="ai-head">
      <div>
        <strong>AI-консультант</strong>
        <p>Демо-режим — цены не называет, помогает собрать параметры</p>
      </div>
      <button class="ai-close" data-ai-close aria-label="Закрыть">✕</button>
    </div>
    <div class="ai-body" data-ai-body>
      <div class="ai-msg bot">Здравствуйте! Помогу разобраться, что вам нужно — забор, ворота или навес — и подготовлю параметры для расчёта. Что вас интересует?</div>
    </div>
    <div class="ai-input-row">
      <input type="text" data-ai-input placeholder="Например: сколько будет стоить забор на 50 метров?">
      <button data-ai-send aria-label="Отправить">➤</button>
    </div>
  </div>

  <script>window.YM_COUNTER_ID = 00000000; /* замените на свой ID Метрики */</script>
  <script src="/js/main.js"></script>
"""

def page(filename, title, description, canonical, body, extra_scripts=""):
    html = head(title, description, canonical) + header() + body + footer() + extra_scripts + "</body>\n</html>\n"
    with open(os.path.join(OUT, filename), "w", encoding="utf-8") as f:
        f.write(html)
    print("wrote", filename)

# page bodies are assembled in build_pages.py (imported below to keep this file focused on partials)
if __name__ == "__main__":
    import build_pages
    build_pages.build(page)
