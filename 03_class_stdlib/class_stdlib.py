import hashlib
from itertools import product


# --- クラスの基本：商品を表すProductクラス -----------------------------------
class Product:
    """商品を表すクラス"""

    def __init__(self, name, price, quantity):
        self.name = name          # 商品名
        self.price = price        # 価格
        self.quantity = quantity  # 数量

    def total(self):
        """価格x数量（在庫の合計金額）を返す"""
        return self.price * self.quantity

    def show(self):
        print(f"{self.name}: {self.price:,}円 x {self.quantity}個 = {self.total():,}円")


items = [
    Product("カメラ", 13000, 20),
    Product("テレビ", 58000, 15),
    Product("冷蔵庫", 65000, 8),
]

print("=== 商品一覧 ===")
for item in items:
    item.show()


# --- 2分探索木のNodeクラスの前段階 --------------------------------------------
class Node:
    """木の1つの節を表すクラス"""

    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


root = Node(17, left=Node(14), right=Node(19))
print()
print("=== Nodeクラス ===")
print("根:", root.value)
print("左の子:", root.left.value)
print("右の子:", root.right.value)

# --- 標準ライブラリを使ってみる ----------------------------------------------
print()
print("=== itertools.product ===")
for p, q in product([True, False], repeat=2):
    print(p, q)

print()
print("=== hashlib.sha256 ===")
print(hashlib.sha256("hello".encode()).hexdigest())
