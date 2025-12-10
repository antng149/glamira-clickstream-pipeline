# Data Quality Verification Report

----------------------------------------------------------------------
1. Completeness Check (Kiểm tra độ đầy đủ)
----------------------------------------------------------------------

# Raw Data (MongoDB)
Command: db.summary.countDocuments()
Result: 41,432,473 records.
Status: PASSED ✅  (Khớp với dữ liệu nguồn)

# Processed IP Data
MongoDB (ip_locations): 3,239,628 documents
Output File (ip_locations.csv): 3,239,629 lines (bao gồm header)
Status: PASSED ✅  (Không mất mát dữ liệu khi export)

----------------------------------------------------------------------
2. Consistency Check (Kiểm tra tính nhất quán)
----------------------------------------------------------------------

Event Type                      Count (MongoDB)      Note
----------------------------------------------------------------------
view_product_detail             19,417               Khớp logic
add_to_cart_action              11,311               Tỷ lệ phù hợp so với View
product_detail_rec_visible      16,944               Recommendation đầy đủ

----------------------------------------------------------------------
3. Uniqueness Check (Kiểm tra trùng lặp)
----------------------------------------------------------------------

File kiểm tra: products.csv
Command chạy:
cut -d, -f1 products.csv | sort | uniq -d

Result: Empty (Không có dòng nào xuất hiện)
Conclusion: 19,277 sản phẩm là Unique 100% ✔

----------------------------------------------------------------------
4. Final Conclusion
----------------------------------------------------------------------

Dữ liệu đã được nạp, làm sạch và xử lý thành công.
Hệ thống sẵn sàng cho các bước phân tích tiếp theo. 🚀
