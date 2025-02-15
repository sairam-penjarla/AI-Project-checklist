import os
import random
from PIL import Image, ImageDraw

class ThumbnailHandler:
    def __init__(self, mockup_folder, output_folder, chrome_coordinates, safari_coordinates, chrome_width, safari_width):
        self.mockup_folder = mockup_folder
        self.output_folder = output_folder
        self.chrome_coordinates = chrome_coordinates
        self.safari_coordinates = safari_coordinates
        self.chrome_width = chrome_width
        self.safari_width = safari_width
        self.mockup_files = [os.path.join(mockup_folder, f) for f in os.listdir(mockup_folder) if f.endswith((".png", ".jpg", ".jpeg"))]

    def process_screenshot(self, screenshot_image, file_name):
        if not self.mockup_files:
            return None, "No mockups available."

        selected_mockup = random.choice(self.mockup_files)
        mockup_image = Image.open(selected_mockup).convert("RGBA")
        mockup_basename = os.path.basename(selected_mockup)

        # Determine mockup type and dimensions
        if mockup_basename.startswith("chrome_"):
            coordinates = self.chrome_coordinates
            mockup_width = self.chrome_width
        else:
            coordinates = self.safari_coordinates
            mockup_width = self.safari_width

        # Resize screenshot
        mockup_scale = mockup_width / screenshot_image.width
        new_height = int(screenshot_image.height * mockup_scale)
        resized_screenshot = screenshot_image.resize((mockup_width, new_height), Image.Resampling.LANCZOS)

        # Paste screenshot onto mockup
        composite = mockup_image.copy()
        x, y = coordinates
        composite.paste(resized_screenshot, (x, y), resized_screenshot)

        # Save to output folder
        output_filename = file_name
        output_path = os.path.join(self.output_folder, output_filename)
        composite.save(output_path, format="PNG")
        return output_path, None