# 🚀 Web Test Automation Projesi

Bu proje, **Selenium WebDriver** ve **Python** kullanarak web uygulamalarını otomatik test etmek için tasarlanmış bir **Page Object Model (POM)** tabanlı test framework'üdür.

## 📋 İçindekiler

- [Proje Yapısı](#proje-yapısı)
- [Kurulum](#kurulum)
- [Kod Yapısı](#kod-yapısı)
- [Kullanım](#kullanım)
- [Jenkins CI/CD](#jenkins-cicd)
- [Test Çalıştırma](#test-çalıştırma)

## 📁 Proje Yapısı

```
webTestAuto/
├── conftest.py              # Pytest konfigürasyonu ve fixture'lar
├── requirements.txt         # Proje bağımlılıkları
├── README.md               # Bu dokümantasyon
├── jenkinsfile             # Jenkins pipeline konfigürasyonu
├── dockerfile              # Docker container konfigürasyonu
├── pages/                  # Page Object Model sınıfları
│   ├── __init__.py
│   └── login_page.py       # Login sayfası için POM sınıfı
├── tests/                  # Test dosyaları
│   ├── __init__.py
│   └── test_login.py       # Login testleri
└── utils/                  # Yardımcı sınıflar ve utilities
    ├── __init__.py
    ├── config.py           # Konfigürasyon ayarları
    └── driver_factory.py   # WebDriver oluşturma factory'si
```

## 🛠️ Kurulum

### 1. Repository'yi Clone Et
```bash
git clone https://github.com/emreosminho/webTestAutomation.git
cd webTestAutomation
```

### 2. Bağımlılıkları Yükle
```bash
pip install -r requirements.txt
```

### 3. Testleri Çalıştır
```bash
pytest tests/test_login.py -v
```

## 🏗️ Kod Yapısı

### **Driver Factory Pattern** (`utils/driver_factory.py`)
- **Factory Pattern** kullanarak WebDriver instance'ları oluşturur
- **ChromeDriverManager** otomatik driver yönetimi sağlar
- Windows uyumluluğu için path düzeltmeleri yapar

### **Configuration Management** (`utils/config.py`)
- Merkezi konfigürasyon yönetimi
- Test verileri ve URL'ler tek yerde toplanır
- SauceDemo test sitesi kullanılır

### **Page Object Model** (`pages/login_page.py`)
- **Page Object Model (POM)** design pattern kullanır
- Locator'lar ve sayfa aksiyonları tek yerde toplanır
- Test kodunu sayfa kodundan ayırır

### **Pytest Configuration** (`conftest.py`)
- **Pytest fixture** kullanarak driver yaşam döngüsünü yönetir
- Her test için temiz bir browser instance'ı sağlar

## 🚀 Kullanım

### Basit Test Çalıştırma
```bash
# Tek test dosyası
pytest tests/test_login.py

# Verbose output ile
pytest tests/test_login.py -v

# Tüm testler
pytest
```

### Gelişmiş Test Çalıştırma
```bash
# HTML raporu oluştur
pytest --html=report.html --self-contained-html

# Parallel test çalıştırma
pytest -n auto

# Specific test çalıştır
pytest tests/test_login.py::test_login_valid_credentials
```

## 🔧 Jenkins CI/CD

Bu proje Jenkins pipeline ile otomatik test çalıştırma özelliğine sahiptir.

### Jenkins Pipeline Özellikleri:
- ✅ Otomatik kod çekme (Git SCM)
- ✅ Python environment kurulumu
- ✅ Bağımlılık yükleme
- ✅ Test çalıştırma
- ✅ HTML rapor oluşturma
- ✅ Artifact saklama

### Jenkins Kurulumu:
1. Jenkins'te yeni pipeline job oluşturun
2. Repository URL'sini ekleyin: `https://github.com/emreosminho/webTestAutomation.git`
3. Jenkinsfile otomatik algılanacaktır
4. Pipeline'ı çalıştırın

## 🐳 Docker Desteği

Proje Docker ile containerize edilmiştir.

```bash
# Docker image build et
docker build -t web-test-automation .

# Container çalıştır
docker run --rm web-test-automation
```

## 📊 Test Sonuçları

- **Test Framework:** Pytest
- **Browser:** Chrome (Headless mode destekli)
- **Test Site:** https://www.saucedemo.com
- **Rapor Formatı:** HTML + Allure

## 🔧 Troubleshooting

### ChromeDriver Sorunları
- WebDriver Manager otomatik driver yönetimi sağlar
- Windows path sorunları otomatik düzeltilir

### Jenkins Sorunları
- Pipeline'da Python ve pip komutlarının mevcut olduğundan emin olun
- Headless browser modunu kullanın

## 📈 Gelişmiş Özellikler

- ✅ **Page Object Model** design pattern
- ✅ **Factory Pattern** for driver management
- ✅ **Explicit Waits** for stability
- ✅ **Jenkins CI/CD** integration
- ✅ **Docker** containerization
- ✅ **HTML Reporting**
- ✅ **Cross-platform** support

## 👥 Katkıda Bulunma

1. Fork'layın
2. Feature branch oluşturun (`git checkout -b feature/amazing-feature`)
3. Commit'leyin (`git commit -m 'Add amazing feature'`)
4. Push'layın (`git push origin feature/amazing-feature`)
5. Pull Request açın

---

**Happy Testing! 🚀**
