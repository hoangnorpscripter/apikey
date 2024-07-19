const fs = require('fs');
const schedule = require('node-schedule');
const randomstring = require('randomstring');

// Hàm tạo API key
function generateApiKey(length = 32) {
    const characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789';
    return randomstring.generate({ length: length, charset: characters });
}

// Hàm lưu API key vào file
function saveApiKey(apiKey, filePath = 'api_key.json') {
    fs.writeFileSync(filePath, JSON.stringify({ api_key: apiKey }));
}

// Hàm tải API key từ file
function loadApiKey(filePath = 'api_key.json') {
    try {
        const data = fs.readFileSync(filePath);
        return JSON.parse(data).api_key;
    } catch (error) {
        return null;
    }
}

// Hàm cập nhật API key
function updateApiKey() {
    const newApiKey = generateApiKey();
    saveApiKey(newApiKey);
    console.log(`New API Key: ${newApiKey}`);
}

// Lên lịch cập nhật API key hàng ngày vào lúc 00:00
schedule.scheduleJob('0 0 * * *', updateApiKey);

// Cập nhật API key ban đầu khi khởi động
updateApiKey();

// Hàm ghi API key vào file HTML

const p = document.getElementById('key');
p.innerHTML = loadApiKey()

schedule.scheduleJob('1 0 * * *', writeApiKeyToHtml);
