# faster-whisper

keywords: stt 语音转文字

faster-whisper is a reimplementation of OpenAI's Whisper model using CTranslate2, which is a fast inference engine for Transformer models.

github地址: https://github.com/SYSTRAN/faster-whisper

安装：
```bash
pip install faster-whisper
```

使用：
```python
# 设置代理用于模型下载
import os
os.environ["HTTP_PROXY"] = "http://127.0.0.1:10809"
os.environ["HTTPS_PROXY"] = "http://127.0.0.1:10809"

from faster_whisper import WhisperModel

model_size = "large-v3"
model = WhisperModel(model_size, device="cpu", compute_type="int8")

segments, info = model.transcribe("data/hotwords.mp3", beam_size=5)
print("Detected language '%s' with probability %f" % (info.language, info.language_probability))
for segment in segments:
    print("[%.2fs -> %.2fs] %s" % (segment.start, segment.end, segment.text))
```


2025/5/6
