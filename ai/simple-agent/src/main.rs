use genai::chat::{ChatMessage, ChatRequest, ChatStreamEvent};
use genai::Client;
use serde::{Deserialize, Serialize};
use std::io::{self, Write};
use futures::StreamExt;

#[derive(Deserialize, Serialize, Debug)]
struct CalculatorArgs {
    x: f64,
    y: f64,
    operation: String,
}

/// A simple tool that performs basic arithmetic.
/// In a more advanced setup, this would be automatically called by the agent.
fn calculator(args: CalculatorArgs) -> f64 {
    match args.operation.as_str() {
        "add" => args.x + args.y,
        "subtract" => args.x - args.y,
        "multiply" => args.x * args.y,
        "divide" => args.x / args.y,
        _ => 0.0,
    }
}

#[tokio::main]
async fn main() -> anyhow::Result<()> {
    let client = Client::default();
    // Using llama3 via Ollama. Make sure Ollama is running and has llama3 pulled.
    let model = "llama3.2:3b";

    println!("--------------------------------------------------");
    println!("AI Agent Chat Interface");
    println!("Provider: Ollama | Model: {}", model);
    println!("Tools available: calculator (simulated)");
    println!("Type 'exit' to quit.");
    println!("--------------------------------------------------");

    let mut chat_history: Vec<ChatMessage> = vec![
        ChatMessage::system("You are a helpful AI assistant running locally via Ollama.")
    ];

    loop {
        print!("You: ");
        io::stdout().flush()?;

        let mut input = String::new();
        io::stdin().read_line(&mut input)?;
        let input = input.trim();

        if input == "exit" {
            println!("Goodbye!");
            break;
        }
        if input.is_empty() {
            continue;
        }

        chat_history.push(ChatMessage::user(input));

        // Create the chat request
        let chat_req = ChatRequest::new(chat_history.clone());
        
        // Execute the chat request with streaming
        print!("AI: ");
        io::stdout().flush()?;

        match client.exec_chat_stream(model, chat_req, None).await {
            Ok(res) => {
                let mut full_response = String::new();
                let mut stream = res.stream;
                while let Some(Ok(event)) = stream.next().await {
                    if let ChatStreamEvent::Chunk(chunk) = event {
                        print!("{}", chunk.content);
                        io::stdout().flush()?;
                        full_response.push_str(&chunk.content);
                    }
                }
                println!(); // New line after stream ends
                chat_history.push(ChatMessage::assistant(full_response));
            }
            Err(e) => {
                println!(); // Ensure error starts on new line
                eprintln!("Error: {}. (Is Ollama running and model '{}' pulled?)", e, model);
            }
        }
    }

    Ok(())
}
