"""
Face recognition
"""
# Modules
from cv2 import cv2
import face_recognition as fr
import numpy
import os
from datetime import datetime

# Create DB
path = 'Empleados'
my_images = []
employee_names = []
employee_list = os.listdir(path)

for name in employee_list:
    current_image = cv2.imread(f'{path}/{name}')
    my_images.append(current_image)
    employee_names.append(os.path.splittext(name)[0])

print(employee_names)

# Code images
def code(images):

    # Create a new list
    code_list = []

    # Images to RGB
    for image in images:
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        # Code
        code = fr.face_encodings(image)[0]

        # Add to list
        code_list.append(code)
    # Return code list
    return code_list


# Register 
def register(person):
    f = open('registro.csv', 'r+')
    data_list = f.readlines()
    register_names = []
    for line in data_list:
        enter = line.split(',')
        register_names.append(enter[0])
    
    if person not in register_names:
        now = datetime.now()
        str_now = now.strftime('%H:%M:%S')
        f.writelines(f'\n{person}, {str_now}')


employee_code_list = code(my_images)

# Take photo from webcam
capture = cv2.VideoCapture(0, cv2.CAP_DSHOW)

# Read image from webcam
success, image = capture.read()

if not success:
    print('No webcam photo')
else:
    # Acknowledge captured face
    captured_face = fr.face_locations(image)
    
    # Code captured face
    code_captured_face = fr.face_encondings(image, captured_face)

    # Look for matches
    for code_face, location_face in zip(code_captured_face, captured_face):
        matches = fr.compare_faces(employee_code_list, code_face)
        distances = fr.face_distance(employee_code_list, code_face)

        print(distances)

        matches_index = numpy.argmin(distances)

        # Display matches
        if distances[matches_index] > 0.6:
            print("There are not matches")

        else:

            # Look for name of the found employee
            name = employee_names[matches_index]

            y1, x2, y2, x1 = location_face
            cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.rectangle(image, (x1, y2 - 35), (x2, y2), (0, 255, 0), cv2.FILLED)
            cv2.putText(image, name, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 2555, 255), 2)

            register(name)

            # Display got image
            cv2.imshow('Webcam', image)

            # Keep open window
            cv2.waitKey(0)
