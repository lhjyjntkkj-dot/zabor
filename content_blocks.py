"""Reusable HTML-generating blocks shared across pages."""

def img_placeholder(text="Демонстрационное изображение"):
    return f'<div class="img-ph">{text}</div>'

# Варианты забора в квизе (без цен — квиз не показывает стоимость)
QUIZ_FENCE_TYPES = [
    ("profnastil", "Профнастил"),
    ("evroshtaketnik", "Евроштакетник"),
    ("zhalyuzi", "Жалюзи"),
    ("grid3d", "3D-сетка"),
    ("rabitsa", "Рабица"),
    ("other", "Другой вариант"),
]

# Варианты ширины ворот, м
GATE_WIDTHS = ["3", "3.5", "4", "4.5", "5", "5.5", "6"]

def calculator_block(standalone=False):
    """Квиз-лидформа. Цены клиенту НЕ показываются — задача собрать качественную заявку."""
    fence_cards = "".join(
        f"""
          <button type="button" class="fence-card" data-quiz-fence="{fid}">
            <div class="fence-thumb">{img_placeholder()}</div>
            <div class="fence-info">
              <strong>{label}</strong>
            </div>
          </button>"""
        for fid, label in QUIZ_FENCE_TYPES
    )

    gate_widths = "".join(
        f'<button type="button" class="chip" data-gate-width="{w}">{w.replace(".", ",")} м</button>'
        for w in GATE_WIDTHS
    )

    return f"""
  <div class="wizard" data-quiz>
    <div class="wizard-stepline">
      <span class="step-count" data-step-count>Шаг 1 из 6</span>
    </div>
    <div class="wizard-progress" data-progress>
      <span data-progress-dot></span><span data-progress-dot></span><span data-progress-dot></span>
      <span data-progress-dot></span><span data-progress-dot></span><span data-progress-dot></span>
    </div>

    <div class="wizard-steps">

      <div class="wizard-step" data-step="1">
        <h3>Какая длина забора вам нужна?</h3>
        <div class="calc-field" style="margin-top:18px;">
          <label for="quiz-length">Длина забора, м</label>
          <input type="number" id="quiz-length" data-quiz-length min="1" step="1" inputmode="numeric" placeholder="Например, 50">
          <p class="step-hint" style="margin:10px 0 0;">Если точный метраж неизвестен — укажите примерно.</p>
          <p class="quiz-error" data-error-length hidden>Укажите длину забора числом больше нуля.</p>
        </div>
      </div>

      <div class="wizard-step" data-step="2">
        <h3>Какой забор хотите установить?</h3>
        <p class="step-hint">Выберите подходящий вариант.</p>
        <div class="fence-gallery">{fence_cards}
        </div>
        <p class="quiz-error" data-error-fence hidden>Выберите тип забора.</p>
      </div>

      <div class="wizard-step" data-step="3">
        <h3>Нужны ворота?</h3>
        <div class="chip-row">
          <button type="button" class="chip active" data-gate-choice="none">Не нужны</button>
          <button type="button" class="chip" data-gate-choice="sliding">Откатные</button>
          <button type="button" class="chip" data-gate-choice="swing">Распашные</button>
        </div>

        <div data-gate-width-block hidden style="margin-top:22px;">
          <div class="calc-field">
            <label>Ширина ворот</label>
            <div class="chip-row">
              {gate_widths}
              <button type="button" class="chip" data-gate-width="custom">Другая ширина</button>
            </div>
          </div>
          <div class="calc-field" data-gate-custom-block hidden>
            <label for="quiz-gate-custom">Укажите ширину, м</label>
            <input type="number" id="quiz-gate-custom" data-gate-custom min="1" step="0.1" inputmode="decimal" placeholder="Например, 7">
          </div>
          <p class="quiz-error" data-error-gate hidden>Укажите ширину ворот.</p>
        </div>
      </div>

      <div class="wizard-step" data-step="4">
        <h3>Нужна калитка?</h3>
        <div class="chip-row">
          <button type="button" class="chip" data-wicket-choice="yes">Да</button>
          <button type="button" class="chip active" data-wicket-choice="no">Нет</button>
        </div>

        <div class="calc-field" data-wicket-count-block hidden style="margin-top:22px;">
          <label>Количество калиток</label>
          <div class="chip-row">
            <button type="button" class="chip active" data-wicket-count="1">1</button>
            <button type="button" class="chip" data-wicket-count="2">2</button>
            <button type="button" class="chip" data-wicket-count="3">3</button>
          </div>
        </div>
      </div>

      <div class="wizard-step" data-step="5">
        <h3>Есть дополнительные пожелания?</h3>
        <div class="calc-field" style="margin-top:18px;">
          <label for="quiz-comment" class="visually-hidden-label">Дополнительные пожелания</label>
          <textarea id="quiz-comment" data-quiz-comment rows="4" placeholder="Например: нужен демонтаж старого забора, сложный участок, нужен навес, автоматика на ворота и т.д."></textarea>
          <p class="step-hint" style="margin:10px 0 0;">Можно оставить пустым</p>
        </div>
      </div>

      <div class="wizard-step" data-step="6">
        <h3>Куда отправить расчёт?</h3>
        <p class="step-hint">Оставьте имя и номер телефона. Специалист CH PROJECT свяжется с вами, уточнит детали участка и подготовит расчёт.</p>

        <div class="quiz-recap" data-quiz-recap></div>

        <form data-quiz-form novalidate>
          <input type="text" name="website" tabindex="-1" autocomplete="off" aria-hidden="true" class="hp-field">
          <div class="form-row cols-2">
            <div class="field">
              <label for="quiz-name">Имя</label>
              <input type="text" id="quiz-name" name="name" placeholder="Как к вам обращаться" required>
            </div>
            <div class="field">
              <label for="quiz-phone">Телефон</label>
              <input type="tel" id="quiz-phone" name="phone" data-phone-mask placeholder="+7 (___) ___-__-__" required>
            </div>
          </div>
          <p class="quiz-error" data-error-contacts hidden>Укажите имя и телефон — без них не сможем связаться.</p>
          <button type="submit" class="btn btn-primary btn-block" data-quiz-submit>Получить расчёт</button>
          <p class="form-foot-note">Нажимая «Получить расчёт», вы соглашаетесь с <a href="/privacy.html" style="text-decoration:underline;">политикой обработки персональных данных</a>.</p>
        </form>
      </div>

    </div>

    <div class="wizard-nav" data-quiz-nav>
      <button type="button" class="btn btn-ghost" data-quiz-back>Назад</button>
      <button type="button" class="btn btn-primary" data-quiz-next>Далее →</button>
    </div>

    <div class="quiz-success" data-quiz-success hidden>
      <div class="check">✓</div>
      <h3 class="h-3" style="margin-bottom:10px;">Спасибо! Заявка принята.</h3>
      <p>Мы свяжемся с вами для уточнения деталей.</p>
      <p class="quiz-success-note">Хотите сделать расчёт точнее? Отправьте фотографию участка — по фото мы быстрее оценим объект.</p>
      <div class="cta-row" style="justify-content:center;">
        <a href="#" class="btn btn-primary" data-telegram-link data-send-photo>Отправить фото участка</a>
        <a href="/index.html" class="btn btn-ghost">Вернуться на сайт</a>
      </div>
    </div>
  </div>
"""


