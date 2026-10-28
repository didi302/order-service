# 订单业务规则

## 创建订单
订单创建后状态为 CREATED。

## 取消订单
只有 CREATED 状态允许取消订单。

## 退款规则
当前版本支持退款，仅 PAID 状态订单允许退款。

## 核心业务标识
DEEPMAP-BUSINESS-ORDER-001
