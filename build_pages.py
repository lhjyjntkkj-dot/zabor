from content_blocks import (
    img_placeholder, calculator_block, lead_form_block, faq_block,
    portfolio_grid_block, reviews_block, PORTFOLIO_ITEMS,
)

def build(page):
    build_home(page)
    build_service_pages(page)
    build_calculator(page)
    build_portfolio(page)
    build_contacts(page)
    build_privacy(page)


# ---------------------------------------------------------------- HOME ----
def build_home(page):
    body = f"""
  <section class="hero">
    <div class="container">
      <div class="hero-grid">
        <div class="reveal in">
          <div class="hero-eyebrow"><span class="dot"></span> Рязанская область</div>
          <h1 class="h-display">Заборы и ворота под ключ</h1>
          <p class="lead">Точный расчёт по параметрам вашего участка.</p>
          <div class="cta-row">
            <a href="/calculator.html" class="btn btn-primary btn-lg">Получить расчёт</a>
            <a href="/contacts.html" class="btn btn-ghost">Отправить фото участка</a>
          </div>
          <p class="hero-chain">Выезд на замер • Изготовление • Доставка • Монтаж</p>
        </div>
        <div class="hero-visual reveal in">
          {img_placeholder("Фото выполненного объекта CH PROJECT")}
          <span class="placeholder-tag">Демонстрационное изображение</span>
        </div>
      </div>
    </div>
  </section>

  <section class="usp-strip">
    <div class="container">
      <div class="usp-grid">
        <div class="usp-item"><strong>Работаем по договору</strong><p>Условия и сроки фиксируются письменно</p></div>
        <div class="usp-item"><strong>Прозрачный расчёт</strong><p>Стоимость складывается из понятных статей</p></div>
        <div class="usp-item"><strong>Фото выполненных работ</strong><p>Показываем реальные объекты в портфолио</p></div>
        <div class="usp-item"><strong>Без скрытых доплат</strong><p>Дополнительные работы согласуются заранее</p></div>
      </div>
    </div>
  </section>

  <section id="services">
    <div class="container">
      <div class="section-head reveal">
        <span class="eyebrow">Услуги</span>
        <h2 class="h-1" style="margin-top:10px;">Всё для ограждения участка — в одном месте</h2>
        <p class="lead">От материала до монтажа: заборы, ворота, навесы и металлоконструкции по индивидуальному проекту.</p>
      </div>
      <div class="service-grid reveal">
        <div class="service-card">
          <div class="service-icon">▦</div>
          <h3>Заборы</h3>
          <ul>
            <li>Профнастил</li>
            <li>Металлический штакетник</li>
            <li>3D-сетка</li>
            <li>Сетка-рабица</li>
          </ul>
          <a href="/zabory.html" class="btn btn-ghost btn-sm">Рассчитать</a>
        </div>
        <div class="service-card">
          <div class="service-icon">⊟</div>
          <h3>Ворота</h3>
          <ul>
            <li>Откатные</li>
            <li>Распашные</li>
            <li>Калитки</li>
            <li>Автоматические системы</li>
          </ul>
          <a href="/vorota.html" class="btn btn-ghost btn-sm">Рассчитать</a>
        </div>
        <div class="service-card">
          <div class="service-icon">⌂</div>
          <h3>Навесы</h3>
          <ul>
            <li>Для автомобиля</li>
            <li>Для двора</li>
            <li>Террасы</li>
            <li>Коммерческие объекты</li>
          </ul>
          <a href="/navesy.html" class="btn btn-ghost btn-sm">Рассчитать</a>
        </div>
        <div class="service-card">
          <div class="service-icon">╬</div>
          <h3>Металлоконструкции</h3>
          <ul>
            <li>Каркасы</li>
            <li>Навесы</li>
            <li>Индивидуальные конструкции</li>
          </ul>
          <a href="/metallokonstrukcii.html" class="btn btn-ghost btn-sm">Рассчитать</a>
        </div>
      </div>
    </div>
  </section>

  <section id="calculator">
    <div class="container">
      <div class="section-head reveal">
        <span class="eyebrow">Заявка на расчёт</span>
        <h2 class="h-1" style="margin-top:10px;">Расчёт по параметрам вашего участка</h2>
        <p class="lead">Ответьте на несколько вопросов — специалист подготовит расчёт и свяжется с вами для уточнения деталей.</p>
      </div>
      <div class="reveal">
        {calculator_block()}
      </div>
    </div>
  </section>

  <section id="portfolio">
    <div class="container">
      <div class="split-head reveal">
        <div class="section-head">
          <span class="eyebrow">Портфолио</span>
          <h2 class="h-1" style="margin-top:10px;">Реализованные проекты</h2>
        </div>
        <a href="/portfolio.html" class="btn btn-ghost btn-sm">Все проекты</a>
      </div>
      <div class="reveal">
        {portfolio_grid_block(limit=6, filters=False)}
      </div>
    </div>
  </section>

  <section id="why">
    <div class="container">
      <div class="section-head reveal">
        <span class="eyebrow">Почему CH PROJECT</span>
        <h2 class="h-1" style="margin-top:10px;">Что вы получаете</h2>
      </div>
      <div class="why-grid reveal">
        <div class="why-item"><h3>Работаем под ключ</h3><p>От расчёта материалов до монтажа.</p></div>
        <div class="why-item"><h3>Один подрядчик</h3><p>Не нужно отдельно искать материалы, доставку и монтаж.</p></div>
        <div class="why-item"><h3>Реальные объекты</h3><p>Показываем выполненные работы.</p></div>
        <div class="why-item"><h3>Расчёт до начала работ</h3><p>Вы заранее понимаете состав проекта и стоимость.</p></div>
      </div>
    </div>
  </section>

  <section id="process">
    <div class="container">
      <div class="section-head reveal">
        <span class="eyebrow">Как мы работаем</span>
        <h2 class="h-1" style="margin-top:10px;">Забор под ключ</h2>
      </div>
      <div class="process-list reveal">
        <div class="process-item"><div class="process-num">01</div><div><h3>Расчёт</h3><p>Рассчитываем материалы и стоимость работ.</p></div></div>
        <div class="process-item"><div class="process-num">02</div><div><h3>Замер</h3><p>При необходимости выезжаем на объект.</p></div></div>
        <div class="process-item"><div class="process-num">03</div><div><h3>Материалы</h3><p>Организуем закупку и доставку.</p></div></div>
        <div class="process-item"><div class="process-num">04</div><div><h3>Монтаж</h3><p>Устанавливаем конструкцию на участке.</p></div></div>
        <div class="process-item" style="border-bottom:none;"><div class="process-num">05</div><div><h3>Сдача объекта</h3><p>Проверяем результат вместе с заказчиком.</p></div></div>
      </div>
      <div class="cta-row reveal" style="margin-top:32px;">
        <a href="/calculator.html" class="btn btn-primary">Получить расчёт</a>
      </div>
    </div>
  </section>

  <section id="compare">
    <div class="container">
      <div class="offer-card reveal">
        <div>
          <span class="eyebrow">Сравнение расчётов</span>
          <h2 class="h-2" style="margin:10px 0 12px;">Уже получили расчёт от другой компании?</h2>
          <p class="lead">Пришлите его нам — сравним комплектацию.</p>
          <p style="color:var(--text-dim);font-size:.92rem;margin-top:10px;">Иногда разница в цене объясняется толщиной металла, количеством столбов, фундаментом или комплектацией.</p>
        </div>
        <a href="/contacts.html" class="btn btn-light">Отправить расчёт</a>
      </div>
    </div>
  </section>

  <section id="geo">
    <div class="container">
      <div class="section-head reveal">
        <span class="eyebrow">География</span>
        <h2 class="h-1" style="margin-top:10px;">Работаем по Рязанской области</h2>
        <p class="lead">Выезжаем на замер, привозим материал и монтируем на объекте. Уточните адрес участка в заявке — подскажем сроки выезда.</p>
      </div>
      <div class="cta-row reveal">
        <a href="/calculator.html" class="btn btn-primary">Получить расчёт</a>
        <a href="tel:+70000000000" class="btn btn-ghost" data-phone-link>Позвонить</a>
      </div>
    </div>
  </section>

  <section id="reviews">
    <div class="container">
      <div class="section-head reveal">
        <span class="eyebrow">Отзывы</span>
        <h2 class="h-1" style="margin-top:10px;">Отзывы клиентов</h2>
      </div>
      <div class="reveal">{reviews_block()}</div>
    </div>
  </section>

  <section id="faq">
    <div class="container">
      <div class="section-head reveal">
        <span class="eyebrow">Вопросы</span>
        <h2 class="h-1" style="margin-top:10px;">Частые вопросы</h2>
      </div>
      <div class="reveal">{faq_block()}</div>
    </div>
  </section>

  <section id="final-cta">
    <div class="container">
      <div class="final-cta reveal">
        <h2 class="h-2">Не знаете, какой вариант выбрать?</h2>
        <p class="lead">Отправьте фото участка — поможем подобрать конструкцию и подготовим предварительный расчёт.</p>
        <div class="cta-row">
          <a href="/calculator.html" class="btn btn-primary">Получить расчёт</a>
          <a href="/contacts.html" class="btn btn-ghost">Отправить фото</a>
        </div>
      </div>
    </div>
  </section>
"""
    page(
        "index.html",
        "CH PROJECT — заборы, ворота и металлоконструкции под ключ | Рязанская область",
        "Установка заборов, ворот и навесов под ключ в Рязанской области. Точный расчёт, аккуратный монтаж, один подрядчик от материала до установки.",
        "/",
        body,
        extra_scripts='  <script src="/js/calculator.js"></script>\n',
    )


