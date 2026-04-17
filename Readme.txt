🎨 PROJECT NAME
artiFact by Artist

👉 AI-powered Artist Recognition + Neural Style Transfer Web App

🚀 1. WHAT YOU BUILT (SUMMARY)

You built a full AI web application that does two major things:

🧠 1. Artist Recognition System
Upload a painting/image
AI predicts which famous artist created that style
Shows:
Artist name
Biography
Genre
Nationality
Years active
🎨 2. Neural Style Transfer System
Upload:
Content image
Style image
AI combines them
Generates artistic output image
User can download final image
🏗️ 2. HOW YOU BUILT IT (APPROACH)
📌 Step 1: Dataset Preparation

You used:

dataset/train/
Folder of artist images
Each folder = one artist

Example:

dataset/train/
 ├── Picasso/
 ├── Van_Gogh/
 ├── Monet/

👉 Used ImageFolder from torchvision to auto-label data

📌 Step 2: Model Training

You used:

ResNet-18 (Pretrained CNN)

Why?

Fast
Accurate
Good for image classification

Output:

Model learns painting styles
Predicts artist class

Saved as:

artist_model.pth
📌 Step 3: Flask Web App

You created a backend using:

Flask (Python Web Framework)

It handles:

Image upload
Prediction
Style transfer
File download
📌 Step 4: AI Pipeline
🔍 Artist Prediction Flow:
Image → Resize → Tensor → CNN Model → Artist Name
🎨 Style Transfer Flow:
Content Image + Style Image → VGG-based Stylization → Output Image
📌 Step 5: Frontend UI

You built a 2-section interface:

🎯 LEFT SIDE
Artist Detection
Image upload
Prediction result
Artist details
🎨 RIGHT SIDE
Style Transfer
Content image upload
Style image upload
Generated output
Download button
📌 Step 6: Database (CSV File)

You used:

artists.csv

Contains:

Column	Meaning
name	Artist name
years	Birth–Death
genre	Art style
nationality	Country
bio	Description
🎨 3. FEATURES OF YOUR PROJECT

✔ AI Artist Prediction
✔ Neural Style Transfer
✔ Image Upload System
✔ Download Output Image
✔ Artist Biography Display
✔ Beautiful UI Design
✔ Dual AI System (Classification + Generation)

🧠 4. TECH STACK
Layer	Technology
Frontend	HTML + CSS
Backend	Flask
AI Model	PyTorch
CNN Model	ResNet-18
Style Transfer	VGG-based neural transfer
Dataset	ImageFolder + CSV metadata
🖥️ 5. UI STRUCTURE
🎨 LEFT PANEL (Artist Detection)
Upload painting
AI predicts artist
Shows:
Name
Genre
Nationality
Biography
Uploaded image preview
🎨 RIGHT PANEL (Style Transfer)
Upload content image
Upload style image
Generate output image
Download button
📌 FOOTER

Displays credits:

ML Developer: Mayank Singh
Email: 01mayank7773@gmail.com
Data Processing: Jitendra Nath
Web Developer: Sanish
⚙️ 6. HOW SYSTEM WORKS (FLOW)
USER UPLOAD IMAGE
        ↓
Flask Backend Receives File
        ↓
ResNet-18 Model Predicts Artist
        ↓
CSV Fetches Artist Info
        ↓
UI Displays Result

AND

CONTENT + STYLE IMAGE
        ↓
Neural Style Transfer (VGG)
        ↓
Generated Image Saved
        ↓
User Downloads Image
🎯 7. WHY THIS PROJECT IS STRONG (VIVA POINTS)

✔ Combines AI + Web Development
✔ Uses Deep Learning (CNN + VGG)
✔ Real-world application of Art + AI
✔ Dual functionality system
✔ Dataset + model training + deployment
✔ Full-stack implementation

🧾 8. VIVA EXPLANATION (SIMPLE)

“We built an AI-based web application called artiFact that identifies artists from paintings using a CNN model and also performs neural style transfer using deep learning to generate artistic images by combining content and style images.”

🚀 9. WHAT YOU ACHIEVED

You successfully built:

✔ AI Model (Artist Classifier)
✔ Neural Style Transfer System
✔ Flask Web App
✔ Dataset handling
✔ Full UI + backend integration
✔ Download system
✔ Complete AI project deployment

🏁 FINAL RESULT

👉 A complete AI Art Intelligence System

Detects artist style
Generates new artwork
Shows metadata
Allows download
Fully web-based