import argparse
import shutil
from dataclasses import dataclass
from pathlib import Path

from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QApplication, QFileDialog, QMainWindow

from ..watermarker import marker
from ..watermarker.my_blind_marker import MyBlindMarker
from .Ui_marker import Ui_MainWindow


@dataclass(frozen=True)
class PathsConfig:
    OUTPUT_PATH: Path = Path("./output").resolve()
    FONT_PATH: Path = Path("./font").resolve()
    TEMP_PATH: Path = Path("./temp").resolve()

    DEFAULT_FONT: Path = FONT_PATH / "SmileySans-Oblique.ttf"


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.input_pic: Path = None
        self.output_pic: Path = None
        self.temp_pic: Path = None
        self.blind_temp_pic: Path = None

        self.checkBox_text.setDisabled(True)  # 打开图片后才允许编辑文字水印选项
        self.disable_text_options()  # 打开图片后才允许编辑文字水印选项
        self.checkBox_blind.setDisabled(True)  # 打开图片后才允许编辑盲水印选项
        self.disable_blind_options()  # 打开图片后才允许编辑盲水印选项

        self.setup_signals()

    def setup_signals(self):
        self.action_open.triggered.connect(self.open_pic)
        self.action_save.triggered.connect(self.save_pic)
        self.action_save_as.triggered.connect(self.save_pic_as)
        self.checkBox_text.stateChanged.connect(self.on_checkBox_text_changed)
        self.checkBox_blind.stateChanged.connect(self.on_checkBox_blind_changed)

        self.lineEdit_text.textChanged.connect(self.generate_temp_pic)
        self.spinBox_size.valueChanged.connect(self.generate_temp_pic)
        self.spinBox_space.valueChanged.connect(self.generate_temp_pic)
        self.horizontalSlider_red.valueChanged.connect(self.generate_temp_pic)
        self.horizontalSlider_green.valueChanged.connect(self.generate_temp_pic)
        self.horizontalSlider_blue.valueChanged.connect(self.generate_temp_pic)
        self.horizontalSlider_opacity.valueChanged.connect(self.generate_temp_pic)
        self.horizontalSlider_angle.valueChanged.connect(self.generate_temp_pic)
        self.horizontalSlider_quality.valueChanged.connect(self.generate_temp_pic)

        self.lineEdit_blind_text.textChanged.connect(self.generate_blind_temp_pic)

    def enable_text_options(self):
        self.lineEdit_text.setEnabled(True)
        self.spinBox_size.setEnabled(True)
        self.spinBox_space.setEnabled(True)
        self.horizontalSlider_red.setEnabled(True)
        self.horizontalSlider_green.setEnabled(True)
        self.horizontalSlider_blue.setEnabled(True)
        self.horizontalSlider_opacity.setEnabled(True)
        self.horizontalSlider_angle.setEnabled(True)
        self.horizontalSlider_quality.setEnabled(True)

    def disable_text_options(self):
        self.lineEdit_text.setDisabled(True)
        self.spinBox_size.setDisabled(True)
        self.spinBox_space.setDisabled(True)
        self.horizontalSlider_red.setDisabled(True)
        self.horizontalSlider_green.setDisabled(True)
        self.horizontalSlider_blue.setDisabled(True)
        self.horizontalSlider_opacity.setDisabled(True)
        self.horizontalSlider_angle.setDisabled(True)
        self.horizontalSlider_quality.setDisabled(True)

    def enable_blind_options(self):
        self.lineEdit_blind_text.setEnabled(True)

    def disable_blind_options(self):
        self.lineEdit_blind_text.setDisabled(True)

    def on_checkBox_text_changed(self):
        if self.checkBox_text.isChecked():
            self.enable_text_options()
            self.generate_temp_pic()
        else:
            self.disable_text_options()
            self.replace_temp_pic_with_input_pic()

        if self.checkBox_blind.isChecked():
            self.checkBox_blind.setChecked(False)
            self.checkBox_blind.setChecked(True)

    def on_checkBox_blind_changed(self):
        if self.checkBox_blind.isChecked():
            self.enable_blind_options()
            self.generate_blind_temp_pic()
        else:
            self.disable_blind_options()
            self.replace_blind_temp_pic_with_temp_pic()
            self.lineEdit_decode_blind_text.clear()

    def replace_blind_temp_pic_with_temp_pic(self):
        if self.blind_temp_pic.exists():
            self.blind_temp_pic.unlink()
        self.label_pic.setPixmap(QPixmap(str(self.temp_pic)))

    def replace_temp_pic_with_input_pic(self):
        shutil.copy(self.input_pic, self.temp_pic)
        self.label_pic.setPixmap(QPixmap(str(self.temp_pic)))

    def open_pic(self):
        file_path, _ = QFileDialog.getOpenFileName(
            self, "打开文件", "", "所有文件 (*);;图片文件 (*.png *.jpg *.bmp)"
        )
        if file_path:
            self.input_pic = Path(file_path)
        else:
            # 处理用户取消选择文件的情况
            self.input_pic = None
            return

        self.groupBox_pic.setTitle(f"{self.input_pic.name}")
        print("打开文件：", self.input_pic)
        self.label_pic.setPixmap(QPixmap(str(self.input_pic)))

        self.checkBox_text.setEnabled(True)
        self.enable_text_options()
        self.generate_temp_pic()

        self.checkBox_blind.setEnabled(True)
        self.enable_blind_options()
        self.generate_blind_temp_pic()

    def save_pic(self):
        self.output_pic = PathsConfig.OUTPUT_PATH / self.input_pic.name

        if not self.output_pic.parent.exists():
            self.output_pic.parent.mkdir(parents=True)

        if self.output_pic.exists():
            self.output_pic.unlink()

        if self.blind_temp_pic.exists():
            shutil.copy(self.blind_temp_pic, self.output_pic)
            print(f"保存文件：{self.output_pic}")
        elif self.temp_pic.exists():
            if self.output_pic.exists():
                self.output_pic.unlink()
            shutil.copy(self.temp_pic, self.output_pic)
            print(f"保存文件：{self.output_pic}")
        else:
            print("临时文件不存在")

    def save_pic_as(self):
        file_path, _ = QFileDialog.getSaveFileName(
            self, "另存为", "", "所有文件 (*);;图片文件 (*.png *.jpg *.bmp)"
        )
        if file_path:
            self.output_pic = Path(file_path)
        else:
            # 处理用户取消选择文件的情况
            self.output_pic = None
            return

        if self.temp_pic.exists():
            if self.output_pic.exists():
                self.output_pic.unlink()
            shutil.copy(self.temp_pic, self.output_pic)
            print(f"保存文件：{self.output_pic}")
        else:
            print("临时文件不存在")

    def generate_temp_pic(self):
        if not self.input_pic:
            print("请先打开图片文件")
            return
        self.temp_pic = PathsConfig.TEMP_PATH / self.input_pic.name
        print(f"临时文件：{self.temp_pic}")
        # 定义参数
        red = self.horizontalSlider_red.value()
        green = self.horizontalSlider_green.value()
        blue = self.horizontalSlider_blue.value()
        # 确保每个颜色值都是两位十六进制数
        color = "#{:02x}{:02x}{:02x}".format(red, green, blue)
        parse = argparse.ArgumentParser(formatter_class=argparse.RawTextHelpFormatter)
        parse.add_argument("--file", default=self.input_pic, type=str)

        parse.add_argument("--mark", default=self.lineEdit_text.text(), type=str)
        parse.add_argument("--out", default=str(PathsConfig.TEMP_PATH))
        parse.add_argument("--color", default=color, type=str)
        parse.add_argument("--space", default=self.spinBox_space.value(), type=int)
        parse.add_argument(
            "--angle", default=self.horizontalSlider_angle.value(), type=int
        )
        parse.add_argument(
            "--font-family", default=str(PathsConfig.DEFAULT_FONT), type=str
        )
        parse.add_argument("--font-height-crop", default="1.2", type=str)
        parse.add_argument("--size", default=self.spinBox_size.value(), type=int)
        parse.add_argument(
            "--opacity",
            default=self.horizontalSlider_opacity.value() / 100,
            type=float,
        )
        parse.add_argument(
            "--quality", default=self.horizontalSlider_quality.value(), type=int
        )

        args = parse.parse_args()
        print(args)
        # 生成水印
        mark = marker.gen_mark(args)
        # 添加水印
        marker.add_mark(args.file, mark, args)

        if self.temp_pic.exists():
            self.label_pic.setPixmap(QPixmap(str(self.temp_pic)))
        else:
            print("生成临时文件失败")

    def generate_blind_temp_pic(self):
        self.blind_temp_pic = (
            self.temp_pic.parent / f"{self.temp_pic.name}_blind{self.temp_pic.suffix}"
        )
        print(f"盲水印临时文件：{self.blind_temp_pic}")
        mbm = MyBlindMarker()
        mbm.add_blind_mark(
            self.temp_pic, self.blind_temp_pic, self.lineEdit_blind_text.text()
        )

        self.lineEdit_decode_blind_text.setText(
            mbm.decode_blind_mark(self.blind_temp_pic)
        )

        if self.blind_temp_pic.exists():
            self.label_pic.setPixmap(QPixmap(str(self.blind_temp_pic)))
        else:
            print("生成盲水印临时文件失败")


def main():
    app = QApplication([])
    app.setStyle("Fusion")
    window = MainWindow()
    window.show()
    app.exec()
