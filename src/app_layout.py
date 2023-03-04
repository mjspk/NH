from flet import (
    ButtonStyle,
    Column,
    Container,
    Control,
    IconButton,
    Page,
    PopupMenuButton,
    PopupMenuItem,
    RoundedRectangleBorder,
    Row,
    Text,
    TextButton,
    TextField,
    border,
    border_radius,
    colors,
    icons,
    padding,
)
from patients_view import PatientsView
from settings_view import SettingsView
from sidebar import Sidebar
 
 
class AppLayout(Row):
    def __init__(self, app, page: Page, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.app = app
        self.page = page
        self.page.on_resize = self.page_resize
        self.sidebar = Sidebar(self, page)
        self.patients_view=PatientsView(app)
        self.settings_view =SettingsView(app)
        self.views = [self.patients_view, self.settings_view]
        self._active_view: Control = self.patients_view
        self.controls = [self.sidebar, self.active_view]

    @property
    def active_view(self):
        return self._active_view

    @active_view.setter
    def active_view(self, view):
        self._active_view = view
        self.controls[-1] = self._active_view
        self.update()

    def page_resize(self, e):
        self.sidebar.width = 250 if self.sidebar.visible else 0
        self.update()

