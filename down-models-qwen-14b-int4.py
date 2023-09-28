from modelscope import AutoModelForCausalLM, AutoTokenizer, snapshot_download
from modelscope import GenerationConfig

cache_dir = './Qwen-14B-Chat-Int4'
model_dir = snapshot_download('qwe/Qwen-14B-Chat-Int4',cache_dir=cache_dir, revision='v1.0.3')

## 可以在其他服务器下载，国内源，速度还是很好的
## 