# --------------------------------------------------------- SERVICE PAGES ----
SERVICE_PAGES = {
    "zabory.html": {
        "title": "Заборы под ключ в Рязанской области — профнастил, евроштакетник, жалюзи | CH PROJECT",
        "description": "Установка заборов из профнастила, металлического штакетника, 3D-сетки и рабицы в Рязанской области. Точный расчёт и аккуратный монтаж под ключ.",
        "h1": "Заборы под ключ",
        "lead": "Профнастил, металлический штакетник, 3D-сетка и сетка-рабица — рассчитаем и установим ограждение вашего участка.",
        "items": [
            ("Профнастил", "Практичное и доступное решение для периметра участка."),
            ("Металлический штакетник", "Аккуратный внешний вид, пропускает свет и воздух."),
            ("3D-сетка", "Технический и временный вариант ограждения."),
            ("Сетка-рабица", "Бюджетное решение для хозяйственных участков."),
        ],
    },
    "vorota.html": {
        "title": "Ворота под ключ в Рязанской области — откатные и распашные | CH PROJECT",
        "description": "Изготовление и установка откатных, распашных ворот и калиток в Рязанской области. Автоматические системы, единый стиль с забором.",
        "h1": "Ворота под ключ",
        "lead": "Откатные, распашные ворота, калитки и автоматические системы — в едином стиле с вашим забором.",
        "items": [
            ("Откатные ворота", "Удобны при ограниченном пространстве перед въездом."),
            ("Распашные ворота", "Классическое и надёжное решение."),
            ("Калитки", "Изготавливаем в цвет и стиль основного ограждения."),
            ("Автоматические системы", "Открытие ворот без выхода из машины."),
        ],
    },
    "navesy.html": {
        "title": "Навесы под ключ в Рязанской области — для авто, двора, террас | CH PROJECT",
        "description": "Изготовление навесов для автомобиля, двора, террас и коммерческих объектов в Рязанской области. Индивидуальный проект и монтаж под ключ.",
        "h1": "Навесы под ключ",
        "lead": "Навесы для автомобиля, двора, террас и коммерческих объектов — по индивидуальному проекту.",
        "items": [
            ("Для автомобиля", "Защита машины от осадков и солнца."),
            ("Для двора", "Укрытие зоны отдыха или хозяйственной площадки."),
            ("Террасы", "Навес как продолжение дома."),
            ("Коммерческие объекты", "Навесы для парковок, входных групп, складов."),
        ],
    },
    "metallokonstrukcii.html": {
        "title": "Металлоконструкции под ключ в Рязанской области | CH PROJECT",
        "description": "Изготовление металлических каркасов, навесов и конструкций по индивидуальному проекту в Рязанской области.",
        "h1": "Металлоконструкции",
        "lead": "Каркасы, навесы и конструкции по индивидуальному проекту — от расчёта до монтажа.",
        "items": [
            ("Каркасы", "Основа для навесов, хозблоков и технических построек."),
            ("Навесы", "Металлокаркас под любые размеры и назначение."),
            ("Индивидуальные конструкции", "Проектируем под задачу заказчика."),
        ],
    },
}

