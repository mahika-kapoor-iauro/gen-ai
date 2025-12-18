import { ContractAgent } from './agents/contractAgent';
import { loadLegalDocument } from './parsers/contractParser';

async function main() {
    try {
        const documentPath = 'path/to/legal/document'; // Specify the path to the legal document
        const legalDocument = await loadLegalDocument(documentPath);
        
        const contractAgent = new ContractAgent();
        const reviewResults = await contractAgent.reviewContract(legalDocument);
        
        console.log('Review Results:', reviewResults);
    } catch (error) {
        console.error('Error during contract review:', error);
    }
}

main();