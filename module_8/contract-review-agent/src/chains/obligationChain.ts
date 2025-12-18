import { Chain } from 'langchain';
import { obligationPrompt } from '../prompts/obligationPrompt';
import { contractParser } from '../parsers/contractParser';

export const obligationChain = new Chain({
    input: 'legalDocument',
    output: 'keyObligations',
    steps: [
        {
            name: 'Parse Contract',
            action: async (input) => {
                const parsedDocument = await contractParser(input);
                return parsedDocument;
            },
        },
        {
            name: 'Extract Obligations',
            action: async (parsedDocument) => {
                const obligations = await obligationPrompt(parsedDocument);
                return obligations;
            },
        },
    ],
});