def build_service_pages(page):
    for filename, data in SERVICE_PAGES.items():
        items_html = "".join(
            f"""
        <div class="why-item"><h3>{title}</h3><p>{desc}</p></div>"""
            for title, desc in data["items"]
        )
        body = f"""
  <section class="page-hero">
    <div class="container">
      <div class="crumbs"><a href="/index.html">Главная</a> / {data['h1']}</div>
      <h1 class="h-1">{data['h1']}</h1>
      <p class="lead">{data['lead']}</p>
      <div class="cta-row" style="margin-top:26px;">
        <a href="/calculator.html" class="btn btn-primary">Получить расчёт</a>
        <a href="/portfolio.html" class="btn btn-ghost">Посмотреть работы</a>
      </div>
    </div>
  </section>

  <section>
    <div class="container">
      <div class="why-grid reveal">{items_html}
      </div>
    </div>
  </section>

  <section>
    <div class="container">
      <div class="section-head reveal">
        <span class="eyebrow">Заявка на расчёт</span>
        <h2 class="h-1" style="margin-top:10px;">Расчёт по параметрам вашего участка</h2>
      </div>
      <div class="reveal">{calculator_block()}</div>
    </div>
  </section>

  <section>
    <div class="container">
      <div class="section-head reveal">
        <span class="eyebrow">Вопросы</span>
        <h2 class="h-1" style="margin-top:10px;">Частые вопросы</h2>
      </div>
      <div class="reveal">{faq_block()}</div>
    </div>
  </section>
"""
        page(filename, data["title"], data["description"], "/" + filename, body,
             extra_scripts='  <script src="/js/calculator.js"></script>\n')


