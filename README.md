# ✈️ YOLOv8 Foreign Object Debris (FOD) Detection

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![YOLOv8](https://img.shields.io/badge/Model-YOLOv8-green)
![Roboflow](https://img.shields.io/badge/Data-Roboflow-purple)

Цей проєкт демонструє пайплайн для виявлення сторонніх предметів (FOD - Foreign Object Debris) за допомогою комп'ютерного зору. Модель натренована на кастомному датасеті з використанням архітектури **YOLOv8** та платформи **Roboflow**.

Така система може використовуватись для автоматичного моніторингу чистоти поверхонь (наприклад, злітних смуг аеропортів або промислових підлог).

## 🎥 Демонстрація роботи

Модель здатна розпізнавати дрібні об'єкти в реальному часі.

![Demo Animation](https://github.com/user-attachments/assets/19406a09-835a-48e6-9d72-e2a19e2f309e)

🔴 **[Дивитися повне відео на YouTube](https://youtube.com/shorts/5oNuL0XsUKY)**

---

## 📂 Структура репозиторію

* `best.pt` — ваги навченої моделі (готової до використання).
* `copy_yolo_train_roboflow.ipynb` — Jupyter Notebook з повним циклом навчання моделі (від завантаження даних з Roboflow до тренування).

## 🚀 Як запустити проєкт
### 🧪 Тестування на прикладі 
**Увага! Всі файли повинно знаходитися в одній папці.**
#### 1. Клонування репозиторію
```bash
git clone [https://github.com/kloktadanyil/yolov8-object-detection.git](https://github.com/kloktadanyil/yolov8-object-detection.git)
```
```bash
cd yolov8-object-detection
```
#### 2. завантажте відео
Щоб переконатися, що модель працює правильно, ви можете використати моє тестове відео.
1. **Завантажте тестове відео:** 📥 **[Завантажити video_test.mp4](https://youtube.com/shorts/WpaYRwc7CQA)** *(Збережіть його в папку з проєктом)*

#### 3. Встановлення залежностей
```bash
pip install ultralytics opencv-python
```
**Підготуйте відео:** Покладіть ваше відео (test_video.mp4) у папку з проєктом.
#### 4 Запустіть  розпізнавання:
  Ви можете запустити детекцію однією командою в терміналі:
 ```bash
 python yolo_inf.py
 ```
### 🧪 Тестування на власному відео 
**Увага!Всі файли повинно знаходитися в одній папці**
Щоб протестувати модель на власному комп'ютері, виконайте наступні кроки:

#### 1. Клонування репозиторію
```bash
git clone [https://github.com/kloktadanyil/yolov8-object-detection.git](https://github.com/kloktadanyil/yolov8-object-detection.git)
```
```bash
cd yolov8-object-detection
```
#### 2. Встановлення залежностей
```bash
pip install ultralytics
```
#### 3. Запуск розпізнавання 
Створіть файл main.py та вставте туди цей код, щоб запустити детекцію на вашому відео або через веб-камеру:
```python
from ultralytics import YOLO

# Завантаження натренованої моделі
model = YOLO("best.pt")

# Запуск на відеофайлі
model.predict(source="path/to/your/video.mp4", show=True, conf=0.5)
```

# yolov8-object-detection
Object detection pipeline using YOLOv8 and Roboflow. Includes training notebooks and inference scripts.

🛠 Технологічний стек
Модель: YOLOv8 (Ultralytics)

Мова: Python

Дані: Roboflow (анотація та аугментація)

Середовище навчання: Google Colab
