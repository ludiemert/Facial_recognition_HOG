# 🧑‍💻 Face Recognition Project

This project uses the [face_recognition](https://github.com/ageitgey/face_recognition) library and OpenCV to perform **facial recognition**, detecting and comparing similarities between faces in different images. The goal is to demonstrate how computer vision techniques can be applied to encode facial features and evaluate their correspondence.  

---

## 🛠️ Features

- **Face Detection**  
  Identifies faces in images and returns their coordinates.  
- **Facial Encoding**  
  Extracts 128 unique measurements from a face, creating a numerical representation for comparison.  
- **Face Comparison**  
  Verifies the similarity between two faces using facial encodings and calculates the distance between them.  
- **Visual Display**  
  Displays images with detected faces highlighted by rectangles.  

---

## 🖥️ Technologies Used

- [Python](https://www.python.org/)  
- [OpenCV](https://opencv.org/)  
- [Face Recognition](https://github.com/ageitgey/face_recognition)  

---

## 🚀 Requirements and Setup

Ensure your environment is correctly configured before running the project.

### **Prerequisites**

- Python 3.8 or higher.  
- Install the required dependencies by running:  

```bash
pip install opencv-python face_recognition
```

Directory Structure
Ensure the files are organized as follows:

bash
Copiar código
face-recognition-project/
├── Elon.jpg           # Original test image
├── ElonTest.jpg       # Second test image for similarity check
├── face_recognition.py # Main project script
└── README.md          # This file
Running the Script
Clone the repository to your local environment:

bash
Copiar código
git clone https://github.com/your-username/face-recognition-project.git
cd face-recognition-project
Ensure the images (Elon.jpg and ElonTest.jpg) are in the same directory as the script.

Run the script:

bash
Copiar código
python face_recognition.py
The following outputs will be displayed:

Images with face detection (green rectangles).
Facial similarity results (True or False).
Facial distance between the images.
🧪 Code Explanation
The program follows these steps:

Image Loading and Conversion:

The images are loaded and converted to the RGB format for analysis using the face_recognition library.
Face Detection:

The face_locations() function returns the coordinates of the detected face.
Facial Encoding:

The unique features of the face are extracted using face_encodings(), creating a numerical representation with 128 measurements.
Comparison and Distance:

The compare_faces() function checks if the faces are similar.
The face_distance() function calculates a distance metric between the encodings.
Display Results:

The images are displayed with the faces highlighted, and the comparison results are shown in the console.
Example console output:

bash
Copiar código
[True] [0.4567]
📊 Expected Results
A smaller distance (e.g., distance < 0.6) indicates greater similarity between the faces.
The comparison function (True/False) indicates whether the images contain the same detected face.
Project Visualization
After running the script, two windows will pop up showing the analyzed images:

Original Image (Elon.jpg):
The face will be highlighted with a green rectangle.

Test Image (ElonTest.jpg):
The same processing will be applied to highlight the face and compare it with the original image.

🔍 Graphic Demonstration
Original Image:

Test Image:

🛡️ Possible Improvements
Support for multiple faces in an image.
Add a graphical interface for dynamic image uploads.
Implement support for video (real-time detection).
Support saving results in a JSON file or database.
🤝 Contributions
Contributions are welcome! Follow the steps below to contribute:

Fork the repository.

Create a branch for your feature or fix:

bash
Copiar código
git checkout -b my-feature
Commit your changes:

bash
Copiar código
git commit -m "My new feature"
Push to the branch:

bash
Copiar código
git push origin my-feature
Open a Pull Request in the original repository.

📄 License
This project is licensed under the MIT License.

📧 Contact
If you have questions or suggestions, feel free to reach out:

Author: Your Name
Email: your-email@domain.com
vbnet
Copiar código

### **What’s New in the English Version?**
1. Direct translation of the content while ensuring clarity and technical accuracy.
2. Adjusted formatting to fit an international audience.
3. Maintained all critical sections such as prerequisites, setup, results, and contributions.

Feel free to replace placeholders like `your-username` and `your-email` with your actual information.


### 📦 Contribution

 - Feel free to contribute by submitting pull requests or reporting issues.

- #### My LinkedIn - [![Linkedin Badge](https://img.shields.io/badge/-LucianaDiemert-blue?style=flat-square&logo=Linkedin&logoColor=white&link=https://www.linkedin.com/in/lucianadiemert/)](https://www.linkedin.com/in/lucianadiemert/)

## 🌐 **Contact**
<img align="left" src="https://www.github.com/ludiemert.png?size=150">

#### [**Luciana Diemert**](https://github.com/ludiemert)

🛠 Full-Stack Developer <br>
🖥️ Python Enthusiast | Computer Vision | AI Integrations <br>
📍 São Jose dos Campos – SP, Brazil

<a href="https://www.linkedin.com/in/lucianadiemert" target="_blank"><img src="https://img.shields.io/badge/LinkedIn-0077B5?style=flat&logo=linkedin&logoColor=white" alt="LinkedIn Badge" height="25"></a>&nbsp;
<a href="mailto:lucianadiemert@gmail.com" target="_blank"><img src="https://img.shields.io/badge/Gmail-D14836?style=flat&logo=gmail&logoColor=white" alt="Gmail Badge" height="25"></a>&nbsp;
<a href="#"><img src="https://img.shields.io/badge/Discord-%237289DA.svg?logo=discord&logoColor=white" title="LuDiem#0654" alt="Discord Badge" height="25"></a>&nbsp;
<a href="https://www.github.com/ludiemert" target="_blank"><img src="https://img.shields.io/badge/GitHub-100000?style=flat&logo=github&logoColor=white" alt="GitHub Badge" height="25"></a>&nbsp;

<br clear="left"/>

---
Developed with ❤ by [ludiemert](https://github.com/ludiemert).
