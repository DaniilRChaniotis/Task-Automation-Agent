from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QLineEdit, QListWidget


app = QApplication([])


main_window = QMainWindow()
main_window.setWindowTitle("Task Automation Agent")
main_window.resize(400, 400)


label = QLabel("Welcome to your Task Automation Agent!", main_window)
label.move(50, 20)
label.resize(300, 50)


input_field = QLineEdit(main_window)
input_field.move(50, 80)
input_field.resize(300, 30)


button_show = QPushButton("Show Text", main_window)
button_show.move(50, 130)


task_list = QListWidget(main_window)
task_list.move(50, 200)
task_list.resize(300, 120)

button_add_task = QPushButton("Add Task", main_window)
button_add_task.move(50, 330)

def update_label():
    text = input_field.text()
    label.setText(text)
    label.resize(300, 50)

def add_task():
    task = input_field.text()  
    if task:  
        task_list.addItem(task)
        input_field.clear()

button_show.clicked.connect(update_label)  
button_add_task.clicked.connect(add_task)  

main_window.show()

app.exec_()
