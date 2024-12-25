# Gemma-Math-Problem-Solver

## Overview

This is a simple Streamlit app that integrates the **Langchain** framework with **GROQ's Chat Model (Gemma2)** to solve mathematical problems. The app also uses additional tools like a calculator and Wikipedia search to enhance the problem-solving experience. The user interacts with the app by entering a math question, and the app provides a detailed solution.

## Features

- **Mathematical Problem Solving**: Use the `LLMMathChain` tool to solve complex math problems.
- **Wikipedia Search**: The app can pull information from Wikipedia to provide context or answer general knowledge questions.
- **Logical Reasoning**: The app offers detailed explanations of the steps taken to solve the math problem, using the Langchain logic agent.
- **Interactive Interface**: The app uses Streamlit's chat message interface to handle conversations interactively.

## How It Works

1. **Input**: Users can enter a math-related question into a text box.
2. **GROQ Chat (Gemma2)**: The entered question is processed using the **Gemma2** model to generate a solution.
3. **Wikipedia API**: For questions needing general information, the app can pull relevant data from Wikipedia.
4. **Calculator**: The app can perform basic math operations using a Langchain-powered calculator.
5. **Logical Reasoning**: A reasoning tool is used to provide detailed explanations of how the solution was derived.
6. **Callbacks**: Streamlit's callback handler is used to display intermediate steps as the agent processes the question.

## Setup

### Prerequisites

- Python 3.8+
- A GROQ API key for the **Gemma2** model.
- The following Python libraries:
  - `streamlit`
  - `langchain`
  - `langchain_groq`
  - `streamlit-chat` (if not part of `streamlit`)

### Installation

1. Clone this repository or download the files.
   
   ```bash
   https://github.com/Muhammad-Rebaal/Gemma-Math-Problem-Solver.git
