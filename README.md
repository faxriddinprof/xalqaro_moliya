# Xalqaro Moliya - Loyiha README

## Loyiha haqida
Bu loyiha "Jahon moliya markazlari rivojlanish bosqichlari" mavzusida yaratilgan Django web ilovasi.

## O'rnatish

### 1. Virtual muhit yaratish
```bash
python -m venv venv
venv\Scripts\activate
```

### 2. Kerakli paketlarni o'rnatish
```bash
pip install django
```

### 3. Database migratsiya
```bash
python manage.py migrate
```

### 4. Admin user yaratish (ixtiyoriy)
```bash
python manage.py createsuperuser
```

### 5. Serverni ishga tushirish
```bash
python manage.py runserver
```

## Static fayllar

### Qo'shish kerak bo'lgan rasmlar:
1. `static/img/logo.png` - Navbar logotipi
2. `static/img/profile.jpg` - Profil rasmi
3. `static/img/footer-logo.png` - Footer logotipi

## Loyiha strukturasi

```
xalqaro_moliya/
├── config/                 # Asosiy sozlamalar
│   ├── settings.py        # Django sozlamalari
│   ├── urls.py            # Asosiy URL konfiguratsiya
│   └── wsgi.py
├── slides/                # Slides ilovasi
│   ├── views.py           # View'lar
│   ├── urls.py            # URL pattern'lar
│   └── models.py
├── templates/             # HTML template'lar
│   ├── base.html          # Asosiy template
│   ├── navbar.html        # Navbar
│   ├── footer.html        # Footer
│   ├── resume.html        # Resume sahifasi
│   └── international_finance/        # Xalqaro moliya slides sahifalari
│       ├── 1-slide.html
│       ├── 2-slide.html
│       └── ... (15 tagacha)
└── static/                # Static fayllar
    ├── css/
    │   └── style.css
    ├── img/
    └── js/
```

## Sahifalar

- `/` - Asosiy resume sahifasi
- `/slide/1/` - 1-slayd
- `/slide/2/` - 2-slayd
- ... `/slide/15/` gacha

## Ishlab chiquvchi
**Faxriddin Baxtiyorov**
- Tashkent State University of Economics
- Junior Python Developer

## Fan ma'lumotlari
- **Fan:** Xalqaro moliya
- **Mavzu:** Jahon moliya markazlari rivojlanish bosqichlari
