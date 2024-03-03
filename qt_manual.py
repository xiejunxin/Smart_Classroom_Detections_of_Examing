# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dc6.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow_1(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(850, 600)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("manual.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.manual_browser = QtWidgets.QTextBrowser(self.centralwidget)
        self.manual_browser.setStyleSheet("")
        self.manual_browser.setObjectName("manual_browser")
        self.verticalLayout.addWidget(self.manual_browser)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "用户使用手册"))
        self.manual_browser.setHtml(_translate("MainWindow",
                                               "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" "
                                               "\"http://www.w3.org/TR/REC-html40/strict.dtd\">\n "
                                               "<html><head><meta name=\"qrichtext\" content=\"1\" /><title>产品名称 - "
                                               "用户使用手册</title><style type=\"text/css\">\n "
                                               "p, li { white-space: pre-wrap; }\n"
                                               "</style></head><body style=\" font-family:\'SimSun\'; "
                                               "font-size:9.07563pt; font-weight:400; font-style:normal;\">\n "
                                               "<h1 align=\"center\" style=\" margin-top:18px; margin-bottom:12px; "
                                               "margin-left:0px; margin-right:0px; -qt-block-indent:0; "
                                               "text-indent:0px;\"><span style=\" font-size:9pt; font-weight:600; "
                                               "color:#0000ff;\">考场异常行为检测系统</span></h1>\n "
                                               "<h1 align=\"center\" style=\" margin-top:18px; margin-bottom:12px; "
                                               "margin-left:0px; margin-right:0px; -qt-block-indent:0; "
                                               "text-indent:0px;\"><span style=\" font-size:9pt; font-weight:600; "
                                               "color:#0000ff;\">用户使用手册 </span><span style=\" font-size:9pt; "
                                               "font-weight:600;\"> </span></h1>\n "
                                               "<p style=\" margin-top:0px; margin-bottom:12px; margin-left:0px; "
                                               "margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span "
                                               "style=\" font-size:16pt; font-weight:600;\">1.视频播放与解析</span></p>\n "
                                               "<p style=\" margin-top:0px; margin-bottom:12px; margin-left:0px; "
                                               "margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span "
                                               "style=\" font-size:12pt;\">  "
                                               "本项目程序的界面应用采用PyQt5进行可视化开发，由于PyQt5"
                                               "本身兼容性和解码等问题的存在，当您使用我们的应用程序选择视频进行上传时，若上传的视频非以“.avi"
                                               "”格式为后缀的视频文件，比如现在常见的“.mp4"
                                               "”格式的视频，将会出现在应用页面无法播放的问题，主要表现为上传视频后主播放器没有反应，为了能够在本应用程序中能够正常播放非“.avi"
                                               "”格式的视频，我们推荐您在自己的系统上安装一个解码器，安装过程附在后面。不过不用担心，这对于核心功能的使用并不会产生影响，考虑到本项目应用的目的是对上传的考场视频进行异常行为的检测，即使无法在窗口内播放，您依旧可以正常上传视频文件并进行异常行为的检测过程，并将结果下载保存到本地后播放观看效果。</span></p>\n "
                                               "<p style=\" margin-top:0px; margin-bottom:12px; margin-left:0px; "
                                               "margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span "
                                               "style=\" font-size:12pt;\">  解码器的安装：我们推荐您安装K-Lite Codec Pack "
                                               "Basic解码器，当然其他的解码器您也可以根据情况自行进行安装，以K-Lite Codec Pack "
                                               "Basic解码器为例，进入安装官网：</span><span style=\" font-size:12pt; "
                                               "color:#0000ff;\">https://www.codecguide.com/download_k"
                                               "-lite_codec_pack_basic.htm</span><span style=\" font-size:12pt; "
                                               "color:#000000;\">，选择“Download”下的“Server "
                                               "1”点击下载即可。考虑到可能会出现部分浏览器对于陌生程序的下载拦截，下载完成后在浏览器的下载器中对此程序选择信任并保留，然后执行安装过程即可，安装流程一直选择“next”直至安装成功。</span></p>\n "
                                               "<p style=\" margin-top:0px; margin-bottom:12px; margin-left:0px; "
                                               "margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span "
                                               "style=\" font-size:16pt; font-weight:600;\">2.视频保存</span></p>\n "
                                               "<p style=\" margin-top:0px; margin-bottom:12px; margin-left:0px; "
                                               "margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span "
                                               "style=\" font-size:12pt;\">  "
                                               "在系统处理完视频后，您将进入处理后的新页面，这里你可以选择保存处理完成后的视频，我们为您提供了两个版本可供下载，一个是含有骨骼点框架的版本，另一个是不含有骨骼点框架的版本，当你选择使用其一进行保存时，我们将会需要您选择一个文件的保存位置，考虑到视频的兼容性和保存过程的正常进行，防止系统崩溃，我们将要求您在选择一个合适的文件保存位置之后并对保存后的视频文件进行命名，名称因您而定，但请务必为文件名称增加后缀名“.avi”，比如您要保存的视频文件选择命名为“output”,请在文件名那里输入完整的“output.avi”，如此方可顺利成功保存，给您带来的不便敬情谅解。</span></p>\n "
                                               "<p style=\" margin-top:0px; margin-bottom:12px; margin-left:0px; "
                                               "margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span "
                                               "style=\" font-size:16pt; font-weight:600;\">3.视频检测程序</span></p>\n "
                                               "<p style=\" margin-top:0px; margin-bottom:12px; margin-left:0px; "
                                               "margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span "
                                               "style=\" font-size:12pt;\">  "
                                               "由于视频检测的过程需要消耗大量的算力资源，因此我们不建议您在检测处理一个视频还没有结束的过程中就再次点击处理，这将极容易造成计算机系统卡顿和程序的崩溃，为保证用户的使用体验，在用户选择一种方法进行处理时，我们将取消用户对原窗口的一些特定按钮的交互和反馈。另外，由于Python内置的一些模块使用过程的不可预估和防范的问题的存在，以及考虑到程序内部双线程的实现逻辑，当您处理完一个视频并在处理窗口看到了处理之后的效果，并选择了想要的视频处理版本完成下载，请务必点击当前处理窗口的“退出”按钮再进行第二轮的处理，为保证您的使用体验，在开启第二个窗口后若您没有点击“退出”按钮，将取消对原窗口的交互，给您带来的不便敬请谅解。</span></p>\n "
                                               "<p style=\" margin-top:0px; margin-bottom:12px; margin-left:0px; "
                                               "margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span "
                                               "style=\" font-size:16pt; font-weight:600;\">4.使用建议</span></p>\n "
                                               "<p style=\" margin-top:0px; margin-bottom:12px; margin-left:0px; "
                                               "margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span "
                                               "style=\" font-size:12pt;\">  "
                                               "在使用本应用程序的过程中，开发组建议您按照如下的流程进行使用，首先点击“选择视频源”上传一个本地的视频文件，如果您安装了1"
                                               ".中的解码器，那么任一合规的视频文件都将被正确载入并在窗口内播放，否则将只能载入并播放“.avi"
                                               "”格式的视频，不过这不会影响后续视频的处理，仅决定是否可以载入播放。</span></p>\n "
                                               "<p style=\" margin-top:0px; margin-bottom:12px; margin-left:0px; "
                                               "margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span "
                                               "style=\" font-size:12pt;\">  "
                                               "“播放”和“暂停”以及视频下方的进度条均可以对被正确载入和播放的视频进行控制，拖拽进度条可以将视频的进度进行自定义的定位。</span"
                                               "></p>\n "
                                               "<p style=\" margin-top:0px; margin-bottom:12px; margin-left:0px; "
                                               "margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span "
                                               "style=\" font-size:12pt;\">  "
                                               "在选择核心功能“检测异常行为”之前，请至少勾选一种检测方式，我们开发组为用户提供了4"
                                               "种方式以供选择，并且支持四种方式的任意组合，您可以根据自己想要的方法进行组合并且进行尝试。然后点击该按钮，由于处理过程比较消耗算力资源，因此需要一个较长时间的等待，为了让用户清楚进度，我们将会为您载入进度可视化。此外，如果用户在处理视频时，对于同一个视频选择了同一种检测方式，我们的系统将会保存上一次的检测结果，以至于您不会在重复处理时进行第二次无意义的等待。</span></p>\n "
                                               "<p style=\" margin-top:0px; margin-bottom:12px; margin-left:0px; "
                                               "margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span "
                                               "style=\" font-size:12pt;\">  "
                                               "当处理过程结束后将弹出第二个窗口，在这里你可以选择查看处理之后的视频，并可以选择是否有骨骼点的版本进行下载，将视频保存到本地。在右上角的“异常行为检测情况”一栏中，我们为用户提供了对视频处理过程中疑似出现异常行为的时刻进行提示的功能，在这里用户可以看到上传的视频在哪些时刻可能出现了异常行为，方便用户进行定位和查证。</span></p>\n "
                                               "<p style=\" margin-top:0px; margin-bottom:12px; margin-left:0px; "
                                               "margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span "
                                               "style=\" font-size:12pt;\">  "
                                               "最后，点击各窗口的“退出”按钮后可以退出本窗口，出于人性化和使用体验的考虑，“退出”按钮点击将会增加一个对话框，以让用户确定是否退出当前窗口。若用户选择了退出主窗口，那么此时在进行的所有进程都会被中断，并关闭所有窗口，包括正在进行的进度条提示。另外，出于系统程序执行过程中需要进行的准备工作和对计算资源的充分使用，我们建议您在进行视频处理的过程中不要过于频繁地对应用进行交互，比如“频繁点击处理按钮并取消然后重复”这样的行为我们并不建议。</span></p>\n "
                                               "<p style=\" margin-top:0px; margin-bottom:12px; margin-left:0px; "
                                               "margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span "
                                               "style=\" font-size:16pt; font-weight:600;\">5.项目介绍</span></p>\n "
                                               "<p style=\" margin-top:0px; margin-bottom:12px; margin-left:0px; "
                                               "margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span "
                                               "style=\" font-size:12pt;\">  "
                                               "本项目是由来自南京航空航天大学（NUAA"
                                               "）计算机科学与技术学院的四名本科生进行的大学生创新创业训练项目的产品，创作意义在于使用现有的先进的计算机科学技术，对于考场中的异常行为进行检测和监控，省去事后大量人力检查考场监控视频的资源消耗，不过由于技术和条件有限，以及场景的限制，对于很多考场情况下的细微异常行为动作目前还没有办法进行检测，希望能在未来得到一定程度的改进。</span></p>\n "
                                               "<p style=\" margin-top:0px; margin-bottom:12px; margin-left:0px; "
                                               "margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span "
                                               "style=\" font-size:12pt;\">  "
                                               "本项目完全开源，欢迎各位仁人志士参与本项目的改进和修改，使之更加完备和先进，这是项目的开源地址：</span><span style=\" "
                                               "font-size:12pt; "
                                               "color:#0000ff;\">https://github.com/xiejunxin/OSKernel2023-DbStars"
                                               ".git</span><span style=\" font-size:12pt; color:#000000;\">，期待您的pull "
                                               "requests。</span></p>\n "
                                               "<p style=\"-qt-paragraph-type:empty; margin-top:0px; "
                                               "margin-bottom:12px; margin-left:0px; margin-right:0px; "
                                               "-qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p>\n "
                                               "<p style=\" margin-top:0px; margin-bottom:12px; margin-left:0px; "
                                               "margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span "
                                               "style=\" "
                                               "font-size:12pt"
                                               ";\">如果您在使用中遇到任何问题，欢迎反馈给开发组，我们收到后将会第一时间进行修改和矫正，这是我们的联系邮箱：</span><span "
                                               "style=\" font-size:12pt; "
                                               "color:#0000ff;\">1833610970@qq.com</span><span style=\" "
                                               "font-size:12pt; color:#000000;\">.</span></p>\n "
                                               "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; "
                                               "margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span "
                                               "style=\" font-family:\'-apple-system\',\'BlinkMacSystemFont\',"
                                               "\'Helvetica Neue\',\'PingFang SC\',\'Microsoft YaHei\',\'Source Han "
                                               "Sans SC\',\'Noto Sans CJK SC\',\'WenQuanYi Micro Hei\',"
                                               "\'sans-serif\'; font-size:10pt; color:#191b1f; "
                                               "background-color:#ffffff;\">Copyright ©2023-2024 NUAA Project Team "
                                               "Composed of Xie Junxin,Chen Yan,Tang Jiayu And Chen Qiuyu,All Rights "
                                               "Reserved.</span></p></body></html>"))


class Manual(QtWidgets.QMainWindow):
    def __init__(self):
        super(Manual, self).__init__()
        self.ui = Ui_MainWindow_1()
        self.ui.setupUi(self)
