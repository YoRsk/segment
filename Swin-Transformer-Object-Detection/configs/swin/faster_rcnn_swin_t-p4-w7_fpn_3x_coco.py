_base_ = [
    '../_base_/models/faster_rcnn_swin_fpn.py',
    '../_base_/datasets/faster_rcnn_coco_instance.py',
    '../_base_/schedules/schedule_1x.py', '../_base_/default_runtime.py'
]

optimizer = dict(
    _delete_=True,
    type='AdamW',
    lr=0.005,
    betas=(0.9, 0.999),
    weight_decay=0.05,
    paramwise_cfg=dict(
        custom_keys={
            'absolute_pos_embed': dict(decay_mult=0.),
            'relative_position_bias_table': dict(decay_mult=0.),
            'norm': dict(decay_mult=0.)
        }))
lr_config = dict(warmup_iters=1000, step=[27, 33])
runner = dict(type='EpochBasedRunner', max_epochs=60)
# epoch 更改,35->60
# learning rate更改 0.0001->0.005