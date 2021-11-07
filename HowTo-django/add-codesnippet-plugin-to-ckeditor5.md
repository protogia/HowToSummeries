
## Paste the follwing config into `BASE_DIR/lib/python3.8/site-packages/ckeditor/configs.py`:

```python
DEFAULT_CONFIG = {
    "skin": "moono-lisa",
    "toolbar_Basic": [["Source", "-", "Bold", "Italic"]],
    "toolbar_Full": [
        [
            "Styles",
            "Format",
            "Bold",
            "Italic",
            "CodeSnippet",
            "Underline",
            "Strike",
            "SpellChecker",
            "Undo",
            "Redo",
        ],
        ["Link", "Unlink", "Anchor"],
        ["Image", "Flash", "Table", "HorizontalRule"],
        ["TextColor", "BGColor"],
        ["Smiley", "SpecialChar"],
        ["Source"],
    ],
    "extraPlugins":"codesnippet",
    "toolbar": "Full",
    "height": 320,
    "width": 1210,
    "filebrowserWindowWidth": 940,
    "filebrowserWindowHeight": 725,
}
```

its important to add `"extraPlugins":"codesnippet"`
