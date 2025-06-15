from fabric.widgets.button import Button


class QVQuickbuttons(Button):
    def __init__(self, name):
        super().__init__(
            name=name,
            style_classes=["quickbuttons-button"],
            label="X",
            v_expand=True
        )
