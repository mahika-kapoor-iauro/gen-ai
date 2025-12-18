export interface Obligation {
    description: string;
    partyResponsible: string;
    dueDate?: Date;
}

export interface ImportantDate {
    event: string;
    date: Date;
}

export interface Risk {
    description: string;
    likelihood: 'low' | 'medium' | 'high';
    impact: 'low' | 'medium' | 'high';
}

export interface ContractReviewResult {
    obligations: Obligation[];
    importantDates: ImportantDate[];
    risks: Risk[];
}