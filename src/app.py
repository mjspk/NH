from flet import (
    AlertDialog,
    AppBar,
    Column,
    Container,
    ElevatedButton,
    Icon,
    Page,
    PopupMenuButton,
    PopupMenuItem,
    RoundedRectangleBorder,
    Row,
    TemplateRoute,
    Text,
    TextField,
    UserControl,
    View,
    colors,
    icons,
    margin,
    padding,
    theme,
    IconButton,
    ButtonStyle
)
from add_patient_view import AddPatientView

from app_layout import AppLayout
from patient_details_view import PatientDetailsView
 
class App(UserControl):
    def __init__(self, page: Page):
        super().__init__()
        self.page = page
        self.appbar = AppBar(
            leading=IconButton(
                icon=icons.MENU,
                icon_color=colors.BLUE_GREY_400,
                selected=False,
                selected_icon=icons.MENU,
                on_click=self.toggle_nav_rail
            ),
            leading_width=60,
            title=Text("NH",size=32, text_align="start"),
            center_title=True,
            toolbar_height=75,
            bgcolor=colors.BLUE_GREY_900,
            elevation=10,
        )
        self.page.appbar = self.appbar
        self.page.update()
    
    
    def build(self):
        # self.layout = AppLayout(
        #     self,
        #     self.page,
        #     tight=True,
        #     expand=True,
        #     vertical_alignment="start",
        # )
        self.layout = PatientDetailsView(self)
        return self.layout
    
    def initialize(self):
        self.page.views.clear()
        self.page.views.append(
            View(
                "/",
                [self.appbar, self.layout],
                padding=padding.all(0),
                bgcolor=colors.BLUE_GREY_200,
            )
        )
        self.page.update()
        self.page.go("/")

  
    
  
    def toggle_nav_rail(self, e):
        self.layout.sidebar.visible = not self.layout.sidebar.visible
        self.page.update()


    