import { ContractAgent } from '../src/agents/contractAgent';

describe('ContractAgent', () => {
    let agent: ContractAgent;

    beforeEach(() => {
        agent = new ContractAgent();
    });

    test('should extract key obligations from the contract', async () => {
        const contractText = 'This is a sample contract text with obligations.';
        const obligations = await agent.extractObligations(contractText);
        expect(obligations).toBeDefined();
        expect(obligations.length).toBeGreaterThan(0);
    });

    test('should extract important dates from the contract', async () => {
        const contractText = 'This contract is effective as of January 1, 2023.';
        const dates = await agent.extractImportantDates(contractText);
        expect(dates).toBeDefined();
        expect(dates.length).toBeGreaterThan(0);
    });

    test('should identify potential risks in the contract', async () => {
        const contractText = 'This contract may have risks associated with non-compliance.';
        const risks = await agent.identifyRisks(contractText);
        expect(risks).toBeDefined();
        expect(risks.length).toBeGreaterThan(0);
    });
});