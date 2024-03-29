# TODO: 数据集缺少字段（segmentation可能)使用swin-tiny预训练模型， python tools/train.py configs/swin/mask_rcnn_swin_tiny_patch4_window7_mstrain_480-800_adamw_3x_coco.py
# TODO: 先尝试使用 faster-rcnn来做目标检测，然后再尝试使用mask-rcnn           mmdet变成了2.23.0版本，而不是2.20.0版本
# images字段:
# id: 图像的唯一标识符。
# file_name: 图像文件的名称。
# width: 图像的宽度。                                                 对于大多数任务来说是必须的，因为它们帮助模型理解图像的尺寸。
# height: 图像的高度。                                                对于大多数任务来说是必须的，因为它们帮助模型理解图像的尺寸。

#images:
#license, coco_url, date_captured, flickr_url: 这些字段通常是可选的，主要用于数据集的元数据描述。

# annotations字段:
# id: 注释的唯一标识符。
# image_id: 注释所属的图像的ID。
# category_id: 注释所属的类别的ID。
# segmentation: 对象的分割掩码，可以是多边形格式（一系列的x,y坐标点）或RLE（Run Length Encoding）格式。    对于实例分割任务是必须的，但对于纯目标检测任务则是可选的。
# area: 分割掩码所覆盖的区域大小。                                           对于实例分割任务通常是必须的，因为它有助于模型理解对象的大小。但对于纯目标检测任务，这个字段可能不是必须的。
# bbox: 对象的边界框，格式为[x_min, y_min, width, height]。                                对于目标检测任务是必须的，提供对象的边界框。
# iscrowd: 指示一个注释是否代表一群对象（iscrowd=1）或单个对象（iscrowd=0）。 这个字段用于指示注释是否代表一群对象。       对于使用RLE格式的分割掩码的特定任务是必须的，但在其他情况下可能是可选的。

# categories字段:
# id: 类别的唯一标识符。
# name: 类别的名称。
# supercategory: 类别的上级分类名称。


