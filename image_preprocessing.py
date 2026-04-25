import cv2
import numpy as np

class ImageProcessor:
    def __init__(self):
        print("Image Processing System Initialized")

    def apply_transformations(self, frame):
        # 1. Convert to Grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # 2. Gaussian Blur (Noise Reduction)
        blurred = cv2.GaussianBlur(gray, (5, 5), 0)

        # 3. Histogram Equalization (Contrast Enhancement)
        equalized = cv2.equalizeHist(blurred)

        # 4. Canny Edge Detection
        edges = cv2.Canny(equalized, 100, 200)

        return gray, blurred, equalized, edges


def stack_images(gray, blurred, equalized, edges):
    """
    Stack images in a 2x2 grid:
    [Gray | Blurred]
    [Equalized | Edges]
    """

    # Convert grayscale images to BGR for stacking
    gray_bgr = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)
    blurred_bgr = cv2.cvtColor(blurred, cv2.COLOR_GRAY2BGR)
    equalized_bgr = cv2.cvtColor(equalized, cv2.COLOR_GRAY2BGR)
    edges_bgr = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)

    top_row = np.hstack((gray_bgr, blurred_bgr))
    bottom_row = np.hstack((equalized_bgr, edges_bgr))

    combined = np.vstack((top_row, bottom_row))

    return combined


def run_realtime():
    processor = ImageProcessor()
    cap = cv2.VideoCapture(0)  # Open webcam

    if not cap.isOpened():
        print("Error: Cannot access webcam")
        return

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Failed to grab frame")
            break

        # Apply transformations
        gray, blurred, equalized, edges = processor.apply_transformations(frame)

        # Stack images for display
        combined = stack_images(gray, blurred, equalized, edges)

        # Show output
        cv2.imshow("Real-Time Image Processing (Press Q to Exit)", combined)

        # Exit on 'q' key
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    run_realtime()