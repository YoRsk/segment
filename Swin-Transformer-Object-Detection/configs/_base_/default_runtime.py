checkpoint_config = dict(interval=2)
# yapf:disable
log_config = dict(
    interval=50,
    hooks=[
        dict(type='TextLoggerHook'),
        # dict(type='TensorboardLoggerHook')
    ])
# yapf:enable
custom_hooks = [dict(type='NumClassCheckHook')]

dist_params = dict(backend='nccl')
log_level = 'INFO'
load_from = None
#load_from = 'C:/Users/liuyi/segment/segment/Swin-Transformer-Object-Detection/mask_rcnn_swin_tiny_patch4_window7.pth'
# When using faster_rcnn_swin_t-p4-w7_fpn_3x_coco.py, the following log will be printed:
# 2024-04-08 01:20:05,839 - mmdet - INFO - load checkpoint from local path: C:/Users/liuyi/segment/segment/Swin-Transformer-Object-Detection/mask_rcnn_swin_tiny_patch4_window7.pth
# 2024-04-08 01:20:06,087 - mmdet - WARNING - The model and loaded state dict do not match exactly

resume_from = None
workflow = [('train', 1)]
