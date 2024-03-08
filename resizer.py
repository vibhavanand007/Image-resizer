import cv2


def resize_image(input_image_path, output_image_path, scale_percent):
    image = cv2.imread(input_image_path, cv2.IMREAD_UNCHANGED)

    # Calculate the new dimensions based on the scale percentage
    new_width = int(image.shape[1] * scale_percent / 100)
    new_height = int(image.shape[0] * scale_percent / 100)

    resized_image = cv2.resize(image, (new_width, new_height))

    cv2.imwrite(output_image_path, resized_image)

    print("Image resized successfully.")

if __name__ == "__main__":
    input_image_path = "file1.png"
    output_image_path = "resize_image.png"

    scale_percent = int(input("Resize into (1-100,%) : "))  # Resize to 50% of original size

    resize_image(input_image_path, output_image_path, scale_percent)