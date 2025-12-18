import { PromptTemplate } from 'langchain/prompts';
import { LLMChain } from 'langchain/chains';
import { Document } from 'langchain/document';

const datePrompt = new PromptTemplate({
    template: "Extract all important dates from the following legal document:\n\n{document}",
    inputVariables: ["document"],
});

export const createDateChain = () => {
    const dateChain = new LLMChain({
        prompt: datePrompt,
        outputKey: "importantDates",
    });

    return async (document: Document) => {
        const result = await dateChain.call({ document: document.text });
        return result.importantDates;
    };
};