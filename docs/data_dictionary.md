# 📘 Data Dictionary & Structure

## 1. Overview
* **Database:** `countly`
* **Main Collection:** `summary`
* **Data Volume:** ~41,432,473 records
* **Source:** Raw Clickstream Data

---

## 2. Collection Structure: `summary`

Bảng dưới đây mô tả chi tiết các trường dữ liệu trong collection chính.

| Field Name | Data Type | Description (Mô tả nghiệp vụ) | Example Value |
| :--- | :--- | :--- | :--- |
| **`_id`** | ObjectId | Khóa chính tự sinh (Unique ID). | `5ed8cb2...` |
| **`time_stamp`** | Number (Long)| Thời gian sự kiện (Unix Timestamp). | `1591266092` |
| **`local_time`** | String | Thời gian thực tế tại múi giờ người dùng. | `2020-06-04 12:21:27` |
| **`ip`** | String | Địa chỉ IP người dùng. | `37.170.17.183` |
| **`device_id`** | String | Mã định danh thiết bị (cho khách vãng lai). | `beb2cacb...` |
| **`user_id_db`** | String | Mã khách hàng (User ID) nếu đã đăng nhập. | `502567` |
| **`store_id`** | String | Mã cửa hàng/thị trường quốc gia (VD: 12 = France). | `12` |
| **`collection`** | String | **Loại sự kiện**. VD: `view_product`. | `view_product_detail` |
| **`current_url`** | String | URL trang hiện tại khách đang xem. | `https://glamira.fr/...` |
| **`referrer_url`** | String | URL trang trước đó. | `https://glamira.fr/men...` |
| **`product_id`** | String | Mã sản phẩm chính (SKU). | `110474` |
| **`viewing_product_id`**| String | Mã sản phẩm được gợi ý. | `89454` |
| **`option`** | Array | Danh sách tùy chọn (Màu, Size...). | `[{ "option_label":... }]` |

---

## 3. Collection Structure: `ip_locations` (Enriched Data)

Bảng tham chiếu địa lý được tạo ra từ quá trình xử lý IP (Step 3).

| Field Name | Data Type | Description |
| :--- | :--- | :--- |
| **`ip`** | String | Địa chỉ IP (Khóa chính). |
| **`country_short`**| String | Mã quốc gia 2 ký tự (ISO 3166). |
| **`country_long`** | String | Tên đầy đủ quốc gia. |
| **`region`** | String | Tên vùng/bang/tỉnh. |
| **`city`** | String | Tên thành phố. |
| **`latitude`** | String | Vĩ độ. |
| **`longitude`** | String | Kinh độ. |