def lead_form_block(source="general", compact=False, title="Оставьте заявку", subtitle="Ответим и уточним детали — обычно в течение рабочего дня."):
    heading = "" if compact else f"""
      <h3 class="h-3" style="margin-bottom:6px;">{title}</h3>
      <p style="color:var(--text-dim);font-size:.92rem;margin-bottom:24px;">{subtitle}</p>
    """
    return f"""
    <div class="form-card">
      {heading}
      <form data-lead-form="{source}" novalidate>
        <input type="text" name="website" tabindex="-1" autocomplete="off" aria-hidden="true" class="hp-field">
        <input type="hidden" name="calc_summary" data-calc-summary value="">
        <div class="form-row cols-2">
          <div class="field">
            <label for="name-{source}">Имя</label>
            <input type="text" id="name-{source}" name="name" placeholder="Как к вам обращаться" required>
          </div>
          <div class="field">
            <label for="phone-{source}">Телефон</label>
            <input type="tel" id="phone-{source}" name="phone" placeholder="+7 ___ ___-__-__" required>
          </div>
        </div>

        <div class="field" style="margin-bottom:16px;">
          <label>Что требуется</label>
          <div class="check-grid">
            <label class="check-item"><input type="checkbox" name="service" value="Забор"> Забор</label>
            <label class="check-item"><input type="checkbox" name="service" value="Ворота"> Ворота</label>
            <label class="check-item"><input type="checkbox" name="service" value="Калитка"> Калитка</label>
            <label class="check-item"><input type="checkbox" name="service" value="Навес"> Навес</label>
            <label class="check-item"><input type="checkbox" name="service" value="Металлоконструкция"> Металлоконструкция</label>
          </div>
        </div>

        <div class="form-row cols-2">
          <div class="field">
            <label for="length-{source}">Длина участка (ориентировочно)</label>
            <input type="text" id="length-{source}" name="length" placeholder="Например, 45 м">
          </div>
          <div class="field">
            <label for="photo-{source}">Фото участка</label>
            <div class="upload-drop" data-upload>
              <label for="photo-{source}" style="cursor:pointer;display:block;">
                <strong data-upload-label>Прикрепить фото</strong>
                JPG, PNG — поможет точнее оценить объём работ
              </label>
              <input type="file" id="photo-{source}" name="photo" accept="image/*" style="display:none;">
            </div>
          </div>
        </div>

        <div class="field" style="margin-bottom:20px;">
          <label for="comment-{source}">Комментарий</label>
          <textarea id="comment-{source}" name="comment" rows="3" placeholder="Особенности участка, сроки, пожелания"></textarea>
        </div>

        <button type="submit" class="btn btn-primary btn-block">Получить расчёт</button>
        <p class="form-foot-note">Нажимая «Получить расчёт», вы соглашаетесь с <a href="/privacy.html" style="text-decoration:underline;">политикой обработки персональных данных</a>.</p>
      </form>
      <div class="form-success" data-form-success>
        <div class="check">✓</div>
        <h3 class="h-3" style="margin-bottom:8px;">Заявка отправлена</h3>
        <p style="color:var(--text-dim);">Мы свяжемся с вами для уточнения деталей.</p>
      </div>
    </div>
"""

