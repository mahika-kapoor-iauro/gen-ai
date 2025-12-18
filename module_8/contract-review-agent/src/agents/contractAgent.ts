class ContractAgent {
    constructor(document) {
        this.document = document;
    }

    async extractObligations() {
        const { extractObligationsChain } = await import('../chains/obligationChain');
        return await extractObligationsChain(this.document);
    }

    async extractImportantDates() {
        const { extractDatesChain } = await import('../chains/dateChain');
        return await extractDatesChain(this.document);
    }

    async identifyRisks() {
        const { identifyRisksChain } = await import('../chains/riskChain');
        return await identifyRisksChain(this.document);
    }

    async reviewContract() {
        const obligations = await this.extractObligations();
        const importantDates = await this.extractImportantDates();
        const risks = await this.identifyRisks();

        return {
            obligations,
            importantDates,
            risks
        };
    }
}

export default ContractAgent;