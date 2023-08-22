import sys,os
from isd.pipeline.train_pipeline import TrainPipeline

obj = TrainPipeline()
obj.run_pipeline()

print("Training succeded.")