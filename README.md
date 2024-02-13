# vistral-chat
Vistral là một trợ lí Tiếng Việt nhiệt tình và trung thực.  


## Vistral Chat Application

This guide will help you run the chat application contained in the `index.html` file.  
Original model: [Vistral-7B-Chat](https://huggingface.co/Viet-Mistral/Vistral-7B-Chat) - Towards a State-of-the-Art Large Language Model for Vietnamese.  
Lightweight model: [Vistral-7B-Chat - GGUF](https://huggingface.co/uonlp/Vistral-7B-Chat-gguf) is now feasible to operate our Vistral-7B-Chat on a single computer even without a dedicated GPU.  


## Prerequisites

Ensure you have the following:

- A modern web browser (Chrome, Firefox, Safari, etc.)
- A local web server (like Python's SimpleHTTPServer, Node's http-server, etc.). Or you can use Live Server feature from VSCode
- A laptop/PC with >8GB RAM


## Start the app using Local API

1. **Download model**

Create a folder named `models`, then download `ggml-vistral-7B-chat-q4_0.gguf` from here <https://huggingface.co/uonlp/Vistral-7B-Chat-gguf> or detail <https://huggingface.co/uonlp/Vistral-7B-Chat-gguf/blob/main/ggml-vistral-7B-chat-q4_0.gguf> and put into the `models` folder

2. **Install llama_cpp Python**

Follow the guide here to install llama_cpp Python <https://github.com/abetlen/llama-cpp-python>

```bash
## Ubuntu 20.04.1 LTS
python3 -V
Python 3.9.13

pip install llama-cpp-python
pip install uvicorn
pip install starlette
pip install fastapi
pip install pydantic_settings
pip install sse_starlette
pip install starlette_context

or

pip install -r requirements.txt
```

3. **Run local OpenAI server**

Run the following script to run an OpenAI API server locally. The server should run at port 8000  

```bash
python3 -m llama_cpp.server --model "./models/ggml-vistral-7B-chat-q4_0.gguf" --n_gpu_layers 1 --n_ctx 4096

or

./server.sh
```
View API document of llama at <http://localhost:8000/docs>  

4. **Run script python test**
```bash
python3 test_llm.py
```

5. **Start Web Server**  
```bash
python -m SimpleHTTPServer -p 8888

or

python3 -m http.server 8888
```

If you're using Node's http-server, you can start it with the command:

```bash
http-server -p 8888
```

Open your web browser and navigate to localhost on the port your server is running. For example, if your server is running on port 8888, you would navigate to <http://localhost:8888/>.  

You should now see the chat interface in your browser. You can type messages into the input field and press "Send" to interact with the chatbot.  

Please note that this is a simple setup meant for local development and testing. It is not suitable for a production environment.  



# License
This code is under the [Apache License v2](https://www.apache.org/licenses/LICENSE-2.0).  