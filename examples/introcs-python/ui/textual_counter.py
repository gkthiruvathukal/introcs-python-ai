from textual.app import App, ComposeResult
from textual.widgets import Button, Static


# start: app
class CounterApp(App):
    """A small Textual app with one piece of state."""

    def compose(self) -> ComposeResult:
        yield Static("0", id="count")
        yield Button("Add one", id="add")
        yield Button("Reset", id="reset")

    def on_mount(self) -> None:
        self.count = 0

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "add":
            self.count += 1
        elif event.button.id == "reset":
            self.count = 0

        self.query_one("#count", Static).update(str(self.count))


if __name__ == "__main__":
    CounterApp().run()
# end: app
