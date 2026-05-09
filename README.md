# **Neural Pet**
Say hello to your **Neural Pet**! Neural Pet emulates a tamagachi-style pet using an LLM
at the core of its structure! Put simply the LLM _is_ the pet. The goal of this project is to incorporate an existing llm into a program written around it, allowing it to be used in a specific way that is not just as a standard chat bot. The current iteration is a cli tool, but has the wiring and structure to be ran as a web application. 


## Features:
Your interactions with your pet can be just like any you would have with your actual dog or cat. However, it need not be a dog or cat; it can be a parrot, a horse, or even a baby dragon! You can feed it, play with it, teach it tricks and perform those tricks. Like any pet, it will need to be fed as well as stimulated. If it goes too many days with out food it will get really hungry and really sad.

## Technical:
Neuro Pet utilizes a few specific important technologies in the tech stack to make it work. The program itself is written in python with llama-cpp and huggingface-hub. It uses SQLite for saving all of the important creature data. And most importantly the program uses the GGUF model **gwen-2.5-1.5b-instruct-q4_k_m.gguf** from the open-source machine learning hub Hugging Face. 

Much like SQLite actually, this model is lightweight and perfect for the small scale of the program. Llama-cpp is used to run the model on the hardware of the machine running it, so the lightweight size of the model is not only useful but necessary. This does also mean there is no reliance on AI data centers or things like paying for tokens, etc. The whole program is self contained and runs locally.

As you interact with the pet, prompts are being sent behind the scenes to the llm with all the relevent information about the pet. This is why SQL is sufficient for maintaining all relevent information and as there is only one pet, SQLite is plenty. There is only one table entry.

## INSTALLATION INSTRUCTIONS

### Package:
    Windows: 
    Linux:

### Source Code:

#### Requirements:
- Python 3.11+
- [uv](https://github.com/astral-sh/uv) package manager
- The GGUF Model from HuggingFace Lib [gwen-2.5-1.5b-instruct-q4_k_m.gguf](https://link.com)
- Llama CPP-Python needs a C++ compiler:
    - Linux: `sudo apt install build-essential`

git clone https://github.com/kristiansroberts/neural_pet
cd NeuralPet
uv sync

Place the gwen-2.5-1.5b-instruct-q4_k_m.gguf file into the models folder

uv run cli.py

## Usage
cli.py contains the interactive loop for the cli version. 
app/main.py exists for the eventual web version/

Upon first loading up the program, a series of prompts will allow for actual pet creation. This is where the name and species is chosen. While interacting with the Nueral Pet you simply tell it how you wish to engage, whether that be feeding, playing, taking a nap or just hanging out. The pet will act accordingly.

## Known limitations
There are a few known limitations and obstacles:

- Quirks with using a small model. It doesn't quite have the capacity of something like chatGPT and while rare it could go rogue.

- CPU speed and power can limit the actual response speed. The initial response after load can take 20-30 seconds or longer. With a fast and powerful cpu this may not be an issue at all.

- Attaching actual visuals to the web version of the app (making it a pet you can see) in the current structure is unfeasible. Since the user can make any pet they want, it would necessitate millions of potential pet looks.


## Roadmap
- Linux and Windows packages

- Web application implementation

- Significantly more in depth keyword matching and local intent parsing to allow for faster engagement



## Author

### Kristian Roberts

I am a backend developer, focused on building my fundamental grasp on modular and scalable design. I am always seeking opportunities to work on new and different projects and look to add varied works to my portfolio.