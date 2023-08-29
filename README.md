  本文主要实现Qwen-7B-Chat与MindChat-Qwen-7B的简单部署与测试

## 环境
  系统：CentOS-7
  CPU: 14C28T
  显卡：Tesla P40 24G
  驱动: 515
  CUDA: 11.7
  cuDNN: 8.9.2.26

## 创建环境
conda create --name qwen-chat python=3.10
conda activate qwen-chat

## 克隆项目
git clone https://github.com/lvxy/qwen-chat-gradio.git
cd qwen-chat-gradio

## 安装依赖
pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple

## 安装依赖-量化依赖库
pip install bitsandbytes -i https://pypi.tuna.tsinghua.edu.cn/simple

load_in_8bit=True量化加载模型，节省显存（大概需要12G）

## 运行
python webui_qwen.py
或者
python webui_mind.py

通过ModelScope下载模型，下载速度还是很好的，下载模型完成，需要一些时间
    Qwen-7B-Chat        14G
    MindChat-Qwen-7B    14G

## 访问使用
    http://127.0.0.1:7860

可以使用体验了


本文参考
https://github.com/X-D-Lab/MindChat/blob/main/webui_demo.py
