import torch
from torchvision import transforms
from PIL import Image

def load_image(path):
    img = Image.open(path).convert("RGB")
    transform = transforms.Compose([
        transforms.Resize((256, 256)),
        transforms.ToTensor()
    ])
    return transform(img).unsqueeze(0)

def save_image(tensor, path):
    img = tensor.clone().detach().squeeze(0)
    img = transforms.ToPILImage()(img)
    img.save(path)

def stylize(content_path, style_path, output_path):
    content = load_image(content_path)
    style = load_image(style_path)

    generated = content.clone().requires_grad_(True)
    optimizer = torch.optim.Adam([generated], lr=0.02)

    for i in range(60):
        optimizer.zero_grad()

        content_loss = torch.mean((generated - content) ** 2)
        style_loss = torch.mean((generated - style) ** 2)

        loss = content_loss + 0.6 * style_loss
        loss.backward()
        optimizer.step()

    save_image(generated, output_path)