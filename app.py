# 1. Khởi tạo kho chứa Git tại máy tính
git init

# 2. Thêm tất cả các file trong thư mục vào Git
git add .

# 3. Tạo một bản lưu (commit)
git commit -m "Khoi tao game Mario Streamlit"

# 4. Đổi tên nhánh chính thành main
git branch -M main

# 5. Kết nối máy tính với GitHub (thay URL bên dưới bằng URL kho chứa của bạn)
git remote add origin https://github.com/Tên_Tài_Khoản/mario-streamlit-game.git

# 6. Đẩy code lên GitHub
git push -u origin main
