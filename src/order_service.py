"""订单管理服务：创建、取消和查询订单。"""

ORDERS = {}

def create_order(order_id, product_id, quantity):
    """创建订单，初始状态为 CREATED。"""
    if quantity <= 0:
        raise ValueError("购买数量必须大于0")
    order = {
        "order_id": order_id,
        "product_id": product_id,
        "quantity": quantity,
        "status": "CREATED"
    }
    ORDERS[order_id] = order
    return order

def get_order(order_id):
    """查询订单详情。"""
    return ORDERS.get(order_id)

def cancel_order(order_id):
    """取消未完成的订单。"""
    order = ORDERS.get(order_id)
    if not order:
        raise ValueError("订单不存在")
    if order["status"] != "CREATED":
        raise ValueError("当前状态不允许取消")
    order["status"] = "CANCELLED"
    return order

def get_order_status(order_id):
    """获取订单状态。"""
    order = get_order(order_id)
    return order["status"] if order else "NOT_FOUND"


def refund_order(order_id):
    order = ORDERS.get(order_id)
    if not order:
        raise ValueError("订单不存在")
    if order["status"] != "PAID":
        raise ValueError("只有已支付订单允许退款")
    order["status"] = "REFUNDED"
    return order
