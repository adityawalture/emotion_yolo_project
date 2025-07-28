import torch
import torch.nn as nn
import torchvision.transforms as transforms
import torchvision.datasets as datasets
from torch.utils.data import DataLoader
from torchvision.models import resnet18

# Data Transform
transform = transforms.Compose([
    transforms.Grayscale(num_output_channels=3),
    transforms.Resize((48, 48)),
    transforms.ToTensor(),
])

# Dataset and Dataloader
train_dataset = datasets.ImageFolder(root='hipster/emotion_yolo_project/datasets/fer2013/versions/1/train', transform=transform)
val_dataset = datasets.ImageFolder(root='hipster/emotion_yolo_project/datasets/fer2013/versions/1/test', transform=transform)

train_loader = DataLoader(train_dataset, batch_size=32, shuffle=True)
val_loader = DataLoader(val_dataset, batch_size=32, shuffle=False)

# Model
model = resnet18(pretrained=True)
model.fc = nn.Linear(model.fc.in_features, 7)  # 7 emotions

criterion = nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(model.parameters(), lr=0.0001)
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)

# Training Loop
for epoch in range(10):
    model.train()
    total_loss = 0
    for images, labels in train_loader:
        images, labels = images.to(device), labels.to(device)
        outputs = model(images)
        loss = criterion(outputs, labels)

        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
        total_loss += loss.item()
    print(f"Epoch [{epoch+1}/10], Loss: {total_loss/len(train_loader):.4f}")

# Save Model
torch.save(model.state_dict(), r'D:\hipster\hipster\emotion_yolo_project\models\resnet18_emotion.pth')
