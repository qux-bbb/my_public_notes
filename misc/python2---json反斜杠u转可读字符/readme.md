# python2---json反斜杠u转可读字符

```python
report_json = json.loads(report_data)
with codecs.open(filepath, 'wb', encoding='utf8', buffering=1024*1024) as f:
    json.dump(report_json, f, ensure_ascii=False, indent=self.options.indent)
```

2020/6/4  
