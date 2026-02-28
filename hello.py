import sys
import os

print(f"Python version: {sys.version}")
print(f"Interpreter path: {sys.executable}")

if 'venv' in sys.executable:
    print("✅ Статус: Работаем в виртуальном окружении (Venv)")
else:
    print("⚠️ Статус: Используется системный Python (не критично, но venv лучше)")