FAQ_ITEMS = [
    ("Сколько стоит забор?", "Стоимость зависит от длины, высоты, материала и комплектации. Калькулятор на сайте даст ориентир, точную сумму фиксируем после уточнения параметров участка."),
    ("Какой материал выбрать?", "Профнастил — практичный вариант, пропускает свет. Штакетник — аккуратнее внешне. 3D-сетка и рабица — для технических целей. Поможем определиться под вашу задачу."),
    ("Можно ли сделать ворота в единомстиле с забором?", "Да, ворота и калитку изготавливаем в одном материале и цвете с основным ограждением."),
    ("Работаете ли вы с материалами заказчика?", "Обсуждается в каждом случае — уточните этот момент в заявке или по телефону."),
    ("Делаете ли демонтаж старого забора?", "Да, демонтаж можно заказать отдельно — учитывается в расчёте калькулятора."),
    ("Можно ли заказать только ворота?", "Да, ворота и калитку можно заказать отдельно от забора."),
    ("Можно ли сделать навес?", "Да, изготавливаем навесы по индивидуальному проекту — для авто, двора, коммерческих объектов."),
    ("Сколько занимает монтаж?", "Срок зависит от объёма — назовём конкретные даты после расчёта и уточнения параметров на выезде."),
    ("Как происходит расчёт?", "Вы указываете параметры в калькуляторе или отправляете фото — мы уточняем детали и готовим смету."),
    ("Есть ли гарантия?", "Гарантия на выполненные работы — условия уточняются в договоре."),
]

