# fine-tuning-onboarding-project

## 1. Resources
1. [OpenAI Fine-tuning Docs](https://platform.openai.com/docs/guides/fine-tuning)
2. OpenAI Fine-tuning API Launch Date: Dec 14, 2021 ([Source](https://venturebeat.com/uncategorized/openai-begins-allowing-customers-to-fine-tune-gpt-3/))

## 2. Introduction
1. What is fine-tuning?
    - Fine-tuning a language model involves taking a pre-trained language model and adapting it to a new task or domain by continuing its training on a smaller set of task-specific data. 
    - This is done by updating the parameters of the pre-trained model using the task-specific data. 
    - By starting with a pre-trained model that has already learned general language patterns and features, fine-tuning can greatly improve the performance of the model on the new task or domain with a relatively small amount of task-specific data.
    (GPT-3.5)

## 3. OpenAI Fine-tuning API
1. Store Your OPENAI_API_KEY    
    ```export OPENAI_API_KEY=your_api_key```
2. Fine-tuning Command    
    ```openai api fine_tunes.create -t <TRAIN_FILE_ID_OR_PATH> -m <BASE_MODEL>```
    - Example.  
    ```openai api fine_tunes.create -t ./dataset/gpt-4.jsonl -m davinci --suffix "GPT-4 v1"```
    - Starts the fine-tuning Process
    - Data must be a JSONL file, following the -t flag
    - Base model can be one of [ada, babbage, curie, davinci] after the -m flag
    - Set the model name as suffix
        - Model Name: davinci:ft-personal:GPT-4-v1-2022-02-15-04-21-04
3. Resume Stream   
    ```openai api fine_tunes.follow -i <JOB_ID>```
    - Streams the process in the command line
    - This information includes
        - job_id
        - cost
        - status (queued)
        - Fine-tune started
        - Completed Epochs
        - Succeeded
4. List all created fine-tunes   
    ```openai api fine_tunes.list```
5. Retreive state of fine-tune   
    ```openai api fine_tunes.get -i <JOB_ID>```
6. Cancel fine-tune   
    ```openai api fine_tunes.cancel -i <JOB_ID>```

4. Fine-tune the GPT-3 model
    1. Find a dataset, convert it to a txt file, and store it under ./raw_data
    2. Fix process.py to create a great dataset for fine-tuning
    3. Start the fine-tuning process, refer to (3-2) above
    4. Test the results with 10 questions (5 from below, and 5 on your own)
        1. What is GPT-4?
        2. What is GPT-4 good at?
        3. How does GPT-4 perform in the bar exam?
        4. How does GPT-4 perform on the MMLU benchmark?
        5. How does GPT-4 perform compared to GPT-3.5