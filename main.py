import os
import json
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Google Sheets API 設定
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
json_str = os.environ["GOOGLE_SHEETS_CREDENTIALS"]
creds_dict = json.loads(json_str)
creds = ServiceAccountCredentials.from_json_keyfile_dict(creds_dict, scope)

# 連接 Google Sheets
client = gspread.authorize(creds)
sheet = client.open_by_url("https://docs.google.com/spreadsheets/d/12Ji57VmiiRQ_77axFXM57Q9ekqho9Y-Uv7iFoJiNAv0/edit?usp=sharing").sheet1

# 假設這裡要抓股票代碼
stocks = sheet.get_all_records()  # 讀取所有資料

# 這裡可以加入即時股價抓取程式邏輯
# 假設只是顯示讀取到的股票清單
print(stocks)
