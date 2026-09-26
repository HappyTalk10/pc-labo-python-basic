# --- 変数とデータ型 -----------------------------------------------------
byte_count = 3          # int型（整数）
label = "3バイトの場合"   # str型（文字列）
is_positive = True       # bool型（真偽値）

print(label)
print("値:", byte_count)
print("型:", type(byte_count))

# --- 四則演算と比較演算子 -------------------------------------------------
bit_count = byte_count * 8   # 1バイト=8ビットなので、8を掛ける
print(f"{byte_count}バイトは{bit_count}ビット")

print(bit_count > 16)   # 比較演算子（16より大きいか）
print(bit_count == 24)  # 等しいか

# --- print()とf-stringの書式指定 ------------------------------------------
n = 5
print(f"{n:3d}")     # 3桁分の幅を確保して右揃えで表示
print(f"{n:08b}")    # 8桁の2進数（2進数表記+0埋め）として表示

# --- つくってみよう：バイト<->ビット変換プログラム -------------------------
def bytes_to_bits(byte_count):
    """バイト数からビット数を求める"""
    return byte_count * 8


def bits_to_bytes(bit_count):
    """ビット数からバイト数を求める（割り切れない場合は切り上げ）"""
    return -(-bit_count // 8)  # 切り上げ割り算


print()
print("=== バイト -> ビット ===")
for b in [1, 3, 10, 100]:
    print(f"{b:4d}バイト -> {bytes_to_bits(b):5d}ビット")

print()
print("=== ビット -> バイト ===")
for bits in [8, 20, 64, 100]:
    print(f"{bits:4d}ビット -> {bits_to_bytes(bits):5d}バイト")
