"""订单标签管理模块，用于验证 DeepMap 的模块级增量更新。

增量测试标识：DEEPMAP-INCREMENTAL-ORDER-TAG-20261030
"""

ORDER_TAGS = {}


def add_order_tag(order_id, tag):
    """为订单新增标签；同一标签不会重复保存。"""
    tags = ORDER_TAGS.setdefault(order_id, [])
    if tag not in tags:
        tags.append(tag)
    return list(tags)


def get_order_tags(order_id):
    """查询订单的全部标签；订单没有标签时返回空列表。"""
    return list(ORDER_TAGS.get(order_id, []))


def remove_order_tag(order_id, tag):
    """删除订单标签；标签不存在时保持原数据不变。"""
    tags = ORDER_TAGS.get(order_id, [])
    if tag in tags:
        tags.remove(tag)
    if not tags:
        ORDER_TAGS.pop(order_id, None)
    return list(tags)
