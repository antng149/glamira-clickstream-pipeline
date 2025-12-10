## 1️⃣ Project Overview (Tổng quan dự án)

Dự án xây dựng hệ thống xử lý dữ liệu lớn (**Big Data Pipeline**) cho dữ liệu hành vi người dùng (Clickstream) của trang thương mại điện tử **Glamira**.

**Mục tiêu:**
- Xây dựng hạ tầng trên Cloud
- Nạp hơn **41 triệu bản ghi** dữ liệu thô
- Thực hiện quy trình **ETL (Extract – Transform – Load)**
- Làm giàu thông tin địa lý và sản phẩm phục vụ Analytics

**Mục tiêu dự án:** 
- Xây dựng hạ tầng trên Cloud, nạp hơn 41 triệu bản ghi dữ liệu thô và thực hiện quy trình ETL (Extract - Transform - Load) để làm sạch, trích xuất thông tin địa lý & danh mục sản phẩm phục vụ Analytics.
---

## 2️⃣ Architecture & Tech Stack (Kiến trúc & Công nghệ)

### 🛠 Tech Stack

#### Cloud Infrastructure
- **Google Cloud Storage (GCS):** lưu trữ Raw Data (`.tar.gz`, `.bin`)
- **Google Compute Engine (GCE):** Ubuntu 22.04 LTS VM (e2-medium, 50GB SSD)

#### Database
- **MongoDB Community 7.0** — Lưu trữ dữ liệu bán cấu trúc (JSON/BSON)

#### Programming & Tools
- **Python 3**
- Libraries: `pymongo`, `IP2Location`, `csv`, `re`
- Tools: `gcloud CLI`, `mongosh`, `mongoexport`

---

## 3️⃣ Key Achievements (Kết quả đạt được)

| Metric | Value | Description |
|-------|------:|-------------|
| **Total Raw Records** | 41,432,473 | Số event được nạp vào `countly.summary` |
| **Processed Unique IPs** | 3,239,628 | IP đã enrich vào `ip_locations` |
| **Extracted Products** | 19,277 | Unique SKU từ URL & event |

## 📊 Key Data Insights (Phân tích dữ liệu chính)

From 41M clickstream events enriched in Phase 1, the user behavior pattern shows:

Dựa trên 41 triệu sự kiện hành vi đã xử lý ở Phase 1, hành vi người dùng thể hiện rõ:

- Người dùng tương tác nhiều nhất tại trang chi tiết sản phẩm  
  (19,417 lượt xem chi tiết sản phẩm)

- Mức độ quan tâm cao đến tùy chọn sản phẩm (màu sắc, size…)  
  (16,850 lượt chọn option + 8,731 lượt chọn chất lượng sản phẩm)

- Tín hiệu chuyển đổi tốt qua hành động thêm vào giỏ hàng  
  (11,311 hành động add-to-cart)

- Hệ thống gợi ý sản phẩm hoạt động hiệu quả  
  (16,944 lượt hiển thị gợi ý & 14,544 lượt người dùng chú ý đến gợi ý)
  
➡️ Kết quả cho thấy dữ liệu đạt chất lượng tốt và sẵn sàng cho các phân tích chuyên sâu ở giai đoạn tiếp theo.

---


---

## 4️⃣ Pipeline Steps (Quy trình xử lý)

### ✔ Step 1: Infrastructure Setup
- Tạo GCS Bucket: `raw-project5-k20`
- Tạo VM Instance + Firewall + API permissions
- Cài đặt MongoDB Server & Python Environment

### ✔ Step 2: Data Ingestion (Nạp liệu)
- Tải dữ liệu từ GCS → VM
- Giải nén **5.5GB → ~30GB**
- `mongorestore` nạp vào database

### ✔ Step 3: IP Location Enrichment
- Dữ liệu quá lớn → **không lookup từng record**
- Giải pháp: **Unique IP Strategy**
- MongoDB Aggregation → danh sách IP unique
- Lookup địa lý bằng `IP2Location .BIN`
- Tạo collection: `ip_locations`

### ✔ Step 4: Product Master Extraction
- Quét event liên quan đến sản phẩm
- Ưu tiên: `product_id` → `viewing_product_id`
- Regex xử lý slug → Tạo Product Master
- Remove duplicate → **Unique Product List**

---

## 5️⃣ Repository Structure (Cấu trúc thư mục)

```
├── docs/
│   ├── DATA_DICTIONARY.md      # Tài liệu mô tả cấu trúc dữ liệu
│   └── TESTING_REPORT.md       # Data Quality Verification Report
├── scripts/
│   ├── process_ips.py          # Enrich IP Location
│   └── extract_products.py     # Trích xuất Product Master
├── data_sample/
│   └── products.csv            # File kết quả mẫu
└── README.md                   # Tài liệu tổng quan dự án
```

---

## 6️⃣ How to Run (Hướng dẫn chạy)

### SSH vào VM
```bash
gcloud compute ssh mongodb-server-project5
```

### Chạy script xử lý IP
```bash
python3 scripts/process_ips.py
```

### Chạy script trích xuất sản phẩm
```bash
python3 scripts/extract_products.py
```

### Kiểm tra file đầu ra
```bash
ls -lh *.csv
```


