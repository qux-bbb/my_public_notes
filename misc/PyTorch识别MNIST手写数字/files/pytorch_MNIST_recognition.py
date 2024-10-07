import argparse
import torch
from torch.utils.data import DataLoader
from torchvision import transforms
from torchvision.datasets import MNIST
import matplotlib.pyplot as plt
from PIL import Image, ImageOps
import numpy as np


class Net(torch.nn.Module):

    def __init__(self):
        super().__init__()
        self.fc1 = torch.nn.Linear(28 * 28, 64)
        self.fc2 = torch.nn.Linear(64, 64)
        self.fc3 = torch.nn.Linear(64, 64)
        self.fc4 = torch.nn.Linear(64, 10)

    def forward(self, x):
        x = torch.nn.functional.relu(self.fc1(x))
        x = torch.nn.functional.relu(self.fc2(x))
        x = torch.nn.functional.relu(self.fc3(x))
        x = torch.nn.functional.log_softmax(self.fc4(x), dim=1)
        return x


def get_data_loader(is_train):
    to_tensor = transforms.Compose([transforms.ToTensor()])
    data_set = MNIST("", is_train, transform=to_tensor, download=True)
    return DataLoader(data_set, batch_size=15, shuffle=True)


def evaluate(test_data, net):
    n_correct = 0
    n_total = 0
    with torch.no_grad():
        for (x, y) in test_data:
            outputs = net.forward(x.view(-1, 28 * 28))
            for i, output in enumerate(outputs):
                if torch.argmax(output) == y[i]:
                    n_correct += 1
                n_total += 1
    return n_correct / n_total


def train():
    train_data = get_data_loader(is_train=True)
    test_data = get_data_loader(is_train=False)
    net = Net()

    print("initial accuracy:", evaluate(test_data, net))
    optimizer = torch.optim.Adam(net.parameters(), lr=0.001)
    for epoch in range(2):
        for (x, y) in train_data:
            net.zero_grad()
            output = net.forward(x.view(-1, 28 * 28))
            loss = torch.nn.functional.nll_loss(output, y)
            loss.backward()
            optimizer.step()
        print("epoch", epoch, "accuracy:", evaluate(test_data, net))

    torch.save(net.state_dict(), "model.pth")
    print("Model saved.")


def predict(image_path=None, image_index=None):
    net = Net()
    net.load_state_dict(torch.load("model.pth", weights_only=True))

    if image_path is not None:
        img = Image.open(image_path).convert("L")  # Convert to grayscale
        img = ImageOps.fit(img, (28, 28), method=Image.LANCZOS)  # Resize to 28x28
        img_array = np.array(img)
        img_tensor = torch.tensor(img_array, dtype=torch.float32).view(1, -1) / 255.0  # Normalize
        predict = torch.argmax(net.forward(img_tensor))
        plt.imshow(img, cmap="gray")
        plt.title("prediction: " + str(int(predict)))
        plt.show()
    elif image_index is not None:
        test_data = get_data_loader(is_train=False)
        x, y = test_data.dataset[image_index]
        predict = torch.argmax(net.forward(x.view(-1, 28 * 28)))
        plt.imshow(x.view(28, 28))
        plt.title("prediction: " + str(int(predict)))
        plt.show()
    else:
        test_data = get_data_loader(is_train=False)
        for (n, (x, _)) in enumerate(test_data):
            if n > 3:
                break
            predict = torch.argmax(net.forward(x[0].view(-1, 28 * 28)))
            plt.figure(n)
            plt.imshow(x[0].view(28, 28))
            plt.title("prediction: " + str(int(predict)))
        plt.show()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="MNIST Classification")
    parser.add_argument("--mode", type=str, choices=["train", "predict"], required=True,
                        help="Mode: train or predict")
    parser.add_argument("--image_path", type=str, help="Path to the custom image to predict")
    parser.add_argument("--image_index", type=int, help="Index of the image to predict")

    args = parser.parse_args()

    if args.mode == "train":
        train()
    elif args.mode == "predict":
        predict(args.image_path, args.image_index)