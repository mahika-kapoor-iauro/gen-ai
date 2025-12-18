# Contract Review Agent

## Overview
The Contract Review Agent is a tool designed to automate the extraction of key obligations, important dates, and potential risks from legal documents. Utilizing advanced language processing techniques, this agent streamlines the contract review process, making it more efficient and reliable.

## Features
- **Obligation Extraction**: Identifies and extracts key obligations from legal documents.
- **Date Identification**: Recognizes important dates relevant to the contract.
- **Risk Assessment**: Analyzes the document to identify potential risks associated with the contract.

## Project Structure
```
contract-review-agent
├── src
│   ├── main.ts               # Entry point for the application
│   ├── agents
│   │   └── contractAgent.ts   # Manages the contract review process
│   ├── chains
│   │   ├── obligationChain.ts  # Chain for extracting obligations
│   │   ├── dateChain.ts        # Chain for extracting important dates
│   │   └── riskChain.ts        # Chain for identifying risks
│   ├── prompts
│   │   ├── obligationPrompt.ts  # Prompt for obligations extraction
│   │   ├── datePrompt.ts        # Prompt for date extraction
│   │   └── riskPrompt.ts        # Prompt for risk identification
│   ├── parsers
│   │   └── contractParser.ts    # Handles loading and preparing the legal document
│   ├── types
│   │   └── index.ts             # Type definitions and interfaces
│   └── utils
│       └── helpers.ts           # Utility functions
├── tests
│   └── agent.test.ts            # Unit tests for the ContractAgent
├── package.json                  # npm configuration file
├── tsconfig.json                 # TypeScript configuration file
└── README.md                     # Project documentation
```

## Installation
To set up the project, clone the repository and install the dependencies:

```bash
git clone <repository-url>
cd contract-review-agent
npm install
```

## Usage
To run the contract review agent, execute the following command:

```bash
npm start
```

Ensure that you have a legal document ready for processing. The agent will load the document and extract the relevant information.

## Testing
To run the unit tests for the ContractAgent, use the following command:

```bash
npm test
```

## Contributing
Contributions are welcome! Please submit a pull request or open an issue for any enhancements or bug fixes.

## License
This project is licensed under the MIT License. See the LICENSE file for details.