import json
import os
from PIL import Image


def get_image_size(image_path):
    with Image.open(image_path) as img:
        return img.width, img.height


def convert_to_coco_json(bbox_txt_dir, images_dir, output_json_path):
    # Initialize the COCO dataset structure
    coco_format = {
        "images": [],
        "annotations": [],
        "categories": []
    }

    # Add category information (assuming a single class dataset)
    coco_format['categories'].append({
        'id': 1,
        'name': 'tree',  # or your class name
        'supercategory': 'none',
    })

    annotation_id = 1
    image_id = 1

    for filename in os.listdir(bbox_txt_dir):
        if filename.endswith('.txt'):
            # Construct image file path and get image size
            image_file_name = filename.replace('.txt', '.png')  # Change the extension if necessary
            image_path = os.path.join(images_dir, image_file_name)
            width, height = get_image_size(image_path)

            # Add image information
            image_info = {
                "id": image_id,
                "file_name": image_file_name,
                "width": width,
                "height": height
            }
            coco_format['images'].append(image_info)

            # Read bounding box information from .txt file
            with open(os.path.join(bbox_txt_dir, filename), 'r') as file:
                for line in file:
                    x_min, y_min, x_max, y_max = map(int, line.strip().split(' '))

                    width = x_max - x_min
                    height = y_max - y_min

                    # Create annotation entry
                    annotation = {
                        "id": annotation_id,
                        "image_id": image_id,
                        "category_id": 1,  # Single class
                        "bbox": [x_min, y_min, width, height],
                        "area": width * height,
                        "iscrowd": 0
                    }
                    coco_format['annotations'].append(annotation)
                    annotation_id += 1

            image_id += 1

    # Ensure the directory exists
    os.makedirs(os.path.dirname(output_json_path), exist_ok=True)

    # Write the COCO data to a file
    with open(output_json_path, 'w') as outfile:
        json.dump(coco_format, outfile, indent=4)


if __name__ == '__main__':
    bbox_txt_dir = './bbox_txt'  # 相对于脚本的路径
    images_dir = './rgb'  # 相对于脚本的路径
    output_json_path = './annotations/coco_annotations.json'  # 输出文件的路径
    convert_to_coco_json(bbox_txt_dir, images_dir, output_json_path)
