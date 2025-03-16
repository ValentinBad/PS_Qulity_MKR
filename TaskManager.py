import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QListWidget, QVBoxLayout, QPushButton, QWidget, QInputDialog, QMessageBox
from PyQt6.QtGui import QDragEnterEvent, QDropEvent, QDrag
from PyQt6.QtCore import Qt, QMimeData
from PyQt6.QtCore import pyqtSignal

# Клас для створення списку завдань з можливістю перетягування
class TaskList(QListWidget):
    itemAdded = pyqtSignal()  # Оголошуємо сигнал

    def __init__(self):
        super().__init__()
        self.setAcceptDrops(True)  
        self.setDragEnabled(True) 
        self.setSelectionMode(QListWidget.SelectionMode.SingleSelection)
        self.setDefaultDropAction(Qt.DropAction.MoveAction)

    def addItem(self, text):
        super().addItem(text)  # Викликаємо стандартний метод додавання
        self.itemAdded.emit()  # Відправляємо сигнал після додавання
        
    # Метод для початку перетягування
    def startDrag(self, supportedActions):
        item = self.currentItem() 
        if item:
            mime_data = QMimeData()   
            mime_data.setText(item.text()) 
            drag = QDrag(self)  
            drag.setMimeData(mime_data)  # Додаємо дані до перетягування
            if drag.exec(Qt.DropAction.MoveAction) == Qt.DropAction.MoveAction:  # Якщо перетягування виконано
                self.takeItem(self.row(item))  
    
    # Метод для обробки події перетягування при вході об'єкта
    def dragEnterEvent(self, event: QDragEnterEvent):
        if event.mimeData().hasText():  # Якщо є текстові дані
            event.acceptProposedAction() 
    
    # Метод для обробки події перетягування при переміщенні
    def dragMoveEvent(self, event: QDropEvent):
        event.acceptProposedAction()  # Підтверджуємо запропоновану дію
    
    # Метод для обробки події після падіння елемента
    def dropEvent(self, event: QDropEvent):
        text = event.mimeData().text()  
        self.addItem(text) 
        event.acceptProposedAction()  

# Головний клас для керування завданнями
class TaskManager(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Task Manager")  # Встановлюємо заголовок вікна
        self.setGeometry(100, 100, 600, 400)  # Встановлюємо розміри вікна
        
        # Створюємо три списки завдань: "To Do", "In Progress", "Done"
        self.lists = {"To Do": TaskList(), "In Progress": TaskList(), "Done": TaskList()}
        
        layout = QVBoxLayout()  # Створюємо вертикальний лейаут для розміщення елементів
        # Додаємо списки та кнопки для кожної категорії завдань
        for name, widget in self.lists.items():
            layout.addWidget(widget)  # Додаємо список
            btn_add = QPushButton(f"Add to {name}")  # Кнопка для додавання завдання
            btn_add.clicked.connect(lambda checked, n=name: self.add_task(n))  # Підключаємо подію на натискання
            layout.addWidget(btn_add)
            
            btn_edit = QPushButton(f"Edit {name}")  # Кнопка для редагування завдання
            btn_edit.clicked.connect(lambda checked, n=name: self.edit_task(n))  # Підключаємо подію редагування
            layout.addWidget(btn_edit)
        
        container = QWidget()  # Створюємо контейнер для всіх віджетів
        container.setLayout(layout)  # Встановлюємо лейаут для контейнера
        self.setCentralWidget(container)  # Встановлюємо контейнер як центральний віджет
    
    # Метод для додавання нового завдання до списку
    def add_task(self, list_name):
        text, ok = QInputDialog.getText(self, "New Task", "Enter task name:")  # Відображаємо діалог для введення назви
        if ok and text:  # Якщо користувач ввів текст і натиснув ОК
            self.lists[list_name].addItem(text)  
    
    # Метод для редагування існуючого завдання
    def edit_task(self, list_name):
        selected_item = self.lists[list_name].currentItem()  # Отримуємо вибраний елемент
        if selected_item:
            new_text, ok = QInputDialog.getText(self, "Edit Task", "Modify task:", text=selected_item.text())  # Діалог редагування
            if ok and new_text:  # Якщо текст змінено
                selected_item.setText(new_text)  
        else:
            QMessageBox.warning(self, "Warning", "Select a task to edit.")  # Якщо завдання не вибрано, виводимо попередження
    
# Основна частина програми
if __name__ == "__main__":
    app = QApplication(sys.argv)  # Створюємо об'єкт застосунку
    window = TaskManager()  # Створюємо головне вікно
    window.show()  # Відображаємо вікно
    sys.exit(app.exec())  # Запускаємо цикл подій застосунку
    