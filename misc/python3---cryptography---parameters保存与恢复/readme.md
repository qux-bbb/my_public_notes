# python3---cryptography---parameters保存与恢复

安装模块：  
```r
pip install cryptography
```

保存 parameters  
```python
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import dh
from cryptography.hazmat.primitives.serialization import Encoding, ParameterFormat

# Generate some parameters. These can be reused.
parameters = dh.generate_parameters(generator=2, key_size=2048,
                                    backend=default_backend())
parameters_bytes = parameters.parameter_bytes(Encoding.DER, ParameterFormat.PKCS3)
open('parameters_bytes', 'wb').write(parameters_bytes)
```

恢复 der 格式的 parameters  
```python
from cryptography.hazmat.backends import default_backend

parameters_bytes = open('parameters_bytes', 'rb').read()
parameters = default_backend().load_der_parameters(parameters_bytes)
```


2020/5/7  