# -------------------------------------------------------------- CALCULATOR ----
def build_calculator(page):
    body = f"""
  <section class="page-hero">
    <div class="container">
      <div class="crumbs"><a href="/index.html">Главная</a> / Заявка на расчёт</div>
      <h1 class="h-1">Получить расчёт забора</h1>
      <p class="lead">Укажите параметры ограждения — специалист CH PROJECT подготовит расчёт и свяжется с вами для уточнения деталей участка.</p>
    </div>
  </section>
  <section>
    <div class="container">
      {calculator_block(standalone=True)}
    </div>
  </section>
"""
    page("calculator.html",
         "Заявка на расчёт забора и ворот в Рязанской области | CH PROJECT",
         "Оставьте параметры участка — подготовим расчёт забора, ворот и калитки. Профнастил, евроштакетник, жалюзи, 3D-сетка, рабица, откатные и распашные ворота.",
         "/calculator.html", body,
         extra_scripts='  <script src="/js/calculator.js"></script>\n')


# --------------------------------------------------------------- PORTFOLIO ----
def build_portfolio(page):
    body = f"""
  <section class="page-hero" data-portfolio-page>
    <div class="container">
      <div class="crumbs"><a href="/index.html">Главная</a> / Реализованные проекты</div>
      <h1 class="h-1">Реализованные проекты</h1>
      <p class="lead">Ниже — demo-проекты с пометкой «пример оформления проекта». После выполнения объектов CH PROJECT они будут заменены на реальные фотографии.</p>
    </div>
  </section>
  <section>
    <div class="container">
      {portfolio_grid_block()}
    </div>
  </section>
  <section>
    <div class="container">
      <div class="final-cta reveal">
        <h2 class="h-2">Хотите похожий результат на своём участке?</h2>
        <p class="lead">Оставьте заявку или отправьте фото участка — подготовим предварительный расчёт.</p>
        <div class="cta-row">
          <a href="/calculator.html" class="btn btn-primary">Получить расчёт</a>
          <a href="/contacts.html" class="btn btn-ghost">Отправить фото</a>
        </div>
      </div>
    </div>
  </section>
"""
    page("portfolio.html",
         "Реализованные проекты — заборы, ворота, навесы | CH PROJECT",
         "Примеры оформления проектов CH PROJECT: заборы, ворота, навесы и металлоконструкции в Рязанской области.",
         "/portfolio.html", body)


