# PyTorch识别MNIST手写数字

## 脚本
[pytorch_MNIST_recognition.py](./files/pytorch_MNIST_recognition.py)  

## 解释
### 训练过程

1. **数据准备**：
   - 使用 `get_data_loader` 函数加载MNIST数据集。该函数返回一个 `DataLoader` 对象，它负责批量加载数据并打乱顺序。
   - 数据集中的每个图像都被转换为PyTorch张量，并且归一化到[0, 1]范围。

2. **模型定义**：
   - 定义了一个简单的四层全连接神经网络 `Net`，其中包含三个隐藏层和一个输出层。
   - 使用ReLU激活函数增加非线性，并在输出层使用log_softmax进行概率输出。

3. **优化器设置**：
   - 使用Adam优化器，它是一种自适应学习率的优化算法，适用于许多不同的问题。

4. **训练循环**：
   - 对于每个epoch（这里设置为2个epoch），遍历训练数据集。
   - 在每次迭代中，首先将网络梯度清零（`net.zero_grad()`）。
   - 前向传播计算输出，并计算损失（使用负对数似然损失 `nll_loss`）。
   - 反向传播计算梯度，并更新网络权重（`optimizer.step()`）。
   - 每个epoch结束后，在测试集上评估模型的准确率并打印结果。

5. **模型保存**：
   - 训练完成后，使用 `torch.save` 将模型的状态字典保存到文件 `model.pth`。

### 预测过程

1. **加载模型**：
   - 使用 `Net()` 创建一个新的网络实例。
   - 从文件 `model.pth` 中加载之前训练好的权重。

2. **图像预处理**：
   - 如果提供了图像路径 (`--image_path`)，则打开图像文件，将其转换为灰度图，调整大小为28x28像素，并归一化到[0, 1]范围。
   - 如果提供了图像索引 (`--image_index`)，则直接从测试数据集中获取对应的图像和标签。
   - 如果没有提供图像路径和索引，则默认显示测试集中的前几个图像。

3. **前向传播**：
   - 将预处理后的图像输入到网络中进行前向传播，得到输出概率。

4. **结果展示**：
   - 使用 `torch.argmax` 找出概率最高的类别作为预测结果。
   - 使用matplotlib库显示图像，并在图像上标注预测结果。

### 示例

#### 训练示例
```bash
python script.py --mode train
```
这条命令将启动训练过程，训练两个epoch，并在每个epoch结束后打印测试集上的准确率。最后，保存训练好的模型。

#### 预测示例（使用自定义图像）
```bash
python script.py --mode predict --image_path path/to/my_image.png
```
这条命令将加载训练好的模型，并对指定的图像进行预测，然后显示图像和预测结果。

#### 预测示例（使用数据集索引）
```bash
python script.py --mode predict --image_index 123
```
这条命令将对MNIST测试集中索引为123的图像进行预测，并显示结果。

#### 预测示例（默认行为）
```bash
python script.py --mode predict
```
这条命令将显示测试集中的前四个图像及其预测结果。

通过这些步骤，代码实现了对MNIST数据集的训练和预测功能，并提供了灵活的方式来处理不同的预测场景。


## 信息来源
1. 10分钟入门神经网络 PyTorch 手写数字识别 https://www.bilibili.com/video/BV1GC4y15736
2. 基于PyTorch实现MNIST手写数字识别 https://mp.weixin.qq.com/s/2NxHk9G0mr4zdMwAWE5BfQ
3. 腾讯元宝
