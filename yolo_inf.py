import os
from ultralytics import YOLO

model_path = "best.pt"
video_path = "test_video.mp4" 

def run_inference (modelyolo,video):
        

    # cheking files
    if not os.path.exists(modelyolo):
        print(f" Erorr: Dont find the path '{modelyolo}'")
        print("Please download best.pt in the directory with project.")
        exit()
    if not os.path.exists(video):
        print(f" Erorr: Dont find the path '{video}'")
        print("Please put the test video in the directory with project.")
        exit()
    #starting video processing
    print(f" Starting the processing '{video}'")

    try:
        model = YOLO(modelyolo)
        results = model.predict(source=video, save=False, conf=0.5, show=True)

        print("\n Done!")
        print(f"Results are in in  {results[0].save_dir}")

    except Exception as e:
        print(f"Error {e}")

if __name__ == "__main__":
    run_inference (model_path,video_path)
