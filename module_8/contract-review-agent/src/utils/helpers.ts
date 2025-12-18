import { format } from 'date-fns';

export function formatDate(date: Date): string {
    return format(date, 'yyyy-MM-dd');
}

export function validateDate(dateString: string): boolean {
    const regex = /^\d{4}-\d{2}-\d{2}$/;
    return regex.test(dateString);
}

export function extractKeyTerms(text: string, terms: string[]): string[] {
    return terms.filter(term => text.includes(term));
}

export function cleanText(text: string): string {
    return text.replace(/\s+/g, ' ').trim();
}