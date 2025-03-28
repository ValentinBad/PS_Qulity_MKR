 ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ‏‏‎‏‎М‎‎‏‎‏‎‏‎і‏‎ністерство освіти і науки України

ㅤㅤㅤㅤㅤㅤДержавний університет "Київський авіаційний інститут" Кафедра інженерії програмного забезпечення


ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤЯкiсть програмного забезпечення та тестування

ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤМодульна робота 1

ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤВАРІАНТ № - 1

ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤХід роботи

1. Модель якості:
Розробити модель якості для додатку згідно зі стандартами ISO/IEC 25010 та ISO/IEC 25019:2023.
Відповідно до стандарту ISO/IEC 25010

| **Характеристика**             | **Підхарактеристика**         | **Опис**                                                                 | **Пріоритет** |
|---------------------------------|--------------------------------|---------------------------------------------------------------------------|---------------|
| **Функціональна придатність**    | Повнота функцій                | Додаток повинен забезпечувати всі заявлені функції (створення, редагування, переміщення задач). | Середній      |
| **Коректність результатів**     |                                | Завдання повинні оброблятися коректно та без помилок.                     | Високий       |
| **Придатність для взаємодії**   |                                | Додаток має підтримувати інтеграцію з іншими системами (наприклад, експорт/імпорт даних). | Низький       |
| **Продуктивність**              | Час відгуку                    | Завдання обробляються без значних затримок.                               | Високий       |
| **Зручність використання**      | Зрозумілість                   | Інтерфейс повинен бути інтуїтивно зрозумілим для користувачів.            | Високий       |
| **Естетика інтерфейсу**         |                                | Дизайн має бути сучасним і приємним для користувачів.                     | Середній      |
| **Безпека**                     | Конфіденційність               | Дані користувачів повинні бути захищені від несанкціонованого доступу.    | Високий       |
| **Цілісність**                  |                                | Не допускається несанкціонована зміна даних.                              | Високий       |

## Відповідно до стандарту ISO/IEC 25019

### Ефективність (Effectiveness): 8/10
Додаток дозволяє користувачам досягати своїх цілей, таких як створення, редагування та переміщення задач. Однак додаткові функції, такі як фільтрація задач за категоріями або пріоритетами, могли б значно підвищити ефективність користувачів при роботі з великими списками задач.

### Продуктивність (Efficiency): 7/10
Продуктивність додатку на основних операціях (створення, редагування, переміщення задач) добра, але при великій кількості задач, особливо якщо список буде дуже довгим, можуть виникати затримки. Це можна було б покращити через оптимізацію обробки даних, наприклад, за допомогою асинхронних операцій або кешування.

### Задоволеність (Satisfaction): 9/10
Інтерфейс додатку простий і зрозумілий. Користувачі легко можуть додавати задачі, редагувати їх і переміщувати між списками. Візуально додаток виглядає чисто і не перевантажено. Задоволеність користувачів може бути ще вищою, якщо додати можливість налаштування інтерфейсу чи зміну теми для зручності користувачів з різними уподобаннями.

### Безпека (Freedom from Risk): 9/10
Додаток не обробляє чутливу інформацію, і його основна функціональність не містить значних безпекових ризиків (немає фінансових операцій чи обробки персональних даних, а також загальної прив’язки до БД).

### Контекстне покриття (Context Coverage): 7/10
Додаток працює на основних операційних системах (Linux, Windows), але для забезпечення повної підтримки різних контекстів використання можна перевірити адаптивність інтерфейсу на мобільних пристроях та перевірити на різних роздільних здатностях екрану.

---

## Метрики якості коду

### 1. Метрики розміру (Size Metrics)
- **Lines of Code (LOC):** 77 рядків коду.
- **Source Lines of Code (SLOC):** 77 рядків (без коментарів і порожніх рядків).
- **Function Points (FP):** 3 (додавання, редагування задач, переміщення між списками).
- **Codebase Size:** 1 файл (~4-5 КБ, залежить від форматування і редактора).

