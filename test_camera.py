print("TEST STARTED")


from app.vision.camera import capture_image


print("Camera module loaded")



image = capture_image()



if image is None:

    print("Camera not detected")


else:

    print("Image captured successfully")