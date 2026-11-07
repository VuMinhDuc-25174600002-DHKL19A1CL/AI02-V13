# Smart Campus AI02 — Web V13

Ứng dụng Streamlit phân loại ảnh rác theo 6 lớp TrashNet: bìa carton, thủy tinh, kim loại, giấy, nhựa và rác khác.

## Tải mã nguồn

Tải `AI02_V13_submission.zip` từ danh sách file của repository và giải nén. Gói gồm mã nguồn, checkpoint MobileNetV3-Large, mô hình Baseline, cùng báo cáo huấn luyện. Bộ ảnh TrashNet không được đóng gói.

## Tính năng

- Nhận diện ảnh đơn, so sánh mô hình và phân tích hàng loạt.
- Nhận diện đa góc bằng 2–6 ảnh chụp thật của cùng một vật; xác suất được tổng hợp từ mô hình đã chọn.
- Tư vấn khả năng tái chế theo nhãn dự đoán và thông tin người dùng khai báo. Đây là hướng dẫn tham khảo, không thay thế quy định của điểm thu gom địa phương.
- Lịch sử phiên và xuất CSV.

Đa góc có thể giúp kết quả ổn định hơn nhưng không đảm bảo chính xác hơn. Mô hình chỉ dự đoán trong 6 lớp đã huấn luyện và có thể sai.

## Chạy trên Windows

Tạo/kích hoạt môi trường Python đã cài các thư viện của dự án, sau đó tại thư mục này chạy:

```powershell
python -m pip install -r requirements.txt -r requirements_cnn.txt
python -m streamlit run app.py --server.address 127.0.0.1 --server.port 8501
```

Hoặc chạy `01_CHAY_LOCAL_V13.bat`, rồi mở http://localhost:8501.

## Mô hình và dữ liệu

Checkpoint MobileNetV3-Large và Baseline được đặt trong `model/`; kết quả đánh giá nằm trong `results/` và `results_cnn/`. Mô hình SVM cải tiến V4 (`improved.joblib`) không nằm trong gói upload web do vượt giới hạn kích thước; có thể tạo lại từ mã nguồn huấn luyện. Bộ ảnh huấn luyện không được đóng gói. Để huấn luyện lại, tải TrashNet và làm theo `README_V9.md`/`README_V13.md`.

Chỉ nạp checkpoint tin cậy do dự án tạo ra. Không tải hoặc nạp các file mô hình không rõ nguồn gốc.
