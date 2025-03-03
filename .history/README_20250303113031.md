Here's the updated **README.md**, including a note about the missing `images` folder for privacy reasons.  

---

# **Face Recognizer**

This project is a **face recognition system** built using **OpenCV** and **LBPH (Local Binary Patterns Histograms)**. It detects and recognizes faces from a webcam feed using a trained model.

## **Project Structure**
- **`aifile.py`** → The main script for real-time face recognition.
- **`practice_train.py`** → A training script that processes images, encodes labels, and generates a trained model (`trainer.yml`).
- **`train_faces.py`** → A secondary training script with a slightly different approach for handling face recognition training.

## **⚠️ Important Note**
🚨 **The `images/` folder has been removed for privacy reasons.**  
- This means the dataset required for training is not included in this repository.  
- To train the model, you need to create your own dataset by placing face images in an `images/` folder.

---

## **Features**
✅ Real-time face detection using Haar Cascade  
✅ Face recognition using LBPH algorithm  
✅ Supports training from images stored in a directory  
✅ Saves trained data for later recognition  

---

## **Installation & Setup**
### **1. Clone the Repository**
```sh
git clone https://github.com/your-username/your-repo.git
cd your-repo
```

### **2. Install Dependencies**
Ensure you have the required Python libraries:
```sh
pip install opencv-python opencv-contrib-python numpy pillow
```

### **3. Prepare Training Data**
Since the `images/` folder is missing, you need to create it manually and organize your dataset:
```
images/
├── person1/
│   ├── img1.jpg
│   ├── img2.jpg
├── person2/
│   ├── img1.jpg
│   ├── img2.jpg
```

### **4. Train the Model**
Run either of the training scripts to process the images and generate the model:
```sh
python practice_train.py
```
or
```sh
python train_faces.py
```
- This will create:
  - `trainer.yml` → The trained model.
  - `labels.pickle` → Mappings of labels to names.

### **5. Run the Face Recognizer**
Once training is complete, start real-time face recognition:
```sh
python aifile.py
```
- Press **'q'** to exit the program.

---

## **How It Works**
### **1️⃣ Training (`practice_train.py` & `train_faces.py`)**
- Loads images from the `images/` directory.
- Converts images to grayscale for better detection.
- Detects faces using **Haar Cascade**.
- Encodes faces and labels, then trains a **LBPH recognizer**.
- Saves the trained model as `trainer.yml`.

### **2️⃣ Real-Time Recognition (`aifile.py`)**
- Captures video from the webcam.
- Converts frames to grayscale.
- Detects faces and uses the trained model to recognize them.
- Displays the name of the recognized person on the video feed.

---

## **Author**
Author: [Mohammed Abdullah Amaan](mailto:abdullah@abdullahamaan.com)
---

Let me know if you need any more changes! 🚀