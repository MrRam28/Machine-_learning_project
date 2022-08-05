from collections import namedtuple

DataIngestionConfig=namedtuple("DataIngestionConfig",
["dataset_download_url","tgz_download_dir","raw_dir","ingestes_train_dir","ingestes_test_dir"])

DataValidationConfig= namedtuple("DataValidationConfig",["Schema_file path"])

DataTransformationConfig=namedtuple("DataTransformationConfig",["add_bedroom_per_room",
                                                                "transformed_train_dir",
                                                                "transformed_test_dir",
                                                                "preprocessed_object_file_path"])


ModelTrainerConfig=namedtuple("ModelTrainerCongfig",["trained_model_file_path","base_accuracy"])

ModelEvoluationConfig=namedtuple("ModelEvoluationConfig",["model_evoluation_file_path","time_stamp"])

ModelPusherConfig=namedtuple("ModelPusherConfig",["export_dir_path"])


