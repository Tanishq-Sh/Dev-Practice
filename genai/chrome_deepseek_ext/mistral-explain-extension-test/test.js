require('dotenv').config();
const axios = require('axios');

const API_URL = 'https://api.mistral.ai/v1/chat/completions';
const API_KEY = process.env.MISTRAL_API_KEY;

async function getExplanation(text) {
    try {
        const response = await axios.post(
            API_URL,
            {
                model: process.env.MODEL_NAME, // Adjust the model if needed
                messages: [{ role: "user", content: `Explain this: ${text}` }],
            },
            {
                headers: {
                    'Authorization': `Bearer ${API_KEY}`,
                    'Content-Type': 'application/json'
                }
            }
        );

        // Extract and display the explanation
        const explanation = response.data.choices[0].message.content;
        console.log("Explanation:", explanation);
    } catch (error) {
        console.error("Error:", error.response ? error.response.data : error.message);
    }
}

// Test with a sample text
getExplanation("What is a neural network?");
