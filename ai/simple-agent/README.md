# Simple AI Agent in Rust

This project demonstrates a simple AI Agent built with Rust that uses local models for inference.

## Prerequisites

- [Rust](https://www.rust-lang.org/tools/install)
- [Ollama](https://ollama.com/)

## Getting Started

1. **Install Ollama** and make sure it is running.
2. **Pull the llama3 model**:
   ```bash
   ollama pull llama3
   ```
3. **Run the agent**:
   ```bash
   cargo run
   ```

## Features

- **CLI Chat Interface**: Interactive chat in your terminal.
- **Local Inference**: Uses Ollama to run models locally (defaulting to `llama3`).
- **Tool Support (Simulated)**: The codebase includes a `calculator` tool structure, showing how to define tools for an agent.

## How it works

The agent uses the `genai` crate to communicate with the Ollama API. It maintains a chat history to provide context for each subsequent request.
