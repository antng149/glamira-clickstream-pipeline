import csv
import re
from pymongo import MongoClient
from urllib.parse import urlparse

# --- CẤU HÌNH ---
DB_NAME = "countly"
COLLECTION_NAME = "summary"
OUTPUT_FILE = "products.csv"

def extract_product_name(url):
    """
    Hàm tách tên sản phẩm từ URL.
    Ví dụ: .../glamira-pendant-viktor.html -> glamira pendant viktor
    """
    if not url:
        return None
    try:
        # 1. Lấy phần đường dẫn (bỏ https://... và ?...)
        path = urlparse(url).path
        # 2. Lấy phần tên file cuối cùng (glamira-pendant-viktor.html)
        slug = path.split('/')[-1]
        # 3. Bỏ đuôi .html
        if slug.endswith('.html'):
            slug = slug[:-5]
        # 4. Thay dấu gạch ngang bằng khoảng trắng cho đẹp
        clean_name = slug.replace('-', ' ').title()
        return clean_name
    except:
        return None

def main():
    print("--- BẮT ĐẦU TÁCH TÊN SẢN PHẨM ---")
    client = MongoClient('localhost', 27017)
    db = client[DB_NAME]

    # Pipeline: Gộp 2 luồng dữ liệu và Lọc trùng Product ID
    pipeline = [
        {
            "$match": {
                "collection": {
                    "$in": [
                        "view_product_detail",
                        "select_product_option",
                        "select_product_option_quality",
                        "add_to_cart_action",
                        "product_detail_recommendation_visible",
                        "product_detail_recommendation_noticed",
                        "product_view_all_recommend_clicked"
                    ]
                }
            }
        },
        {
            "$project": {
                "product_id": {
                    "$ifNull": ["$product_id", "$viewing_product_id"]
                },
                "url": {
                    "$ifNull": ["$current_url", "$referrer_url"]
                }
            }
        },
        {
            "$match": {
                "product_id": {"$exists": True, "$ne": ""},
                "url": {"$exists": True, "$ne": ""}
            }
        },
        # Nhóm theo Product ID để lấy 1 URL đại diện duy nhất
        {
            "$group": {
                "_id": "$product_id",
                "sample_url": {"$first": "$url"}
            }
        }
    ]

    print("Đang quét và xử lý dữ liệu (Có thể mất vài phút)...")
    
    # Cho phép ghi đĩa nếu RAM không đủ (allowDiskUse=True)
    cursor = db[COLLECTION_NAME].aggregate(pipeline, allowDiskUse=True)

    count = 0
    with open(OUTPUT_FILE, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['product_id', 'product_name', 'source_url']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for doc in cursor:
            p_id = doc['_id']
            url = doc['sample_url']
            
            # Gọi hàm tách tên
            p_name = extract_product_name(url)
            
            if p_name:
                writer.writerow({
                    'product_id': p_id,
                    'product_name': p_name,
                    'source_url': url
                })
                count += 1
                
                if count % 1000 == 0:
                    print(f"Đã tìm thấy: {count} sản phẩm...")

    print(f"--- HOÀN TẤT! ---")
    print(f"Tổng số sản phẩm tìm được: {count}")
    print(f"File kết quả: {OUTPUT_FILE}")

if __name__ == "__main__":
    main()
