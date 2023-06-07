from ultralytics import YOLO
import pytesseract
import cv2
import pandas as pd
import sqlite3 as sql
import re

model = YOLO('best.pt')
############------- DATABASE---------#############
db = sql.connect("plates.sqlite")
cursor = db.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS plates (id, plate)")
#result = model.predict(source="deneme.mp4", show=True, stream=True)
cap = cv2.VideoCapture("deneme.mp4")
pytesseract.pytesseract.tesseract_cmd = r'C:/Program Files/Tesseract-OCR/tesseract.exe'
id_counter = 1
plate_counter = {}
plate_counter_list, last_list, keys = [], [], []

while cap.isOpened():
    ret, frame = cap.read()

    if not ret:
        break
    
    results = model.predict(frame, show=True, stream=True)
    for r in results:
        boxes = r.boxes.xyxy

        if len(boxes) > 0:
            boxes_df = pd.DataFrame(boxes, columns=['x1', 'y1', 'x2', 'y2'])

            for index, row in boxes_df.iterrows():
                    x1, y1, x2, y2 = row['x1'], row['y1'], row['x2'], row['y2']
                    x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
                    cropped = frame[y1:y2, x1:x2]

                
                    gray = cv2.cvtColor(cropped, cv2.COLOR_BGR2GRAY)
                    blur = cv2.GaussianBlur(gray, (3, 3), 0)
                    #thresh = cv2.threshold(blur, 128, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
                    thresh = cv2.threshold(blur, 128, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

                    cv2.imshow("xop", thresh)

                    crop_img_text = pytesseract.image_to_string(thresh, lang='eng')
                    print("oldu", crop_img_text)
                    if len(crop_img_text) > 5:
                        if not re.search(r'[!*\'+()%/?~|,«—:\[\]§.°¥a-z]', crop_img_text):
                            if crop_img_text[0] == ' ' or crop_img_text[0] == '-':
                                crop_img_text = crop_img_text[1:]
                            if crop_img_text[-1] == ' ' or crop_img_text[-1] == '-':
                                crop_img_text = crop_img_text[:-1]
                            plate_counter_list.append(crop_img_text)
                            if crop_img_text in plate_counter:
                                plate_counter[crop_img_text] += 1
                            else:
                                plate_counter[crop_img_text] = 1
                            for key, value in plate_counter.items():
                                if value > 3:
                                    last_list.append(key)
                                    keys.append(key)
                                    if len(last_list) > 1 and last_list[-1] != last_list[-2]:
                                        last_list = [last_list[-1]]
                                    cursor.execute("insert into plates (id, plate) values (?,?)", (id_counter, last_list[-1]))
                                    print("sözlük", last_list)
                                    print("dict", plate_counter)
                                    id_counter = id_counter + 1
                                    db.commit()
                            for key in keys:
                                if key in plate_counter:
                                    del plate_counter[key]



        if cv2.waitKey(1) == ord('q'):
            break

    
cap.release()
cv2.destroyAllWindows()
db.close()
