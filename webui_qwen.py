# coding:utf-8
import json
import os
import time

import gradio as gr
import torch
from modelscope.hub.snapshot_download import snapshot_download
from transformers import AutoModelForCausalLM, AutoTokenizer
from transformers.generation.utils import GenerationConfig

cache_dir = './'

snapshot_download('qwen/Qwen-7B-Chat',
                  cache_dir=cache_dir,
                  revision='v1.0.5')

tokenizer = AutoTokenizer.from_pretrained("qwen/Qwen-7B-Chat", revision = 'v1.0.5',trust_remote_code=True)
model = AutoModelForCausalLM.from_pretrained("qwen/Qwen-7B-Chat", revision = 'v1.0.5',device_map="auto", trust_remote_code=True,load_in_8bit=True).eval()
model.generation_config = GenerationConfig.from_pretrained("qwen/Qwen-7B-Chat",revision = 'v1.0.5', trust_remote_code=True)


title = """
    QWenChat
"""
description = ''
submit_btn = '发送'
retry_btn = '🔄 重新生成'
undo_btn = '↩️ 撤销'
clear_btn = '🗑️ 清除历史'


def predict(message, history):

    if history is None:
        history = []
    history = history[-20:]
    response, history = model.chat(tokenizer, message, history=history) 

    history.append((message, response))

    for i in range(len(response)):
        time.sleep(0.02)
        yield response[:i + 1]


demo = gr.ChatInterface(predict,
                        title=title,
                        description=description,
                        cache_examples=True,
                        submit_btn=submit_btn,
                        retry_btn=retry_btn,
                        clear_btn=clear_btn,
                        undo_btn=undo_btn).queue()

demo.launch(enable_queue=True, share=True,server_name="0.0.0.0", server_port=7860)