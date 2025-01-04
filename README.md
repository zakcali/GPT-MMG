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

note: you can use experimental models without paying for them, look for the url: https://ai.google.dev/gemini-api/docs/models/experimental-models

current experimental model is: gemini-exp-1206

you need to edit delay routine to not to throttle the apii but it may still throttle (stops responding after a outputting few files)
```
await new Promise(resolve => setTimeout(resolve, 60 * 1000)); // Delay
```
