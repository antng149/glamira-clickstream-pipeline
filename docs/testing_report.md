content = """# 🧪 Data Quality Verification Report

## 1. Completeness Check (Kiểm tra độ đầy đủ)

### Raw Data (MongoDB)
- **Command:** `db.summary.countDocuments()`
- **Result:** `41,432,473` records
- **Status:** ✅ *PASSED* — Khớp với dữ liệu nguồn

### Processed IP Data
| Source | Count |
|--------|------:|
| MongoDB (`ip_locations`) | 3,239,628 documents |
| Output File (`ip_locations.csv`) | 3,239,629 lines *(bao gồm header)* |

- **Status:** ✅ *PASSED* — Không mất mát dữ liệu khi export

---

## 2. Consistency Check (Kiểm tra tính nhất quán)

Đối chiếu tính hợp lý số lượng sự kiện theo loại:

| Event Type | Count (MongoDB) | Ghi chú |
|-----------|----------------:|--------|
| view_product_detail | 19,417 | Khớp logic |
| add_to_cart_action | 11,311 | Tỷ lệ phù hợp so với View |
| product_detail_rec_visible | 16,944 | Recommendation đầy đủ |

---

## 3. Uniqueness Check (Kiểm tra trùng lặp)

Kiểm tra File: **products.csv**

- **Command:**
  ```bash
  cut -d, -f1 products.csv | sort | uniq -d
  ```
- **Result:** *Empty* — Không có mã sản phẩm trùng lặp  
- **Conclusion:** `19,277` sản phẩm là **Unique 100%** ✔

---

## 4. Final Conclusion

Dữ liệu đã được:
✔ Nạp  
✔ Làm sạch  
✔ Xuất ra đúng chuẩn
