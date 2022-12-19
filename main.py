# TODO: api; postmanem wysłać zdjęcia??

# Doinstalowane paczki: imutils, numpy, opencv-python

import imutils
import numpy
import cv2
from flask import Flask
from flask_restful import Resource, Api
import json

app = Flask(__name__)
api = Api(app)

# Ścieżka do do pliku .prototxt
# z tekstowym opisem architektury sieci
protopath = "MobileNetSSD_deploy.prototxt"

# Ścieżka do modelu z wyuczoną siecią
modelpath = "MobileNetSSD_deploy.caffemodel"

# Utworzenie detektora wykrywającego elementy na zdjęciu
# na podstawie protofile i modelu
detector = cv2.dnn.readNetFromCaffe(prototxt=protopath, caffeModel=modelpath)

# Wypisanie wszystkich możliwych klas z modelu
model_classes = ["background", "aeroplane", "bicycle", "bird", "boat",
                 "bottle", "bus", "car", "cat", "chair", "cow", "diningtable",
                 "dog", "horse", "motorbike", "person", "pottedplant", "sheep",
                 "sofa", "train", "tvmonitor"]


# Metoda zwracająca odpowiednią odmianę słowa "osoba"
# w zależności od liczby osób wykrytych na zdjęciu
def peopleDeclination(people_counter):
    if people_counter == 1:
        string = "osoba"
    elif 1 < people_counter < 5:
        string = "osoby"
    else:
        string = "osób"
    return string

def beDeclination(people_counter):
    if 1 < people_counter < 5:
        string = "znajdują"
    else:
        string = "znajduje"
    return string

# Metoda wykrywająca i zliczająca liczbę osób na zdjęciu
def personDetectionFromImage(image):
    # Wczytanie zdjęcia poprzez podanie ścieżki
    image = cv2.imread(image)

    # Zmiana rozmiaru zdjęcia
    image = imutils.resize(image, width=600)

    # Krotka zawierająca dwa pierwsze elementy image.shape
    # czyli wysokość i szerokość zdjęcia
    (height, width) = image.shape[0:2]

    # Utworzenie blob'a (binary large object)
    # poprzez metodę korzystającą z sieci neuronowej,
    # przyjmującą ścieżkę do zdjęcia, współczynnik skali,
    # rozmiar oraz średnie wartości odejmowania
    # (image, scalefactor, size, mean)
    # (dnn - deep neural network - głęboka sieć neuronowa)
    blob = cv2.dnn.blobFromImage(image, 0.008, (width, height), (30, 90, 130))

    # Przekazanie bloba do detectora
    detector.setInput(blob)

    # Zmienna zawierająca wszystkie detekcje
    person_detections = detector.forward()

    # Zmienna przechowująca liczbę wykrytych osób na zdjęciu
    people_counter = 0

    for i in numpy.arange(0, person_detections.shape[2]):
        #  Wyliczenie dopasowania wykrycia
        result_match = person_detections[0, 0, i, 2]
        # Interpretowanie wyników dopasowania większych od 0.6
        if result_match > 0.6:
            # Przypisanie numeru indeksu danej detekcji
            index = int(person_detections[0, 0, i, 1])

            # Jeżeli index detekcji nie jest zgodny z indexem osoby
            # w tablicy klas - pominięcie detekcji i przejście do kolejnej
            if model_classes[index] != "person":
                continue

            # Zwiększenie licznika osób po wykryciu
            people_counter = people_counter + 1

            # Wyliczenie ramki zaznaczającej wykrytą osobę
            person_box = person_detections[0, 0, i, 3:7] * numpy.array([width, height, width, height])
            (startX, startY, endX, endY) = person_box.astype("int")

            # Kolor ramki
            frame_color = (0, 255, 0)
            # Grubość ramki
            frame_thickness = 1
            # Narysowanie ramki dookoła wykrytej osoby
            cv2.rectangle(image, (startX, startY), (endX, endY), frame_color, frame_thickness)

    result = (f"Na zdjęciu {beDeclination(people_counter)} się "
          f"{people_counter} "
          f"{peopleDeclination(people_counter)}.")
    print(result)
    cv2.imshow("Wykrywanie osob", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def callPersonDetection():
    personDetectionFromImage("people1.png")
    personDetectionFromImage("people2.png")
    personDetectionFromImage("people3.jpg")
    personDetectionFromImage("people4.png")


if __name__ == '__main__':
    app.run(debug=True)
