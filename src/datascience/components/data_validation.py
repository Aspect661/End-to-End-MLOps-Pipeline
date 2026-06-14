import os
import urllib.request as request
from src.datascience import logger
import zipfile
from src.datascience.entity.config_entity import (DataValidationConfig) 
import pandas as pd

class DataValidation:

    def __init__(self, config: DataValidationConfig):
        self.config = config

    def validate_all_columns(self) -> bool:
    
        try:
            validation_status = True  # Start as True
            
            data = pd.read_csv(self.config.unzip_data_dir)
            all_cols = list(data.columns)
            
            all_schema = self.config.all_schema.get("COLUMNS", {}).keys()
            
            # Check all columns first
            for col in all_cols:
                if col not in all_schema:
                    validation_status = False
                    logger.error(f"Column '{col}' not found in schema")
                    break  # Stop on first mismatch
            
            # Write status ONCE after loop completes
            with open(self.config.STATUS_FILE, "w") as f:
                f.write(f"Validation status: {validation_status}.")
            
            return validation_status
            
        except Exception as e:
            logger.error(f"Validation error: {e}")
            raise e