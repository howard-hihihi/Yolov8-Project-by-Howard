# pip uninstall pip setuptools
# pip3 install --upgrade pip
# pip3 install --upgrade setuptools
# pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
# git clone https://github.com/ultralytics/ultralytics
# cd ultralytics
# pip install ultralytics
# pip install labelme
# $ labelme --> 出現UI介面

import ultralytics
from ultralytics import YOLO                    # YOLOv8 套件
import multiprocessing                          # 多執行續套件

if __name__ == "__main__":
    multiprocessing.freeze_support()            # 避免多執行續造成主程式重複執行

    model = YOLO('weights/yolov8n-seg.pt')                  # Step 1 : 載入預訓練模型

    results = model.train(                          # Step 2 : 訓練模型
        data = 'C:\\Users\\user\\Desktop\\Yolov8 Project\\datasets\\robo_yolov8_v2\\data.yaml',     # - 指定訓練任務檔
        imgsz = 640,                                # - 輸入影像大小
        epochs = 5,                               # - 訓練世代數
        patience = 50,                              # - 等待世代數，無改善就提前結束訓練
        batch = 1,                                  # - 批次大小
        project = "Yolov8_segmentation",            # - 專案名稱
        name = "exp_01"                             # - 續練實驗名稱
    )