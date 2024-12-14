
## Title: Webcam Photo Sharer
####  Description: An app that starts the computer webcam, lets the user capture a photo
and uploads the photo to the web and creates a sharable link.
Objects: 

    CameraScreen:
            start()
            stop()
            capture()
    FileSharer:
            filepath
            api
            share()
# Design
![Design](./design-frontend.png)

##### For using this Software you need uploadcare account and api key and public key put in a .env file in the same folder as this file

    UPLOADCARE_PUBLIC_KEY=public_key put here
    UPLOADCARE_SECRET_KEY=secret key put here
