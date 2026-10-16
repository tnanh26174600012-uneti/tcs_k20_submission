from datetime import datetime

# Checkpoint A & B: Nhập dữ liệu 4 trường
ma_quan_sat = input("Nhập mã quan sát: ")
dai_luong = input("Nhập tên đại lượng: ")
gia_tri_raw = input("Nhập giá trị đo: ")
don_vi = input("Nhập đơn vị: ")

# Chuyển kiểu giá trị đo sang float
gia_tri_do = float(gia_tri_raw)

# Checkpoint C: Lấy thời điểm hiện tại
thoi_diem = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Checkpoint C: Xuất bản ghi bằng f-string
print(f"Mã quan sát : {ma_quan_sat}")
print(f"Đại lượng : {dai_luong}")
print(f"Giá trị : {gia_tri_do:.2f} {don_vi}")
print(f"Thời điểm : {thoi_diem}")