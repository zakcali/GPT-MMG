# GPT-MMG
GPT-NER for MMG reports

nodejs program to send mmg-reports and receive tagged outputs

you must define enviromental variable GEMINI_API_KEY, which you obtain from google-ai-studio

Install the libraries by entering the following command in the keyboard:
```
npm install @google/generative-ai
```
make empty folders named "reports" and "ouputs"

copy contents of the "test-reports" folder to the "reports"

Run the program by typing:
```
node test-mmg-1206.js
```
find the tagged html reports in "outputs" folder

js (nodejs) program reads the file named "mmg prompt.html", appends one report to the end of prompt, sends promt to gemini-api, receives and outputs the responses

you may need to edit delay routine to not to throttle the api but it may still throttle (stops responding after outputting a few files)
```
await new Promise(resolve => setTimeout(resolve, 60 * 1000)); // Delay
```
you can directly paste contents of the "ai-studio prompt.txt" file to the https://aistudio.google.com/prompts/new_chat and see the tagged output one report at a time. Note: you must save the output as an html file, by adding ".html" extension, and see the result in a browser.
you can directly paste contents of the "ai-studio prompt.txt" file to the and see the tagged output one report at a time. Note: you must save the output as a html file, by adding ".html" extension, and see the result by opening that file in a web browser. Please edit safety setting in google ai studio, and set "block none" for all of them.

note: you can use experimental models without paying for them, look for the url: https://ai.google.dev/gemini-api/docs/models/experimental-models

current experimental model is: gemini-exp-1206

look for limits of experimental models: https://discuss.ai.google.dev/t/whats-the-rate-limit-for-the-experimental-models/38226

you can list the usable models for you with your api key. type this to your address bar of the browser https://generativelanguage.googleapis.com/v1beta/models?key=$GEMINI_API_KEY

if your GEMINI_API_KEY is "lFrWertd-tUyhGhpWwWwsD", then you must type this
```
https://generativelanguage.googleapis.com/v1beta/models?key=lFrWertd-tUyhGhpWwWwsD
```

