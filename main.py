import random
import string
import schedule
import time
import json
from flask import Flask, render_template

app = Flask(__name__)


# Hàm tạo API key ngẫu nhiên
def generate_api_key(length=32):
    characters = string.ascii_letters + string.digits
    api_key = ''.join(random.choice(characters) for _ in range(length))
    return api_key

# Lưu API key vào file
def save_api_key(api_key, file_path='api_key.json'):
    with open(file_path, 'w') as file:
        json.dump({'api_key': api_key}, file)

# Tải API key từ file
def load_api_key(file_path='api_key.json'):
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            return data.get('api_key')
    except FileNotFoundError:
        return None

# Hàm cập nhật API key
def update_api_key():
    new_api_key = generate_api_key()
    save_api_key(new_api_key)
    print(f"New API Key: {new_api_key}")

# Lên lịch cập nhật API key mỗi ngày vào lúc 00:00
schedule.every().day.at("00:00").do(update_api_key)

# Chạy vòng lặp vô hạn để thực hiện lịch trình
def run_schedule():
    while True:
        schedule.run_pending()
        time.sleep(1)

import threading
threading.Thread(target=run_schedule).start()

# Route cho trang chủ
@app.route('/')
def index():
    api_key = load_api_key()
    return render_template('index.html', api_key=api_key)

if __name__ == '__main__':
    # Cập nhật API key ngay khi khởi động
    update_api_key()
    app.run(debug=True)
    app.run(host='0.0.0.0', port=5000)