player.onItemInteracted(STICK, function () {
    blocks.fill(
    DIAMOND_BLOCK,
    pos(2, 2, 2),
    pos(12, 12, 12),
    FillOperation.Replace
    )
})