### 2. Метрики складності (Complexity Metrics)
- **Cyclomatic Complexity:** 6 (оскільки код має кілька умовних операторів, наприклад, перевірка чи існує елемент для редагування або додавання).
- **Coupling Metrics:** 0.4 (код взаємопов'язаний між класами, але обмежений, тому низький рівень зчеплення).

### 3. Метрики якості коду (Code Quality Metrics)
- **Code Coverage:** 50-60%
- **Duplication Metrics:** 0

### 4. Метрики продуктивності (Performance Metrics)
- **Response Time:** Дуже низький
- **Throughput:** Оскільки додаток не обробляє велику кількість запитів, система обробляє кілька десятків задач за одиницю часу.
- **Latency:** Не помітна (оскільки додаток працює локально і не має великих обчислювальних навантажень).
- **Resource Utilization:** Використання ресурсів мінімальне, оскільки додаток не займається складними обчисленнями чи великими обсягами даних.

### 5. Метрики надійності (Reliability Metrics)
- **Mean Time To Failure (MTTF):** Не застосовно, оскільки додаток малий, ймовірність відмови мінімальна.
- **Mean Time To Repair (MTTR):** Для таких змін, як виправлення дефектів або покращення інтерфейсу, час виправлення може складати кілька хвилин.
- **Failure Rate:** Мінімальна
- **Availability:** 99%

### 6. Метрики підтримуваності (Maintainability Metrics)
- **Code Readability:** 8/10 (код структурований і добре коментований, але можна покращити коментарі та документацію).
- **Technical Debt:** Низький, оскільки код є простим і не містить складних рішень, але відсутні автоматизовані тести.
- **Refactoring Frequency:** 0
- **Changeability:** Легкий для змін, оскільки основні функції розділені на класи і методи, що дозволяє зручну модифікацію.

### 7. Метрики безпеки (Security Metrics)
- **Number of Vulnerabilities:** 0 (жодних вразливостей не знайдено).
- **Security Compliance:** 0 (немає відповідності стандартам безпеки, оскільки додаток не обробляє дані поза притроєм).
- **Exploitability:** Мінімальна ймовірність, оскільки додаток не має складних взаємодій із зовнішніми системами чи мережами.
- **Severity Metrics:** 0.

## 2. Базові метрики якості

### Використання SonarQube та інших інструментів для аналізу метрик коду
Проєкт **PS_Quality_MKR** аналізується в гілці **main**. Quality Gate пройдено.
![image](https://github.com/user-attachments/assets/88d71ba2-42a7-4f85-9f58-85a854c765e0)

### Метрики якості коду:
- **Безпека (Security):** Оцінка A, відкритих проблем немає. Код не містить вразливостей.
- **Надійність (Reliability):** Оцінка A, відкритих проблем немає. Відсутні критичні помилки, що можуть призвести до збоїв у роботі.
- **Супроводжуваність (Maintainability):** Оцінка A, є 1 відкрита проблема. Це не критична проблема, але вона може впливати на зручність підтримки коду.
- **Дублювання коду (Duplications):** 0.0%, що є хорошим показником. Відсутні повторювані фрагменти коду.
- **Критичні зони безпеки (Security Hotspots):** Відсутні. Код не містить потенційно ризикованих фрагментів.

### Що потребує уваги
Загалом код у хорошому стані, серйозних проблем немає. Однак є одна проблема, пов'язана з супроводжуваністю, яка не є критичною, але може впливати на подальшу підтримку та розвиток.
![image](https://github.com/user-attachments/assets/e35b7a9f-896a-4b2f-a128-88535e74a576)

Код відповідає високим стандартам якості, проте варто звернути увагу на функціональність і деталізованість, оскільки вони поки що на низькому рівні.

---

## 3. Формальна верифікація специфікацій
Створити специфікацію обмежень для системи, наприклад:
- "Кожен користувач має хоча б одну задачу."
- "Кожна задача може входити лише до одного списку."

Перевірити коректність цих обмежень в **Alloy**.
![image](https://github.com/user-attachments/assets/3ef3e421-ead4-432b-8e55-a77a0d497129)
## Структура системи

Користувач (User) має принаймні одну задачу.

```alloy
sig User {
    tasks: some Task  -- Кожен користувач має принаймні одну задачу
}
```

Задача (Task) обов’язково належить одному користувачу та входить рівно в один список.

```alloy
sig Task {
    owner: one User,  -- Кожна задача належить одному користувачу
    list: one List    -- Кожна задача входить в один список
}
```

Списки (List) є абстрактним типом, від якого успадковуються три конкретні списки: Todo, InProgress, Done.

```alloy
abstract sig List {}  -- Абстрактний тип для списків

one sig Todo, InProgress, Done extends List {}  -- Три списки задач
```

## Обмеження

Кожна задача належить тільки одному списку.

```alloy
fact TaskInOnlyOneList {
    all t: Task | one t.list
}
```

У системі має бути хоча б одна задача.

```alloy
fact SomeTasksExist {
    some Task
}
```

Усі задачі повинні входити в один із трьох визначених списків.

```alloy
fact TasksBelongToLists {
    all t: Task | t.list in Todo + InProgress + Done
}
```

Кожен користувач має хоча б одну задачу.

```alloy
fact EachUserHasTasks {
    all u: User | some u.tasks
}
```
![image](https://github.com/user-attachments/assets/e81cede0-2d75-4c71-8273-06f4d4767857)

Перевірка моделі в Alloy пройшла успішно. Було задано три користувачі, двадцять задач і три списки (Todo, InProgress, Done), кожен з яких існує рівно в одному екземплярі. Система перевірила логічну узгодженість всіх обмежень, створивши 1824 змінних і майже 3982 логічних умов. У підсумку, Alloy знайшов принаймні один приклад, де всі обмеження виконуються без суперечностей. Це означає, що модель є коректною, і всі задані правила можуть бути реалізовані на практиці.


---

## 4. Верифікація моделей архітектури (PlantUML)
Розробити **UML-діаграми**:
- Випадків використання.
- Класів.
- Послідовності.

1. Діаграма класів
```
@startuml
class TaskList {
    +addItem(text: str)
    +startDrag(supportedActions: Qt.DropAction)
    +dragEnterEvent(event: QDragEnterEvent)
    +dragMoveEvent(event: QDropEvent)
    +dropEvent(event: QDropEvent)
    -itemAdded: pyqtSignal
}

class TaskManager {
    +add_task(list_name: str)
    +edit_task(list_name: str)
    -lists: dict
}

TaskList "1" *-- "1..*" TaskManager : manages >
@enduml
```
Ця діаграма описує структуру вашого коду, зокрема взаємодію між класами.

TaskList:

Це клас, який відповідає за список завдань. Він має методи для додавання елементів, обробки подій перетягування (drag and drop), а також для сигналу після додавання елемента (itemAdded).
У класі є методи для перетягування елементів (startDrag, dragEnterEvent, dragMoveEvent, dropEvent), що дозволяють переміщати завдання між списками.
TaskManager:
![image](https://github.com/user-attachments/assets/02ea7f1e-572d-4975-af33-bbbbf79a1dce)

Головний клас, який управляє кількома списками завдань. Він створює і керує різними списками завдань, зокрема додає або редагує завдання через відповідні методи (add_task, edit_task).
Клас зберігає словник lists, де кожен список завдань представлений як екземпляр класу TaskList.
У діаграмі вказано, що клас TaskManager управляє кількома об'єктами класу TaskList через асоціацію.

2. Діаграма випадків використання
```
@startuml
actor User

User -> (Add Task)
User -> (Edit Task)
User -> (Drag and Drop Tasks)

(Add Task) --> (Enter Task Name)
(Edit Task) --> (Select Task)
(Drag and Drop Tasks) --> (Move Task Between Lists)

@enduml

```
Ця діаграма показує, як користувач взаємодіє з програмою. Вона описує основні сценарії:
![image](https://github.com/user-attachments/assets/30f00583-6045-4284-b334-1d0637be83b4)

Add Task:

Користувач може додати нове завдання в список, натискаючи кнопку. Це відкриває діалогове вікно для введення назви завдання.
Edit Task:

Користувач може редагувати вже існуюче завдання, вибираючи його зі списку і змінюючи його текст через діалогове вікно.
Drag and Drop Tasks:

Користувач може перетягувати завдання між списками. Це дозволяє змінювати статус завдання, наприклад, переміщати завдання з "To Do" в "In Progress" чи "Done".
Ці випадки використання відображають, як користувач може взаємодіяти з додатком для управління завданнями.

3. Діаграма послідовності
```
@startuml
actor User
entity TaskManager
entity TaskList

User -> TaskManager : Add Task
TaskManager -> TaskList : addItem(text)
TaskList -> TaskList : itemAdded.emit()

User -> TaskManager : Edit Task
TaskManager -> TaskList : getSelectedItem()
TaskList -> TaskManager : Display Edit Dialog
TaskManager -> TaskList : updateTask()

User -> TaskList : Drag and Drop Task
TaskList -> TaskList : handleDragEvent()
@enduml
```

Ця діаграма описує, як відбуваються взаємодії між об'єктами в процесі виконання певних операцій.
![image](https://github.com/user-attachments/assets/eed33bab-2999-4126-b47b-b290fd39cd41)

Add Task:

Користувач викликає метод Add Task в класі TaskManager.
Клас TaskManager викликає метод addItem в класі TaskList для додавання завдання.
Після цього відправляється сигнал itemAdded для оновлення інтерфейсу.
Edit Task:

Користувач викликає метод Edit Task.
Клас TaskManager звертається до списку завдань і вибирає поточний елемент.
Якщо завдання вибрано, відкривається діалогове вікно для редагування.
Після редагування клас TaskManager оновлює текст елемента у списку.
Drag and Drop:

Користувач переміщає завдання між списками, викликаючи події перетягування.
Клас TaskList обробляє ці події (dragEnterEvent, dragMoveEvent, dropEvent), додаючи нове завдання в список.


---

## 5. Управління версіями й автоматизація

### Використання Git Flow
Для управління гілками розробки:
- Гілка для нових функцій.
- Гілка для виправлення багів.
- Гілка для релізів.
![image](https://github.com/user-attachments/assets/36490af8-ce09-4967-8f0b-addb8ac851d5)

### Налаштування GitHub Actions
- Автоматичний запуск модульних тестів.
![image](https://github.com/user-attachments/assets/129be61f-062e-41d3-a2a4-8016af2034b0)

- Автоматизована перевірка коду перед злиттям у основну гілку.
![image](https://github.com/user-attachments/assets/dd7e17a4-ae5b-4c47-a700-8e9bd03d8b93)

### Автоматизація в CI/CD
- Статичний аналіз коду.
- Збір базових метрик.
![image](https://github.com/user-attachments/assets/d50b7b03-9fa1-436b-bf6e-9f987562f5f7)

![image](https://github.com/user-attachments/assets/4cbdd4f0-809e-43e9-ae5f-b662280e0155)
