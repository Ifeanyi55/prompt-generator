import { client } from "@gradio/client";

const app = await client("https://ifeanyi-promptgenerator.hf.space/");
const result = await app.predict("/predict", [		
				"Landscape of", // string  in 'prompt' Textbox component
	]);

console.log(result.data);
