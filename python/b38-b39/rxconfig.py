import reflex as rx

config = rx.Config(
    app_name="b38",
    plugins=[
        rx.plugins.SitemapPlugin(),
        rx.plugins.TailwindV4Plugin(),
    ]
)