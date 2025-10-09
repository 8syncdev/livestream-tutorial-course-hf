"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from rxconfig import config


class State(rx.State):
    """The app state."""

def message_chat(question_user: str='Câu hỏi từ người dùng', answer_ai: str = 'Trả lời từ AI'):

    return rx.box(
        rx.box(question_user, class_name='flex justify-start p-[0.5rem] rounded-[0.5rem] bg-slate-100 text-black'),
        rx.box(answer_ai, class_name='flex justify-end p-[0.5rem] rounded-[0.5rem] bg-slate-200 text-black'),
        class_name='space-y-[0.5rem]'
    )


def chat() -> rx.Component:
    example_data = [
        (
            "Python là gì", # câu hỏi của người dùng
            "Câu trả lời từ AI", # câu trả lời của AI
        ),
        (
            "C++ là gì?",
            "Câu trả lời từ AI"
        ),
        (
            "C++ là gì?",
            "Câu trả lời từ AI"
        ),
        (
            "C++ là gì?",
            "Câu trả lời từ AI"
        ),
        (
            "C++ là gì?",
            "Câu trả lời từ AI"
        ),
    ]

    return rx.box(
        *[
           message_chat(item[0], item[1]) for item in example_data
        ],
        class_name='space-y-[0.5rem] h-[70vh] overflow-auto'
    )

def input_chat() -> rx.Component:
    # hstack: horizontal stack layout cho các components theo chiều ngang
    return rx.hstack(
        rx.input(placeholder='Nhập câu hỏi cho AI'),
        rx.button("Gửi"),
        class_name='h-[30vh]'
    )


def index() -> rx.Component:
    # Welcome Page (Index)
    return rx.container(
        chat(),
        input_chat(),
        class_name='h-screen w-screen'
    )


app = rx.App()
app.add_page(index)
