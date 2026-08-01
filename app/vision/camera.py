import cv2



def open_camera():

    camera = cv2.VideoCapture(0)


    if not camera.isOpened():

        return None


    return camera




def capture_image():

    camera = open_camera()


    if camera is None:

        print("Camera could not open")

        return None



    success, frame = camera.read()


    camera.release()



    if success:

        return frame


    return None