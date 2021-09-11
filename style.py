import tensorflow as tf
import tensorflow_hub as hub
from matplotlib import gridspec
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np
plt.ioff()


def tensor_to_image(tensor):
  tensor = tensor*255
  tensor = np.array(tensor, dtype=np.uint8)
  if np.ndim(tensor)>3:
    assert tensor.shape[0] == 1
    tensor = tensor[0]
  return Image.fromarray(tensor)

def pokemonize(img_path, pokemon_img_path, output_file_name):
    # Load content and style images (see example in the attached colab).
    content_image = plt.imread(img_path)
    style_image = plt.imread(pokemon_img_path)

    # Convert to float32 numpy array, add batch dimension, and normalize to range [0, 1]. Example using numpy:
    content_image = content_image.astype(np.float32)[np.newaxis, ...] / 255.
    style_image = style_image.astype(np.float32)[np.newaxis, ...] / 255.
    # Optionally resize the images. It is recommended that the style image is about
    # 256 pixels (this size was used when training the style transfer network).
    # The content image can be any size.
    style_image = tf.image.resize(style_image, (256, 256))

    # Load image stylization module.
    hub_module = hub.load('https://tfhub.dev/google/magenta/arbitrary-image-stylization-v1-256/2')

    # Stylize image.
    outputs = hub_module(tf.constant(content_image), tf.constant(style_image))
    stylized_image = outputs[0] 

    tensor_to_image(stylized_image).save(f"files/{output_file_name}.png")