import os
import time

### For downloading artifacts
import mlflow
MLFLOW_SERVER="http://13.52.243.246:5000"
mlflow.set_tracking_uri(MLFLOW_SERVER)
MLFLOW_RUN = "4f9a2ca283f141769647f773ae61c15a" # run_name = "languid-dolphin-519"
MLFLOW_MODEL_PATH = 'huggingface_optimum_artifacts'
EFS_ACCESS_POINT = '/mnt/efs/mhist-lambda' # root directory is mounted here

# Download ONNX model from MLflow server (called manually)
def download_latest_model():
    print('MLflow Tracking URI:', mlflow.get_tracking_uri())
    run = mlflow.get_run(MLFLOW_RUN)
    print('Downloading from runName =', run.data.tags['mlflow.runName'], 'run_id =', run.info.run_id)
    # tags = run.data.tags
    # metrics = run.data.metrics

    start_time = time.monotonic()
    mlflow_files = mlflow.artifacts.download_artifacts(tracking_uri=MLFLOW_SERVER, run_id=MLFLOW_RUN, artifact_path=MLFLOW_MODEL_PATH, dst_path=LAMBDA_TMP)
    downloaded_time = time.monotonic()
    print('Downloaded model files:\n', os.listdir(mlflow_files))
    print(f'Downloaded model in {(downloaded_time-start_time):.2f}s')
    # mlflow_files=mlflow.artifacts.list_artifacts(tracking_uri=MLFLOW_SERVER, run_id=MLFLOW_RUN, artifact_path=MLFLOW_MODEL_PATH)
