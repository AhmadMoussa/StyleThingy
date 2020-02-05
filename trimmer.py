import cv2

# Opens the Video file
cap = cv2.VideoCapture('blooming.mkv')
i = 0
while (cap.isOpened()):
    ret, frame = cap.read()
    print(i)
    if ret == False:
        break
    cv2.imwrite('frames/' + str(i) + '.png', cv2.resize(frame, (1280,720)))
    i += 2
    if i == 280:
        break

cap.release()
cv2.destroyAllWindows()