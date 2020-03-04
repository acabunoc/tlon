import torch
import torchvision
from six.moves import urllib


def load_mnist(save_path, batch_size_train=64, batch_size_test=1000):
    # this is a temporary work around to pytorch throwing 403s
    # see: https://github.com/pytorch/vision/issues/1938
    opener = urllib.request.build_opener()
    opener.addheaders = [('User-agent', 'Mozilla/5.0')]
    urllib.request.install_opener(opener)

    train_loader = torch.utils.data.DataLoader(
        torchvision.datasets.MNIST(save_path,
                                   train=True,
                                   download=True,
                                   transform=torchvision.transforms.Compose([
                                       torchvision.transforms.ToTensor(),
                                       torchvision.transforms.Normalize([0.5], [0.5])
                                   ])
                                   ),
        batch_size=batch_size_train,
        shuffle=True
    )

    test_loader = torch.utils.data.DataLoader(
        torchvision.datasets.MNIST(save_path, train=False, download=True,
                                   transform=torchvision.transforms.Compose([
                                       torchvision.transforms.ToTensor(),
                                       torchvision.transforms.Normalize([0.5], [0.5])
                                   ])),
        batch_size=batch_size_test, shuffle=True)

    return train_loader, test_loader
