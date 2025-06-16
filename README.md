
# 🧙‍♂️ Mythology Storyteller Bot

Welcome to **Mythology Storyteller Bot**, an intelligent storytelling bot designed to narrate fascinating tales from mythologies around the world. Whether it's Greek, Norse, Hindu, or Egyptian mythology, this bot can bring ancient legends to life in a captivating and interactive format.

## 🌟 Features

- 📜 Generates stories based on user input (character, myth, region, etc.)
- 🌍 Supports multiple mythological traditions
- 🧠 Uses NLP techniques to craft engaging and coherent narratives
- 🔁 Offers random mythology stories for exploration
- 🎤 Text to audio conversion using gTTs

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- `pip` (Python package installer)
- An API key (if using OpenAI/GPT models)

### Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/thomasanto7001/Mythology_Storyteller_Bot.git
   cd Mythology_Storyteller_Bot
   ```

2. **Create a virtual environment (optional but recommended):**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Set up your API keys and environment variables (if any):**

   Create a `.env` file and add:

   ```
   OPENAI_API_KEY=your_key_here
   ```

## 🧪 Usage

Run the bot from the command line:

```bash
python storyteller.py
```

You will be prompted to enter:
- A mythological figure, theme, or region
- The desired tone or genre (epic, humorous, tragic, etc.)

The bot will then generate and narrate a custom mythology story.

## 🧰 File Structure

```
Mythology_Storyteller_Bot/
├── storyteller.py           # Main script to run the bot
├── .gitattributes          
├── requirements.txt         # Python dependencies
└── README.md                # Project documentation
```

## 📦 Dependencies

- `openai`
- `python-dotenv`
- `nltk` or `spaCy` *(optional for text processing)*

## ✨ Sample Prompt

```
> Enter a mythological character or theme:
Loki, Norse Trickster

> Choose a story style (epic, dark, humorous, etc.):
Humorous

> Generating your story with voice ...
```

*Loki, the Norse trickster, once turned into a salmon to escape a group of angry gods...*

## 📜 Future Improvements

- Web or app interface
- Expand mythology database
- Support for multiple story formats (poetry, play, etc.)

## 🙌 Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you'd like to improve or add.


---

> *“Myths are public dreams, and dreams are private myths.” – Joseph Campbell*
