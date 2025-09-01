import numpy as np
from PIL import Image, ImageDraw
import tkinter as tk
from tensorflow.keras.models import load_model
from scipy.ndimage import center_of_mass, shift

model = load_model(r"C:\Users\sajja\OneDrive\Desktop\VSCode\JetLearn\deepLearning\lesson2\digit_recognizer.h5")

class DigitRecognizerApp:
    def __init__(self,model):

        self.model = model
        self.window = tk.Tk()

        self.window.title("Digit Recognizer App")

        self.canvas = tk.Canvas(self.window, width=200, height=200, bg="white")
        self.canvas.grid(row=0,column=0,padx=2,pady=2)
        self.canvas.bind("<B1-Motion>",self.draw)

        self.label = tk.Label(self.window,text="Draw a Digit",font=("Arial",24))
        self.label.grid(row=0,column=1,padx=2,pady=2)

        self.clearBtn = tk.Button(self.window,text="CLEAR",command=self.clearCanvas)
        self.clearBtn.grid(row=1,column=0,padx=2,pady=2)

        self.predictBtn = tk.Button(self.window,text="Predict",command=self.predictDigit)
        self.predictBtn.grid(row=1,column=1,padx=2,pady=2)

        self.image = Image.new("L",(200,200),color="white") # "L" = 8-bit gray scale
        self.draw_obj = ImageDraw.Draw(self.image)

    def draw(self,event):
        x, y = event.x, event.y

        r = 8

        self.canvas.create_oval(x-r,y-r,x+r,y+r,fill="black",outline="black")
        self.draw.obj.ellipse([x-r,y-r,x+r,y+r], fill=0)
    
    def clearCanvas(self):
        self.canvas.delete("all")

        self.image = Image.new("L",(200,200),color="white")
        self.draw_obj = ImageDraw.Draw(self.image)
        self.label.config(text="Draw a digit")
    
    def preprocesImage(self):
        img = self.image.resize((28,28)).convert("L")
        img = np.array(img)

        img = 255 - img
        img = img / 255.0

        cy , cx = center_of_mass(img)
        shiftX = np.round(14-cx)
        shiftY = np.round(14-cy)
        img = shift(img,shift=(shiftY,shiftX),mode="constant",cval=0.0)

        img = np.expand_dims(img,axis=0)

        return img

    def predictDigit(self):
        processedImage = self.preprocesImage()
        prediction = self.model.predict(processedImage)
        digit = np.argmax(prediction)
        self.label.config(text=f"Prediction: {digit}")

    def run(self):
        self.window.mainloop()

app = DigitRecognizerApp(model)
app.run()



        