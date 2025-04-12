# EXACT-Net:EHR-guided lung tumor auto-segmentation for non-small cell lung cancer radiotherapy

## Introduction
An electronic health record (EHR)-guided lung tumor auto-segmentation called EXACT-Net (EHR-enhanced eXACtitude in Tumor segmentation), where the extracted information from EHRs using a pre-trained large language model (LLM) was used to remove the FPs and keep the TP nodules only.

Below is an overview of an EHR-guided automated target segmentation system. The auto-contouring platform contours the initial structures on the diagnostic CT scan. Due to the advantages of PET scans for improved target segmentation, it will be used as the second primary imaging modality for the target segmentation platform. The NLP-based algorithm will extract critical information regarding the location and shape of the tumor.

![image](https://github.com/user-attachments/assets/92d6ff2b-71d8-4950-a4c2-592479ea317f)

## Method
We use two different methods:

1) Prompt engineering and chatGPT API:
We used the GPT 3.5 Turbo LLM through the OpenAI API to demonstrate the feasibility of EHR-guided tumor segmentation. We used an in-house Python interface to the API to read the EHR text files and feed them to the model. To access the API, an API key is required which can be obtained from the OpenAI official website.

2) Fine-Tuning the LLAMA2 model, and using LangChain for training and inference
We fine-tuned the LLAMA2 70B parameters on EHR reports and provided the LLM with a polished answer that will guide the segmenation model, the model is then trained on two A100 GPUs using high performance computing (HPC) platforms.

## Results:
We found a 250% boost in performance in lung nodule detection accuracy.


![image](https://github.com/user-attachments/assets/583d31ed-7057-45e2-81a1-6c92b4bce13f)


If you find it useful, we encourage you to read our paper!

Hooshangnejad, H., Huang, G., Kelly, K., Feng, X., Luo, Y., Zhang, R., Xu, Z., Chen, Q., & Ding, K. (2024). EXACT-Net: Framework for EHR-Guided Lung Tumor Auto-Segmentation for Non-Small Cell Lung Cancer Radiotherapy. Cancers, 16(23), 4097. https://doi.org/10.3390/cancers16234097



