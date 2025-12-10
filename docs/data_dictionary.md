content = """# 📘 Data Dictionary & Structure

## 1. Overview
* **Database:** `countly`  
* **Main Collection:** `summary`  
* **Data Volume:** ~41,432,473 records  
* **Source:** Raw Clickstream Data  

---

## 2. Collection Structure: `summary`

Bảng mô tả chi tiết các trường dữ liệu trong collection chính phục vụ phân tích hành vi người dùng.

| Field Name | Data Type | Description (Mô tả nghiệp vụ) | Example Value |
| :--- | :--- | :--- | :--- |
| **`_id`** | ObjectId | Khóa chính tự sinh theo MongoDB. | `5ed8cb28e1a...` |
| **`time_stamp`** | Number (Long) | Thời gian sự kiện dạng Unix timestamp (UTC). | `1591266092` |
| **`local_time`** | String | Thời gian hiển thị theo múi giờ người dùng. | `2020-06-04 12:21:27` |
| **`ip`** | String | Địa chỉ IP của thiết bị người dùng. | `37.170.17.183` |
| **`device_id`** | String | ID thiết bị đối với khách chưa login. | `beb2cacb-8846...` |
| **`user_id_db`** | String | Mã khách hàng trong hệ thống (nếu đã đăng nhập). | `502567` |
| **`store_id`** | String | Mã thị trường/cửa hàng quốc gia (ví dụ: 12 = France). | `12` |
| **`collection`** | String | Loại sự kiện hệ thống ghi nhận. | `view_product_detail` |
| **`current_url`** | String | URL trang người dùng đang xem. | `https://glamira.fr/...` |
| **`referrer_url`** | String | URL nguồn dẫn tới trang hiện tại. | `https://glamira.fr/men...` |
| **`product_id`** | String | Mã sản phẩm chính (SKU). | `110474` |
| **`viewing_product_id`** | String | Mã sản phẩm được gợi ý hiển thị. | `89454` |
| **`option`** | Array | Thông tin tùy chọn sản phẩm (color, size…). | `[{"option_label": ...}]` |
| **`ua`** | String | User-Agent của trình duyệt. | `Mozilla/5.0 ...` |
| **`browser`** | String | Trình duyệt user sử dụng. | `Chrome` |
| **`os`** | String | Hệ điều hành thiết bị. | `Android` |
| **`device_type`** | String | Phân loại thiết bị: mobile/tablet/desktop. | `mobile` |
| **`screen_resolution`** | String | Độ phân giải của màn hình. | `1080x2340` |

> 🔍 Một số trường có thể rỗng tùy theo loại sự kiện & thiết bị.

---

## 3. Collection Structure: `ip_locations` (Enriched Data)

Bảng tham chiếu địa lý được sinh từ xử lý IP để phân tích theo khu vực.

| Field Name | Data Type | Description |
| :--- | :--- | :--- |
| **`ip`** | String | Địa chỉ IP (Khóa chính). |
| **`country_short`** | String | Mã quốc gia 2 ký tự theo ISO-3166. |
| **`country_long`** | String | Tên quốc gia đầy đủ. |
| **`region`** | String | Vùng/Bang/Tỉnh tương ứng IP. |
| **`city`** | String | Thành phố người dùng truy cập. |
| **`latitude`** | String | Vĩ độ địa lý. |
| **`longitude`** | String | Kinh độ địa lý. |
"""
with open('/mnt/data/DataDictionary.md','w', encoding='utf-8') as f:
    f.write(content)
'/mnt/data/DataDictionary.md'
