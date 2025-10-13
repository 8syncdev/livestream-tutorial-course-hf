from langchain_ollama import OllamaLLM
from langchain.chains.llm import LLMChain # xử lí chuỗi các thao tác do AI sinh ra
from langchain.chains.sql_database.query import create_sql_query_chain # tạo ra câu lệnh truy vấn cơ sở dữ liệu từ AI
from langchain.prompts import PromptTemplate # tạo câu mẫu để AI hiểu được tình huống
from langchain_community.tools import QuerySQLDataBaseTool # tool kết nối vào db được AI trích xuất
from langchain_core.output_parsers import StrOutputParser # Xử lý kết quả đầu ra là dạng markdown
from langchain.sql_database import SQLDatabase # tool kết nối cơ sở dữ liệu
from langchain_core.runnables import RunnablePassthrough # đa tác vụ cho AI
from operator import itemgetter

# Cache
from langchain.cache import InMemoryCache
from langchain.globals import set_llm_cache


llm_gemma = OllamaLLM(
    model='gemma3:1b',
    temperature=0.85, # độ sáng tạo
    num_predict=2025,
    top_p=0.91,
    top_k=40,
    num_ctx=10000
)

cache = InMemoryCache()
set_llm_cache(cache)

def answer(question: str, chain: OllamaLLM):
    ans = ""
    for word in chain.stream({
        'question': question
    }):
        ans += word
        print(word, end="")
    return ans
# answer('What is C++?')


template = PromptTemplate.from_template(
'''
Bạn là một chuyên gia lập trình hãy trả lời câu hỏi sau bằng tiếng việt:
{question}

Quy tắc:
- Câu trả lời phải ngắn gọn dễ hiểu
- Luôn đưa ra các ví dụ khi cần thiết
- Luôn có comment giải thích các code ví dụ đưa ra
'''
)

format_markdown = StrOutputParser()

llm_chain = template | llm_gemma | format_markdown


dap_an = answer(
    question='Python là gì?, đưa ra lộ trình chi tiết cho tôi ở dạng bảng để học',
    chain=llm_chain
)

from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent
FILE_PATH = BASE_DIR / "dap_an.md"

with open(FILE_PATH, 'w', encoding='utf-8') as file:
    file.write(dap_an)
