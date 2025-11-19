import cv2

# 카메라 장치 열기 (기본: 0번 카메라)
cap = cv2.VideoCapture(1, cv2.CAP_DSHOW)

if not cap.isOpened():
    print("카메라를 열 수 없습니다.")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print("프레임을 읽을 수 없습니다.")
        break

    # 그레이스케일 변환
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Adaptive Thresholding (가우시안 방식, blockSize=11, C=2)
    binarized = cv2.adaptiveThreshold(
        gray, 255,
        cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        cv2.THRESH_BINARY,
        55, -10
    )

    # 영상 출력
    cv2.imshow("Original", frame)
    cv2.imshow("Adaptive Binarization", binarized)

    # 'q' 키를 누르면 종료
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 종료 처리
cap.release()
cv2.destroyAllWindows()
