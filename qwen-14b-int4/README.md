## 创建环境
```
conda create --name modelscope python=3.10

conda activate modelscope
```
## 克隆项目
```
git clone https://github.com/lvxy/qwen-chat-gradio.git
cd qwen-chat-gradio
```
## 安装依赖-1
```
pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
```
## 安装依赖-2
```
pip install auto-gptq optimum -i https://pypi.tuna.tsinghua.edu.cn/simple
```

## 下载模型
```
python down-models-qwen-14b-int4.py
可以在他服务器下载，这个是modelscope源(国内)，速度还是非常好的
```

## 运行
    修改 服务器模型文件位置
```
python run-qwen-14b-int4-chat.py
```


## 访问使用
```
    http://127.0.0.1:7860
```
可以使用体验了