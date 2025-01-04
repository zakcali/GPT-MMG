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

note: you can use experimental models without paying for them, look for the url: https://ai.google.dev/gemini-api/docs/models/experimental-models

current experimental model is: gemini-exp-1206

you may need to edit delay routine to not to throttle the api but it may still throttle (stops responding after outputting a few files)
```
await new Promise(resolve => setTimeout(resolve, 60 * 1000)); // Delay
```
you can directly paste contents of the "ai-studio prompt.txt" file to the https://aistudio.google.com/prompts/new_chat and see the tagged output one report at a time. Note: you must save the output as an html file, by adding ".html" extension, and see the result in a browser.
you can directly paste contents of the "ai-studio prompt.txt" file to the and see the tagged output one report at a time. Note: you must save the output as a html file, by adding ".html" extension, and see the result by opening that file in a web browser. Please edit safety setting in google ai studio, and set "block none" for all of them.
