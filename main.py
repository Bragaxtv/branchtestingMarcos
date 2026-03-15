def on_item_interacted_stick():
    blocks.fill(BLACK_WOOL,
        pos(5, 0, 5),
        pos(10, 10, 10),
        FillOperation.REPLACE)
player.on_item_interacted(STICK, on_item_interacted_stick)
