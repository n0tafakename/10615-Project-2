import scipy.misc, numpy as np, os, sys
import imageio
from PIL import Image
from skimage.transform import resize
import pdb

def save_img(out_path, img):
    img = np.clip(img, 0, 255).astype(np.uint8)
    new_img = np.zeros((img.shape[0], img.shape[1], 4), dtype=np.uint8)
    new_img[:, :, :3] = img
    new_img[:, :, 3] = ((1 - (img == 0).all(-1)) * 255).astype(np.uint8)
    assert new_img.shape[-1] == 4
    imageio.imwrite(out_path, new_img)
    # Image.fromarray(new_img).save(out_path, "png")

def scale_img(style_path, style_scale):
    scale = float(style_scale)
    o0, o1, o2 = imageio.imread(style_path, pilmode='RGBA').shape
    scale = float(style_scale)
    new_shape = (int(o0 * scale), int(o1 * scale), o2)
    style_target = _get_img(style_path, img_size=new_shape)
    return style_target

def get_img(src, img_size=False):
   img = imageio.imread(src, pilmode='RGB')

   img = resize(img, (1024, 1024, 3))
   if not (len(img.shape) == 3 and img.shape[2] == 3):
       img = np.dstack((img,img,img))
   if img_size != False:
       img = np.array(Image.fromarray(img).resize(img_size[:2]))
   return img

def exists(p, msg):
    assert os.path.exists(p), msg

def list_files(in_path):
    files = []
    for (dirpath, dirnames, filenames) in os.walk(in_path):
        files.extend([fname for fname in filenames if not fname[0] == '.' ])
        break

    return files