# --------------------------------------------------------------- CONTACTS ----
def build_contacts(page):
    body = f"""
  <section class="page-hero">
    <div class="container">
      <div class="crumbs"><a href="/index.html">Главная</a> / Контакты</div>
      <h1 class="h-1">Контакты</h1>
      <p class="lead">Оставьте заявку, позвоните или напишите в Telegram — ответим и уточним детали проекта.</p>
    </div>
  </section>
  <section>
    <div class="container">
      <div class="two-col">
        <div>
          {lead_form_block(source="contacts", title="Оставить заявку", subtitle="Расскажите, что нужно — забор, ворота, навес или комплекс работ.")}
        </div>
        <div>
          <div class="why-item reveal" style="margin-bottom:16px;border:1px solid var(--line-soft);border-radius:var(--radius-m);">
            <h3>Телефон</h3>
            <p><a href="tel:+70000000000" style="font-size:1.1rem;color:var(--text);">+7 000 000-00-00</a></p>
          </div>
          <div class="why-item reveal" style="margin-bottom:16px;border:1px solid var(--line-soft);border-radius:var(--radius-m);">
            <h3>Мессенджеры</h3>
            <p style="display:flex;gap:14px;margin-top:6px;">
              <a href="#" data-telegram-link style="text-decoration:underline;">Telegram</a>
              <a href="#" style="text-decoration:underline;">ВКонтакте</a>
            </p>
          </div>
          <div class="why-item reveal" style="border:1px solid var(--line-soft);border-radius:var(--radius-m);">
            <h3>География</h3>
            <p>Работаем по Рязанской области.</p>
          </div>
        </div>
      </div>
    </div>
  </section>
"""
    page("contacts.html",
         "Контакты CH PROJECT — заборы, ворота, металлоконструкции в Рязанской области",
         "Свяжитесь с CH PROJECT: оставьте заявку, позвоните или напишите в Telegram. Работаем по Рязанской области.",
         "/contacts.html", body)


# ----------------------------------------------------------------- PRIVACY ----
def build_privacy(page):
    body = """
  <section class="page-hero">
    <div class="container">
      <div class="crumbs"><a href="/index.html">Главная</a> / Политика конфиденциальности</div>
      <h1 class="h-1">Политика конфиденциальности</h1>
      <p class="lead">Текст-заглушка. Замените на юридически выверенную политику перед запуском сайта.</p>
    </div>
  </section>
  <section>
    <div class="container">
      <div style="max-width:720px;color:var(--text-dim);display:flex;flex-direction:column;gap:18px;">
        <p>Настоящая страница — заглушка структуры и должна быть заменена согласованным с юристом текстом политики обработки персональных данных перед публикацией сайта.</p>
        <h3 id="consent" class="h-3" style="color:var(--text);margin-top:10px;">Согласие на обработку персональных данных</h3>
        <p>Раздел для текста согласия, который пользователь принимает при отправке формы заявки. Заполняется перед запуском.</p>
      </div>
    </div>
  </section>
"""
    page("privacy.html",
         "Политика конфиденциальности | CH PROJECT",
         "Политика обработки персональных данных CH PROJECT.",
         "/privacy.html", body)
