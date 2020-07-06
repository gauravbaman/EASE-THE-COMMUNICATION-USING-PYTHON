#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  6 18:41:01 2020

@author: gaurav
"""





import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

train = pd.read_csv('sign_mnist_train.csv')

labels = train['label'].values

train.drop('label', axis = 1, inplace = True)

images = train.values
images = np.array([np.reshape(i, (28, 28)) for i in images])
images = np.array([i.flatten() for i in images])

import speech_recognition as sr

r = sr.Recognizer()
with sr.Microphone() as source:
    print("Speak Anything :")
    audio = r.listen(source)
    try:
        output = r.recognize_google(audio)
       
        
        print("You said : {}".format(output))
        for i in range(len(output)):
            plt.figure(1)
            if output[i]=='a':
                plt.imshow(images[50].reshape(28,28))
            elif output[i]=='c':
                plt.imshow(images[694].reshape(28,28))
            elif output[i]=='d':
                plt.imshow(images[9].reshape(28,28))
            elif output[i]=='e':
                plt.imshow(images[601].reshape(28,28))
            elif output[i]=='f':
                plt.imshow(images[655].reshape(28,28))
            elif output[i]=='g':
                plt.imshow(images[19].reshape(28,28))    
            elif output[i]=='h':
                plt.imshow(images[49].reshape(28,28)) 
            elif output[i]=='i':
                plt.imshow(images[6].reshape(28,28))   
            elif output[i]=='l':
                plt.imshow(images[51].reshape(28,28))  
            elif output[i]=='m':
                plt.imshow(images[35].reshape(28,28))
            elif output[i]=='n':
                plt.imshow(images[614].reshape(28,28))        
            elif output[i]=='o':
                plt.imshow(images[191].reshape(28,28))
            elif output[i]=='p':
                plt.imshow(images[11].reshape(28,28))
            elif output[i]=='q':
                plt.imshow(images[12].reshape(28,28))
            elif output[i]=='r':
                plt.imshow(images[16].reshape(28,28))
            elif output[i]=='s':
                plt.imshow(images[54].reshape(28,28))
            elif output[i]=='t':
                plt.imshow(images[18].reshape(28,28))
            elif output[i]=='u':
                plt.imshow(images[14].reshape(28,28))
            elif output[i]=='v':
                plt.imshow(images[53].reshape(28,28))
            elif output[i]=='w':
                plt.imshow(images[7].reshape(28,28))
            elif output[i]=='x':
                plt.imshow(images[781].reshape(28,28))
            elif output[i]=='y':
                plt.imshow(images[26].reshape(28,28)) 
            elif output[i]=='z':
                plt.imshow(images[644].reshape(28,28))
            plt.show()    
    
    except:
        print("Sorry could not recognize what you said")

