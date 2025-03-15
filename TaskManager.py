import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QListWidget, QVBoxLayout, QPushButton, QWidget, QInputDialog, QMessageBox
from PyQt6.QtGui import QDragEnterEvent, QDropEvent, QDrag
from PyQt6.QtCore import Qt, QMimeData

class TaskList(QListWidget):
    def __init__(self):
        super().__init__()
        self.setAcceptDrops(True)
        self.setDragEnabled(True)
        self.setSelectionMode(QListWidget.SelectionMode.SingleSelection)
        self.setDefaultDropAction(Qt.DropAction.MoveAction)
    
    def startDrag(self, supportedActions):
        item = self.currentItem()
        if item:
            mime_data = QMimeData()
            mime_data.setText(item.text())
            drag = QDrag(self)
            drag.setMimeData(mime_data)
            if drag.exec(Qt.DropAction.MoveAction) == Qt.DropAction.MoveAction:
                self.takeItem(self.row(item))
    
    def dragEnterEvent(self, event: QDragEnterEvent):
        if event.mimeData().hasText():
            event.acceptProposedAction()
    
    def dragMoveEvent(self, event: QDropEvent):
        event.acceptProposedAction()
    
    def dropEvent(self, event: QDropEvent):
        text = event.mimeData().text()
        self.addItem(text)
        event.acceptProposedAction()

class TaskManager(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Task Manager")
        self.setGeometry(100, 100, 600, 400)
        
        self.lists = {"To Do": TaskList(), "In Progress": TaskList(), "Done": TaskList()}
        
        layout = QVBoxLayout()
        for name, widget in self.lists.items():
            layout.addWidget(widget)
            btn_add = QPushButton(f"Add to {name}")
            btn_add.clicked.connect(lambda checked, n=name: self.add_task(n))
            layout.addWidget(btn_add)
            
            btn_edit = QPushButton(f"Edit {name}")
            btn_edit.clicked.connect(lambda checked, n=name: self.edit_task(n))
            layout.addWidget(btn_edit)
        
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)
    
    def add_task(self, list_name):
        text, ok = QInputDialog.getText(self, "New Task", "Enter task name:")
        if ok and text:
            self.lists[list_name].addItem(text)
    
    def edit_task(self, list_name):
        selected_item = self.lists[list_name].currentItem()
        if selected_item:
            new_text, ok = QInputDialog.getText(self, "Edit Task", "Modify task:", text=selected_item.text())
            if ok and new_text:
                selected_item.setText(new_text)
        else:
            QMessageBox.warning(self, "Warning", "Select a task to edit.")
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TaskManager()
    window.show()
    sys.exit(app.exec())