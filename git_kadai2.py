# パターン①：四則演算
import math

# 2つの数字を入力する
number1 = int(input("最初の数字を入力してください: "))
number2 = int(input("2番目の数字を入力してください: "))

# 四則演算を行う
sum = number1 + number2
difference = number1 - number2
product = number1 * number2
quotient = number1 / number2

# 最小公倍数と最大公約数を求める
gcd = math.gcd(number1, number2)
lcm = math.lcm(number1, number2)

# 平均値を求める
average = (number1 + number2) / 2

# 結果を出力する
print("合計:", sum)
print("差:", difference)
print("積:", product)
print("商:", quotient)
print("最小公倍数:", gcd)
print("最大公約数:", lcm)
print("平均値:", average)

# パターン②：数字当てゲーム
import random

print("3桁の数字を当てるゲームです．")

# 正解の数字を決定する
random_number = random.randint(100, 999)

# 回答回数を設定
number_of_guesses = 10

# ゲームを開始する
for i in range(number_of_guesses):

    # ユーザーに数字を入力させる
    guess = int(input("数字を入力してください: "))

    # 正解かどうかを判定する
    if guess == random_number:
        print("正解です！")
        break
    else:
        if guess > random_number:
            print("もっと小さい数字です．")
        else:
            print("もっと大きい数字です．")

# 回答回数が終了したらゲームを終了する
if i == number_of_guesses - 1:
    print("ゲームオーバーです．正解は", random_number, "でした．")
