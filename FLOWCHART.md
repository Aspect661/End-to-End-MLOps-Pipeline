```mermaid
graph TD
    subgraph CONFIG["🔧 CONFIGURATION LAYER"]
        YAML1["📄 config.yaml<br/>(Paths & URLs)"]
        YAML2["📄 schema.yaml<br/>(Data Structure)"]
        YAML3["📄 params.yaml<br/>(Hyperparameters)"]
    end
    
    subgraph MANAGER["⚙️ CONFIGURATION MANAGER & ENTITIES"]
        CM["ConfigurationManager<br/>(Parse & Validate YAML)"]
        
        DIC["DataIngestionConfig<br/>@dataclass"]
        DVC["DataValidationConfig<br/>@dataclass"]
        DTC["DataTransformationConfig<br/>@dataclass"]
        MTC["ModelTrainerConfig<br/>@dataclass"]
        MEC["ModelEvaluationConfig<br/>@dataclass"]
        
        CM -->|get_data_ingestion_config| DIC
        CM -->|get_data_validation_config| DVC
        CM -->|get_data_transformation_config| DTC
        CM -->|get_model_trainer_config| MTC
        CM -->|get_model_evaluation_config| MEC
    end
    
    subgraph COMPONENTS["🔨 COMPONENTS LOGIC LAYER"]
        DI["DataIngestion<br/>Component"]
        DVL["DataValidation<br/>Component"]
        DTF["DataTransformation<br/>Component"]
        MT["ModelTrainer<br/>Component"]
        ME["ModelEvaluation<br/>Component"]
        
        DI -->|raw_data.csv| A1["💾 data/raw/"]
        DVL -->|validation_status.txt| A2["💾 reports/"]
        DTF -->|train.csv<br/>test.csv| A3["💾 data/processed/"]
        MT -->|model.pkl| A4["💾 models/"]
        ME -->|metrics.json| A5["💾 reports/"]
    end
    
    subgraph STAGES["🚀 PIPELINE STAGES & ENTRY POINT"]
        S01["Stage 01<br/>Data Ingestion"]
        S02["Stage 02<br/>Data Validation"]
        S03["Stage 03<br/>Data Transformation"]
        S04["Stage 04<br/>Model Trainer"]
        S05["Stage 05<br/>Model Evaluation"]
        
        S01 --> S02
        S02 --> S03
        S03 --> S04
        S04 --> S05
    end
    
    subgraph TRACKING["📊 EXPERIMENT TRACKING"]
        MLFLOW["MLflow & DagsHub<br/>(Model Registry)"]
    end
    
    ENTRY["▶️ main.py<br/>(Entry Point)"]
    
    %% Data flow from CONFIG to MANAGER
    YAML1 --> CM
    YAML2 --> CM
    YAML3 --> CM
    
    %% Data flow from ENTITIES to COMPONENTS
    DIC --> DI
    DVC --> DVL
    DTC --> DTF
    MTC --> MT
    MEC --> ME
    
    %% Data flow from COMPONENTS to STAGES
    DI --> S01
    DVL --> S02
    DTF --> S03
    MT --> S04
    ME --> S05
    
    %% Entry point orchestrates all stages
    ENTRY --> S01
    
    %% Model Evaluation sends metrics to MLflow
    S05 --> MLFLOW
    
    %% Styling
    classDef configLayer fill:#e3f2fd,stroke:#1976d2,stroke-width:2px,color:#000
    classDef managerLayer fill:#f3e5f5,stroke:#7b1fa2,stroke-width:2px,color:#000
    classDef componentLayer fill:#e8f5e9,stroke:#388e3c,stroke-width:2px,color:#000
    classDef stageLayer fill:#fff3e0,stroke:#f57c00,stroke-width:2px,color:#000
    classDef tracking fill:#fce4ec,stroke:#c2185b,stroke-width:2px,color:#000
    classDef entry fill:#ffe0b2,stroke:#e65100,stroke-width:3px,color:#000
    classDef artifact fill:#eceff1,stroke:#455a64,stroke-width:1px,stroke-dasharray: 5 5,color:#000
    
    class YAML1,YAML2,YAML3 configLayer
    class CM,DIC,DVC,DTC,MTC,MEC managerLayer
    class DI,DVL,DTF,MT,ME componentLayer
    class S01,S02,S03,S04,S05 stageLayer
    class MLFLOW tracking
    class ENTRY entry
    class A1,A2,A3,A4,A5 artifact