
from llama_cpp import Llama

# conda activate llama
# https://github.com/abetlen/llama-cpp-python
# https://llama-cpp-python.readthedocs.io/en/latest/api-reference/#llama_cpp.Llama.create_completion
# https://llama-cpp-python.readthedocs.io/en/latest/api-reference/#llama_cpp.Llama.create_chat_completion
# Run: python3 test_llm.py

llm = Llama(model_path="./models/ggml-vistral-7B-chat-q4_0.gguf", n_gpu_layers=1, n_ctx=4096)

output = llm.create_chat_completion(
    messages = [
        {"role": "system", "content": "Vistral là một trợ lí Tiếng Việt nhiệt tình và trung thực. Luôn trả lời một cách hữu ích nhất có thể, đồng thời giữ an toàn."},
        {
            "role": "user",
            "content": "Tôi có thể học Tiếng Anh ở đâu?"
        }
    ],
    temperature=0.9,
)

print(output)
print(output["choices"][0]["message"]["content"], end='', flush=True)

# {'id': 'chatcmpl-a541602d-d832-4127-8375-4dcf0f90d46b', 'object': 'chat.completion', 'created': 1707824226, 'model': './models/ggml-vistral-7B-chat-q4_0.gguf', 'choices': [{'index': 0, 'message': {'role': 'assistant', 'content': ' Để học tiếng Anh, bạn có nhiều lựa chọn khác nhau:\n1) Trường ngôn ngữ: Nhiều trường đại học cung cấp các khóa học về ngôn ngữ Anh. Tìm kiếm trên mạng và hỏi thăm văn phòng quốc tế của trường hoặc trung tâm giáo dục thường xuyên để biết thêm thông tin chi tiết.\n2) Giao tiếp với người bản xứ: Bạn có thể tham gia một nhóm trao đổi ngôn ngữ, nơi bạn luyện nói tiếng Anh với những người bản xứ đang học ngôn ngữ mẹ đẻ của bạn. Điều này là một cách tuyệt vời để thực hành kỹ năng nghe và nói của bạn trong khi cũng cải thiện phát âm và hiểu biết về văn hóa.\n3) Học trực tuyến: Có nhiều khóa học tiếng Anh trực tuyến từ các trang web như Duolingo, Babbel và Coursera. Chúng thường miễn phí hoặc có giá cả phải chăng và cho phép bạn kiểm soát tốc độ và thời gian của mình.\n4) Ứng dụng di động: Nhiều ứng dụng di động cung cấp nội dung luyện tập ngôn ngữ, chẳng hạn như "Babbel", "Duolingo" và "FluentU." Những tài nguyên này thường bao gồm một loạt các kỹ năng và chủ đề đa dạng mà bạn có thể truy cập bất kỳ lúc nào.\n5) Đọc sách và xem phim bằng tiếng Anh: Chọn những tác phẩm yêu thích của mình, nhưng hãy đọc hoặc xem chúng bằng tiếng Anh thay vì phiên bản gốc của bạn để tăng vốn từ vựng và cải thiện hiểu biết về phong cách văn học/điện ảnh. '}, 'finish_reason': 'stop'}], 'usage': {'prompt_tokens': 50, 'completion_tokens': 318, 'total_tokens': 368}}
