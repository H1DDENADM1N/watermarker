from pathlib import Path

from blind_watermark import WaterMark


class MyBlindMarker:
    def __init__(self):
        self.len_wm: int = None

    def add_blind_mark(self, pic_path: Path, output_path: Path, blind_text: str):
        """
        给图片加盲水印
        :param pic_path: 图片路径
        :param blind_text: 水印文字
        """

        bwm = WaterMark(password_img=1, password_wm=1)
        bwm.read_img(str(pic_path))
        bwm.read_wm(blind_text, mode="str")
        bwm.embed(str(output_path))
        self.len_wm = len(bwm.wm_bit)

    def decode_blind_mark(self, pic_path: Path) -> str:
        """
        解码盲水印
        :param pic_path: 图片路径
        :return: 盲水印文字
        """

        bwm1 = WaterMark(password_img=1, password_wm=1)
        wm_extract = bwm1.extract(str(pic_path), wm_shape=self.len_wm, mode="str")
        return wm_extract


if __name__ == "__main__":
    pic_path = Path(r"C:\Users\user0\Documents\watermarker\temp\test.png")
    output_path = Path(
        r"C:\Users\user0\Documents\watermarker\temp\test_blind_marked.png"
    )
    blind_text = "blind watermark"
    mbm = MyBlindMarker()
    mbm.add_blind_mark(pic_path, output_path, blind_text)
    print(mbm.decode_blind_mark(output_path))
