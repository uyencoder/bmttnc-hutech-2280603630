import sys
from PIL import Image  

def decode_image(encoded_image_path):
    try:
        img = Image.open(encoded_image_path)
    except FileNotFoundError:
        print("LỖI: Không tìm thấy file ảnh. Hãy kiểm tra đường dẫn.")
        return None
    except Exception as e:
        print(f"LỖI: Không thể mở ảnh. Chi tiết lỗi: {e}")
        return None

    width, height = img.size
    binary_message = ""

    for row in range(height):
        for col in range(width):
            pixel = img.getpixel((col, row))
            
            for color in range(3):
                binary_message += str(pixel[color] & 1)

    # Tìm vị trí của chuỗi kết thúc '1111111111111110'
    end_marker = "1111111111111110"
    end_index = binary_message.find(end_marker)
    if end_index != -1:
        binary_message = binary_message[:end_index]  # Cắt phần chứa tin nhắn thực sự

    # Chuyển đổi chuỗi nhị phân thành văn bản
    message = "".join(chr(int(binary_message[i:i+8], 2)) for i in range(0, len(binary_message), 8))

    return message

def main():
    if len(sys.argv) != 2:
        print("Cách dùng: python decrypt.py <encoded_image_path>")
        return
    
    encoded_image_path = sys.argv[1]
    decoded_message = decode_image(encoded_image_path)
    
    if decoded_message:
        print("Thông điệp giải mã:", decoded_message)
    else:
        print("Không tìm thấy tin nhắn trong ảnh!")

if __name__ == "__main__":
    main()
