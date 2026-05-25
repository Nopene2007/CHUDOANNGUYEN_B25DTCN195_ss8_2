user_choice = ""
shop_name = ""
product_name = ""
description = ""
category = ""
keywords_check = ""
sale_price = []

while user_choice != "5":
    print(" HỆ THỐNG QUẢN LÝ NỘI DUNG SẢN PHẨM SHOPEE ")
    print(" 1. Nhập dữ liệu sản phẩm và xem báo cáo thống kê             ")
    print("2. Chuẩn hóa tên Shop                                        ")
    print("3. Kiểm tra mã giảm giá hợp lệ                               ")
    print(" 4. Tìm kiếm và thay thế từ khóa trong mô tả sản phẩm       ")
    print("5. Thoát chương trình                                        ")


    user_choice = input("> Mời bạn chọn chức năng (1-5): ").strip()
    
    if user_choice not in ["1", "2", "3", "4", "5"]:
        print("Lựa chọn không hợp lệ và yêu cầu nhập lại.")
        continue
        
    choice = int(user_choice)
    
    match choice:
        case 1:
            raw_shop_name = input("Nhập tên shop: ")
            raw_product_name = input("Nhập tên sản phẩm: ")
            raw_description = input("Nhập mô tả sản phẩm: ")
            raw_category = input("Nhập danh mục sản phẩm: ")
            raw_keywords_check = input("Nhập danh sách từ khóa tìm kiếm (cách nhau bởi dấu phẩy): ")

            if raw_shop_name.strip() == "":
                print("Tên shop không được bỏ trống")
                continue

            if raw_description.strip() == "":
                print("Mô tả sản phẩm không được rỗng")
                continue

            shop_name = raw_shop_name.strip()
            product_name = raw_product_name.strip()
            description = raw_description.strip()
            category_str = raw_category.strip()
            keywords_str = raw_keywords_check

            clean_product_name = product_name.title()

            clean_category = category_str.lower()

            desc_words = description.split()
            desc_word_count = len(desc_words)

            raw_keywords = keywords_str.split(",")
            keyword_count = 0
            if keywords_str.strip() != "":
                keyword_count = len(raw_keywords)

            print( " BÁO CÁO THỐNG KÊ SẢN PHẨM ")
            print("- Tên shop sau khi loại bỏ khoảng trắng đầu và cuối:", shop_name)
            print("- Tên sản phẩm sau khi loại bỏ khoảng trắng đầu, cuối và viết hoa chữ cái đầu mỗi từ:", clean_product_name)
            print("- Mô tả sản phẩm sau khi loại bỏ khoảng trắng đầu và cuối:", description)
            print("- Độ dài mô tả sản phẩm (số ký tự):", len(description))
            print("- Danh mục sản phẩm sau khi chuẩn hóa khoảng trắng, chuyển thành chữ thường:", clean_category)
            print("- Danh sách từ khóa tìm kiếm sau khi chuẩn hóa khoảng trắng:")
            for i in raw_keywords:
                print(f"  + '{i.strip()}'")
            print("- Số lượng từ khóa tìm kiếm:", keyword_count)
            print("- Mô tả sản phẩm được chuyển toàn bộ sang chữ thường:", description.lower())
            print("- Mô tả sản phẩm được chuyển toàn bộ sang chữ hoa:", description.upper())
            
        case 2:
            if shop_name == "":
                print("Vui lòng thực hiện nhập dữ liệu tại Chức năng 1 trước!")
                continue

            temp_shop = shop_name.lower().replace(" ", "-")
            if not temp_shop.startswith("shop-"):
                clean_shop_name = "shop-" + temp_shop
            else:
                clean_shop_name = temp_shop
                
            print("- Tên shop ban đầu:", shop_name)
            print("- Tên shop sau khi được chuẩn hóa:", clean_shop_name)
            
        case 3:
            if shop_name == "":
                print("Vui lòng thực hiện nhập dữ liệu tại Chức năng 1 trước!")
                continue
                
            code_sale = input("Nhập một mã giảm giá cần kiểm tra: ").strip()

            if  code_sale== "":
                print("Lỗi: Mã giảm giá không được rỗng")
            elif " " in code_sale:
                print("Lỗi: Mã giảm giá không được chứa khoảng trắng")
            elif len(code_sale) < 6 or len(code_sale) > 12:
                print("Lỗi: Mã giảm giá phải có độ dài từ 6 đến 12 ký tự")
            elif code_sale != code_sale.upper():
                print("Lỗi: Mã giảm giá phải được viết hoa toàn bộ")
            elif not code_sale.startswith("SALE"):
                print("Lỗi: Mã giảm giá phải bắt đầu bằng chuỗi SALE")
            else:
                check = True
                for i in code_sale:
                    if i not in "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789":
                        check = False
                
                if not check:
                    print("Lỗi: Mã giảm giá chỉ được chứa chữ cái và chữ số")
                else:
                    sale_price.append(code_sale)
                    print("-> Danh sách mã giảm giá hiện tại của sản phẩm:", sale_price)
                    
        case 4:
            if description == "":
                print("Vui lòng thực hiện nhập dữ liệu tại Chức năng 1 trước!")
                continue
                
            search_keyword = input("Từ khóa cần tìm: ")
            replace_keyword = input("Từ khóa thay thế: ")
            
            if search_keyword in description:
                occurrences = description.count(search_keyword)
                new_description = description.replace(search_keyword, replace_keyword)
                
                print("Hiển thị mô tả sau khi thay thế:", new_description)
                print("Số lần từ khóa cần tìm xuất hiện trong mô tả:", occurrences)
                description = new_description
            else:
                print(f"Không tìm thấy từ khóa '{search_keyword}' trong đoạn mô tả hiện tại.")
                
        case 5:
            print("Thoát chương trình.")