🚀 Glamira Clickstream Data Engineering Pipeline

1. Project Overview (Tổng quan dự án)

Dự án xây dựng hệ thống xử lý dữ liệu lớn (Big Data Pipeline) cho dữ liệu hành vi người dùng (Clickstream) của trang thương mại điện tử Glamira.

Mục tiêu là xây dựng hạ tầng trên Cloud, nạp hơn 41 triệu bản ghi dữ liệu thô, và thực hiện các quy trình ETL (Extract - Transform - Load) để làm sạch, trích xuất thông tin địa lý và danh mục sản phẩm phục vụ cho Analytics.

Role: Data Engineer

Platform: Google Cloud Platform (GCP)

Dataset Volume: ~41,432,473 records

Status: Phase 1 Completed

2. Architecture & Tech Stack (Kiến trúc & Công nghệ)

🛠 Tech Stack

Cloud Infrastructure:

Google Cloud Storage (GCS): Lưu trữ Raw Data (.tar.gz, .bin).

Google Compute Engine (GCE): Máy ảo Ubuntu 22.04 LTS (e2-medium, 50GB SSD) để xử lý dữ liệu.

Database:

MongoDB Community 7.0: NoSQL Database để lưu trữ dữ liệu bán cấu trúc (JSON/BSON).

Programming & Tools:

Python 3: Ngôn ngữ xử lý chính (ETL).

Libraries: pymongo, IP2Location, csv, re.

Tools: gcloud CLI, mongosh, mongoexport.

3. Key Achievements (Kết quả đạt được)

Dự án đã xử lý thành công khối lượng dữ liệu lớn với các chỉ số cụ thể:

Metric

Value

Description

Total Raw Records

41,432,473

Tổng số sự kiện (events) được nạp vào MongoDB (countly.summary).

Processed Unique IPs

3,239,628

Số lượng IP duy nhất được xử lý và định vị địa lý.

Extracted Products

19,277

Danh sách sản phẩm duy nhất (Unique SKUs) được trích xuất và làm sạch từ URL.

Processing Time

~10 mins

Thời gian xử lý 41 triệu dòng nhờ tối ưu thuật toán Aggregation.

4. Pipeline Steps (Quy trình xử lý)

Step 1: Infrastructure Setup (Hạ tầng)

Thiết lập GCS Bucket (raw-project5-k20) để chứa dữ liệu thô.

Khởi tạo VM Instance trên GCP, cấu hình Firewall và quyền truy cập API.

Cài đặt môi trường: MongoDB Server, Python environment.

Step 2: Data Ingestion (Nạp liệu)

Tải dữ liệu từ GCS về VM.

Giải nén file .tar.gz (5.5GB nén -> ~30GB giải nén).

Sử dụng mongorestore để nạp dữ liệu BSON vào Database.

Step 3: IP Location Enrichment (Làm giàu dữ liệu địa lý)

Thách thức: Dữ liệu quá lớn (41 triệu dòng), không thể tra cứu từng dòng.

Giải pháp: Sử dụng chiến thuật "Unique IP Strategy".

Dùng MongoDB Aggregation để lọc ra danh sách IP duy nhất.

Sử dụng thư viện IP2Location và database .BIN để tra cứu thông tin (Country, City, Region).

Lưu kết quả vào collection riêng ip_locations.

Step 4: Product Master Data Extraction (Trích xuất danh mục)

Mục tiêu: Tạo danh sách sản phẩm chuẩn từ các URL sự kiện.

Logic xử lý:

Quét 7 loại sự kiện liên quan đến sản phẩm (view, add_to_cart, recommendation...).

Xử lý logic ưu tiên: Lấy product_id hoặc viewing_product_id.

URL Parsing: Sử dụng Regex để cắt chuỗi URL, trích xuất tên sản phẩm (Slug) và làm sạch (Capitalize, remove dashes).

Deduplication: Loại bỏ trùng lặp để có danh sách Unique Product.

5. Repository Structure (Cấu trúc thư mục)

```
├── docs/
│   ├── DATA_DICTIONARY.md      # Tài liệu mô tả cấu trúc dữ liệu chi tiết
│   └── TESTING_REPORT.md       # Báo cáo kiểm thử chất lượng dữ liệu
├── scripts/
│   ├── process_ips.py          # Script xử lý IP Location
│   └── extract_products.py     # Script trích xuất thông tin sản phẩm
├── data_sample/
│   └── products.csv            # File kết quả mẫu (Danh sách sản phẩm)
└── README.md                   # Tài liệu tổng quan dự án
```

6. How to Run (Hướng dẫn chạy)

1. SSH vào máy ảo GCP:

gcloud compute ssh mongodb-server-project5


2. Chạy script xử lý IP:

python3 scripts/process_ips.py


3. Chạy script trích xuất sản phẩm:

python3 scripts/extract_products.py


4. Kiểm tra kết quả:

ls -lh *.csv


7. Future Improvements (Cải tiến tương lai)

[ ] Tự động hóa Pipeline bằng Apache Airflow.

[ ] Đẩy dữ liệu đã làm sạch lên BigQuery để phân tích chuyên sâu.

[ ] Xây dựng Dashboard báo cáo bằng Looker Studio.

Author: [Tên của bạn]
Course: K20 Data Engineering
