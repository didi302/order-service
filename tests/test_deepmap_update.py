"""DeepMap 更新识别用的订单服务回归测试。

测试标识：DEEPMAP-UPDATE-ORDER-20261030
"""

import unittest

from src.order_service import ORDERS, cancel_order, create_order, refund_order


class DeepMapOrderUpdateTest(unittest.TestCase):
    """验证订单核心状态流转，便于在 DeepMap 中识别本次更新。"""

    def setUp(self):
        ORDERS.clear()

    def tearDown(self):
        ORDERS.clear()

    def test_create_then_cancel_order(self):
        order = create_order("DEEPMAP-CANCEL-001", "PRODUCT-001", 1)

        self.assertEqual("CREATED", order["status"])
        self.assertEqual("CANCELLED", cancel_order(order["order_id"])["status"])

    def test_paid_order_can_be_refunded(self):
        order = create_order("DEEPMAP-REFUND-001", "PRODUCT-002", 2)
        order["status"] = "PAID"

        self.assertEqual("REFUNDED", refund_order(order["order_id"])["status"])


if __name__ == "__main__":
    unittest.main()
