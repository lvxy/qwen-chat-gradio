# coding:utf-8
import json
import os
import time

import gradio as gr
import torch
from modelscope import AutoTokenizer, AutoModelForCausalLM, snapshot_download

# 服务器模型文件位置
model_dir = "/models/Qwen-14B-Chat-Int4"
tokenizer = AutoTokenizer.from_pretrained(model_dir, trust_remote_code=True)

model = AutoModelForCausalLM.from_pretrained(
    model_dir,
    device_map="auto",
    trust_remote_code=True
).eval()


title = """
    QWen-Chat
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