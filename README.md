# Analysis of Different Code generation Models

This repository contains the code and results for the performances in Python code generation of three different code generation models – CodeT5, CodeGen, and GPT-3.5. The models were evaluated on the MBPP dataset, and the pass@k metric was used as the primary method of evaluation. 

The findings suggest that GPT-3.5 performs best in the few-shot setting, followed by GPT-3.5 in the zero-shot setting, CodeT5 in the few-shot setting, and CodeGen in the few-shot setting. These results indicate that GPT-3.5 is a promising model for code generation tasks, particularly in situations where the training data is limited, and highlight the importance of considering few-shot and zero-shot settings when evaluating code generation models. 

# Resource Requirements
The resource requirements for different code generation models varied. The pre-trained GPT-3.5 model was provided by OpenAI and accessed through its API. It was run locally and did not require any GPU resources. To run the CodeGen and CodeT5 models, GPU resources were required. A VM instance with GPU was created on Google Cloud Platform, specifically using an NVIDIA V100. However, even with NVIDIA V100, the multiple outputs inference for the CodeGen 6B model could not be run. As a result, the CodeGen 2B model was used, which is less computationally intensive but still capable of generating code snippets.
