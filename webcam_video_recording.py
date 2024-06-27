import cv2
from datetime import datetime
import os

if not os.path.exists('video_recordings'):
    os.makedirs('video_recordings')
    
    
# Open the webcam
cap = cv2.VideoCapture(0)

# Get camera properties
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = int( cap.get(cv2.CAP_PROP_FPS))

# Set focus on the camera
cap.set(cv2.CAP_PROP_AUTOFOCUS, 0)
cap.set(cv2.CAP_PROP_FOCUS, 10)


print("Camera Properties:")
print("Width:", width)
print("Height:", height)
print("FPS:", fps)

print("Press 'r' to start recording")
print("Press ESC to exit")

# Define the codec and create a VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'mp4v')

recording = False

while True:
    # Read frames from the webcam
    ret, frame = cap.read()
    if ret:
        # Write the frame to the output file if recording is True
        if recording:
            out.write(frame)
        # Display the resulting frame
        cv2.imshow('frame', frame)
        # Break the loop if 'q' is pressed
        key = cv2.waitKey(1) & 0xFF

        # Start recording if 'r' is pressed
        if recording == False and key == ord('r'):
            recording = True
            now = datetime.now().strftime("%Y%m%d_%H%M%S")
            video_filepath = f'video_recordings/recording_{now}.mp4'
            out = cv2.VideoWriter(video_filepath, fourcc, fps, (width, height))
            print("Recording...")
            print("Press 'q' to stop recording")
        # Stop recording if 'q' is pressed
        elif recording == True and key == ord('q'):
            out.release()
            recording = False
            print("Stopped recording. Saved video as:", video_filepath)
            print("Press 'r' to start recording")
            print("Press ESC to exit")
        # Exit program if ESC is pressed
        elif recording == False and key == 27:
            break
    else:
        break



# Release the webcam and close the output file
cap.release()

# Destroy all windows
cv2.destroyAllWindows()