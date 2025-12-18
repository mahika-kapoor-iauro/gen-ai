import { PromptTemplate } from 'langchain/prompts';
import { LLMChain } from 'langchain/chains';
import { OpenAI } from 'langchain/llms';

const riskPromptTemplate = `
You are a legal analysis assistant. Your task is to identify potential risks in the following legal document. Please analyze the text and highlight any clauses or terms that may pose risks to the parties involved.

Document:
{document}
`;

const riskPrompt = new PromptTemplate({
  template: riskPromptTemplate,
  inputVariables: ['document'],
});

const riskChain = new LLMChain({
  llm: new OpenAI({ temperature: 0.5 }),
  prompt: riskPrompt,
});

export default riskChain;