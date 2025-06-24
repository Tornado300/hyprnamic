from fabric.widgets.button import Button


class QVQuickbutton(Button):
    def __init__(self, name):
        super().__init__(
            name=name,
            style_classes=["quickbutton-button"],
            label="X",
            v_expand=True
        )
