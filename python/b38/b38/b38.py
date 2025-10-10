"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from rxconfig import config


class State(rx.State):
    """The app state."""
    current_message: str = ""
    messages: list[tuple[str, str]] = [
        ("Python là gì", "Python là một ngôn ngữ lập trình cấp cao, dễ học và mạnh mẽ. Nó được sử dụng rộng rãi trong phát triển web, data science, AI/ML, và nhiều lĩnh vực khác."),
        ("C++ là gì?", "C++ là ngôn ngữ lập trình hướng đối tượng, mở rộng từ C. Nó được sử dụng để phát triển hệ thống, game, và các ứng dụng hiệu suất cao."),
        ("JavaScript có gì đặc biệt?", "JavaScript là ngôn ngữ lập trình chính cho web development, cho phép tạo tương tác động trên trang web và phát triển ứng dụng full-stack."),
        ("Machine Learning là gì?", "Machine Learning là một nhánh của AI cho phép máy tính học và cải thiện từ dữ liệu mà không cần lập trình rõ ràng."),
        ("React vs Vue?", "React và Vue đều là framework JavaScript phổ biến. React được phát triển bởi Facebook, Vue có syntax đơn giản hơn và dễ học."),
    ]

    def send_message(self):
        if self.current_message.strip():
            # Thêm message mới vào danh sách
            self.messages.append((self.current_message, "Đây là câu trả lời từ AI..."))
            self.current_message = ""

def message_chat(question_user: str='Câu hỏi từ người dùng', answer_ai: str = 'Trả lời từ AI'):

    return rx.box(
        # User message
        rx.box(
            rx.box(
                rx.text(question_user, class_name="text-base leading-relaxed font-medium"),
                class_name="max-w-[80%] p-4 rounded-2xl rounded-bl-md bg-gradient-to-r from-blue-500 to-blue-600 text-white shadow-lg"
            ),
            class_name="flex justify-end mb-4"
        ),
        # AI message  
        rx.box(
            rx.box(
                rx.text(answer_ai, class_name="text-base leading-relaxed font-medium"),
                class_name="max-w-[80%] p-4 rounded-2xl rounded-br-md bg-gradient-to-r from-gray-100 to-gray-200 text-gray-800 shadow-lg border border-gray-200"
            ),
            class_name="flex justify-start mb-4"
        ),
        class_name='space-y-2'
    )


def chat() -> rx.Component:
    return rx.box(
        rx.foreach(
            State.messages,
            lambda msg: message_chat(msg[0], msg[1])
        ),
        class_name='flex flex-col space-y-4 h-[70vh] overflow-y-auto px-4 py-6 scrollbar-thin scrollbar-thumb-gray-300 scrollbar-track-gray-100'
    )

def input_chat() -> rx.Component:
    return rx.box(
        rx.hstack(
            rx.input(
                value=State.current_message,
                on_change=State.set_current_message,
                placeholder='Nhập câu hỏi cho AI...',
                class_name='flex-1 px-4 py-4 rounded-full border-2 border-gray-200 focus:border-blue-500 focus:outline-none transition-all duration-200 shadow-sm hover:shadow-md text-base font-medium text-gray-800 placeholder-gray-500 min-h-[3rem]'
            ),
            rx.button(
                "Gửi",
                on_click=State.send_message,
                class_name='px-6 py-4 bg-gradient-to-r from-blue-500 to-blue-600 text-white rounded-full hover:from-blue-600 hover:to-blue-700 transition-all duration-200 shadow-lg hover:shadow-xl transform hover:scale-105 active:scale-95 text-base font-semibold min-h-[3rem]'
            ),
            class_name='flex items-center gap-3 p-6 bg-white border-t border-gray-200'
        ),
        class_name='h-[30vh] flex items-end'
    )


def index() -> rx.Component:
    return rx.box(
        # Header với gradient background
        rx.box(
            rx.hstack(
                rx.icon("bot", class_name="w-8 h-8 text-white"),
                rx.text("AI Chat Assistant", class_name="text-2xl font-bold text-white"),
                class_name="flex items-center gap-3"
            ),
            class_name="bg-gradient-to-r from-blue-600 to-purple-600 p-6 shadow-lg"
        ),
        # Chat area với background pattern
        rx.box(
            chat(),
            class_name="flex-1 bg-gradient-to-br from-gray-50 to-blue-50"
        ),
        # Input area
        input_chat(),
        class_name='h-screen w-screen flex flex-col bg-white'
    )


app = rx.App()
app.add_page(index)
