import os
import torch
import torch.nn as nn
from PIL import Image
from flask import Flask, render_template, request, send_file
from torchvision import transforms, models, datasets
from style import stylize
from artist_info import get_artist_info

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
STATIC_FOLDER = "static"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(STATIC_FOLDER, exist_ok=True)

dataset = datasets.ImageFolder("dataset/train")
class_names = dataset.classes

model = models.resnet18()
model.fc = nn.Linear(model.fc.in_features, len(class_names))
model.load_state_dict(torch.load("artist_model.pth", map_location="cpu"))
model.eval()

transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor()
])

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    file = request.files["image"]

    path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(path)

    # save image also in static so browser can show it
    static_path = os.path.join("static", file.filename)
    Image.open(path).save(static_path)

    image = Image.open(path).convert("RGB")
    img = transform(image).unsqueeze(0)

    with torch.no_grad():
        output = model(img)
        _, pred = torch.max(output, 1)

    artist = class_names[pred.item()]
    info = get_artist_info(artist)

    return render_template(
        "index.html",
        result=artist,
        image_file=file.filename,
        info=info
    )

@app.route("/style", methods=["POST"])
def style_transfer():
    content = request.files["content"]
    style = request.files["style"]

    content_path = os.path.join(UPLOAD_FOLDER, content.filename)
    style_path = os.path.join(UPLOAD_FOLDER, style.filename)

    content.save(content_path)
    style.save(style_path)

    output_path = os.path.join(STATIC_FOLDER, "output.jpg")

    stylize(content_path, style_path, output_path)

    return render_template("index.html", output_image="output.jpg")

@app.route("/download")
def download():
    return send_file("static/output.jpg", as_attachment=True)

if __name__ == "__main__":
    print("🚀 artiFact running...")
    app.run(debug=True)