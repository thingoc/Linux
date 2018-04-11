clear
echo "Hãy chắc chắn bạn đã tạo kho trên github.com"
echo "Xin hãy chọn chức năng:"
echo "- Nhập vào 1 để tạo kho mới tại thư mục hiện hành"
echo "- Nhập vào 2 để tự động push lên github"
echo "- Kiểm tra xem file đã được đẩy lên chưa? nếu thấy hiện màu đỏ các file hãy chọn tùy chọn 2"
read -p "Nhập vào chức năng:" chucnang
case $chucnang in 
1)
	echo "#MY PROJECT" > README.md
	git init
	git add README.md
	read -p "Nhập vào tin nhắn của bạn để push lên github:" tinnhan
	git commit -m "$tinnhan"
	read -p "NHập vào đường dẫn kho github bạn đã tạo (copy link kho trên thanh địa chỉ):" duongdan
	git remote add origin $duongdan".git"
	git config credential.helper store 
	git push -f origin master
	echo "Bạn đã tạo kho thành công!";;
2)
	git add .
	read -p "Nhập vào tin nhắn của bạn để push lên github:" message
	git commit -m "$message"
	git push -f origin master
	echo "Đẩy file lên thành công";;
3)
	git status
	echo "Hãy chạy lại chương trình";;
*)
	echo "Nhập sai chức năng!"
esac 

