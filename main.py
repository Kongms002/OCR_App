import flet as ft


class AllergyApp(ft.UserControl):
    def build(self):
        self.camera_button = ft.FloatingActionButton(
            icon=ft.icons.CAMERA, on_click=self.capture_image
        )

        self.allergy_button = ft.FloatingActionButton(
            icon=ft.icons.ADD, on_click=self.show_allergy_options
        )

        self.allergy_options = [
            "난류",
            "우유",
            "메밀",
            "땅콩",
            "대두",
            "밀",
            "고등어",
            "게",
            "새우",
            "돼지고기",
            "복숭아",
            "토마토",
            "아황산류",
            "호두",
            "닭고기",
            "쇠고기",
            "오징어",
            "조개류",
        ]

        self.allergy_checkbox_list = [
            ft.Checkbox(value=False, label=allergy, on_change=self.allergy_changed)
            for allergy in self.allergy_options
        ]

        self.display_allergy_options = ft.Row(
            controls=[ft.Column(controls=self.allergy_checkbox_list)]
        )

        return ft.Column(
            controls=[
                ft.Row(
                    [ft.Text(value="Allergy App", style="headlineMedium")],
                    alignment="center",
                ),
                ft.Row(controls=[self.camera_button, self.allergy_button]),
                self.display_allergy_options,
            ]
        )

    def show_allergy_options(self, e):
        self.display_allergy_options.visible = not self.display_allergy_options.visible

    def capture_image(self, e):
        # getUserMedia를 사용하여 웹캠에서 이미지를 캡처
        navigator = ft.get_js_global("navigator")
        media_options = {"video": True}

        navigator.mediaDevices.getUserMedia(media_options).then(
            lambda stream: self.handle_camera_stream(stream),
            lambda error: print(f"Error accessing camera: {error}"),
        )

    def handle_camera_stream(self, stream):
        # 캡처된 이미지를 Canvas에 표시
        video = ft.create_element("video")
        video.srcObject = stream
        video.autoplay = True

        canvas = ft.create_element("canvas")
        canvas.width = video.videoWidth
        canvas.height = video.videoHeight

        video.onloadeddata = lambda e: self.capture_frame(canvas, video)

    def capture_frame(self, canvas, video):
        # Canvas에 현재 프레임을 그리고 이미지로 변환하여 표시
        context = canvas.getContext("2d")
        context.drawImage(video, 0, 0, canvas.width, canvas.height)

        image_data_url = canvas.toDataURL("image/png")
        self.display_image.src = image_data_url


async def main(page: ft.Page):
    page.title = "Allergy App"
    page.horizontal_alignment = "center"
    page.scroll = "adaptive"
    await page.update_async()

    app = AllergyApp()
    await page.add_async(app)


ft.app(main)
