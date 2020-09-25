import json

class ModelPackageValidationSpecification:
    template = """
{    
    "ValidationSpecification": {
        "ValidationRole": "ROLE_REPLACE_ME",
        "ValidationProfiles": [
            {
                "ProfileName": "ValidationProfile1",
                "TransformJobDefinition": {
                    "MaxConcurrentTransforms": 1,
                    "MaxPayloadInMB": 6,
                    "TransformInput": {
                        "DataSource": {
                            "S3DataSource": {
                                "S3DataType": "S3Prefix",
                                "S3Uri": "BATCH_S3_INPUT_REPLACE_ME"
                            }
                        },
                        "ContentType": "INPUT_CONTENT_TYPE_REPLACE_ME",
                        "CompressionType": "None"
                    },
                    "TransformOutput": {
                        "S3OutputPath": "VALIDATION_S3_OUTPUT_REPLACE_ME/batch-transform-output",
                        "Accept": "OUTPUT_CONTENT_TYPE_REPLACE_ME",
                        "KmsKeyId": ""
                    },
                    "TransformResources": {
                        "InstanceType": "INSTANCE_TYPE_REPLACE_ME",
                        "InstanceCount": 1
                    }
                }
            }
        ]
    }
}    
"""

    def get_validation_specification_dict(self, validation_role, batch_transform_input, input_content_type, output_content_type, instance_type, output_s3_location):
        return json.loads(self.get_validation_specification_json(validation_role, batch_transform_input, input_content_type, output_content_type, instance_type, output_s3_location))

    def get_validation_specification_json(self, validation_role, batch_transform_input, input_content_type, output_content_type, instance_type, output_s3_location):

        return self.template.replace("ROLE_REPLACE_ME", validation_role)\
            .replace("BATCH_S3_INPUT_REPLACE_ME", batch_transform_input)\
            .replace("INPUT_CONTENT_TYPE_REPLACE_ME", input_content_type)\
            .replace("OUTPUT_CONTENT_TYPE_REPLACE_ME", output_content_type)\
            .replace("INSTANCE_TYPE_REPLACE_ME", instance_type)\
            .replace("VALIDATION_S3_OUTPUT_REPLACE_ME", output_s3_location)