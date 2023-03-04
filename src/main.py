import flet
from flet import (
    Page,
    colors,
    theme,
)

from app import App
 
if __name__ == "__main__":
 
    def main(page: Page):
        page.title = "NH"
        page.padding = 0
        page.theme = theme.Theme(font_family="Verdana")
        page.theme.page_transitions.windows = "cupertino"
        page.fonts = {"Pacifico": "Pacifico-Regular.ttf"}
        page.bgcolor = colors.BLUE_GREY_200
        app = App(page)
        page.add(app)
        page.update()
        app.initialize()


flet.app(target=main, assets_dir="../assets")
 
