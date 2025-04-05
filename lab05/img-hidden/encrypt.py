import sys
from PIL import Image  

def encode_image(image_path, message):
    try:
        print("Đang mở ảnh từ đường dẫn:", image_path)
        img = Image.open(image_path)
    except FileNotFoundError:
        print("LỖI: Không tìm thấy file ảnh. Hãy kiểm tra đường dẫn.")
        return
    except Exception as e:
        print(f"LỖI: Không thể mở ảnh. Chi tiết lỗi: {e}")
        return

    width, height = img.size
    binary_message = ''.join(format(ord(char), '08b') for char in message)
    binary_message += '1111111111111110'  # Dấu hiệu kết thúc tin nhắn
    
    max_bits = width * height * 3  # Số bit có thể chứa
    if len(binary_message) > max_bits:
        print("LỖI: Thông điệp quá dài để giấu trong ảnh này.")
        return

    data_index = 0
    for row in range(height):
        for col in range(width):
            pixel = list(img.getpixel((col, row)))  # Lấy giá trị RGB
            
            for color in range(3):  # Lặp qua R, G, B
                if data_index < len(binary_message):
                    pixel[color] = (pixel[color] & ~1) | int(binary_message[data_index])
                    data_index += 1

            img.putpixel((col, row), tuple(pixel))
            
            if data_index >= len(binary_message):
                break  # Dừng khi đã mã hóa xong
    
    encoded_image_path = "encoded_image.png"
    img.save(encoded_image_path)
    print(f"Steganography hoàn tất. Ảnh đã mã hóa lưu tại: {encoded_image_path}")

def main():
    if len(sys.argv) != 3:
        print("Cách dùng: python encrypt.py <image_path> <message>")
        return 
    
    image_path = sys.argv[1]
    message = sys.argv[2]
    encode_image(image_path, message)
    
if __name__ == "__main__":
    main()
