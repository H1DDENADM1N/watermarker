from Ui_marker import Ui_MainWindow_pic_marker
from PySide6.QtWidgets import (QApplication, QMainWindow, QFileDialog)
from PySide6.QtGui import QPixmap
import marker
import argparse
import os

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow_pic_marker()
        self.ui.setupUi(self)
        self.pic_name = None
        self.default_output = None
        self.setup_signals()

    def setup_signals(self):
        self.ui.pushButton_generate.clicked.connect(self.generate_pic)
        self.ui.action_open.triggered.connect(self.open_pic)
        self.ui.action_save.triggered.connect(self.save_pic)
        self.ui.action_save_as.triggered.connect(self.save_pic_as)

    def open_pic(self):
        self.pic_name, _ = QFileDialog.getOpenFileName(self, "打开文件", "", "所有文件 (*);;图片文件 (*.png *.jpg *.bmp)")
        if self.pic_name:
            self.ui.groupBox_pic.setTitle(f"{os.path.basename(self.pic_name)}")
            print("打开文件：", self.pic_name)
            self.ui.label_pic.setPixmap(QPixmap(self.pic_name))
    def save_pic(self):
        if self.pic_name:
            print(f"保存文件：{self.default_output}")
            # 定义参数
            red = self.ui.horizontalSlider_red.value()
            green = self.ui.horizontalSlider_green.value()
            blue = self.ui.horizontalSlider_blue.value()
            # 确保每个颜色值都是两位十六进制数
            color = "#{:02x}{:02x}{:02x}".format(red, green, blue)
            parse = argparse.ArgumentParser(formatter_class=argparse.RawTextHelpFormatter)
            parse.add_argument("--file", default=self.pic_name, type=str)
            parse.add_argument("--mark", default=self.ui.lineEdit_text.text(), type=str)
            parse.add_argument("--out", default="./output")
            parse.add_argument("--color", default=color, type=str)
            parse.add_argument("--space", default=self.ui.spinBox_space.value(), type=int)
            parse.add_argument("--angle", default=self.ui.horizontalSlider_angle.value(), type=int)
            parse.add_argument("--font-family", default="./font/SmileySans-Oblique.ttf", type=str)
            parse.add_argument("--font-height-crop", default="1.2", type=str)
            parse.add_argument("--size", default=self.ui.spinBox_size.value(), type=int)
            parse.add_argument("--opacity", default=self.ui.horizontalSlider_opacity.value() / 100, type=float)
            parse.add_argument("--quality", default=self.ui.horizontalSlider_quality.value(), type=int)

            args = parse.parse_args()
            print(args)
            # 生成水印
            mark = marker.gen_mark(args)
            # 添加水印
            marker.add_mark(args.file, mark, args)

    def save_pic_as(self):
        self.output_name, _ = QFileDialog.getSaveFileName(self, "另存为", "", "所有文件 (*);;图片文件 (*.png *.jpg *.bmp)")
        if self.output_name:
            print(f"另存为：{self.output_name}")
            os.replace(self.default_output, self.output_name)

    def generate_pic(self):
        self.save_pic()
        current_file_name = os.path.basename(self.pic_name)
        # 获取当前脚本的绝对路径
        script_path = os.path.abspath(__file__)
        # 获取当前脚本所在的目录
        directory_path = os.path.dirname(script_path)
        self.default_output = os.path.join(directory_path, f"./output/{current_file_name}")
        print(f"生成文件：{self.default_output}")
        self.ui.label_pic.setPixmap(QPixmap(self.default_output))




if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