here is the current output as Jan 5, 2025
```
{
  "models": [
    {
      "name": "models/chat-bison-001",
      "version": "001",
      "displayName": "PaLM 2 Chat (Legacy)",
      "description": "A legacy text-only model optimized for chat conversations",
      "inputTokenLimit": 4096,
      "outputTokenLimit": 1024,
      "supportedGenerationMethods": [
        "generateMessage",
        "countMessageTokens"
      ],
      "temperature": 0.25,
      "topP": 0.95,
      "topK": 40
    },
    {
      "name": "models/text-bison-001",
      "version": "001",
      "displayName": "PaLM 2 (Legacy)",
      "description": "A legacy model that understands text and generates text as an output",
      "inputTokenLimit": 8196,
      "outputTokenLimit": 1024,
      "supportedGenerationMethods": [
        "generateText",
        "countTextTokens",
        "createTunedTextModel"
      ],
      "temperature": 0.7,
      "topP": 0.95,
      "topK": 40
    },
    {
      "name": "models/embedding-gecko-001",
      "version": "001",
      "displayName": "Embedding Gecko",
      "description": "Obtain a distributed representation of a text.",
      "inputTokenLimit": 1024,
      "outputTokenLimit": 1,
      "supportedGenerationMethods": [
        "embedText",
        "countTextTokens"
      ]
    },
    {
      "name": "models/gemini-1.0-pro-latest",
      "version": "001",
      "displayName": "Gemini 1.0 Pro Latest",
      "description": "The original Gemini 1.0 Pro model. This model will be discontinued on February 15th, 2025. Move to a newer Gemini version.",
      "inputTokenLimit": 30720,
      "outputTokenLimit": 2048,
      "supportedGenerationMethods": [
        "generateContent",
        "countTokens"
      ],
      "temperature": 0.9,
      "topP": 1
    },
    {
      "name": "models/gemini-1.0-pro",
      "version": "001",
      "displayName": "Gemini 1.0 Pro",
      "description": "The best model for scaling across a wide range of tasks",
      "inputTokenLimit": 30720,
      "outputTokenLimit": 2048,
      "supportedGenerationMethods": [
        "generateContent",
        "countTokens"
      ],
      "temperature": 0.9,
      "topP": 1
    },
    {
      "name": "models/gemini-pro",
      "version": "001",
      "displayName": "Gemini 1.0 Pro",
      "description": "The best model for scaling across a wide range of tasks",
      "inputTokenLimit": 30720,
      "outputTokenLimit": 2048,
      "supportedGenerationMethods": [
        "generateContent",
        "countTokens"
      ],
      "temperature": 0.9,
      "topP": 1
    },
    {
      "name": "models/gemini-1.0-pro-001",
      "version": "001",
      "displayName": "Gemini 1.0 Pro 001 (Tuning)",
      "description": "The original Gemini 1.0 Pro model version that supports tuning. Gemini 1.0 Pro will be discontinued on February 15th, 2025. Move to a newer Gemini version.",
      "inputTokenLimit": 30720,
      "outputTokenLimit": 2048,
      "supportedGenerationMethods": [
        "generateContent",
        "countTokens",
        "createTunedModel"
      ],
      "temperature": 0.9,
      "topP": 1
    },
    {
      "name": "models/gemini-1.0-pro-vision-latest",
      "version": "001",
      "displayName": "Gemini 1.0 Pro Vision",
      "description": "The original Gemini 1.0 Pro Vision model version which was optimized for image understanding. Gemini 1.0 Pro Vision was deprecated on July 12, 2024. Move to a newer Gemini version.",
      "inputTokenLimit": 12288,
      "outputTokenLimit": 4096,
      "supportedGenerationMethods": [
        "generateContent",
        "countTokens"
      ],
      "temperature": 0.4,
      "topP": 1,
      "topK": 32
    },
    {
      "name": "models/gemini-pro-vision",
      "version": "001",
      "displayName": "Gemini 1.0 Pro Vision",
      "description": "The original Gemini 1.0 Pro Vision model version which was optimized for image understanding. Gemini 1.0 Pro Vision was deprecated on July 12, 2024. Move to a newer Gemini version.",
      "inputTokenLimit": 12288,
      "outputTokenLimit": 4096,
      "supportedGenerationMethods": [
        "generateContent",
        "countTokens"
      ],
      "temperature": 0.4,
      "topP": 1,
      "topK": 32
    },
    {
      "name": "models/gemini-1.5-pro-latest",
      "version": "001",
      "displayName": "Gemini 1.5 Pro Latest",
      "description": "Alias that points to the most recent production (non-experimental) release of Gemini 1.5 Pro, our mid-size multimodal model that supports up to 2 million tokens.",
      "inputTokenLimit": 2000000,
      "outputTokenLimit": 8192,
      "supportedGenerationMethods": [
        "generateContent",
        "countTokens"
      ],
      "temperature": 1,
      "topP": 0.95,
      "topK": 40,
      "maxTemperature": 2
    },
    {
      "name": "models/gemini-1.5-pro-001",
      "version": "001",
      "displayName": "Gemini 1.5 Pro 001",
      "description": "Stable version of Gemini 1.5 Pro, our mid-size multimodal model that supports up to 2 million tokens, released in May of 2024.",
      "inputTokenLimit": 2000000,
      "outputTokenLimit": 8192,
      "supportedGenerationMethods": [
        "generateContent",
        "countTokens",
        "createCachedContent"
      ],
      "temperature": 1,
      "topP": 0.95,
      "topK": 64,
      "maxTemperature": 2
    },
    {
      "name": "models/gemini-1.5-pro-002",
      "version": "002",
      "displayName": "Gemini 1.5 Pro 002",
      "description": "Stable version of Gemini 1.5 Pro, our mid-size multimodal model that supports up to 2 million tokens, released in September of 2024.",
      "inputTokenLimit": 2000000,
      "outputTokenLimit": 8192,
      "supportedGenerationMethods": [
        "generateContent",
        "countTokens",
        "createCachedContent"
      ],
      "temperature": 1,
      "topP": 0.95,
      "topK": 40,
      "maxTemperature": 2
    },
    {
      "name": "models/gemini-1.5-pro",
      "version": "001",
      "displayName": "Gemini 1.5 Pro",
      "description": "Stable version of Gemini 1.5 Pro, our mid-size multimodal model that supports up to 2 million tokens, released in May of 2024.",
      "inputTokenLimit": 2000000,
      "outputTokenLimit": 8192,
      "supportedGenerationMethods": [
        "generateContent",
        "countTokens"
      ],
      "temperature": 1,
      "topP": 0.95,
      "topK": 40,
      "maxTemperature": 2
    },
    {
      "name": "models/gemini-1.5-pro-exp-0801",
      "version": "exp-0801",
      "displayName": "Gemini Experimental 1206",
      "description": "Experimental release (December 6th, 2024) of Gemini.",
      "inputTokenLimit": 2097152,
      "outputTokenLimit": 8192,
      "supportedGenerationMethods": [
        "generateContent",
        "countTokens"
      ],
      "temperature": 1,
      "topP": 0.95,
      "topK": 64,
      "maxTemperature": 2
    },
    {
      "name": "models/gemini-1.5-pro-exp-0827",
      "version": "exp-1206",
      "displayName": "Gemini Experimental 1206",
      "description": "Experimental release (December 6th, 2024) of Gemini.",
      "inputTokenLimit": 2097152,
      "outputTokenLimit": 8192,
      "supportedGenerationMethods": [
        "generateContent",
        "countTokens"
      ],
      "temperature": 1,
      "topP": 0.95,
      "topK": 64,
      "maxTemperature": 2
    },
    {
      "name": "models/gemini-1.5-flash-latest",
      "version": "001",
      "displayName": "Gemini 1.5 Flash Latest",
      "description": "Alias that points to the most recent production (non-experimental) release of Gemini 1.5 Flash, our fast and versatile multimodal model for scaling across diverse tasks.",
      "inputTokenLimit": 1000000,
      "outputTokenLimit": 8192,
      "supportedGenerationMethods": [
        "generateContent",
        "countTokens"
      ],
      "temperature": 1,
      "topP": 0.95,
      "topK": 40,
      "maxTemperature": 2
    },
    {
      "name": "models/gemini-1.5-flash-001",
      "version": "001",
      "displayName": "Gemini 1.5 Flash 001",
      "description": "Stable version of Gemini 1.5 Flash, our fast and versatile multimodal model for scaling across diverse tasks, released in May of 2024.",
      "inputTokenLimit": 1000000,
      "outputTokenLimit": 8192,
      "supportedGenerationMethods": [
        "generateContent",
        "countTokens",
        "createCachedContent"
      ],
      "temperature": 1,
      "topP": 0.95,
      "topK": 64,
      "maxTemperature": 2
    },
    {
      "name": "models/gemini-1.5-flash-001-tuning",
      "version": "001",
      "displayName": "Gemini 1.5 Flash 001 Tuning",
      "description": "Version of Gemini 1.5 Flash that supports tuning, our fast and versatile multimodal model for scaling across diverse tasks, released in May of 2024.",
      "inputTokenLimit": 16384,
      "outputTokenLimit": 8192,
      "supportedGenerationMethods": [
        "generateContent",
        "countTokens",
        "createTunedModel"
      ],
      "temperature": 1,
      "topP": 0.95,
      "topK": 64,
      "maxTemperature": 2
    },
    {
      "name": "models/gemini-1.5-flash",
      "version": "001",
      "displayName": "Gemini 1.5 Flash",
      "description": "Alias that points to the most recent stable version of Gemini 1.5 Flash, our fast and versatile multimodal model for scaling across diverse tasks.",
      "inputTokenLimit": 1000000,
      "outputTokenLimit": 8192,
      "supportedGenerationMethods": [
        "generateContent",
        "countTokens"
      ],
      "temperature": 1,
      "topP": 0.95,
      "topK": 40,
      "maxTemperature": 2
    },
    {
      "name": "models/gemini-1.5-flash-exp-0827",
      "version": "exp-1206",
      "displayName": "Gemini Experimental 1206",
      "description": "Experimental release (December 6th, 2024) of Gemini.",
      "inputTokenLimit": 2097152,
      "outputTokenLimit": 8192,
      "supportedGenerationMethods": [
        "generateContent",
        "countTokens"
      ],
      "temperature": 1,
      "topP": 0.95,
      "topK": 64,
      "maxTemperature": 2
    },
    {
      "name": "models/gemini-1.5-flash-002",
      "version": "002",
      "displayName": "Gemini 1.5 Flash 002",
      "description": "Stable version of Gemini 1.5 Flash, our fast and versatile multimodal model for scaling across diverse tasks, released in September of 2024.",
      "inputTokenLimit": 1000000,
      "outputTokenLimit": 8192,
      "supportedGenerationMethods": [
        "generateContent",
        "countTokens",
        "createCachedContent"
      ],
      "temperature": 1,
      "topP": 0.95,
      "topK": 40,
      "maxTemperature": 2
    },
    {
      "name": "models/gemini-1.5-flash-8b",
      "version": "001",
      "displayName": "Gemini 1.5 Flash-8B",
      "description": "Stable version of Gemini 1.5 Flash-8B, our smallest and most cost effective Flash model, released in October of 2024.",
      "inputTokenLimit": 1000000,
      "outputTokenLimit": 8192,
      "supportedGenerationMethods": [
        "createCachedContent",
        "generateContent",
        "countTokens"
      ],
      "temperature": 1,
      "topP": 0.95,
      "topK": 40,
      "maxTemperature": 2
    },
    {
      "name": "models/gemini-1.5-flash-8b-001",
      "version": "001",
      "displayName": "Gemini 1.5 Flash-8B 001",
      "description": "Stable version of Gemini 1.5 Flash-8B, our smallest and most cost effective Flash model, released in October of 2024.",
      "inputTokenLimit": 1000000,
      "outputTokenLimit": 8192,
      "supportedGenerationMethods": [
        "createCachedContent",
        "generateContent",
        "countTokens"
      ],
      "temperature": 1,
      "topP": 0.95,
      "topK": 40,
      "maxTemperature": 2
    },
    {
      "name": "models/gemini-1.5-flash-8b-latest",
      "version": "001",
      "displayName": "Gemini 1.5 Flash-8B Latest",
      "description": "Alias that points to the most recent production (non-experimental) release of Gemini 1.5 Flash-8B, our smallest and most cost effective Flash model, released in October of 2024.",
      "inputTokenLimit": 1000000,
      "outputTokenLimit": 8192,
      "supportedGenerationMethods": [
        "createCachedContent",
        "generateContent",
        "countTokens"
      ],
      "temperature": 1,
      "topP": 0.95,
      "topK": 40,
      "maxTemperature": 2
    },
    {
      "name": "models/gemini-1.5-flash-8b-exp-0827",
      "version": "001",
      "displayName": "Gemini 1.5 Flash 8B Experimental 0827",
      "description": "Experimental release (August 27th, 2024) of Gemini 1.5 Flash-8B, our smallest and most cost effective Flash model. Replaced by Gemini-1.5-flash-8b-001 (stable).",
      "inputTokenLimit": 1000000,
      "outputTokenLimit": 8192,
      "supportedGenerationMethods": [
        "generateContent",
        "countTokens"
      ],
      "temperature": 1,
      "topP": 0.95,
      "topK": 40,
      "maxTemperature": 2
    },
    {
      "name": "models/gemini-1.5-flash-8b-exp-0924",
      "version": "001",
      "displayName": "Gemini 1.5 Flash 8B Experimental 0924",
      "description": "Experimental release (September 24th, 2024) of Gemini 1.5 Flash-8B, our smallest and most cost effective Flash model. Replaced by Gemini-1.5-flash-8b-001 (stable).",
      "inputTokenLimit": 1000000,
      "outputTokenLimit": 8192,
      "supportedGenerationMethods": [
        "generateContent",
        "countTokens"
      ],
      "temperature": 1,
      "topP": 0.95,
      "topK": 40,
      "maxTemperature": 2
    },
    {
      "name": "models/gemini-2.0-flash-exp",
      "version": "2.0",
      "displayName": "Gemini 2.0 Flash Experimental",
      "description": "Gemini 2.0 Flash Experimental",
      "inputTokenLimit": 1048576,
      "outputTokenLimit": 8192,
      "supportedGenerationMethods": [
        "generateContent",
        "countTokens",
        "bidiGenerateContent"
      ],
      "temperature": 1,
      "topP": 0.95,
      "topK": 40,
      "maxTemperature": 2
    },
    {
      "name": "models/gemini-exp-1206",
      "version": "exp_1206",
      "displayName": "Gemini Experimental 1206",
      "description": "Experimental release (December 6th, 2024) of Gemini.",
      "inputTokenLimit": 2097152,
      "outputTokenLimit": 8192,
      "supportedGenerationMethods": [
        "generateContent",
        "countTokens"
      ],
      "temperature": 1,
      "topP": 0.95,
      "topK": 64,
      "maxTemperature": 2
    },
    {
      "name": "models/gemini-exp-1121",
      "version": "exp-1206",
      "displayName": "Gemini Experimental 1206",
      "description": "Experimental release (December 6th, 2024) of Gemini.",
      "inputTokenLimit": 2097152,
      "outputTokenLimit": 8192,
      "supportedGenerationMethods": [
        "generateContent",
        "countTokens"
      ],
      "temperature": 1,
      "topP": 0.95,
      "topK": 64,
      "maxTemperature": 2
    },
    {
      "name": "models/gemini-exp-1114",
      "version": "exp-1206",
      "displayName": "Gemini Experimental 1206",
      "description": "Experimental release (December 6th, 2024) of Gemini.",
      "inputTokenLimit": 2097152,
      "outputTokenLimit": 8192,
      "supportedGenerationMethods": [
        "generateContent",
        "countTokens"
      ],
      "temperature": 1,
      "topP": 0.95,
      "topK": 64,
      "maxTemperature": 2
    },
    {
      "name": "models/gemini-2.0-flash-thinking-exp",
      "version": "2.0",
      "displayName": "Gemini 2.0 Flash Thinking Experimental",
      "description": "Gemini 2.0 Flash Thinking Experimental",
      "inputTokenLimit": 32767,
      "outputTokenLimit": 8192,
      "supportedGenerationMethods": [
        "generateContent",
        "countTokens"
      ],
      "temperature": 1,
      "topP": 0.95,
      "topK": 64,
      "maxTemperature": 2
    },
    {
      "name": "models/gemini-2.0-flash-thinking-exp-1219",
      "version": "2.0",
      "displayName": "Gemini 2.0 Flash Thinking Experimental",
      "description": "Gemini 2.0 Flash Thinking Experimental",
      "inputTokenLimit": 32767,
      "outputTokenLimit": 8192,
      "supportedGenerationMethods": [
        "generateContent",
        "countTokens"
      ],
      "temperature": 1,
      "topP": 0.95,
      "topK": 64,
      "maxTemperature": 2
    },
    {
      "name": "models/learnlm-1.5-pro-experimental",
      "version": "001",
      "displayName": "LearnLM 1.5 Pro Experimental",
      "description": "Alias that points to the most recent stable version of Gemini 1.5 Pro, our mid-size multimodal model that supports up to 2 million tokens.",
      "inputTokenLimit": 32767,
      "outputTokenLimit": 8192,
      "supportedGenerationMethods": [
        "generateContent",
        "countTokens"
      ],
      "temperature": 1,
      "topP": 0.95,
      "topK": 64,
      "maxTemperature": 2
    },
    {
      "name": "models/embedding-001",
      "version": "001",
      "displayName": "Embedding 001",
      "description": "Obtain a distributed representation of a text.",
      "inputTokenLimit": 2048,
      "outputTokenLimit": 1,
      "supportedGenerationMethods": [
        "embedContent"
      ]
    },
    {
      "name": "models/text-embedding-004",
      "version": "004",
      "displayName": "Text Embedding 004",
      "description": "Obtain a distributed representation of a text.",
      "inputTokenLimit": 2048,
      "outputTokenLimit": 1,
      "supportedGenerationMethods": [
        "embedContent"
      ]
    },
    {
      "name": "models/aqa",
      "version": "001",
      "displayName": "Model that performs Attributed Question Answering.",
      "description": "Model trained to return answers to questions that are grounded in provided sources, along with estimating answerable probability.",
      "inputTokenLimit": 7168,
      "outputTokenLimit": 1024,
      "supportedGenerationMethods": [
        "generateAnswer"
      ],
      "temperature": 0.2,
      "topP": 1,
      "topK": 40
    }
  ]
}

```
