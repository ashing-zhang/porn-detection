import os.path as osp
import numpy as np
import onnxruntime
from PIL import Image


def load_images(img_paths, image_size):
    inputs = []
    for path in img_paths:
        img = Image.open(path).convert("RGB")
        img = img.resize((image_size, image_size))
        image = np.array(img, dtype=np.float32)
        image /= 255.0
        inputs.append(image) 
    return np.asarray(inputs)


def load_model():
    path = osp.join(osp.dirname(__file__), 'model.onnx')
    model = onnxruntime.InferenceSession(path)
    return model


model = load_model()
input_name = model.get_inputs()[0].name
tags = ['drawings', 'hentai', 'neutral', 'porn', 'sexy']


def with_tags(out):
    global tags
    out = {tag: round(float(o),3) for (tag, o) in zip(tags, out)}
    return out


def classify(img_path):
    global model
    global input_name
    img = load_images([img_path], 224)
    out = model.run(None, {input_name: img})[0][0]
    out = with_tags(out)
    return out


def classify_many(img_paths):
    global model
    global input_name
    global tags
    img = load_images(img_paths, 224)
    many = model.run(None, {input_name: img})[0]
    out = [ with_tags(out) for out in many ]
    return out
