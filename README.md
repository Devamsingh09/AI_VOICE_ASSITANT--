
# AI VOICE ASSISTANT 🤖

![Screenshot (22)](https://github.com/user-attachments/assets/c96177d4-757d-4e59-be61-8e8b3aa3d05d)
![Screenshot (21)](https://github.com/user-attachments/assets/cced6184-3810-4ffd-aa76-b84f855d9595)
![Screenshot (20)](https://github.com/user-attachments/assets/e566c39f-7676-4cb8-858a-ff47d1323ef8)



This is an AI Voice Assistant project built using **Streamlit** and the **Gemini API**. It leverages the **Gemini Pro** model to deliver powerful, intelligent responses to user queries, offering a seamless conversational experience.

## Features

- **AI Assistant**: A conversational assistant powered by Gemini Pro's advanced AI model.
- **Streamlit Interface**: The assistant is accessible via a user-friendly web interface built with Streamlit.
- **Gemini API Integration**: The AI Assistant uses the Gemini API for intelligent responses based on user input.

## Prerequisites

Before running the project locally, make sure to install the necessary dependencies:

1. **Python 3.9 or above** (recommended for compatibility)
2. **Streamlit**: For the web interface.
3. **Gemini API Key**: For authenticating and connecting with the Gemini API.

## Installation

1. Clone the repository:

    ```bash
    git clone <repository-url>
    cd <project-directory>
    ```

2. Install the required Python packages:

    ```bash
    pip install -r requirements.txt
    ```

3. Set up your **Gemini API Key**:

   - Sign up for **Gemini Pro** and get your API key.
   - Set the API key as an environment variable for secure access:

     ```bash
     export GEMINI_API_KEY="your-api-key"
     ```

   Alternatively, you can pass the API key in the app directly, but using an environment variable is recommended for security.

4. Run the app locally:

    ```bash
    streamlit run app.py
    ```

5. Open your browser and navigate to the local address (`localhost:8501`) to start using the AI Voice Assistant.

## Limitations

- **Deployment Status**: Due to some technical issues with Streamlit, the app is currently not deployed. However, we are working on resolving the issues and will deploy the app soon.
- **API Limitations**: Ensure you have sufficient API quota from Gemini to avoid hitting rate limits.

## Upcoming Features

- Deployment of the AI Voice Assistant app on a live server.
- Enhanced conversation memory and context handling.
- Additional features and integrations for improved user interaction.

## Contributing

If you wish to contribute to the project, feel free to fork the repository and submit a pull request with your changes. We welcome contributions that enhance the functionality or fix any issues.
