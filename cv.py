import cv2, math
from collections import deque
import mediapipe as mp

mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

def judge_hand(que):
    N = len(que)
    x_all,y_all = 0,0
    for i in que:
        x_all+=i[0]
        y_all+=i[1]
    center_x = x_all / N
    center_y = y_all / N
    for i in que:
        # print([i[0]-center_x,i[0]-center_y],end=' ')
        if i[0]-center_x>10 or i[1]-center_y>10:
            return None
    # print()
    # print(que)
    # print(center_x,center_y)
    return (int(center_x),int(center_y))

def normalized_to_pixel_coordinates(
        normalized_x: float, normalized_y: float, image_width: int,
        image_height: int):
    """Converts normalized value pair to pixel coordinates."""

    # Checks if the float value is between 0 and 1.
    def is_valid_normalized_value(value: float) -> bool:
        return (value > 0 or math.isclose(0, value)) and (value < 1 or
                                                          math.isclose(1, value))
    if not (is_valid_normalized_value(normalized_x) and
            is_valid_normalized_value(normalized_y)):
        # TODO: Draw coordinates even if it's outside of the image bounds.
        return None
    x_px = min(math.floor(normalized_x * image_width), image_width - 1)
    y_px = min(math.floor(normalized_y * image_height), image_height - 1)
    return x_px, y_px

def main():
    deques = []
    # For webcam input:
    cap = cv2.VideoCapture(0)
    with mp_hands.Hands(
            min_detection_confidence=0.8,
            min_tracking_confidence=0.5) as hands:
        while cap.isOpened():
            success, image = cap.read()
            if not success:
                print("Ignoring empty camera frame.")
                # If loading a video, use 'break' instead of 'continue'.
                continue

            # Flip the image horizontally for a later selfie-view display, and convert
            # the BGR image to RGB.
            image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)
            # To improve performance, optionally mark the image as not writeable to
            # pass by reference.
            image.flags.writeable = False
            results = hands.process(image)

            # Draw the hand annotations on the image.
            image.flags.writeable = True
            image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

            if results.multi_hand_landmarks:
                for hand_landmarks in results.multi_hand_landmarks:
                    mp_drawing.draw_landmarks(
                        image, hand_landmarks, mp_hands.HAND_CONNECTIONS)
                    lip = hand_landmarks.landmark[8]
                    normal_lip = normalized_to_pixel_coordinates(lip.x,lip.y,image.shape[1],image.shape[0])
                    deques.append(normal_lip)
                    if len(deques)>10:
                        deques.pop(0)
                    if len(deques) == 10:
                        #判断是否为一定区域内
                        temp = judge_hand(deques)
                        if temp:
                            hand_point_center = temp
                            cv2.circle(image, hand_point_center, 10,(0,255,0), 2)
            cv2.imshow('MediaPipe Hands', image)
            if cv2.waitKey(5) & 0xFF == 27:
                break

    cap.release()




if __name__ == '__main__':
    main()
