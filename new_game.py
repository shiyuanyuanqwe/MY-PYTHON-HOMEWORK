import random

print("-----GAME START-----")

def generate_secret():
    return random.randint(1, 100)

def get_user_guess():
    while True:
        guess_str = input("请输入数字（1-100）：")
        if guess_str.isdigit():
            return int(guess_str)
        print("请输入有效的数字")

def check_guess(guess, secret):
    if guess == secret:
        return "胜利！"
    elif guess > secret:
        return "猜大了！"
    else:
        return "猜小了！"

def play_game():
    secret = generate_secret()
    attempts = 0

    while True:
        guess = get_user_guess()
        attempts += 1
        result = check_guess(guess, secret)
        print(result)
        if result == "胜利！":
            print(f"你用{attempts}次猜中了！")
            break
    print("-----GAME OVER-----")

play_game()
