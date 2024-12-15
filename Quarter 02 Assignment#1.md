# Understanding OpenAI Chat Completion API Parameters
The Purpose of the assignment is to understand the purpose and funtions of parameters used with the OpenAI Chat Completion API. These paaremeters plays a pivotal role in producing customized and coherent responses  from Open Chat GPT.
## Parameters
### 1. Messages
The messages parameter comprises a list of message objects, each being assigned specific role and context for a more interactive and coherent conversation between the user and the AI model. The role is defined through:
**“Systems”**: provide high level instructions or messages for the assistance
**“Users”**: provide message or queries for the model.
**“Assistants”**: provide information for the end user based on their questions.
### 2. Model  
This parameter provide information about the version of Open AI model which is used to generate responses. Open AI models are chosen after considering their myriad powerful features and drawbacks. Among them **GPT- 4** is the advanced model which can handle complex and multi-faceted problems.
### 3. Max Completion Tokens
Token is refer to the output of text a model returns. The max_ token parameter allows to assign an appropriate value to LLM to limit the response length to fit the given context.
Example: max_tokens =500
### 4. N 
This parameter allows to generate multiple alternative variations in the responses for a given conversation. Experiment with the different values of "n" *(e.g., 1,2,3..)*, and higher value of the “n” will offer more diverse response options.
### 5. Stream
This parameter allows to stream responses to the client in incremental chunks before full completion is finished. The stream is set to True to get responses in partial chunks as they are generated to create more natural flow.  .
### 6. Temperature
Temperature controls the randomness and uniqueness in the generated responses. The sampling temperature range between 0 to 1. Assigning higher values (e.g., 0.8) to LLM generate diverse and  creative responses while lower values (e.g., 0.2) will produce more focused and deterministic responses.
### 7. Top_p
This parameter is known as **“nucleus sampling”** or **“penalty”** in API. It controls quality of responses by limiting the cumulative probability of the likely token. The sampling range from 0 to 2. Higher values (e.g., 0.9) make LLM more random while lesser values (e.g, 0.2) provide more focused answers.
### 8. Tools
A set of resources that can be used by model during the process of generating output. Tools are used as extensions or as specific API integration to perform special functions *(e.g., Web search for accessing data, interpretation and calculation etc.)*

