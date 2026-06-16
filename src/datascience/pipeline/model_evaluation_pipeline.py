from src.datascience.config.configuration import ConfigurationManager
from src.datascience.components.model_evaluation import ModelEvaluation
from src.datascience import logger


STAGE_NAME = "Model Evaluation Stage"

class ModelEvaluationTrainingPipeline:
    def __init__(self):
        pass

    def initiate_model_evaluation(self):
        config_manager = ConfigurationManager()
        model_evaluation_config = config_manager.get_model_evaluation_config()
        model_evaluation = ModelEvaluation(config = model_evaluation_config)
        model_evaluation.log_into_mlflow()