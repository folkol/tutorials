# Architecture

The simple-agent is a lightweight Rust-based CLI application designed to demonstrate interaction with local Large Language Models (LLMs) via Ollama. Its architecture is built around three main pillars:

1. Core Components
   - CLI Interface: A standard input/output loop in src/main.rs that handles user prompts and displays AI responses.
   - Client Layer ([genai crate](https://crates.io/crates/genai)): Acts as a multi-provider abstraction layer. It handles the communication with the Ollama API, including request formatting and response parsing.
   - Local Inference Engine (Ollama): The backend service that runs the actual model (e.g., llama3.2:3b). It processes the tokens and generates responses.
   - State Management: A simple Vec<ChatMessage> that acts as the "short-term memory," maintaining the context of the conversation throughout the session.

2. Capabilities
   - Local Inference: All processing happens on your machine, ensuring privacy and allowing offline use.
   - Context Awareness: The agent tracks system, user, and assistant messages to provide coherent follow-up responses.
   - Output Streaming: Uses asynchronous streams (futures::StreamExt) to display characters in real-time as they are generated, improving the user experience.
   - Error Handling: Basic checks to ensure the backend (Ollama) is reachable and the requested model is available.

3. Interaction with Tools
   In its current state, tool interaction is simulated and manual:
   - Definition: A calculator function and its arguments (CalculatorArgs) are defined in the code.
   - Execution: The agent does not yet autonomously decide to call tools. While the UI mentions "Tools available," the current logic simply sends text back and forth.
   - Future Integration: To make it functional, the genai client would need to be passed a ChatRequest containing tool definitions (JSON schemas). The model would then respond with a "tool call" request instead of plain text, which the Rust code would execute before sending the result back to the model.

4. Dynamic Tool Addition
   Can it add tools dynamically?
   - Current State: No. Tools are hard-coded as Rust functions. Adding a new tool requires modifying the source code and recompiling the application.
   - Architectural Path to Dynamic Tools: To support dynamic addition, the architecture would need:
       - A Registry Pattern: A way to register function pointers or closures at runtime.
       - Plugin Support: Loading external libraries (like .so or .dylib files) or using a scripting language (like Rhai or Lua) to define new tool logic without a full recompile.
       - Dynamic Schema Generation: Tools would need to provide their own JSON metadata so the LLM knows how to use them.


## Summary of the Flow

1. Input: User types a message.
2. Context: Message is added to the history.
3. Request: [genai](https://crates.io/crates/genai) sends the full history to the local Ollama endpoint.
4. Stream: Ollama generates chunks; the app prints them and aggregates them.
5. Update: The full response is saved to history for the next turn.
