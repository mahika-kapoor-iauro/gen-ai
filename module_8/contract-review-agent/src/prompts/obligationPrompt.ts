const obligationPrompt = `
You are a legal assistant tasked with extracting key obligations from a legal document. Please read the following text carefully and identify all obligations that are imposed on the parties involved. 

Obligations are typically expressed as duties, responsibilities, or actions that one party must perform for another. 

Here is the text:

{{document_text}}

Please list the obligations in a clear and concise manner, ensuring that each obligation is distinct and easy to understand.
`;

export default obligationPrompt;