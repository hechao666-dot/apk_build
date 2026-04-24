import flet as ft

def main(page: ft.Page):
    page.title = "居中布局示例"
    
    # 1. 创建文字组件，初始隐藏
    result_text = ft.Text(value="已点击按钮", visible=False, color="blue", size=20)

    # 2. 点击逻辑
    def button_clicked(e):
        result_text.visible = True
        result_text.update()

    # 3. 布局：使用 Column 并设置对其方式
    page.add(
        ft.Column(
            [
                ft.ElevatedButton("点击我", on_click=button_clicked),
                result_text,
            ],
            alignment=ft.MainAxisAlignment.CENTER,        # 垂直方向居中
            horizontal_alignment=ft.CrossAxisAlignment.CENTER, # 水平方向居中
            expand=True, # 让 Column 占满整个窗口空间
        )
    )

ft.run(main=main,view=ft.AppView.WEB_BROWSER)