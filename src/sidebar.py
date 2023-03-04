from flet import (
    UserControl,
    Column,
    Container,
    Row,
    Text,
    NavigationRail,
    NavigationRailDestination,
    alignment,
    border_radius,
    colors,
    icons,
    padding,
    margin,
)
 
 
class Sidebar(UserControl):
 
    def __init__(self, app_layout, page):
        super().__init__()
        self.app_layout = app_layout
        self.page = page
        self.top_nav_rail = NavigationRail(
            selected_index=None,
            label_type="all",
            on_change=self.top_nav_change,
            destinations= [
            NavigationRailDestination(
                label_content=Text("Patients"),
                label="Patients",
                icon=icons.PEOPLE_OUTLINED,
                selected_icon=icons.PEOPLE_OUTLINED
            ),
            NavigationRailDestination(
                label_content=Text("Settings"),
                label="Settings",
                icon=icons.SETTINGS,
                selected_icon=icons.SETTINGS
            ),
 
        ],
            bgcolor=colors.BLUE_GREY,
            extended=True,
            expand=True
        )
        self.top_nav_rail.selected_index =0
 
    def build(self):
        self.view = Container(
            content=Column([self.top_nav_rail, ], tight=True),
            padding=padding.all(15),
            margin=margin.all(0),
            width=250,
            bgcolor=colors.BLUE_GREY,
        )
        return self.view
    
    def toggle_nav_rail(self, e):
        self.view.visible = not self.view.visible
        self.view.update()
        self.page.update()
        
    def top_nav_change(self, e):
        self.app_layout.active_view = self.app_layout.views[int(e.data)]
        self.update()
