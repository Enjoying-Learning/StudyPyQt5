## 学习笔记

- [x] [1. 使用 vscode 从零开始学习 PyQt5](https://www.jianshu.com/p/c37c5b1c9a5e)
- [x] [2. 使用 vscode 从零开始学习 PyQt5（二）](https://www.jianshu.com/p/6118e29e3051)

## PyQt5 主要类介绍

PyQt5 API 拥有 620 多个类和 6000 个函数。它是一个跨平台的工具包，可以运行在所有主流的操作系统上，包括 Windows、Linux 和 Mac OS。下面介绍一些常用的类：

- [x] `QObject`：在类层次结构中是顶级类（Top Class），它是所有 PyQt 对象的基类。
- [x] `QPaintDevice`：所有可绘制的对象的基类。
- [x] `QApplication`：用于管理图形用户界面应用程序的控制流和主要设置。它包含主事件循环，对来自窗口系统和其他资源的所有事件进行处理和调度；它也对应用程序的初始化和结束进行处理，并且提供对话管理；还对绝大多数系统范围和应用程序范围的设置进行处理。
- [x] `QWidget`：所有用户界面对象的基类。`QDialog` 类和 `QFrame` 类继承自 `QWidget` 类，这两个类有自己的子类系统（Sub-Class System）。
- [x] `QFrame`：有框架的窗口控件的基类。它也被用来直接创建没有任何内容的简单框架，但是通常要用到 `QHBox` 或 `QVBox`，因为它们可以自动布置放到框架中的窗口控件。
- [x] `QMainWindow`：提供一个有菜单栏、锚接窗口（如工具栏）和状态栏的主应用程序窗口。
- [x] `QDialog`：最普通的顶级窗口。如果一个窗口控件没有被嵌入到父窗口控件中，那么该窗口控件就被称为顶级窗口控件。在通常情况下，顶级窗口控件是有框架和标题栏的窗口。在 Qt 中，`QMainWindow` 和不同的 `QDialog` 的子类是最普通的顶级窗口。

下面是常用的控件。

- [x] `QLabel` 控件：用来显示文本或图像。
- [x] `QLineEdit` 窗口控件：提供了一个单页面的单行文本编辑器。
- [x] `QTextEdit` 窗口控件：提供了一个单页面的多行文本编辑器。
- [x] `QPushButton` 窗口控件：提供了一个命令按钮。
- [x] `QRadioButton` 控件：提供了一个单选钮和一个文本或像素映射标签。
- [x] `QCheckBox` 窗口控件：提供了一个带文本标签的复选框。
- [x] `QspinBox` 控件：允许用户选择一个值，要么通过按向上/向下键增加/减少当前显示值，要么直接将值输入到输入框中。
- [x] `QScrollBar` 窗口控件：提供了一个水平的或垂直的滚动条。
- [x] `QSlider` 控件：提供了一个垂直的或水平的滑动条。
- [x] `QComboBox` 控件：一个组合按钮，用于弹出列表。
- [x] `QMenuBar` 控件：提供了一个横向菜单栏。
- [x] `QStatusBar` 控件：提供了一个适合呈现状态信息的水平条，通常放在QMainWindow的底部。
- [x] `QToolBar` 控件：提供了一个工具栏，可以包含多个命令按钮，通常放在 `QMainWindow` 的顶部。
- [x] `QListView` 控件：可以显示和控制可选的多选列表，可以设置ListMode或IconMode。
- [x] `QPixmap` 控件：可以在绘图设备上显示图像，通常放在 `QLabel` 或 `QPushButton` 类中。
- [x] `Qdialog` 控件：对话框窗口的基类。

`QWidget` 是所有用户界面类的基类，它能接收所有的鼠标、键盘和其他系统窗口事件。没有被嵌入到父窗口中的 `Widget` 会被当作一个窗口来调用，当然，它也可以使用 `setWindowFlags(Qt.WindowFlags)` 函数来设置窗口的显示效果。`QWidget` 的构造函数可以接收两个参数，其中第一个参数是该窗口的父窗口；第二个参数是该窗口的 `Flag`，也就是 `Qt.WindowFlags`。根据父窗口来决定 `Widget` 是嵌入到父窗口中还是被当作一个独立的窗口来调用，根据 `Flag` 来设置 `Widget` 窗口的一些属性。

`QMainWindow`（主窗口）一般是应用程序的框架，在主窗口中可以添加所需要的 `Widget`，比如添加菜单栏、工具栏、状态栏等。主窗口通常用于提供一个大的中央窗口控件（如文本编辑或者绘制画布）以及周围的菜单栏、工具栏和状态栏。`QMainWindow` 常常被继承，这使得封装中央控件、菜单栏，工具栏以及窗口状态变得更容易，也可以使用 Qt Designer 来创建主窗口。

## QApplication类

`QApplication` 类用于管理图形用户界面应用程序的控制流和主要设置，可以说 `QApplication` 是 PyQt 的整个后台管理的命脉。任何一个使用 PyQt 开发的图形用户界面应用程序，都存在一个 `QApplication` 对象。

在 PyQt 中，可以通过如下代码载入必需的模块，获得 `QApplication` 类。

```python
from PyQt5.QtWidgets import  QApplication
```

在 PyQt 的应用程序实例中包含了 `QApplication` 类的初始化，通常放在 Python 脚本的 `if __name__ == "__main__":` 语句后面，作为主程序的入口。因为 `QApplication` 对象做了很多初始化，所以它必须在创建窗口之前被创建。

`QApplication` 类还可以处理命令行参数，在 `QApplication` 类初始化时，需要引入参数 `sys.argv`。`sys.argv` 是来自命令行的参数列表，Python 脚本可以从 shell 运行，比如用鼠标双击 `qtSample.py`，就启动了一个 PyQt 应用程序。引入 `sys.argv` 后就能让程序从命令行启动，比如在命令行中输入 `python qtSample.py`，也可以达到同样的效果。
 `QApplication` 类的初始化可以参考以下脚本引用。应用程序整体框架为：

```python
if __name__ == "__main__":
    app = QApplication(sys.argv)
    # 界面生成代码 ...

    sys.exit(app.exec_())  
```

`sys.exit()` 函数可以结束一个应用程序，使应用程序在主循环中退出。

`QApplication` 采用事件循环机制，当 `QApplication` 初始化后，就进入应用程序的主循环（Main Loop），开始进行事件处理，主循环从窗口系统接收事件，并将这些事件分配到应用程序的控件中。当调用 `sys.exit()` 函数时，主循环就会结束。

PyQt5 的应用程序是事件驱动的，比如键盘事件、鼠标事件等。在没有任何事件的情况下，应用程序处于睡眠状态。主循环控制应用程序什么时候进入睡眠状态，什么时候被唤醒。
