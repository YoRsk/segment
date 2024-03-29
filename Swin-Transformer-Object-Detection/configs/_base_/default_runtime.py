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
load_from = 'C:/Users/liuyi/segment/segment/Swin-Transformer-Object-Detection/mask_rcnn_swin_tiny_patch4_window7.pth'
resume_from = None
workflow = [('train', 1)]
