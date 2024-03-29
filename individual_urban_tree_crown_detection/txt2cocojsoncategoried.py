import json
import os
from PIL import Image


def get_image_size(image_path):
    with Image.open(image_path) as img:
        return img.width, img.height


def read_split_file(split_file_path):
    with open(split_file_path, 'r') as file:
        return [line.strip() for line in file.readlines()]


def convert_to_coco_json(bbox_txt_dir, images_dir, img_list_dir, output_dir):
    # Read image list for each split
    train_images = set(read_split_file(os.path.join(img_list_dir, 'train.txt')))
    val_images = set(read_split_file(os.path.join(img_list_dir, 'val.txt')))
    test_images = set(read_split_file(os.path.join(img_list_dir, 'test.txt')))

    # Initialize COCO dataset structure for each split
    coco_format_train = {"images": [], "annotations": [], "categories": []}
    coco_format_val = {"images": [], "annotations": [], "categories": []}
    coco_format_test = {"images": [], "annotations": [], "categories": []}

    # Add category information (assuming a single class dataset)
    category_info = {'id': 1, 'name': 'tree', 'supercategory': 'none'}
    for coco_format in [coco_format_train, coco_format_val, coco_format_test]:
        coco_format['categories'].append(category_info)

    annotation_id = 1
    image_id = 1

    for filename in os.listdir(bbox_txt_dir):
        if filename.endswith('.txt'):
            image_file_name = filename.replace('.txt', '.png')  # Change the extension if necessary
            image_path = os.path.join(images_dir, image_file_name)
            width, height = get_image_size(image_path)

            # Determine which split the image belongs to
            if image_file_name in train_images:
                coco_format = coco_format_train
            elif image_file_name in val_images:
                coco_format = coco_format_val
            elif image_file_name in test_images:
                coco_format = coco_format_test
            else:
                continue  # Skip images not in any split

            # Add image information
            image_info = {"id": image_id, "file_name": image_file_name, "width": width, "height": height}
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

    # Ensure the output directory exists
    os.makedirs(output_dir, exist_ok=True)

    # Write the COCO data to files
    for split_name, coco_format in zip(['train', 'val', 'test'],
                                       [coco_format_train, coco_format_val, coco_format_test]):
        with open(os.path.join(output_dir, f'coco_annotations_{split_name}.json'), 'w') as outfile:
            json.dump(coco_format, outfile, indent=4)


if __name__ == '__main__':
    bbox_txt_dir = './bbox_txt'  # 相对于脚本的路径
    images_dir = './rgb'  # 相对于脚本的路径
    img_list_dir = './img_list/4'  # 相对于脚本的路径，包含train.txt, val.txt, test.txt
    output_dir = './annotations'  # 输出文件的路径
    convert_to_coco_json(bbox_txt_dir, images_dir, img_list_dir, output_dir)
