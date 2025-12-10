import IP2Location
from pymongo import MongoClient
import time

# --- CẤU HÌNH ---
BIN_FILE_PATH = "IP-COUNTRY-REGION-CITY.BIN"
MONGO_DB_NAME = "countly"
SOURCE_COLLECTION = "summary"
TARGET_COLLECTION = "ip_locations" # Bảng mới để lưu kết quả

def process_ip_locations():
    print("--- BẮT ĐẦU XỬ LÝ IP ---")
    start_time = time.time()

    # 1. Kết nối MongoDB
    client = MongoClient('localhost', 27017)
    db = client[MONGO_DB_NAME]
    
    # 2. Khởi tạo thư viện IP2Location
    print(f"Đang load database IP từ: {BIN_FILE_PATH}...")
    ip2loc_obj = IP2Location.IP2Location(BIN_FILE_PATH)

    # 3. Lấy danh sách IP duy nhất (Dùng Aggregation để tiết kiệm RAM)
    print("Đang quét tìm các IP duy nhất trong 41 triệu bản ghi...")
    print("Việc này có thể mất vài phút, vui lòng chờ...")
    
    pipeline = [
        {"$group": {"_id": "$ip"}} # Nhóm theo IP để lấy unique
    ]
    
    # Cho phép ghi ra ổ cứng (allowDiskUse) nếu RAM không đủ
    unique_ips_cursor = db[SOURCE_COLLECTION].aggregate(pipeline, allowDiskUse=True)
    
    # 4. Xử lý và Lưu kết quả
    batch_data = []
    count = 0
    
    print("Đang tra cứu địa điểm và lưu vào DB...")
    
    for doc in unique_ips_cursor:
        ip_address = doc['_id']
        
        # Bỏ qua nếu IP rỗng hoặc null
        if not ip_address:
            continue
            
        # Tra cứu thông tin
        rec = ip2loc_obj.get_all(ip_address)
        
        # Tạo bản ghi kết quả
        location_data = {
            "ip": ip_address,
            "country_short": rec.country_short,
            "country_long": rec.country_long,
            "region": rec.region,
            "city": rec.city,
            "latitude": rec.latitude,
            "longitude": rec.longitude
        }
        
        batch_data.append(location_data)
        count += 1
        
        # Ghi theo lô (Batch) mỗi 1000 dòng để nhanh hơn
        if len(batch_data) >= 1000:
            db[TARGET_COLLECTION].insert_many(batch_data)
            batch_data = []
            print(f"Đã xử lý: {count} IP...")

    # Ghi nốt số còn lại nếu có
    if batch_data:
        db[TARGET_COLLECTION].insert_many(batch_data)

    end_time = time.time()
    print(f"--- HOÀN THÀNH ---")
    print(f"Tổng số IP duy nhất đã xử lý: {count}")
    print(f"Thời gian chạy: {end_time - start_time:.2f} giây")
    print(f"Kết quả đã lưu vào collection: '{TARGET_COLLECTION}'")

if __name__ == "__main__":
    process_ip_locations()
