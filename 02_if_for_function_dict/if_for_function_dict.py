# --- 条件分岐（if / elif / else） -----------------------------------------
score = 82

if score >= 90:
    print("S判定")
elif score >= 80:
    print("A判定")
else:
    print("B判定以下")

# --- ループ（for, range） -------------------------------------------------
for i in range(3):
    print(f"{i}回目")

fruits = ["りんご", "みかん", "ぶどう"]
for fruit in fruits:
    print(fruit)

# --- 辞書（dict） -----------------------------------------------------------
port_names = {80: "HTTP", 443: "HTTPS", 21: "FTP"}
print(port_names[80])
print(port_names.get(8080, "登録なし"))

for port, name in port_names.items():
    print(f"{port}番 -> {name}")

# --- 関数の引数（複数引数・デフォルト引数） ---------------------------------
def rank(score, passing_score=60):
    """点数からランクを返す（合格ラインはデフォルト60点）"""
    if score < passing_score:
        return "不合格"
    elif score >= 90:
        return "S"
    elif score >= 80:
        return "A"
    else:
        return "B"


print(rank(85))
print(rank(55))
print(rank(55, passing_score=50))  # 合格ラインを50点に変更

# --- つくってみよう：得点からランク判定＋集計プログラム ----------------------
scores = [95, 82, 67, 40, 73]
counts = {}  # ランクごとの人数を数える辞書

print()
print("=== 各生徒の判定 ===")
for s in scores:
    r = rank(s)
    print(f"{s:3d}点 -> {r}")
    counts[r] = counts.get(r, 0) + 1  # そのランクの人数を1増やす

print()
print("=== ランク別人数 ===")
for r, count in counts.items():
    print(f"{r}: {count}人")
