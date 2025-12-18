import fs from 'fs';
import path from 'path';

export const loadContract = (filePath: string): string => {
    const absolutePath = path.resolve(filePath);
    if (!fs.existsSync(absolutePath)) {
        throw new Error(`File not found: ${absolutePath}`);
    }
    return fs.readFileSync(absolutePath, 'utf-8');
};

export const prepareDocument = (document: string): string => {
    // Basic formatting can be added here
    return document.trim();
};