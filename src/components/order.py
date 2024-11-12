# 假设我们有一个处理订单的服务
orders = {}  # 用于存储已处理的订单

def process_order(order_id, amount):
    # 检查订单是否已经处理过
    if order_id in orders:
        print(f"Order {order_id} has already been processed.")
        return

    # 处理订单
    print(f"Processing order {order_id} for amount {amount}.")
    # 这里是实际的订单处理逻辑，比如更新数据库、发送通知等

    # 保存订单已处理的记录
    orders[order_id] = amount

# 客户端发起请求
process_order("123", 100)
process_order("123", 100)  # 重复请求
