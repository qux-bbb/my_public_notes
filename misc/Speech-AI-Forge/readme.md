# Speech-AI-Forge

Speech-AI-Forge 是一个围绕 TTS 生成模型开发的项目，实现了 API Server 和 基于 Gradio 的 WebUI。

github地址: https://github.com/lenML/Speech-AI-Forge

huggingface可以试一下: https://huggingface.co/spaces/lenML/ChatTTS-Forge


尝试如下方式安装运行，失败了
```bash
git clone https://github.com/lenML/ChatTTS-Forge.git --depth=1
cd ChatTTS-Forge
uv venv venv_ChatTTS_Forge --python 3.10
source venv_chattts_forge/bin/activate
uv pip install -r requirements.txt
python -m scripts.download_models --source modelscope
python -m scripts.download_audio_backend
uv pip install torch torchvision torchaudio --index-url https://mirror.sjtu.edu.cn/pytorch-wheels/cu121

python webui.py
```


2025/4/4
