from rembg import remove
from PIL import Image
image_input = Image.open(input_path)
output = remove(image_input)
output.save(output_path)
