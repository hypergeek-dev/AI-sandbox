from transformers import BlenderbotTokenizer, BlenderbotForConditionalGeneration

def main():
    model_name = "facebook/blenderbot-400M-distill"
    tokenizer = BlenderbotTokenizer.from_pretrained(model_name)
    model = BlenderbotForConditionalGeneration.from_pretrained(model_name)

    conversation_history = []

    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            print("Goodbye!")
            break

        conversation_history.append(f"User: {user_input}")
        truncated_history = "\n".join(conversation_history[-3:])
        inputs = tokenizer(truncated_history, return_tensors="pt", truncation=True)
        reply_ids = model.generate(**inputs, max_length=50)
        bot_response = tokenizer.decode(reply_ids[0], skip_special_tokens=True)
        conversation_history.append(f"Bot: {bot_response}")

        print(f"Bot: {bot_response}")

if __name__ == "__main__":
    main()
