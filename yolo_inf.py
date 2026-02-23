import os
from ultralytics import YOLO

#  НАЛАШТУВАННЯ 
model_path = "best.pt"
video_path = "test_video.mp4" 

#  ПЕРЕВІРКА ФАЙЛІВ 
if not os.path.exists(model_path):
    print(f"❌ Помилка: Не знайдено файл моделі '{model_path}'")
    print("Будь ласка, завантажте best.pt у папку з проєктом.")
    exit()

if not os.path.exists(video_path):
    print(f"❌ Помилка: Не знайдено відео '{video_path}'")
    print("Будь ласка, покладіть тестове відео у папку з проєктом.")
    exit()

# ЗАПУСК 
print(f"🚀 Завантажую модель та починаю обробку '{video_path}'...")

try:
    model = YOLO(model_path)
    results = model.predict(source=video_path, save=True, conf=0.5, show=True)

    print("\n Роботу завершено!")
    print(f"Результати збережено в папку: {results[0].save_dir}")

except Exception as e:
    print(f"Виникла помилка під час виконання: {e}")