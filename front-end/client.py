# front-end/app.py
import flet as ft
import requests


class MyApp(ft.UserControl):
    def build(self):
        # UI 구성 요소들은 여기에 추가

        # 버튼을 클릭하면 서버에 GET 요청을 보내는 함수를 호출
        button = ft.Button(text="Send Request", on_click=self.send_request)

        return ft.Column(controls=[button])

    def send_request(self, e):
        # Flask 서버의 /api/hello 엔드포인트에 GET 요청을 보냄
        response = requests.get("http://127.0.0.1:5000/api/hello")

        # 서버 응답을 콘솔에 출력
        print("Server Response:", response.json())


# 메인 함수
async def main(page: ft.Page):
    page.title = "MyApp"
    page.horizontal_alignment = "center"
    page.scroll = "adaptive"
    await page.update_async()

    # Flet 애플리케이션 인스턴스 생성
    app = MyApp()

    # 애플리케이션의 루트 컨트롤을 페이지에 추가
    await page.add_async(app)


# Flet 애플리케이션 실행
ft.app(main)
