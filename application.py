import os
from PIL import Image

# Loop through all photos that need framing and export framed photo
for image in os.listdir("input"):
    # Load in frame photo that we will paste onto
    frame_photo_path = os.path.join(R"templates\shadow.png")
    photo_frame = Image.open(frame_photo_path)

    file_to_open = os.path.join("input", image)
    img_to_paste = Image.open(file_to_open)
    photo_frame.paste(img_to_paste, (100, 50), mask=img_to_paste)
    photo_frame.save(os.path.join("output", image))