import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader, random_split
from torchvision import transforms, datasets
import timm
from tqdm import tqdm

class EndangeredSpeciesClassifier(nn.Module):
    def __init__(self, num_classes):
        super(EndangeredSpeciesClassifier, self).__init__()
        self.model = timm.create_model('deit_base_patch16_224', pretrained=True, num_classes=num_classes)
        self.activation = nn.Softmax(dim=1)

    def forward(self, x):
        x = self.model(x)
        x = self.activation(x)
        return x

def train_and_save_deit_model():
    # Define data transforms
    transform = transforms.Compose([
        transforms.Resize((224, 224)),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
    ])

    # Load dataset
    dataset_root = 'C:/Users/getan/GitHub/ML/Endangered_Images'
    dataset = datasets.ImageFolder(root=dataset_root, transform=transform)
    train_size = int(0.8 * len(dataset))
    val_size = len(dataset) - train_size
    train_dataset, val_dataset = random_split(dataset, [train_size, val_size])

    # Data loaders
    train_loader = DataLoader(train_dataset, batch_size=32, shuffle=True)
    val_loader = DataLoader(val_dataset, batch_size=32, shuffle=False)

    # Define model, loss, and optimizer
    num_classes = 30
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    model = EndangeredSpeciesClassifier(num_classes=num_classes).to(device)
    criterion = nn.CrossEntropyLoss()
    optimizer = optim.AdamW(model.parameters(), lr=0.001)

    # Training loop
    epochs = 10
    for epoch in range(epochs):
        model.train()
        running_loss = 0.0
        for images, labels in tqdm(train_loader, leave=False):
            images, labels = images.to(device), labels.to(device)
            optimizer.zero_grad()
            outputs = model(images)
            loss = criterion(outputs, labels)
            loss.backward()
            optimizer.step()
            running_loss += loss.item()

        model.eval()
        val_loss = 0.0
        correct = 0
        total = 0
        with torch.no_grad():
            for images, labels in val_loader:
                images, labels = images.to(device), labels.to(device)
                outputs = model(images)
                loss = criterion(outputs, labels)
                val_loss += loss.item()
                _, predicted = torch.max(outputs, 1)
                total += labels.size(0)
                correct += (predicted == labels).sum().item()

        tqdm.write(f'Epoch [{epoch+1}/{epochs}], Loss: {running_loss/len(train_loader):.4f}, Val Loss: {val_loss/len(val_loader):.4f}, Accuracy: {correct/total:.4f}')

    # Save the model
    torch.save(model.state_dict(), 'C:/Users/getan/GitHub/ML/ENAnimalDIET.pt')
    tqdm.write("DeiT model saved to C:/Users/getan/GitHub/ML/ENAnimalDEIT.pt")


train_and_save_deit_model()
