// Replace 'your_api_key_here' with your actual Mistral API key.
const API_URL = 'https://api.mistral.ai/v1/chat/completions';
const API_KEY = '5lRu14dB81ejsnT3Deb7gMoez2cuBjSl';

async function getExplanation(text) {
  try {
    const response = await fetch(API_URL, {
      method: 'POST',
      headers: {
        'Authorization': `Bearer ${API_KEY}`,
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        model: "mistral-tiny", // Adjust the model if needed.
        messages: [{ role: "user", content: `Explain this: ${text}` }]
      })
    });
    const data = await response.json();

    // Adjust extraction based on API response structure.
    const explanation = data.choices[0].message.content;
    return explanation;
  } catch (error) {
    console.error("Error fetching explanation:", error);
    return "Error fetching explanation.";
  }
}

// Create a context menu item for text selections.
chrome.contextMenus.create({
  id: "explain-text",
  title: "Explain this: \"%s\"",
  contexts: ["selection"]
});

// Listen for a click on the context menu.
chrome.contextMenus.onClicked.addListener((info, tab) => {
  if (info.menuItemId === "explain-text" && info.selectionText) {
    getExplanation(info.selectionText).then(explanation => {
      // Inject a script into the current page that shows an alert with the explanation.
      chrome.scripting.executeScript({
        target: { tabId: tab.id },
        function: showExplanation,
        args: [explanation]
      });
    });
  }
});

// This function will be executed in the context of the page.
function showExplanation(explanation) {
  alert(explanation);
}
