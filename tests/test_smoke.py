def test_smoke():
    from lambdawalker.yolo.log.vis_log import save_visual_log
    assert save_visual_log is not None
    print("yolo OK")
