import sys
import os
sys.path.append('/home/valentin/QPZ_MKR')
import pytest
from PyQt6.QtWidgets import QApplication, QMainWindow, QInputDialog, QListWidget
from TaskManager import TaskManager


# Тест для методу add_task
def test_add_task(qtbot):
    manager = TaskManager()  # Створюємо екземпляр головного вікна
    qtbot.addWidget(manager)  # Додаємо вікно в тестування

    initial_count = manager.lists["To Do"].count()  # Отримуємо кількість елементів до додавання
    
    # Імітуємо введення через QInputDialog
    with qtbot.waitSignal(manager.lists["To Do"].itemAdded):  # Чекаємо на сигнал itemAdded
        manager.add_task("To Do")  # Викликаємо метод для додавання завдання
    
    # Перевіряємо, чи кількість елементів збільшилася на 1
    assert manager.lists["To Do"].count() == initial_count + 1
