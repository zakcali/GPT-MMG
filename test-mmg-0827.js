const { GoogleGenerativeAI, HarmCategory, HarmBlockThreshold } = require("@google/generative-ai");
const fs = require('node:fs/promises');
const path = require('path'); // For path manipulation

const genAI = new GoogleGenerativeAI(process.env.GEMINI_API_KEY);
const systemInstruction = { role: "system", parts: [{ text: "" }] };
const generationConfig = {
  temperature: 0.0,
};

const safetySettings = [
  {
    category: HarmCategory.HARM_CATEGORY_HARASSMENT, threshold: HarmBlockThreshold.BLOCK_NONE,
  },
    {
    category: HarmCategory.HARM_CATEGORY_HATE_SPEECH, threshold: HarmBlockThreshold.BLOCK_NONE,
  },
    {
    category: HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT, threshold: HarmBlockThreshold.BLOCK_NONE,
  },
    {
    category: HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT, threshold: HarmBlockThreshold.BLOCK_NONE,
  },
];
const apiVersion = 'v1beta';
const modelName = 'gemini-exp-1206'; // https://ai.google.dev/gemini-api/docs/models/gemini
// https://ai.google.dev/gemini-api/docs/models/experimental-models?hl=tr
const mistakes = [
    '<span class="ANAT">Sol memenin</span> MLO ve CC mammogramları elde olunmuştur', 'Sol memenin MLO ve CC mammogramları elde olunmuştur',
    '<span class="ANAT">Sağ memenin</span> MLO ve CC mammogramları elde olunmuştur', 'Sağ memenin MLO ve CC mammogramları elde olunmuştur',
    '<span class="ANAT">SAĞ</span> MAMMOGRAFİ RAPORUNUN DA OKUNMASI ÖNERİLİR', 'SAĞ MAMMOGRAFİ RAPORUNUN DA OKUNMASI ÖNERİLİR',
    '<span class="ANAT">SOL</span> MAMMOGRAFİ RAPORUNUN DA OKUNMASI ÖNERİLİR', 'SOL MAMMOGRAFİ RAPORUNUN DA OKUNMASI ÖNERİLİR',
	'HASTANIN <span class="ANAT">SOL MAMMOGRAFİ</span> RAPORUNUN', 'HASTANIN SOL MAMMOGRAFİ RAPORUNUN',
		'HASTANIN <span class="ANAT">SAĞ MAMMOGRAFİ</span> RAPORUNUN', 'HASTANIN SAĞ MAMMOGRAFİ RAPORUNUN',
    ];

async function run() {
const model = genAI.getGenerativeModel({ model: modelName, generationConfig, safetySettings, systemInstruction,},
     );
    // read prompt
    let prompt;
    try {
        prompt = await fs.readFile('mmg prompt.html', { encoding: 'utf8' });
    } catch (err) {
        console.error(err);
        return; // Exit if prompt reading fails
    }

    // Get list of report files
    const reportsDir = 'reports';
    const files = await fs.readdir(reportsDir);
    const reportFiles = files.filter(file => path.extname(file) === '.txt');

    // Process each report file
    for (const reportFile of reportFiles) {
        const reportPath = path.join(reportsDir, reportFile);
        let report;
        try {
            report = await fs.readFile(reportPath, { encoding: 'utf8' });
        } catch (err) {
            console.error(`Error reading report file ${reportPath}:`, err);
            continue; // Skip to the next file if reading fails
        }

        // Replace double spaces with single spaces in radiology report
        report = report.toString().split('  ').join(' ');

        const result = await model.generateContent(prompt + report);
		const response = await result.response;
		const text = response.text();

		// remove html snippet header and footer, if exists
		const regex = /```html([\s\S]+?)```/g;
		const matches = [];
		let match;
		while ((match = regex.exec(text)) !== null) {
			matches.push(match[1]); // Without trimming whitespace
		}
		let output;
		if (matches.length === 0) {
			output = text;
		} else output = matches;

		// correct frequently made mistakes from array
		for (let i=0; i<mistakes.length; i+=2) {
			output=output.toString().split(mistakes[i]).join(mistakes[i+1]);
		}
        // Construct output file name
        const outputFileName = path.basename(reportFile, '.txt') + '-output.html';
        const outputPath = path.join('outputs', outputFileName);

        // Write output
        await fs.writeFile(outputPath, output, { encoding: 'utf8' }, err => {
            if (err) {
                console.error(`Error writing output file ${outputPath}:`, err);
            }
        });
		// Send next prompt and report to the model with a 1-minute delay
        await new Promise(resolve => setTimeout(resolve, 60 * 1000)); // Delay

        console.log(text);
    }
}

run();