def faq_block(id_prefix="faq"):
    items = ""
    for i, (q, a) in enumerate(FAQ_ITEMS):
        items += f"""
        <div class="faq-item" data-faq-item>
          <button class="faq-q">{q}<span class="plus"></span></button>
          <div class="faq-a"><p>{a}</p></div>
        </div>"""
    return f'<div data-faq-list>{items}\n      </div>'

PORTFOLIO_ITEMS = [
    ("fence", "Заборы", "Ограждение участка из профнастила", "68 м", "Профнастил, столбы 60×60"),
    ("shtaketnik", "Штакетник", "Ограждение частного дома", "42 м", "Металлический штакетник, двойная зашивка"),
    ("gate", "Ворота", "Откатные ворота с калиткой", "5 м проём", "Откатные, автоматика"),
    ("gate", "Ворота", "Распашные ворота", "4 м проём", "Распашные, ковка-имитация"),
    ("navesy", "Навесы", "Навес для автомобиля", "18 м²", "Поликарбонат, каркас из профтрубы"),
    ("metall", "Металлоконструкции", "Каркас хозблока", "12 м²", "Индивидуальный проект"),
    ("fence", "Заборы", "Ограждение по периметру участка", "120 м", "3D-сетка, столбы с полимерным покрытием"),
    ("shtaketnik", "Штакетник", "Комбинированный забор с кирпичными столбами", "56 м", "Штакетник + кладка"),
    ("navesy", "Навесы", "Навес-терраса", "24 м²", "Металлокаркас, поликарбонат"),
]

def portfolio_grid_block(limit=None, filters=True, id_attr=""):
    items = PORTFOLIO_ITEMS[:limit] if limit else PORTFOLIO_ITEMS
    filter_html = ""
    if filters:
        filter_html = """
    <div class="filter-row">
      <button class="chip active" data-filter="all">Все</button>
      <button class="chip" data-filter="fence">Заборы</button>
      <button class="chip" data-filter="shtaketnik">Штакетник</button>
      <button class="chip" data-filter="gate">Ворота</button>
      <button class="chip" data-filter="navesy">Навесы</button>
      <button class="chip" data-filter="metall">Металлоконструкции</button>
    </div>"""
    cards = ""
    for cat, tag, title, length, materials in items:
        cards += f"""
      <div class="portfolio-card" data-portfolio-card data-category="{cat}">
        <div class="portfolio-thumb">{img_placeholder()}</div>
        <div class="portfolio-body">
          <div class="tag">{tag} · пример оформления проекта</div>
          <h4>{title}</h4>
          <div class="portfolio-meta">
            <span>Длина/площадь: {length}</span>
            <span>Материалы: {materials}</span>
          </div>
        </div>
      </div>"""
    return f'{filter_html}\n    <div class="portfolio-grid"{id_attr}>{cards}\n    </div>'

def reviews_block():
    return """
  <div class="review-grid">
    <div class="review-card">
      <div class="review-meta">
        <div class="review-avatar">Фото</div>
        <div>
          <div style="font-weight:600;font-size:.92rem;">Здесь будет имя клиента</div>
          <span>Здесь будет дата</span>
        </div>
      </div>
      <p>Здесь будут реальные отзывы клиентов CH PROJECT — с текстом, фото объекта и датой.</p>
    </div>
    <div class="review-card">
      <div class="review-meta">
        <div class="review-avatar">Фото</div>
        <div>
          <div style="font-weight:600;font-size:.92rem;">Здесь будет имя клиента</div>
          <span>Здесь будет дата</span>
        </div>
      </div>
      <p>Раздел готов принимать отзывы по мере выполнения объектов — заглушка будет заменена на реальные истории.</p>
    </div>
    <div class="review-card">
      <div class="review-meta">
        <div class="review-avatar">Фото</div>
        <div>
          <div style="font-weight:600;font-size:.92rem;">Здесь будет имя клиента</div>
          <span>Здесь будет дата</span>
        </div>
      </div>
      <p>Каждый отзыв можно сопроводить фотографией готового объекта — структура блока уже готова.</p>
    </div>
  </div>
"""
