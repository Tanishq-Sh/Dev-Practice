// Import default configuration for local development
import { API_KEY, MODEL_NAME, API_URL } from "./config.js";

// Retrieve configuration from chrome.storage.local, or fallback to local config
function getConfig(callback) {
  chrome.storage.local.get(["MISTRAL_API_KEY", "MISTRAL_MODEL", "MISTRAL_API_URL"], function (result) {
    // Use the stored values if they exist; otherwise fall back to the defaults
    const apiKey = result.MISTRAL_API_KEY || API_KEY;
    const modelName = result.MISTRAL_MODEL || MODEL_NAME;
    const apiUrl = result.MISTRAL_API_URL || API_URL;

    if (!apiKey || !modelName || !apiUrl) {
      console.error("Missing API key, model name, or API URL. Please set them in extension storage.");
    }
    callback(apiKey, modelName, apiUrl);
  });
}

async function getExplanation(text, apiKey, modelName, apiUrl) {
  try {
    const response = await fetch(apiUrl, {
      method: 'POST',
      headers: {
        'Authorization': `Bearer ${apiKey}`,
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        model: modelName, // Use model name from configuration
        messages: [{ role: "user", content: `Explain this: ${text}` }]
      })
    });
    const data = await response.json();
    return data.choices[0].message.content;
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
    getConfig((apiKey, modelName, apiUrl) => {
      getExplanation(info.selectionText, apiKey, modelName, apiUrl).then(explanation => {
        // Inject a script into the current page that shows a styled modal with the explanation.
        chrome.scripting.executeScript({
          target: { tabId: tab.id },
          function: showExplanation,
          args: [explanation]
        });
      });
    });
  }
});

// Function injected into the page to display a modal overlay.
function showExplanation(explanation) {
  // Remove any existing modal
  const existingModal = document.getElementById("mistral-modal");
  if (existingModal) {
    existingModal.remove();
  }

  // Create modal container
  const modal = document.createElement("div");
  modal.id = "mistral-modal";
  modal.style.position = "fixed";
  modal.style.top = "0";
  modal.style.left = "0";
  modal.style.width = "100%";
  modal.style.height = "100%";
  modal.style.backgroundColor = "rgba(0, 0, 0, 0.6)";
  modal.style.display = "flex";
  modal.style.alignItems = "center";
  modal.style.justifyContent = "center";
  modal.style.zIndex = "9999";

  // Create modal content container
  const content = document.createElement("div");
  content.style.background = "#fff";
  content.style.padding = "20px 30px";
  content.style.borderRadius = "8px";
  content.style.boxShadow = "0 2px 10px rgba(0, 0, 0, 0.3)";
  content.style.maxWidth = "600px";
  content.style.width = "80%";
  content.style.position = "relative";
  content.style.fontFamily = "Arial, sans-serif";

  // Title
  const title = document.createElement("h2");
  title.textContent = "Explanation";
  title.style.marginTop = "0";
  title.style.fontSize = "24px";
  title.style.color = "#333";
  content.appendChild(title);

  // Explanation text
  const explanationPara = document.createElement("p");
  explanationPara.textContent = explanation;
  explanationPara.style.fontSize = "16px";
  explanationPara.style.lineHeight = "1.5";
  explanationPara.style.color = "#555";
  content.appendChild(explanationPara);

  // Create close button
  const closeButton = document.createElement("button");
  closeButton.textContent = "×";
  closeButton.style.position = "absolute";
  closeButton.style.top = "10px";
  closeButton.style.right = "10px";
  closeButton.style.background = "transparent";
  closeButton.style.border = "none";
  closeButton.style.fontSize = "24px";
  closeButton.style.cursor = "pointer";
  closeButton.style.color = "#888";
  closeButton.onclick = function () {
    modal.remove();
  };
  content.appendChild(closeButton);

  // Append content to modal and modal to body.
  modal.appendChild(content);
  document.body.appendChild(modal);
}
